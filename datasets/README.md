# Datasets

## Source Governance

Read `SOURCE_USE_POLICY.md` before proposing training or evaluation use and `MULTIMODAL_PROVENANCE.md` before registering vision-language material. Scientific role, feasibility, legal status, ethics status, contamination, and release membership are independent.

## Purpose

Define canonical benchmark data contracts, source provenance, splits, leakage controls, and versioning.

## Status

Current status: SUBMITTED_TO_REVIEW

## Required Reading

- `DATASET_SPECIFICATION.md`
- `EXAMPLE_PROVENANCE.md`
- `SOURCE_REGISTRY.md`
- `SPLIT_POLICY.md`
- `LEAKAGE_PREVENTION.md`
- `VERSIONING_POLICY.md`
- task specifications under `tasks/`
- the open-world task hierarchy in `TASK_TAXONOMY.md`

The loader reads approved local JSONL artifacts from `data/processed/`. External datasets are not downloaded automatically. Source-specific acquisition, legal review, provenance, ethics, and scientific inclusion must be complete before export.

Retrieval uses separate corpus, query, and qrel artifacts. Synthetic files under `data/sample/` validate software contracts only and are not scientific evidence.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Added task-specification and example-provenance entry points. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Added task taxonomy and bounded-release semantics. | SUBMITTED_TO_REVIEW |
