"""Thin wrapper around the Anthropic SDK, tuned for this channel.

All generation runs on Claude Opus 4.8 (`claude-opus-4-8`) with adaptive
thinking — the model decides how hard to think per call, which is ideal when
some tasks (ranking 20 ideas) are light and others (writing a 12-minute
researched script) are heavy.

We use the SDK's `messages.parse()` structured-output helper so every call
returns a validated Pydantic object — the model physically cannot hand the
next pipeline stage a malformed package. A full ~12-minute script lands well
under the non-streaming token ceiling, so we don't need streaming here.
"""

from __future__ import annotations

import anthropic
from pydantic import BaseModel

MODEL = "claude-opus-4-8"

# Shared client. Reads ANTHROPIC_API_KEY from the environment.
_client = anthropic.Anthropic()


def generate_structured(
    *,
    system: str,
    user: str,
    schema: type[BaseModel],
    max_tokens: int = 16000,
    effort: str = "high",
) -> BaseModel:
    """One-shot call that returns a validated instance of `schema`."""
    response = _client.messages.parse(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        thinking={"type": "adaptive"},
        output_config={"effort": effort},
        messages=[{"role": "user", "content": user}],
        output_format=schema,
    )
    if response.parsed_output is None:
        raise RuntimeError(
            f"Model returned no structured output (stop_reason={response.stop_reason})"
        )
    return response.parsed_output
