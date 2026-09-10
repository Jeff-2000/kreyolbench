"""Source adapter registry.

Adapters return metadata plans by default. They intentionally do not download or
redistribute data until source-specific license review is complete.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass
from typing import Any

from kreyolbench.governance import (
    AccessStatus,
    CollectionStatus,
    DiscoveryStatus,
    EthicsStatus,
    LegalReviewStatus,
    PermissionStatus,
    RedistributionStatus,
    ScientificInclusionStatus,
    SourceRecord,
    SourceRecordType,
)


@dataclass(frozen=True)
class SourcePlan:
    source_id: str
    url: str | None
    access_method: str
    record_type: SourceRecordType
    discovery_status: DiscoveryStatus
    access_status: AccessStatus
    legal_review_status: LegalReviewStatus
    collection_status: CollectionStatus
    derived_use_status: PermissionStatus
    redistribution_status: RedistributionStatus
    ethics_status: EthicsStatus
    scientific_status: ScientificInclusionStatus
    next_steps: list[str]

    @property
    def redistribution_allowed(self) -> bool | None:
        """Compatibility view; use ``redistribution_status`` for new code."""

        if self.redistribution_status == RedistributionStatus.APPROVED:
            return True
        if self.redistribution_status in {
            RedistributionStatus.LINK_ONLY,
            RedistributionStatus.DERIVED_ONLY,
            RedistributionStatus.PROHIBITED,
        }:
            return False
        return None

    @property
    def review_status(self) -> str:
        """Deprecated summary of independent v2 gates."""

        if self.redistribution_status == RedistributionStatus.APPROVED:
            return "approved_public_release"
        if self.redistribution_status == RedistributionStatus.LINK_ONLY:
            return "approved_link_only"
        if self.redistribution_status == RedistributionStatus.DERIVED_ONLY:
            return "approved_derived_only"
        if self.redistribution_status == RedistributionStatus.PROHIBITED:
            return "not_approved_for_redistribution"
        if self.legal_review_status == LegalReviewStatus.PENDING:
            return "pending_legal_review"
        return "pending_subset_review"


def build_source_plan(config: dict[str, Any]) -> SourcePlan:
    if config.get("source_schema_version") != 2:
        warnings.warn(
            "Source schema v1 is deprecated; migrate to source_schema_version: 2",
            DeprecationWarning,
            stacklevel=2,
        )
        return _build_legacy_source_plan(config)

    source = SourceRecord.model_validate(config)
    next_steps = [
        "record retrieval date before collection",
        "hash every downloaded artifact",
        "run PII and duplicate checks before annotation",
    ]
    if source.source_governance.legal_review_status != LegalReviewStatus.APPROVED:
        next_steps.insert(0, "complete license review before redistributing text")
    return SourcePlan(
        source_id=source.source_id,
        url=source.url,
        access_method=source.access_method,
        record_type=source.record_type,
        discovery_status=source.source_governance.discovery_status,
        access_status=source.source_governance.access_status,
        legal_review_status=source.source_governance.legal_review_status,
        collection_status=source.source_governance.collection_status,
        derived_use_status=source.source_governance.derived_use_status,
        redistribution_status=source.source_governance.redistribution_status,
        ethics_status=source.source_governance.ethics_status,
        scientific_status=source.source_governance.scientific_status,
        next_steps=next_steps,
    )


def _build_legacy_source_plan(config: dict[str, Any]) -> SourcePlan:
    review_status = str(config.get("review_status", "pending_legal_review"))
    redistribution_by_status = {
        "approved_public_release": RedistributionStatus.APPROVED,
        "reviewed_public_domain_notice": RedistributionStatus.APPROVED,
        "reviewed_standard_wikimedia_terms": RedistributionStatus.CONDITIONAL,
        "approved_link_only": RedistributionStatus.LINK_ONLY,
        "approved_derived_only": RedistributionStatus.DERIVED_ONLY,
        "not_approved_for_redistribution": RedistributionStatus.PROHIBITED,
    }
    redistribution_status = redistribution_by_status.get(
        review_status, RedistributionStatus.UNKNOWN
    )
    legal_status = (
        LegalReviewStatus.PENDING
        if review_status.startswith("pending")
        else LegalReviewStatus.CONDITIONAL
    )
    return SourcePlan(
        source_id=str(config["source_id"]),
        url=config.get("url"),
        access_method=str(config.get("access_method", "manual")),
        record_type=SourceRecordType.SOURCE_COLLECTION,
        discovery_status=DiscoveryStatus.DISCOVERED,
        access_status=AccessStatus.UNKNOWN,
        legal_review_status=legal_status,
        collection_status=CollectionStatus.PERMISSION_UNKNOWN,
        derived_use_status=PermissionStatus.UNKNOWN,
        redistribution_status=redistribution_status,
        ethics_status=EthicsStatus.NOT_STARTED,
        scientific_status=ScientificInclusionStatus.PENDING_EXPERT_REVIEW,
        next_steps=[
            "migrate this source record to schema version 2",
            "complete license review before redistributing text",
        ],
    )


def known_source_families() -> list[str]:
    return [
        "aka_official",
        "cmu_haitian",
        "creoleval",
        "diaspora_publications",
        "haiti_government_publications",
        "haitian_news_candidates",
        "mit_ayiti_resources",
        "opus",
        "social_media_candidates",
        "universal_dependencies_haitian",
    ]
