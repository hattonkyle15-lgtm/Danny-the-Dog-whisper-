"""
Channel configuration — the single source of truth for the channel's identity.

Everything the engine generates is steered by these values. Change them here
and every script, title, and Short the pipeline produces will follow the new
brief. This is what keeps 500 videos sounding like ONE channel.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ChannelConfig:
    # ---- Identity -----------------------------------------------------------
    # Pick ONE name and never look back. Faceless history channels that hit 1M
    # have a name that promises the emotion, not the topic.
    # Strong candidates for the dark/untold-history lane:
    #   "The Buried Century"  ·  "Lanterns Out"  ·  "Footnote Horrors"
    #   "The Unmarked"        ·  "Before the Histories"  ·  "Grim Records"
    name: str = "The Unmarked"
    tagline: str = "The history they left out of the textbook."

    niche: str = "dark and untold history"
    # The promise every video must keep. This is the channel's contract with
    # the viewer — break it and retention dies.
    promise: str = (
        "Every video reveals a true, disturbing, or forgotten piece of history "
        "that the viewer has never heard — researched, sourced, and told like a "
        "campfire story they can't stop listening to."
    )

    # ---- Voice & tone -------------------------------------------------------
    # Narration persona. This is the 'character' of the faceless narrator.
    narrator_voice: str = (
        "A calm, literate, slightly ominous storyteller. Speaks plainly, never "
        "sensationalist, but lets the horror of the facts speak for itself. "
        "Think a documentarian who has read the primary sources and is quietly "
        "furious they were forgotten. No jokes. No filler. No 'hey guys'."
    )
    reading_level: str = "accessible to a sharp 15-year-old; no academic jargon"

    # ---- Hard rules (non-negotiable for quality + safety + monetization) ----
    rules: tuple[str, ...] = (
        "Historically accurate. No invented quotes, dates, or events. If a "
        "detail is disputed, say so.",
        "Advertiser-friendly. Dark subject matter is fine, but no gratuitous "
        "gore, no glorifying violence, no graphic descriptions that would "
        "trigger demonetization. Imply dread; don't wallow in it.",
        "Respectful of victims. The horror is the point; mockery never is.",
        "Cite the kind of source a fact-checker could verify (archives, "
        "court records, named historians, contemporary accounts).",
        "Cold open in the first sentence — start mid-tension, never with "
        "'In the year...' or a definition.",
    )

    # ---- Format targets -----------------------------------------------------
    longform_minutes: tuple[int, int] = (8, 12)   # sweet spot for watch-time + RPM
    longform_words_per_minute: int = 150          # narration pace
    shorts_per_video: int = 4                      # discovery funnel into long-form
    shorts_max_seconds: int = 50

    # ---- Output ------------------------------------------------------------
    output_dir: str = "output"


CONFIG = ChannelConfig()
