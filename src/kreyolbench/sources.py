"""Source adapter registry.

Adapters return metadata plans by default. They intentionally do not download or
redistribute data until source-specific license review is complete.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SourcePlan:
    source_id: str
    url: str | None
    access_method: str
    redistribution_allowed: bool | None
    review_status: str
    next_steps: list[str]


def build_source_plan(config: dict[str, Any]) -> SourcePlan:
    source_id = str(config["source_id"])
    review_status = str(config.get("review_status", "pending_legal_review"))
    next_steps = [
        "record retrieval date before collection",
        "hash every downloaded artifact",
        "run PII and duplicate checks before annotation",
    ]
    if review_status.startswith("pending"):
        next_steps.insert(0, "complete license review before redistributing text")
    return SourcePlan(
        source_id=source_id,
        url=config.get("url"),
        access_method=str(config.get("access_method", "manual")),
        redistribution_allowed=config.get("redistribution_allowed"),
        review_status=review_status,
        next_steps=next_steps,
    )


def known_source_families() -> list[str]:
    return [
        "cmu_haitian",
        "creoleval",
        "opus",
        "ebible_hat_1985",
        "wikimedia_htwiki",
        "mspp_publications",
        "un_haiti_ht",
        "haitian_news_candidates",
    ]

