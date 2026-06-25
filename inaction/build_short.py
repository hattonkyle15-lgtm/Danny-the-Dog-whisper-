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

Viral-grade craft (works on ANY footage):
  - top contrast scrim so white text always reads
  - white-flash cut transitions for snap/energy
  - animated pop-in ranking numbers
  - gentle Ken Burns push-in on every clip
Music: uses inaction/music.mp3 if present, else a soft placeholder pad.

INPUT CLIPS (drop real files in inaction/clips/; they override the placeholders):
  clip1.mp4  entertain522  "animal hugging"          -> shown as #3
  clip2.mp4  raquelcristal "runs to owner"           -> shown as #2
  clip3.mp4  vnphib        "dog seeing owner again"  -> shown as #4
  clip4.mp4  caballo       "horse resting head"      -> shown as #1 (+ 0.5s intro flash)

Tune START_AT to pick each clip's strongest in-point. Run: python3 inaction/build_short.py
"""

import argparse
import glob
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

# Export with NO audio so you can add licensed music in YouTube after upload.
# Set True (and optionally drop inaction/music.mp3) if you ever want baked-in audio.
INCLUDE_AUDIO = False

# In-point (seconds) into each clip for its strongest moment. Tune these.
# clip1=#3 fox(rescue), clip2=#2 dog(guards baby), clip3=#4 capybara family, clip4=#1 elephant(saves baby from croc)
START_AT = {"clip1.mp4": 54.0, "clip2.mp4": 20.0, "clip3.mp4": 4.0, "clip4.mp4": 1.0}

# Opening 0.5s flash points at the #1 clip's peak (the elephant rescue action).
INTRO_FLASH_AT = 3.5

# (name, clip, in-point, duration)
INTRO = ("intro", "clip4.mp4", INTRO_FLASH_AT, 0.5)
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
    (0.5,  3.0,  "Phrase", "Nobody gets\\Nleft behind"),
    (3.0,  5.5,  "Rank",  "#3"),
    (3.0,  5.5,  "Phrase", "He never\\Nforgot them"),
    (5.5,  8.5,  "Rank",  "#2"),
    (5.5,  8.5,  "Phrase", "He guards her\\Nlike his own"),
    (8.5,  14.5, "Rank",  "#1"),
    (8.5,  14.5, "Phrase", "A mom saved her baby\\Nfrom a crocodile"),
    (14.5, 15.5, "End",   "Which one made you cry?"),
    (14.5, 15.5, "Ends",  "#4   #3   #2   #1"),
]

# Generic ranking captions for --auto (volume) mode: emotional but content-agnostic,
# so they fit any animal clip without hand-writing per video. Same ranking format.
GENERIC_CUES = [
    (0.0,  0.5,  "Rank",  "#1 made me cry…"),
    (0.5,  3.0,  "Rank",  "#4"),
    (0.5,  3.0,  "Phrase", "Wait for it…"),
    (3.0,  5.5,  "Rank",  "#3"),
    (3.0,  5.5,  "Phrase", "This one hurts"),
    (5.5,  8.5,  "Rank",  "#2"),
    (5.5,  8.5,  "Phrase", "I wasn't ready"),
    (8.5,  14.5, "Rank",  "#1"),
    (8.5,  14.5, "Phrase", "Pure love"),
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
    # Colours &HAABBGGRR. White fill, black outline, heavy outline+shadow.
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
    pos = {"Rank": (540, 360), "Phrase": (540, 600),
           "End": (540, 820), "Ends": (540, 1000)}
    lines = []
    for start, end, style, text in CUES:
        x, y = pos[style]
        if style == "Rank" and " " in text:
            # intro flash line: lower, hard pop-in
            tag = f"{{\\an5\\pos(540,640)\\fad(60,80)\\fscx70\\fscy70\\t(0,140,\\fscx108\\fscy108)\\t(140,240,\\fscx100\\fscy100)}}"
        elif style == "Rank":
            # ranking number: spring pop-in
            tag = f"{{\\an5\\pos({x},{y})\\fad(70,120)\\fscx55\\fscy55\\t(0,170,\\fscx108\\fscy108)\\t(170,280,\\fscx100\\fscy100)}}"
        elif style == "Phrase":
            tag = f"{{\\an5\\pos({x},{y})\\fad(150,120)}}"
        else:  # End / Ends
            tag = f"{{\\an5\\pos({x},{y})\\fad(160,0)}}"
        lines.append(
            f"Dialogue: 0,{t(start)},{t(end)},{style},,0,0,0,,{tag}{text}")
    with open(path, "w") as f:
        f.write(header + "\n".join(lines) + "\n")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        sys.exit(f"ffmpeg failed: {' '.join(str(c) for c in cmd[:6])} ...")


def make_scrim():
    """Top gradient scrim (darkens top third) so white text reads on any clip."""
    out = os.path.join(TMP, "scrim.png")
    run([FF, "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}",
         "-vf", "format=rgba,geq=r=0:g=0:b=0:a='clip(155*(1-Y/800),0,155)'",
         "-frames:v", "1", out])
    return out


VIDEO_EXTS = {".mp4", ".mov", ".m4v", ".avi", ".mkv", ".webm"}
SEARCH_DIRS = [CLIPS, HERE]            # look in clips/ first, then the project folder
NAME_PATTERNS = ["clip{n}", "clip {n}", "clip_{n}", "clip-{n}", "clip {n} ", "clip{n} "]


def resolve_src(clip):
    """Find clipN no matter the spacing/case/extension, in clips/ or the project folder.
    Real files always win; the bundled *.placeholder.mp4 is the fallback."""
    n = "".join(ch for ch in os.path.splitext(clip)[0] if ch.isdigit())
    for d in SEARCH_DIRS:
        for pat in NAME_PATTERNS:
            stem = pat.format(n=n).strip()
            for f in sorted(glob.glob(os.path.join(d, stem + ".*"))):
                if ".placeholder." in os.path.basename(f).lower():
                    continue
                if os.path.splitext(f)[1].lower() in VIDEO_EXTS:
                    return f
    placeholder = os.path.join(CLIPS, f"clip{n}.placeholder.mp4")
    if os.path.exists(placeholder):
        print(f"  (using placeholder for clip{n} — add your clip {n} to use real footage)")
        return placeholder
    sys.exit(f"Could not find a video for clip {n} (looked for 'clip {n}.*' in {CLIPS} and {HERE})")


# Source clips have the original creator's captions burned in. Crop this many
# pixels off the top / bottom of each to remove them (subject stays centre-frame).
CROP_TOP = {"clip2.mp4": 625, "clip4.mp4": 225}
CROP_BOTTOM = {"clip1.mp4": 300, "clip4.mp4": 330}
# Clips whose subject is a short, wide strip boxed in by burned-in captions/badges:
# crop the captions off, then show the WHOLE strip fitted over a blurred fill so
# the subject is never sliced. dict = pixels cropped off (top,bottom,left,right).
FIT_BLUR = {}


def normalize_clip(name, clip, ss, dur, scrim, zoom=True, flash=True):
    src = resolve_src(clip)
    # Decimate to FPS FIRST (sources may be 60fps; zoompan maps 1 output frame
    # per input frame, so without this every segment comes out 2x too long).
    # Then a gentle Ken Burns push-in (~7% over the segment).
    zp = (f"fps={FPS},zoompan=z='min(1+0.00045*on,1.12)':d=1:"
          f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}"
          if zoom else f"fps={FPS}")
    fade = ",fade=t=in:st=0:d=0.10:color=white" if flash else ""
    if clip in FIT_BLUR:
        c = FIT_BLUR[clip]
        crop = (f"crop=iw-{c['left']+c['right']}:ih-{c['top']+c['bottom']}:"
                f"{c['left']}:{c['top']}")
        fc = (f"[0:v]{crop},split=2[fg][bg];"
              f"[bg]scale={W}:{H}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H},gblur=sigma=24[bg2];"
              f"[fg]scale={W}:{H}:force_original_aspect_ratio=decrease[fg2];"
              f"[bg2][fg2]overlay=(W-w)/2:(H-h)/2,setsar=1,{zp}[z];"
              f"[z][1:v]overlay=0:0{fade},format=yuv420p[o]")
    else:
        ct = CROP_TOP.get(clip, 0)
        cb = CROP_BOTTOM.get(clip, 0)
        pre = f"crop=iw:ih-{ct + cb}:0:{ct}," if (ct or cb) else ""
        fc = (f"[0:v]{pre}scale={W}:{H}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H},setsar=1,{zp}[z];"
              f"[z][1:v]overlay=0:0{fade},format=yuv420p[o]")
    out = os.path.join(TMP, f"{name}.mp4")
    run([FF, "-y", "-ss", str(ss), "-t", str(dur), "-i", src, "-i", scrim,
         "-filter_complex", fc, "-map", "[o]", "-an", "-r", str(FPS),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "veryfast",
         "-profile:v", "high", "-level", "4.0", out])
    return out


def end_screen():
    out = os.path.join(TMP, "end.mp4")
    run([FF, "-y", "-f", "lavfi", "-t", str(END_DUR),
         "-i", f"color=c=0x14141e:s={W}x{H}:r={FPS}",
         "-vf", "fade=t=in:st=0:d=0.12:color=white,format=yuv420p",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "veryfast",
         "-profile:v", "high", "-level", "4.0", out])
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
    ap = argparse.ArgumentParser(description="Build a Top-4 ranking Short.")
    ap.add_argument("--clips", help="folder holding clip1..clip4 (default: clips/)")
    ap.add_argument("--out", help="output mp4 path (default: final_short.mp4)")
    ap.add_argument("--auto", action="store_true",
                    help="volume mode: generic captions, no hand-tuned in-points/crops")
    args = ap.parse_args()

    global CLIPS, OUT, TMP, START_AT, INTRO, SEGMENTS, TOTAL
    global CUES, CROP_TOP, CROP_BOTTOM, FIT_BLUR
    if args.clips:
        CLIPS = os.path.abspath(args.clips)
    if args.out:
        OUT = os.path.abspath(args.out)
        TMP = os.path.join(os.path.dirname(OUT), "_build")
    if args.auto:
        # Rough cuts for the daily batch: start each clip at 0, no caption crops,
        # generic emotional captions. Re-cut winners by hand afterwards.
        START_AT = {f"clip{i}.mp4": 0.0 for i in range(1, 5)}
        CROP_TOP, CROP_BOTTOM, FIT_BLUR = {}, {}, {}
        CUES = GENERIC_CUES
        INTRO = ("intro", "clip4.mp4", 0.3, 0.5)
        SEGMENTS = [
            ("seg4", "clip3.mp4", 0.0, 2.5),
            ("seg3", "clip1.mp4", 0.0, 2.5),
            ("seg2", "clip2.mp4", 0.0, 3.0),
            ("seg1", "clip4.mp4", 0.0, 6.0),
        ]
        TOTAL = INTRO[3] + sum(s[3] for s in SEGMENTS) + END_DUR

    os.makedirs(TMP, exist_ok=True)
    scrim = make_scrim()
    pieces = [normalize_clip(*INTRO, scrim, zoom=True, flash=False)]
    for seg in SEGMENTS:
        pieces.append(normalize_clip(*seg, scrim))
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

    if INCLUDE_AUDIO:
        audio = build_audio(TOTAL)
        run([FF, "-y", "-i", titled, "-i", audio,
             "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
             "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
             "-shortest", OUT])
    else:
        # Silent export — add music in YouTube after upload.
        run([FF, "-y", "-i", titled, "-an", "-c:v", "copy",
             "-movflags", "+faststart", OUT])

    info = subprocess.run([FF, "-i", OUT], capture_output=True, text=True).stderr
    print(f"\nDONE -> {OUT}\nPlanned: {TOTAL:.1f}s  {W}x{H} @ {FPS}fps")
    for line in info.splitlines():
        if "Duration" in line or "Stream" in line:
            print("  " + line.strip())


if __name__ == "__main__":
    main()
