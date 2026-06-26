#!/usr/bin/env bash
# make_daily.sh — pull TikToks, batch them in 4s, render ranking Shorts.
#
# Usage:   ./make_daily.sh [links_file]        (default: daily_links.txt)
# Output:  daily/<YYYY-MM-DD>/short_01.mp4 ... short_05.mp4   (silent, 1080x1920)
#
# Each GROUP OF 4 links = one Short. Within a group the order is the ranking:
#   link 1 -> #4   link 2 -> #3   link 3 -> #2   link 4 -> #1 (best, gets the flash)
# So put the strongest/most emotional clip 4th in each group (4th, 8th, 12th...).
#
# These are ROUGH auto-cuts (each clip starts at 0:00, generic captions). Review
# them, pick the 1-2 best, and have Claude re-cut those by hand for posting.

set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
LINKS="${1:-$ROOT/daily_links.txt}"
DAY="$(date +%Y-%m-%d)"
OUT="$ROOT/daily/$DAY"
RAW="$OUT/raw"
mkdir -p "$RAW"

command -v yt-dlp >/dev/null 2>&1 || { echo "yt-dlp not found. Run: brew install yt-dlp ffmpeg"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "python3 not found."; exit 1; }
[ -f "$LINKS" ] || { echo "No links file at $LINKS (one TikTok URL per line)."; exit 1; }

echo "== Downloading clips from $LINKS =="
i=0
while IFS= read -r url || [ -n "$url" ]; do
  url="$(printf '%s' "$url" | tr -d '[:space:]')"
  [ -z "$url" ] && continue
  case "$url" in \#*) continue ;; esac
  i=$((i+1))
  printf '[%d] %s\n' "$i" "$url"
  yt-dlp --no-warnings -f "mp4/best" -o "$RAW/clip_$i.%(ext)s" "$url" \
    || echo "   !! download failed, skipping"
done < "$LINKS"
echo "Got source files for ~$i links."

echo "== Rendering Shorts (groups of 4) =="
made=0
b=1
while :; do
  s=$(( (b - 1) * 4 + 1 ))
  ok=1
  for k in 0 1 2 3; do
    [ -z "$(ls "$RAW"/clip_$((s + k)).* 2>/dev/null | head -1)" ] && ok=0
  done
  [ "$ok" -eq 0 ] && break

  bdir="$OUT/batch_$b"; mkdir -p "$bdir"
  for k in 0 1 2 3; do
    f="$(ls "$RAW"/clip_$((s + k)).* | head -1)"
    cp "$f" "$bdir/clip_$((k + 1)).mp4"
  done

  short="$OUT/short_$(printf '%02d' "$b").mp4"
  echo "[batch $b] -> $short"
  if python3 "$ROOT/build_short.py" --auto --clips "$bdir" --out "$short"; then
    made=$((made + 1))
  else
    echo "   !! render failed for batch $b"
  fi
  b=$((b + 1))
done

echo ""
echo "DONE: $made short(s) in $OUT"
ls "$OUT"/short_*.mp4 2>/dev/null || echo "(none — check that you have at least 4 working links)"
