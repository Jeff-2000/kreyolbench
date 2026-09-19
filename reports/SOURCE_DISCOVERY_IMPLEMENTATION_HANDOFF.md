# Source Discovery Expansion Handoff

## STEP COMPLETED

Current status: SUBMITTED_TO_REVIEW

Prepared by: Codex, AI-assisted. Date: 2026-09-10.

## What Was Implemented

- 22 deduplicated intake leads: 15 registered-source references, four unresolved leads and three references.
- 12 new metadata-only source records; 33 active non-synthetic feasibility reviews and a separate synthetic control.
- Claim-level evidence validation, attributed sizes, provenance relationships, an expanded review packet and domain/modality hypotheses.
- Preserved the initial 21-candidate review and source authorization snapshot.

## Files Created

- `configs/governance/source_discovery.yaml` and 12 source configs.
- `datasets/SOURCE_DISCOVERY.md` and `src/kreyolbench/source_discovery.py`.
- `reports/SOURCE_DISCOVERY_EXPANSION_REVIEW_PACKET_V0_1.md` and `reports/SOURCE_DOMAIN_MODALITY_MATRIX_V0_1.md`.
- 22 discovery/source evidence reports and two historical YAML snapshots.
- `tests/test_source_discovery.py` and this handoff.

## Files Modified

- Feasibility ledger and governance validator; Markdown/YAML decision registries.
- Source-registry, config, source-package, reports and test guidance.
- Research changelog, roadmap and the existing UD family evidence report.

## Scientific Decisions Made

No task, source permission, metric, split or release approval. Domain fit remains a hypothesis. Aya origin and other resource descriptions were corrected against provider metadata; uncertain claims remain explicit.

## Engineering Decisions Made

KB-ENG-008 records the discovery intake and the claim-level feasibility-v2 architecture implemented on 2026-09-10. KB-ENG-009 and active feasibility schema v3 now supersede that projection without deleting its history. Coverage remains registry-driven, not limited to 21 sources. Historical snapshots are not active configuration.

## Open Questions and Risks Identified

Exact source revisions, upstream rights, content quality, consent, dialect coverage and cross-corpus contamination remain unresolved. jsbeaudry STEM provenance, Northern Haitian archive identity, VoxLingua Haitian details and translated VICR Haitian coverage need further metadata evidence. Reported counts are not verified unique data. Machine checks validate evidence structure, not its truth.

## Items Requiring Expert Review

Human review of the expanded source packet and bounded subset priorities; legal/ethics review before source use; independent external review of all five task specifications.

## Current Statuses

- Reviews: SUBMITTED_TO_REVIEW or BLOCKED.
- KB-ENG-008: TO_REVIEW_LATER.
- Exactly five unresolved task decisions; release eligibility false.
- Existing permissions, task definitions, labels and release membership unchanged.

## Tests / Validation Performed

- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=src pytest -q tests`: 165 passed.
- `ruff check .`: PASS.
- Text and JSON governance audits: PASS, zero errors and warnings, release eligibility false.
- Scoped `git diff --check`: PASS.
- Source permission regression: PASS; synthetic source remains scientifically excluded.

## Recommended Next Implementation

Review the expansion packet and select bounded subsets for metadata clarification, permission scoping and qualified legal/ethical/linguistic review. Evidence reports and source-review records may be revised; no source content may be acquired on the strength of this handoff. Continue independent task review in parallel. Expected value: evidence-backed source selection and auditable permission boundaries.

Suggested status for next step: SUBMITTED_TO_REVIEW. No automatic acquisition, annotation or training phase.
