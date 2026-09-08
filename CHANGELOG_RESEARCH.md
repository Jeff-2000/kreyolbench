# Research Changelog

## Purpose

Track scientific and governance evolution separately from software release notes.

## Status

Current status: IN_PROGRESS

Owner: Codex

Requires expert validation: No for logging; Yes for scientific decisions referenced here.

## 2026-09-01

Status: IN_PROGRESS

Changes:

- Added project knowledge architecture plan.
- Added formal review-status system.
- Added initial decision, assumption, and risk registers.
- Identified current scaffold as not yet a validated benchmark release.
- Marked v0.1 task freeze, source inclusion, metrics, split policy, and publication claims as requiring expert review.

Scientific implications:

- Current results and sample data must not be represented as benchmark findings.
- Translation and summarization metrics require stronger design before publication use.

## 2026-09-08

Status: SUBMITTED_TO_REVIEW

Implemented:

- machine-readable decision registry and typed eight-state review model
- governance metadata on benchmark, task, label, and source configurations
- deterministic `audit-governance` CLI output for maintainers and CI
- source redistribution consistency checks
- sample-data checks for identifiers, split contamination, source resolution, labels, and raw/normalized linkage
- explicit synthetic-fixture source provenance
- v0.1 expert-review packet

Scientific state:

- all seven scientific governance decisions remain `SUBMITTED_TO_REVIEW`
- translation and summarization evaluation remain `BLOCKED`
- structural audit success does not confer scientific approval
- no datasets were downloaded, no models were trained, and no benchmark task was frozen

Validation:

- 43 tests passed
- the governance audit returned `PASS` with `release_eligible: false`
- lint passed for all files introduced or modified by this implementation

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial research changelog. | IN_PROGRESS |
| 2026-09-08 | Operationalized scientific governance and added expert-review gate. | SUBMITTED_TO_REVIEW |
