#!/usr/bin/env python3
"""
build_short.py — Assemble the "Top 4 Animal Moments That Will Make You Cry" YouTube Short.

Output: inaction/final_short.mp4  (15.5s, 1080x1920, 9:16)
  - 0.0-0.5s  : flash of the #1 moment  ("#1 made me cry…")  -> swipe-stopper
  - 0.5-3.0s  : #4  "He remembered her"
  - 3.0-5.5s  : #3  "This hug says everything"
  - 5.5-8.5s  : #2  "The baby came running back"
  - 8.5-14.5s : #1  "This is pure love"
  - 14.5-15.5s: end screen  ("Which one hit hardest?")
Music: uses inaction/music.mp3 if present, else a soft placeholder pad.

INPUT CLIPS (drop real files in inaction/clips/, overwriting placeholders):
  clip1.mp4  entertain522  "animal hugging"          -> shown as #3
  clip2.mp4  raquelcristal "runs to owner"           -> shown as #2
  clip3.mp4  vnphib        "dog seeing owner again"  -> shown as #4
  clip4.mp4  caballo       "horse resting head"      -> shown as #1 (+ 0.5s intro flash)

Tune START_AT to pick each clip's strongest in-point. Run: python3 inaction/build_short.py
"""

import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS = os.path.join(HERE, "clips")
TMP = os.path.join(HERE, "build")
OUT = os.path.join(HERE, "final_short.mp4")
MUSIC = os.path.join(HERE, "music.mp3")
W, H, FPS = 1080, 1920, 30


def ffmpeg_bin():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("ffmpeg not found. Install it or `pip install imageio-ffmpeg`.")


FF = ffmpeg_bin()

# In-point (seconds) into each clip for its strongest moment. Tune these.
START_AT = {"clip1.mp4": 0.0, "clip2.mp4": 0.0, "clip3.mp4": 0.0, "clip4.mp4": 0.0}

# (name, clip, in-point, duration)
INTRO = ("intro", "clip4.mp4", START_AT["clip4.mp4"], 0.5)
SEGMENTS = [
    ("seg4", "clip3.mp4", START_AT["clip3.mp4"], 2.5),
    ("seg3", "clip1.mp4", START_AT["clip1.mp4"], 2.5),
    ("seg2", "clip2.mp4", START_AT["clip2.mp4"], 3.0),
    ("seg1", "clip4.mp4", START_AT["clip4.mp4"], 6.0),
]
END_DUR = 1.0
TOTAL = INTRO[3] + sum(s[3] for s in SEGMENTS) + END_DUR  # 15.5s

# Timed text cues: (start, end, style, text). \N = line break.
CUES = [
    (0.0,  0.5,  "Rank",  "#1 made me cry…"),
    (0.5,  3.0,  "Rank",  "#4"),
    (0.5,  3.0,  "Phrase", "He remembered her"),
    (3.0,  5.5,  "Rank",  "#3"),
    (3.0,  5.5,  "Phrase", "This hug says\\Neverything"),
    (5.5,  8.5,  "Rank",  "#2"),
    (5.5,  8.5,  "Phrase", "The baby came\\Nrunning back"),
    (8.5,  14.5, "Rank",  "#1"),
    (8.5,  14.5, "Phrase", "This is pure love"),
    (14.5, 15.5, "End",   "Which one hit hardest?"),
    (14.5, 15.5, "Ends",  "#4   #3   #2   #1"),
]


