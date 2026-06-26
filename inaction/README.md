# Top 4 Animal Moments — YouTube Short builder

A complete, ready-to-run pipeline that assembles a **15.5s, 1080×1920 (9:16)**
viral ranking Short from 4 clips: a 0.5s cold-open flash of #1, ranked segments
#4 → #1 with bold high-contrast text, an end card, and background music.

## Status of the deliverables in this folder

| File | What it is |
|------|------------|
| `final_short.mp4` | **Working render** — built from the labeled PLACEHOLDER clips in `clips/`. It proves the exact timing, framing, text and audio. Re-render after dropping in the real footage to get the final upload file. |
| `build_short.py` | The full editing pipeline (crop/scale, ranking, timed ASS text, music, mux). |
| `upload_info.txt` | Title, description, hashtags, pinned comment, category, ranking rationale. |
| `clips/` | Ships with `clip1.placeholder.mp4`…`clip4.placeholder.mp4`. Drop real `clip1.mp4`…`clip4.mp4` here and they automatically override the placeholders. |

## ⚠️ The one thing I could not do (and why)

The 4 sources are TikTok URLs. In this environment **`www.tiktok.com` is blocked
by the organization egress policy** — the proxy returns `403` on CONNECT, and I
am not allowed to bypass a policy denial. So I cannot download the source
footage here. Everything else (the editor, timing, text, music, export) is done
and verified; you only need to supply the 4 video files.

> Note: re-uploading other creators' clips to your own channel may require their
> permission / a license. Make sure you have the rights before publishing.

## How to finish it (1 minute)

1. Get the 4 clips as MP4s. On a machine with normal internet:
   ```bash
   pip install yt-dlp
   yt-dlp -o clip1.mp4 "https://www.tiktok.com/@entertain522/video/7601930178406780190"
   yt-dlp -o clip2.mp4 "https://www.tiktok.com/@raquelcristal02/video/7642525907751603469"
   yt-dlp -o clip3.mp4 "https://www.tiktok.com/@vnphib/video/7616668946967678238"
   yt-dlp -o clip4.mp4 "https://www.tiktok.com/@caballochristina/video/7340468170538503467"
   ```
2. Put them in `inaction/clips/` named `clip1.mp4`…`clip4.mp4`. They override
   the bundled `*.placeholder.mp4` files automatically — no need to delete them.
3. (Optional) Drop an emotional, licensed track at `inaction/music.mp3`.
   Without it, a soft placeholder pad is generated.
4. (Optional) Pick the best moment of each clip by editing `START_AT` (in-point
   seconds) near the top of `build_short.py`.
5. Render:
   ```bash
   python3 inaction/build_short.py      # ffmpeg via `pip install imageio-ffmpeg`
   ```
   Output: `inaction/final_short.mp4`.

## Clip → ranking map

| File | Source | Shown as | On-screen text |
|------|--------|----------|----------------|
| clip3 | vnphib (dog reunion) | **#4** | He remembered her |
| clip1 | entertain522 (hug) | **#3** | This hug says everything |
| clip2 | raquelcristal (runs to owner) | **#2** | The baby came running back |
| clip4 | caballo (horse head rest) | **#1** | This is pure love (+0.5s intro flash) |

## Exact timeline (15.5s)

```
0.0–0.5   flash of #1            "#1 made me cry…"
0.5–3.0   #4 (clip3)            "#4  He remembered her"
3.0–5.5   #3 (clip1)            "#3  This hug says everything"
5.5–8.5   #2 (clip2)            "#2  The baby came running back"
8.5–14.5  #1 (clip4)            "#1  This is pure love"
14.5–15.5 end card             "Which one hit hardest?"
```
