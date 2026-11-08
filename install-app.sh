#!/usr/bin/env bash
# Build "YouTube Converter.app" in ~/Applications: a launcher that starts the local
# server in the background (if it isn't already running) and opens it in your browser.
# Find it with Spotlight or Launchpad, or drag it to the Dock. Re-run after moving this folder.
set -euo pipefail
PROJECT="$(cd "$(dirname "$0")" && pwd)"
APP="$HOME/Applications/YouTube Converter.app"
PORT=8765

rm -rf "$APP"
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources"

cat > "$APP/Contents/Info.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>CFBundleName</key><string>YouTube Converter</string>
  <key>CFBundleDisplayName</key><string>YouTube Converter</string>
  <key>CFBundleIdentifier</key><string>io.github.randyvarianda.yt-converter</string>
  <key>CFBundleExecutable</key><string>launch</string>
  <key>CFBundleIconFile</key><string>AppIcon</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>1.0</string>
  <key>LSUIElement</key><true/>
</dict></plist>
EOF

cat > "$APP/Contents/MacOS/launch" <<EOF
#!/usr/bin/env bash
# Apps opened from Finder get a bare PATH; add Homebrew so ffmpeg and node are found.
export PATH="/opt/homebrew/bin:/usr/local/bin:\$PATH"
URL="http://127.0.0.1:$PORT"
LOG="\$HOME/Library/Logs/yt-converter.log"
if ! curl -s -o /dev/null --max-time 1 "\$URL/"; then
  nohup "$PROJECT/run.sh" $PORT >>"\$LOG" 2>&1 &
  for _ in \$(seq 1 120); do   # first run installs yt-dlp, so allow up to a minute
    curl -s -o /dev/null --max-time 1 "\$URL/" && break
    sleep 0.5
  done
fi
if curl -s -o /dev/null --max-time 1 "\$URL/"; then
  open "\$URL"
else
  osascript -e 'display alert "YouTube Converter could not start" message "See ~/Library/Logs/yt-converter.log for details."'
fi
EOF
chmod +x "$APP/Contents/MacOS/launch"

# Icon: render docs/icon.png (if present) into an .icns.
if [ -f "$PROJECT/docs/icon.png" ]; then
  ICONSET="$(mktemp -d)/AppIcon.iconset"
  mkdir -p "$ICONSET"
  for s in 16 32 128 256 512; do
    sips -z $s $s "$PROJECT/docs/icon.png" --out "$ICONSET/icon_${s}x${s}.png" >/dev/null
    sips -z $((s * 2)) $((s * 2)) "$PROJECT/docs/icon.png" --out "$ICONSET/icon_${s}x${s}@2x.png" >/dev/null
  done
  iconutil -c icns "$ICONSET" -o "$APP/Contents/Resources/AppIcon.icns"
fi

touch "$APP"  # refresh Finder/Spotlight
echo "Installed: $APP"
echo "Open it from Spotlight (\"YouTube Converter\"), or drag it to the Dock."
echo "Stop the server:  pkill -f '$PROJECT/server.py'"
