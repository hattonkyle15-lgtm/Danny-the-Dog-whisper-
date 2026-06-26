#!/usr/bin/env python3
"""make_set.py — batch-build several ranking Shorts from a few source compilations.

Each short pulls 4 moments (slot -> (source, in-point seconds)) where the slot
maps to a rank:  clip4=#1(+flash)  clip2=#2  clip1=#3  clip3=#4.
phrases are listed in display order [#4, #3, #2, #1].
"""
import os
import shutil
import build_short as b

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = {k: os.path.join(HERE, "clips", f"{k}.mp4") for k in ("X", "Y", "Z")}
OUTDIR = os.path.join(HERE, "set6")
os.makedirs(OUTDIR, exist_ok=True)

# (slot, source, in-point). Slots: clip4=#1, clip2=#2, clip1=#3, clip3=#4.
SHORTS = [
    dict(out="short_1.mp4", intro="#1 made me laugh…", end="Which one got you?",
         slots={"clip3": ("Z", 0.0), "clip1": ("Y", 9.0), "clip2": ("X", 42.0), "clip4": ("X", 30.0)},
         flash=31.0,
         phrases=["Living his\\nbest life", "10/10\\nno notes", "Pure chaos", "Main\\ncharacter"]),
    dict(out="short_2.mp4", intro="#1 sent me…", end="Which one got you?",
         slots={"clip3": ("X", 0.0), "clip1": ("Y", 21.0), "clip2": ("X", 15.0), "clip4": ("Z", 30.0)},
         flash=31.0,
         phrases=["Majestic boy", "Too cute\\nto handle", "Pool party", "Best day\\never"]),
    dict(out="short_3.mp4", intro="#1 broke me…", end="Which one got you?",
         slots={"clip3": ("X", 33.0), "clip1": ("Z", 18.0), "clip2": ("Y", 15.0), "clip4": ("Y", 30.0)},
         flash=30.0,
         phrases=["Wind in\\nhis fur", "Found the\\nbest park", "Caught in 4K", "Absolute\\nunit"]),
    dict(out="short_4.mp4", intro="#1 is unreal…", end="Which one got you?",
         slots={"clip3": ("Z", 42.0), "clip1": ("X", 18.0), "clip2": ("X", 54.0), "clip4": ("X", 12.0)},
         flash=13.0,
         phrases=["Good boy", "Ball is\\nlife", "Caught him", "Zoomies\\nchampion"]),
    dict(out="short_5.mp4", intro="#1 had me dead…", end="Which one got you?",
         slots={"clip3": ("Y", 42.0), "clip1": ("Z", 54.0), "clip2": ("X", 39.0), "clip4": ("X", 30.0)},
         flash=31.0,
         phrases=["He has\\nno notes", "Garden\\npatrol", "Unbothered", "Main\\ncharacter"]),
    dict(out="short_6.mp4", intro="#1 got me…", end="Which one got you?",
         slots={"clip3": ("Z", 6.0), "clip1": ("Y", 33.0), "clip2": ("X", 21.0), "clip4": ("Z", 30.0)},
         flash=31.0,
         phrases=["Living the\\ndream", "Tiny\\nacrobat", "Big mood", "Best day\\never"]),
]


def cues_for(intro, phrases, end):
    return [
        (0.0, 0.5, "Rank", intro),
        (0.5, 3.0, "Rank", "#4"), (0.5, 3.0, "Phrase", phrases[0]),
        (3.0, 5.5, "Rank", "#3"), (3.0, 5.5, "Phrase", phrases[1]),
        (5.5, 8.5, "Rank", "#2"), (5.5, 8.5, "Phrase", phrases[2]),
        (8.5, 14.5, "Rank", "#1"), (8.5, 14.5, "Phrase", phrases[3]),
        (14.5, 15.5, "End", end), (14.5, 15.5, "Ends", "#4   #3   #2   #1"),
    ]


def run_short(s):
    for slot, (src, _) in s["slots"].items():
        shutil.copy(SRC[src], os.path.join(HERE, "clips", f"{slot}.mp4"))
    sa = {slot: t for slot, (_, t) in s["slots"].items()}
    b.START_AT = {f"{k}.mp4": v for k, v in sa.items()}
    b.INTRO = ("intro", "clip4.mp4", s["flash"], 0.5)
    b.SEGMENTS = [
        ("seg4", "clip3.mp4", sa["clip3"], 2.5),
        ("seg3", "clip1.mp4", sa["clip1"], 2.5),
        ("seg2", "clip2.mp4", sa["clip2"], 3.0),
        ("seg1", "clip4.mp4", sa["clip4"], 6.0),
    ]
    b.TOTAL = 15.5
    b.CUES = cues_for(s["intro"], s["phrases"], s["end"])
    # Per-source bottom crop to strip burned-in captions (Z has tall 2-line
    # captions; X/Y are lighter). Subject stays centre-frame after the re-fill.
    src_crop = {"X": 300, "Y": 320, "Z": 540}
    b.CROP_TOP = {}
    b.CROP_BOTTOM = {f"{slot}.mp4": src_crop[src] for slot, (src, _) in s["slots"].items()}
    b.FIT_BLUR = {}
    b.OUT = os.path.join(OUTDIR, s["out"])
    b.TMP = os.path.join(OUTDIR, "_build")
    b.build()


if __name__ == "__main__":
    import sys
    only = sys.argv[1:] or [s["out"] for s in SHORTS]
    for s in SHORTS:
        if s["out"] in only:
            print(f"=== {s['out']} ===")
            run_short(s)
