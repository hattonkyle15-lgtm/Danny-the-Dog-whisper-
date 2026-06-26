"""The four generation stages. Each is a pure function: input -> typed output."""

from __future__ import annotations

from config import CONFIG, ChannelConfig
from . import prompts
from .client import generate_structured
from .models import (
    IdeaBank,
    LongformScript,
    Packaging,
    Short,
    VideoIdea,
)
from pydantic import BaseModel


class _Shorts(BaseModel):
    shorts: list[Short]


def brainstorm_ideas(
    seed: str | None = None,
    count: int = 12,
    cfg: ChannelConfig = CONFIG,
) -> list[VideoIdea]:
    """Generate and rank a batch of video ideas.

    `seed` optionally constrains the batch (e.g. "Cold War", "shipwrecks",
    "medieval"); omit it for a wide-open brainstorm.
    """
    constraint = (
        f"Focus this batch on: {seed}." if seed else "Range widely across eras and regions."
    )
    user = (
        f"Generate {count} distinct video ideas. {constraint}\n"
        "Return them sorted by virality_score, highest first."
    )
    bank = generate_structured(
        system=prompts.ideas_system(cfg),
        user=user,
        schema=IdeaBank,
        effort="high",
    )
    return sorted(bank.ideas, key=lambda i: i.virality_score, reverse=True)


def write_script(idea: VideoIdea, cfg: ChannelConfig = CONFIG) -> LongformScript:
    """Write the full long-form narration script for a chosen idea."""
    user = (
        "Write the complete long-form script for this video idea:\n\n"
        f"Working title: {idea.title_working}\n"
        f"Hook: {idea.hook}\n"
        f"Summary: {idea.summary}\n"
        f"Why it works: {idea.why_it_works}\n"
        f"Era/region: {idea.era_or_region}\n"
        f"Sensitivity note: {idea.sensitivity_note}"
    )
    return generate_structured(
        system=prompts.script_system(cfg),
        user=user,
        schema=LongformScript,
        max_tokens=16000,
        effort="high",
    )


def write_shorts(
    idea: VideoIdea,
    script: LongformScript,
    cfg: ChannelConfig = CONFIG,
) -> list[Short]:
    """Derive the funnel Shorts from the finished long-form script."""
    beats = "\n".join(f"[{b.section}] {b.narration}" for b in script.beats)
    user = (
        f"The long-form video is titled: {script.title_working}\n"
        f"Its hook: {script.hook}\n\n"
        f"Full script beats:\n{beats}\n\n"
        f"Write {cfg.shorts_per_video} Shorts that funnel viewers to this video."
    )
    result = generate_structured(
        system=prompts.shorts_system(cfg),
        user=user,
        schema=_Shorts,
        effort="medium",
    )
    return result.shorts


def write_packaging(
    idea: VideoIdea,
    script: LongformScript,
    cfg: ChannelConfig = CONFIG,
) -> Packaging:
    """Write titles, thumbnail, description, tags, and pinned comment."""
    user = (
        f"Working title: {idea.title_working}\n"
        f"Hook: {idea.hook}\n"
        f"Summary: {idea.summary}\n"
        f"Opening line of the video: {script.hook}\n\n"
        "Write the full packaging for this video."
    )
    return generate_structured(
        system=prompts.packaging_system(cfg),
        user=user,
        schema=Packaging,
        effort="high",
    )
