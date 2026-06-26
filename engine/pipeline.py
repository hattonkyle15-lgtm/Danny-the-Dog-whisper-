"""Orchestration: topic/idea -> complete VideoPackage, saved to disk."""

from __future__ import annotations

import json
import re
from pathlib import Path

from config import CONFIG, ChannelConfig
from . import stages
from .models import VideoIdea, VideoPackage


def _slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:60] or "untitled"


def build_package(idea: VideoIdea, cfg: ChannelConfig = CONFIG) -> VideoPackage:
    """Run all generation stages for a single chosen idea.

    Order matters: the script is written first, then Shorts and packaging are
    derived from it so they stay faithful to the actual video.
    """
    print(f"  ✍️  Writing long-form script for: {idea.title_working}")
    script = stages.write_script(idea, cfg)

    print(f"  🎬  Cutting {cfg.shorts_per_video} Shorts from the script...")
    shorts = stages.write_shorts(idea, script, cfg)

    print("  📦  Writing titles / thumbnail / description / tags...")
    packaging = stages.write_packaging(idea, script, cfg)

    return VideoPackage(idea=idea, script=script, shorts=shorts, packaging=packaging)


def save_package(pkg: VideoPackage, cfg: ChannelConfig = CONFIG) -> Path:
    """Write the package to output/<slug>/ as both JSON (machine) and a
    human-readable production brief (Markdown)."""
    out = Path(cfg.output_dir) / _slug(pkg.idea.title_working)
    out.mkdir(parents=True, exist_ok=True)

    (out / "package.json").write_text(pkg.model_dump_json(indent=2))
    (out / "production-brief.md").write_text(_render_brief(pkg, cfg))
    return out


def _render_brief(pkg: VideoPackage, cfg: ChannelConfig) -> str:
    p, s, sc = pkg.packaging, pkg.shorts, pkg.script
    lines: list[str] = []
    add = lines.append

    add(f"# {cfg.name} — Production Brief\n")
    add(f"**Working title:** {pkg.idea.title_working}")
    add(f"**Virality score:** {pkg.idea.virality_score}/100")
    add(f"**Why it works:** {pkg.idea.why_it_works}")
    add(f"**Sensitivity:** {pkg.idea.sensitivity_note}\n")

    add("## Title options")
    for i, t in enumerate(p.titles, 1):
        add(f"{i}. {t}")
    add("")

    add("## Thumbnail")
    add(f"- Concept: {p.thumbnail_concept}")
    add(f"- Text options: {', '.join(p.thumbnail_text)}\n")

    add("## Long-form script")
    add(f"_~{sc.total_word_count} words_\n")
    for b in sc.beats:
        add(f"### {b.section}")
        add(f"> {b.narration}\n")
        add(f"`VISUAL:` {b.visual}\n")

    add("## Sources to verify before publishing")
    for src in sc.sources_to_verify:
        add(f"- [ ] {src}")
    add("")

    add(f"## Shorts ({len(s)})")
    for i, sh in enumerate(s, 1):
        add(f"### Short {i}")
        add(f"**Hook:** {sh.hook}\n")
        add(f"{sh.script}\n")
        add(f"**On-screen:** {' / '.join(sh.on_screen_text)}")
        add(f"**CTA:** {sh.cta}")
        add(f"**Caption:** {sh.caption}\n")

    add("## Description")
    add(p.description + "\n")
    add("## Tags")
    add(", ".join(p.tags) + "\n")
    add("## Pinned comment")
    add(p.pinned_comment + "\n")

    return "\n".join(lines)
