# Daily Shorts automation (runs on YOUR Mac)

This makes **5 ranking Shorts every morning** from TikTok links. It runs on your
Mac because TikTok is **blocked inside Claude's cloud environment** (org network
policy — I can't download from TikTok there, which is why you've been uploading
clips by hand). On your Mac, TikTok works normally.

> **Honest expectations:** automation gives you *volume and consistency*, not a
> guarantee of 1,000,000 views — no tool can promise that. These are ROUGH cuts
> (each clip starts at 0:00 with generic captions). The plan is **Hybrid**: the
> script mass-produces, you skim them, flag the best 1–2, and I re-cut those by
> hand (good in-points + custom captions) for posting. Hand-cut > auto-cut for
> retention every time.

## One-time setup
```bash
brew install yt-dlp ffmpeg python
pip3 install imageio-ffmpeg          # fallback ffmpeg for the renderer
cd ~/Desktop/Danny-the-Dog-whisper-/inaction   # wherever you cloned it
chmod +x make_daily.sh
```

## Each day
1. Put 20 TikTok URLs in `daily_links.txt` (one per line). **Every 4 links = one
   Short**, and within each group the order is the ranking:
   `link1→#4, link2→#3, link3→#2, link4→#1`. **Put the best clip 4th** in each group.
2. Run:
   ```bash
   ./make_daily.sh
   ```
3. Find the results in `daily/<today>/short_01.mp4 … short_05.mp4` (silent, 9:16).
4. Watch them, pick the 1–2 strongest, and send those to me to polish.

## Make it run automatically at 7:00 AM (launchd)
1. Edit `com.kyle.makedaily.plist` (in this folder) and set the **full path** to
   `make_daily.sh` (e.g. `/Users/kyle/Desktop/Danny-the-Dog-whisper-/inaction/make_daily.sh`).
2. Install it:
   ```bash
   cp com.kyle.makedaily.plist ~/Library/LaunchAgents/
   launchctl load ~/Library/LaunchAgents/com.kyle.makedaily.plist
   ```
   It will run every day at 7:00 AM. Logs go to `daily/cron.log`.
   To stop: `launchctl unload ~/Library/LaunchAgents/com.kyle.makedaily.plist`.

## Sourcing clips without hand-picking URLs (optional)
`yt-dlp` can pull the latest videos from a creator or hashtag page, e.g.:
```bash
yt-dlp --playlist-end 4 -o "raw/%(id)s.%(ext)s" "https://www.tiktok.com/@SOME_ANIMAL_ACCOUNT"
```
Quality of auto-picked clips is hit-or-miss, so treat anything sourced this way
as raw material to review — not finished posts.

## Copyright / ToS note
Reposting other creators' TikToks to a channel you monetize can violate
copyright and TikTok's Terms. For studying the pipeline and retention this is
fine; before publishing at scale, use clips you have rights to (your own,
licensed, or creators who allow reposting with credit).
