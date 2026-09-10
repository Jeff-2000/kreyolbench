from pathlib import Path

import pytest
import yaml

from kreyolbench.governance import (
    LegalReviewStatus,
    RedistributionStatus,
    SourceRecordType,
)
from kreyolbench.sources import build_source_plan, known_source_families


REPOSITORY_ROOT = Path(__file__).parents[1]


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_build_source_plan_exposes_v2_governance():
    config = _load_yaml(REPOSITORY_ROOT / "configs" / "sources" / "wikimedia.yaml")

    plan = build_source_plan(config)

    assert plan.record_type == SourceRecordType.SOURCE_COLLECTION
    assert plan.legal_review_status == LegalReviewStatus.CONDITIONAL
    assert plan.redistribution_status == RedistributionStatus.CONDITIONAL
    assert plan.redistribution_allowed is None
    assert plan.review_status == "pending_subset_review"


def test_legacy_source_plan_is_supported_with_warning():
    config = {
        "source_id": "legacy_example",
        "url": None,
        "access_method": "manual",
        "review_status": "approved_link_only",
        "redistribution_allowed": False,
    }

    with pytest.warns(DeprecationWarning, match="schema v1 is deprecated"):
        plan = build_source_plan(config)

    assert plan.redistribution_status == RedistributionStatus.LINK_ONLY
    assert plan.redistribution_allowed is False
    assert plan.review_status == "approved_link_only"


def test_known_source_families_are_registered_as_families():
    records = [
        _load_yaml(path)
        for path in (REPOSITORY_ROOT / "configs" / "sources").glob("*.yaml")
    ]
    for source_id in known_source_families():
        record = next(item for item in records if item["source_id"] == source_id)
        assert record["record_type"] == "SOURCE_FAMILY"

    configured_families = {
        item["source_id"] for item in records if item["record_type"] == "SOURCE_FAMILY"
    }
    assert set(known_source_families()) == configured_families
