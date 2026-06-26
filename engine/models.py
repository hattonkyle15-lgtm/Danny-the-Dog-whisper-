"""Typed data models for everything the engine produces.

Using Pydantic models gives us two things:
  1. Structured outputs from the Claude API validate against these schemas,
     so the model can't return malformed packages.
  2. Each stage of the pipeline hands a typed object to the next stage.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class VideoIdea(BaseModel):
    """A single video concept, ranked for viral potential."""

    title_working: str = Field(description="A working title (not the final clickable one)")
    hook: str = Field(description="The one-sentence curiosity gap that makes someone click")
    summary: str = Field(description="2-3 sentences on what the video covers")
    why_it_works: str = Field(description="The psychological reason this spreads (curiosity gap, taboo, injustice, mystery)")
    era_or_region: str = Field(description="Roughly when/where, for variety tracking")
    virality_score: int = Field(ge=1, le=100, description="Honest estimate of viral potential")
    sensitivity_note: str = Field(description="Any advertiser-safety caution for this topic, or 'none'")


class IdeaBank(BaseModel):
    ideas: list[VideoIdea]


class ScriptBeat(BaseModel):
    """One narrated section of the long-form script."""

    section: str = Field(description="Label, e.g. 'Cold open', 'The turn', 'The reveal', 'The aftermath'")
    narration: str = Field(description="The exact words the narrator says, verbatim")
    visual: str = Field(description="What's on screen during this narration (archival, b-roll, map, text card)")


class LongformScript(BaseModel):
    title_working: str
    hook: str = Field(description="The verbatim first line — the cold open")
    beats: list[ScriptBeat]
    total_word_count: int
    sources_to_verify: list[str] = Field(description="Claims/facts a producer must fact-check before publishing")


class Short(BaseModel):
    """A vertical Short designed to funnel viewers to the long-form video."""

    hook: str = Field(description="First 3 seconds — must stop the scroll")
    script: str = Field(description="Full narration, <= ~50s of speech")
    on_screen_text: list[str] = Field(description="Punchy text overlays, in order")
    cta: str = Field(description="The push to watch the full video / subscribe")
    caption: str = Field(description="The post caption with hashtags")


class Packaging(BaseModel):
    """The clickable metadata — often more important than the video itself."""

    titles: list[str] = Field(description="5 title options, best first, all under 70 chars")
    thumbnail_text: list[str] = Field(description="3 short, high-contrast thumbnail overlay options (1-4 words each)")
    thumbnail_concept: str = Field(description="What the thumbnail image should depict")
    description: str = Field(description="Full YouTube description with a hook paragraph")
    tags: list[str] = Field(description="15-25 SEO tags")
    pinned_comment: str = Field(description="A pinned comment that drives engagement/replies")


class VideoPackage(BaseModel):
    """The complete deliverable for one video."""

    idea: VideoIdea
    script: LongformScript
    shorts: list[Short]
    packaging: Packaging
