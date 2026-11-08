"""Local YouTube -> MP3/MP4 converter.

A small stdlib HTTP server that wraps yt-dlp (stream extraction, signature and
throttling challenges) and FFmpeg (transcode / mux). Bound to 127.0.0.1 only.
"""

import json
import mimetypes
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

import yt_dlp

HOST = "127.0.0.1"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
DOWNLOADS = ROOT / "downloads"  # temp working dirs, one per job
OUTPUT = Path.home() / "Downloads" / "YouTube Converter"  # finished files, in MP3/ and MP4/
JOB_TTL_SECONDS = 60 * 60
MAX_BODY = 8 * 1024

YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com", "youtu.be"}
MP3_BITRATES = {"128", "192", "320"}
MP4_HEIGHTS = [2160, 1440, 1080, 720, 480, 360]
ANSI = re.compile(r"\x1b\[[0-9;]*m")

BASE_OPTS = {
    "quiet": True,
    "no_warnings": True,
    "noplaylist": True,
    "noprogress": True,
    # YouTube's stream URLs are protected by JS challenges; yt-dlp solves them with a JS runtime.
    "js_runtimes": {"node": {}},
}

jobs = {}
jobs_lock = threading.Lock()


class UserError(Exception):
    """An error whose message is safe and useful to show in the UI."""


def clean_error(exc):
    msg = ANSI.sub("", str(exc)).strip()
    return msg.removeprefix("ERROR: ") or "Something went wrong."


def validate_url(raw):
    if not isinstance(raw, str) or len(raw) > 500:
        raise UserError("Paste a YouTube link.")
    url = raw.strip()
    if "://" not in url:
        url = "https://" + url
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or (parsed.hostname or "").lower() not in YOUTUBE_HOSTS:
        raise UserError("That isn't a YouTube link.")
    return url


def fetch_info(url):
    with yt_dlp.YoutubeDL(BASE_OPTS) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except yt_dlp.utils.DownloadError as exc:
            raise UserError(clean_error(exc)) from exc
    if info.get("_type") == "playlist":
        raise UserError("Playlists aren't supported. Paste a single video link.")
    if info.get("is_live"):
        raise UserError("Live streams can't be converted.")
    heights = {f.get("height") for f in info.get("formats", []) if f.get("vcodec") not in (None, "none")}
    return {
        "id": info.get("id"),
        "url": info.get("webpage_url") or url,
        "title": info.get("title"),
        "channel": info.get("channel") or info.get("uploader"),
        "duration": info.get("duration"),
        "thumbnail": info.get("thumbnail"),
        "license": info.get("license"),
        "heights": [h for h in MP4_HEIGHTS if h in heights],
    }


def download_opts(fmt, quality, job_dir):
    opts = {
        **BASE_OPTS,
        "outtmpl": str(job_dir / "%(title).150B [%(id)s].%(ext)s"),
        "windowsfilenames": True,
    }
    if fmt == "mp3":
        if quality not in MP3_BITRATES:
            raise UserError("Pick an MP3 bitrate.")
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": quality},
            {"key": "FFmpegMetadata"},
        ]
    elif fmt == "mp4":
        if not (isinstance(quality, str) and quality.isdigit() and int(quality) in MP4_HEIGHTS):
            raise UserError("Pick a video resolution.")
        # Best stream at or below the chosen height; prefer H.264 + AAC so the
        # merge is a lossless copy and plays everywhere. Above 1080p YouTube only
        # serves VP9/AV1, which get muxed into MP4 as-is.
        opts["format"] = "bv*+ba/b"
        opts["format_sort"] = [f"res:{quality}", "vcodec:h264", "acodec:aac"]
        opts["merge_output_format"] = "mp4"
    else:
        raise UserError("Pick MP3 or MP4.")
    return opts


def update_job(job_id, **fields):
    with jobs_lock:
        jobs[job_id].update(fields)


def unique_path(path):
    n = 2
    candidate = path
    while candidate.exists():
        candidate = path.with_name(f"{path.stem} ({n}){path.suffix}")
        n += 1
    return candidate


def run_job(job_id, url, tasks):
    """Convert one video to each requested format, one after another.

    Each format is built in a private temp dir, then moved into
    ~/Downloads/YouTube Converter/<MP3|MP4>/ so that folder never holds partial files.
    """
    job_dir = DOWNLOADS / job_id
    files = []
    try:
        for index, (fmt, quality) in enumerate(tasks):
            update_job(job_id, task=index + 1, tasks=len(tasks), current=fmt, phase="queued", percent=0)
            task_dir = job_dir / fmt
            convert_one(job_id, url, fmt, download_opts(fmt, quality, task_dir))
            produced = [p for p in task_dir.iterdir() if p.suffix == f".{fmt}"]
            if not produced:
                raise UserError(f"The {fmt.upper()} conversion finished but no file was produced.")
            dest_dir = OUTPUT / fmt.upper()
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = unique_path(dest_dir / produced[0].name)
            shutil.move(str(produced[0]), dest)
            files.append({"format": fmt, "name": dest.name, "folder": f"{OUTPUT.name}/{dest_dir.name}",
                          "size": dest.stat().st_size, "path": str(dest)})
            update_job(job_id, files=list(files))
        update_job(job_id, phase="done", percent=100)
    except Exception as exc:  # noqa: BLE001 - every failure must reach the UI
        update_job(job_id, phase="error", error=clean_error(exc))
    finally:
        shutil.rmtree(job_dir, ignore_errors=True)


