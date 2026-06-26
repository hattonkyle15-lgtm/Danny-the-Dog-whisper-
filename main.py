#!/usr/bin/env python3
"""
The Unmarked — faceless dark-history content engine.

A fully-automated pipeline: it brainstorms video ideas, lets you pick the
winners (or auto-picks the highest-scoring one), then writes a complete,
ready-to-produce package for each — long-form narration script, funnel Shorts,
and full packaging (titles, thumbnail, description, tags).

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...

    # Brainstorm a ranked batch of ideas (cheap, fast):
    python main.py ideas
    python main.py ideas --seed "Cold War" --count 15

    # Take the single best idea and produce the full package end-to-end:
    python main.py auto
    python main.py auto --seed "shipwrecks"

    # Produce full packages for the top N ideas of a batch:
    python main.py batch --top 3 --seed "ancient Rome"

Output lands in output/<slug>/ as package.json + production-brief.md.
"""

from __future__ import annotations

import argparse
import sys

from config import CONFIG
from engine import stages
from engine.pipeline import build_package, save_package


def cmd_ideas(args: argparse.Namespace) -> None:
    ideas = stages.brainstorm_ideas(seed=args.seed, count=args.count)
    print(f"\n💡 {len(ideas)} ideas for {CONFIG.name} (ranked):\n")
    for i, idea in enumerate(ideas, 1):
        print(f"  [{idea.virality_score:>3}] {i}. {idea.title_working}")
        print(f"        hook: {idea.hook}")
        print(f"        why:  {idea.why_it_works}")
        if idea.sensitivity_note.lower() != "none":
            print(f"        ⚠️  {idea.sensitivity_note}")
        print()


def cmd_auto(args: argparse.Namespace) -> None:
    print(f"🧠 Brainstorming ideas{f' on {args.seed!r}' if args.seed else ''}...")
    ideas = stages.brainstorm_ideas(seed=args.seed, count=args.count)
    best = ideas[0]
    print(f"🏆 Best idea ({best.virality_score}/100): {best.title_working}\n")
    print(f"🏗️  Building full package for: {best.title_working}")
    pkg = build_package(best)
    out = save_package(pkg)
    print(f"\n✅ Done. Production brief: {out / 'production-brief.md'}")


def cmd_batch(args: argparse.Namespace) -> None:
    print(f"🧠 Brainstorming ideas{f' on {args.seed!r}' if args.seed else ''}...")
    ideas = stages.brainstorm_ideas(seed=args.seed, count=max(args.count, args.top))
    chosen = ideas[: args.top]
    print(f"🏗️  Building full packages for the top {len(chosen)} ideas...\n")
    for n, idea in enumerate(chosen, 1):
        print(f"[{n}/{len(chosen)}] {idea.title_working}")
        pkg = build_package(idea)
        out = save_package(pkg)
        print(f"    ✅ {out}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=f"{CONFIG.name} content engine")
    sub = parser.add_subparsers(dest="command", required=True)

    p_ideas = sub.add_parser("ideas", help="Brainstorm a ranked batch of video ideas")
    p_ideas.add_argument("--seed", help="Optional theme to constrain the batch")
    p_ideas.add_argument("--count", type=int, default=12)
    p_ideas.set_defaults(func=cmd_ideas)

    p_auto = sub.add_parser("auto", help="Brainstorm + produce the single best idea")
    p_auto.add_argument("--seed", help="Optional theme")
    p_auto.add_argument("--count", type=int, default=12)
    p_auto.set_defaults(func=cmd_auto)

    p_batch = sub.add_parser("batch", help="Produce full packages for the top N ideas")
    p_batch.add_argument("--top", type=int, default=3)
    p_batch.add_argument("--seed", help="Optional theme")
    p_batch.add_argument("--count", type=int, default=12)
    p_batch.set_defaults(func=cmd_batch)

    args = parser.parse_args()
    try:
        args.func(args)
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()
