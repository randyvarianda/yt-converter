# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primarily the author, on their own Mac: paste a YouTube link, get an MP3 and/or MP4 into Downloads, move on. The public GitHub repo is a bonus; occasional visitors clone and run it, but the design serves the author's daily use first and can be personal and opinionated.

## Product Purpose

A local converter that turns a YouTube video into MP3 audio, MP4 video, or both, saved straight into `~/Downloads/YouTube Converter/MP3` and `/MP4`. Success is a link-to-file round trip that takes seconds of attention and no thought.

## Positioning

Runs on the user's own machine (yt-dlp + FFmpeg behind a localhost page), so there are no ads, uploads, pop-ups or rate limits, unlike converter websites. It writes into real folders and can reveal files in Finder, which a website cannot.

## Operating Context

Opened from a Mac app launcher (`~/Applications/YouTube Converter.app`) or Spotlight; the page lives at http://127.0.0.1:8765 in the default browser. Typical flow: copy link from YouTube, paste, glance at the preview, toggle formats/quality, Convert, Show in Finder. Used in short bursts, light or dark system appearance.

## Capabilities and Constraints

- Link lookup with preview (thumbnail, title, channel, duration, license).
- Formats are multi-select: MP3 (128/192/320 kbps) and/or MP4 (available heights, 360p to 4K). One choice per quality row.
- Progress per format (download, convert/merge), errors in plain language, results list with Show in Finder.
- Single static page (`static/index.html`), no build step, no external runtime dependencies; fonts and icons are bundled. Backend API: `/api/info`, `/api/jobs`, `/api/jobs/<id>`, `/api/jobs/<id>/reveal/<n>`.
- Only YouTube links; no playlists or live streams.

## Brand Commitments

- Name: "YouTube Converter". Not affiliated with YouTube or Google; must not imitate YouTube's branding.
- App icon: blue rounded tile with a white download arrow (`docs/icon.png`).
- Bundled assets must stay openly licensed (Lato, Lucide). No Ajaib/PD design-system assets in this repo.

## Evidence on Hand

- Creative Commons test video: Big Buck Bunny (`aqz-KE-bpKQ`), CC BY 3.0, credited when shown.
- No testimonials, usage numbers or press; none may be invented.

## Product Principles

1. Speed of the task beats ornament: paste, pick, convert must stay as fast and obvious as it is now.
2. Tell the truth about quality (e.g. 320 kbps is not better than the source; >1080p may not play in QuickTime).
3. Local and honest: show where files went; never hide what the tool does.

## Accessibility & Inclusion

Controls must stay high-contrast and clearly clickable; the user explicitly rejects low-contrast, mushy neumorphism. Keyboard focus visible, reduced motion respected.