def convert_one(job_id, url, fmt, opts):
    streams = {"total": 2 if fmt == "mp4" else 1, "done": 0}

    def on_progress(d):
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            frac = (d.get("downloaded_bytes", 0) / total) if total else 0
            overall = (min(streams["done"], streams["total"] - 1) + frac) / streams["total"]
            update_job(
                job_id,
                phase="downloading",
                stream=min(streams["done"] + 1, streams["total"]),
                streams=streams["total"],
                percent=round(overall * 90, 1),  # last 10% is FFmpeg
                speed=d.get("speed"),
                eta=d.get("eta"),
            )
        elif d["status"] == "finished":
            streams["done"] += 1

    def on_postprocess(d):
        if d["status"] == "started" and d.get("postprocessor") in ("ExtractAudio", "Merger"):
            update_job(job_id, phase="converting" if fmt == "mp3" else "merging", percent=90, speed=None, eta=None)

    opts = {**opts, "progress_hooks": [on_progress], "postprocessor_hooks": [on_postprocess]}
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])


def sweep_old_jobs():
    cutoff = time.time() - JOB_TTL_SECONDS
    with jobs_lock:
        for jid in [jid for jid, j in jobs.items() if j["created"] < cutoff and j["phase"] in ("done", "error")]:
            del jobs[jid]


def parse_outputs(raw):
    """[{format, quality}, ...] -> [(fmt, quality)], at most one per format, MP3 first."""
    if not isinstance(raw, list) or not raw:
        raise UserError("Pick MP3, MP4 or both.")
    chosen = {}
    for item in raw:
        if not isinstance(item, dict):
            raise UserError("Bad request.")
        fmt, quality = item.get("format"), str(item.get("quality"))
        download_opts(fmt, quality, DOWNLOADS)  # validates format and quality
        chosen[fmt] = quality
    return [(f, chosen[f]) for f in ("mp3", "mp4") if f in chosen]


def start_job(url, outputs):
    sweep_old_jobs()
    tasks = parse_outputs(outputs)
    job_id = uuid.uuid4().hex
    (DOWNLOADS / job_id).mkdir(parents=True)
    with jobs_lock:
        jobs[job_id] = {"id": job_id, "phase": "queued", "percent": 0, "files": [], "created": time.time()}
    threading.Thread(target=run_job, args=(job_id, url, tasks), daemon=True).start()
    return job_id


def public_job(job):
    out = {k: v for k, v in job.items() if k != "created"}
    out["files"] = [{k: v for k, v in f.items() if k != "path"} for f in job.get("files", [])]
    return out


class Handler(BaseHTTPRequestHandler):
    server_version = "yt-converter"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.command, fmt % args))

    # Block DNS-rebinding: only answer requests addressed to this machine.
    def host_ok(self):
        host = (self.headers.get("Host") or "").rsplit(":", 1)[0].strip("[]")
        if host in ("127.0.0.1", "localhost", "::1"):
            return True
        self.send_json(403, {"error": "Forbidden"})
        return False

    def send_json(self, status, body):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0 or length > MAX_BODY:
            raise UserError("Bad request.")
        try:
            body = json.loads(self.rfile.read(length))
        except ValueError as exc:
            raise UserError("Bad request.") from exc
        if not isinstance(body, dict):
            raise UserError("Bad request.")
        return body

    def send_file(self, path):
        self.send_response(200)
        self.send_header("Content-Type", mimetypes.guess_type(path.name)[0] or "application/octet-stream")
        self.send_header("Content-Length", str(path.stat().st_size))
        self.end_headers()
        with path.open("rb") as f:
            shutil.copyfileobj(f, self.wfile)

    def do_GET(self):
        if not self.host_ok():
            return
        path = urlparse(self.path).path
        m = re.fullmatch(r"/api/jobs/([0-9a-f]{32})", path)
        if m:
            with jobs_lock:
                job = jobs.get(m.group(1))
                job = public_job(job) if job else None
            if not job:
                return self.send_json(404, {"error": "This conversion has expired."})
            return self.send_json(200, job)

        rel = "index.html" if path == "/" else path.lstrip("/")
        target = (STATIC / rel).resolve()
        if STATIC in target.parents and target.is_file():
            return self.send_file(target)
        self.send_json(404, {"error": "Not found"})

    def do_POST(self):
        if not self.host_ok():
            return
        path = urlparse(self.path).path
        m = re.fullmatch(r"/api/jobs/([0-9a-f]{32})/reveal/(\d)", path)
        if m:
            # Show a finished file in Finder. Only paths this server wrote are revealed.
            with jobs_lock:
                files = (jobs.get(m.group(1)) or {}).get("files", [])
            idx = int(m.group(2))
            if idx >= len(files) or not Path(files[idx]["path"]).exists():
                return self.send_json(404, {"error": "That file is no longer there."})
            subprocess.run(["open", "-R", files[idx]["path"]], check=False)
            return self.send_json(200, {"ok": True})
        try:
            body = self.read_json()
            url = validate_url(body.get("url"))
            if path == "/api/info":
                return self.send_json(200, fetch_info(url))
            if path == "/api/jobs":
                job_id = start_job(url, body.get("outputs"))
                return self.send_json(202, {"id": job_id})
            self.send_json(404, {"error": "Not found"})
        except UserError as exc:
            self.send_json(400, {"error": str(exc)})
        except Exception as exc:  # noqa: BLE001
            self.send_json(500, {"error": clean_error(exc)})


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found. Install it with: brew install ffmpeg")
    shutil.rmtree(DOWNLOADS, ignore_errors=True)  # jobs live in memory; old files are orphans
    DOWNLOADS.mkdir()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"YouTube converter running at http://{HOST}:{PORT}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