def t(sec):
    cs = int(round(sec * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def write_ass(path):
    # Colours are &HAABBGGRR (AA=00 opaque). White fill, black outline, heavy
    # outline + shadow for readability over bright footage. Anchor = centre (an5).
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Rank,DejaVu Sans,150,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,4,5,40,40,40,1
Style: Phrase,DejaVu Sans,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,3,5,40,40,40,1
Style: End,DejaVu Sans,92,&H0066E0FF,&H0066E0FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,4,5,40,40,40,1
Style: Ends,DejaVu Sans,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,3,5,40,40,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    # Per-style on-screen centre position (x=540 centre).
    pos = {"Rank": (540, 360), "Phrase": (540, 600),
           "End": (540, 820), "Ends": (540, 1000)}
    # The intro single-line uses the Rank style but lower on screen.
    lines = []
    for start, end, style, text in CUES:
        x, y = pos[style]
        if style == "Rank" and text.startswith("#1 made me cry"):
            y = 640
        tag = f"{{\\an5\\pos({x},{y})\\fad(120,120)}}"
        lines.append(
            f"Dialogue: 0,{t(start)},{t(end)},{style},,0,0,0,,{tag}{text}")
    with open(path, "w") as f:
        f.write(header + "\n".join(lines) + "\n")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        sys.exit(f"ffmpeg failed: {' '.join(str(c) for c in cmd[:6])} ...")


def resolve_src(clip):
    real = os.path.join(CLIPS, clip)
    if os.path.exists(real):
        return real
    placeholder = os.path.join(CLIPS, clip.replace(".mp4", ".placeholder.mp4"))
    if os.path.exists(placeholder):
        print(f"  (using placeholder for {clip} — drop a real {clip} in clips/ to override)")
        return placeholder
    sys.exit(f"Missing source clip: {real}")


def normalize_clip(name, clip, ss, dur):
    src = resolve_src(clip)
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
          f"crop={W}:{H},setsar=1,fps={FPS},format=yuv420p")
    out = os.path.join(TMP, f"{name}.mp4")
    run([FF, "-y", "-ss", str(ss), "-t", str(dur), "-i", src,
         "-vf", vf, "-an", "-r", str(FPS),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "veryfast",
         "-profile:v", "high", "-level", "4.0", out])
    return out


def end_screen():
    out = os.path.join(TMP, "end.mp4")
    run([FF, "-y", "-f", "lavfi", "-t", str(END_DUR),
         "-i", f"color=c=0x14141e:s={W}x{H}:r={FPS}",
         "-vf", "format=yuv420p", "-c:v", "libx264", "-pix_fmt", "yuv420p",
         "-preset", "veryfast", "-profile:v", "high", "-level", "4.0", out])
    return out


def build_audio(total):
    out = os.path.join(TMP, "audio.m4a")
    fade = max(0.0, total - 1.2)
    if os.path.exists(MUSIC):
        run([FF, "-y", "-stream_loop", "-1", "-i", MUSIC, "-t", str(total),
             "-af", f"afade=t=in:st=0:d=0.4,afade=t=out:st={fade}:d=1.2,volume=0.9",
             "-c:a", "aac", "-b:a", "192k", out])
    else:  # soft ambient placeholder — replace with licensed emotional music
        run([FF, "-y", "-f", "lavfi", "-t", str(total),
             "-i", "sine=frequency=220:sample_rate=44100",
             "-f", "lavfi", "-t", str(total),
             "-i", "sine=frequency=330:sample_rate=44100",
             "-filter_complex",
             f"[0][1]amix=inputs=2,tremolo=f=4:d=0.5,lowpass=f=900,"
             f"volume=0.10,afade=t=in:st=0:d=0.5,afade=t=out:st={fade}:d=1.2[a]",
             "-map", "[a]", "-c:a", "aac", "-b:a", "160k", out])
    return out


def main():
    os.makedirs(TMP, exist_ok=True)
    pieces = [normalize_clip(*INTRO)]
    for seg in SEGMENTS:
        pieces.append(normalize_clip(*seg))
    pieces.append(end_screen())

    listfile = os.path.join(TMP, "concat.txt")
    with open(listfile, "w") as f:
        for p in pieces:
            f.write(f"file '{p}'\n")
    raw = os.path.join(TMP, "video_notext.mp4")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", listfile, "-c", "copy", raw])

    ass = os.path.join(TMP, "overlay.ass")
    write_ass(ass)
    titled = os.path.join(TMP, "video.mp4")
    run([FF, "-y", "-i", raw, "-vf", f"ass='{ass}'",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium",
         "-crf", "19", "-profile:v", "high", "-level", "4.0", titled])

    audio = build_audio(TOTAL)
    run([FF, "-y", "-i", titled, "-i", audio,
         "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
         "-shortest", OUT])

    info = subprocess.run([FF, "-i", OUT], capture_output=True, text=True).stderr
    print(f"\nDONE -> {OUT}\nPlanned: {TOTAL:.1f}s  {W}x{H} @ {FPS}fps")
    for line in info.splitlines():
        if "Duration" in line or "Stream" in line:
            print("  " + line.strip())


if __name__ == "__main__":
    main()
