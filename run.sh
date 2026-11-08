#!/usr/bin/env bash
# Start the converter at http://127.0.0.1:8765 (sets up .venv with yt-dlp on first run).
set -euo pipefail
cd "$(dirname "$0")"

command -v ffmpeg >/dev/null || { echo "FFmpeg is missing. Install it (macOS: brew install ffmpeg)."; exit 1; }
command -v node >/dev/null || echo "Warning: Node.js not found. yt-dlp needs it for YouTube; install it (macOS: brew install node)."

if [ ! -x .venv/bin/python ]; then
  PY=""
  for c in python3.13 python3.12 python3.11 python3.10 python3; do
    if command -v "$c" >/dev/null && "$c" -c 'import sys; sys.exit(sys.version_info < (3, 10))'; then PY="$c"; break; fi
  done
  [ -n "$PY" ] || { echo "Python 3.10 or newer is required (macOS: brew install python)."; exit 1; }
  "$PY" -m venv .venv
  .venv/bin/pip install -q --upgrade pip
  .venv/bin/pip install -q "yt-dlp[default]"
fi
exec .venv/bin/python server.py "${1:-8765}"
