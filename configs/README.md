# Configs

## Purpose

`configs/` is the source of configuration truth for benchmark metadata, tasks, labels, sources, and orthographic variants.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: Yes for scientific task, label, source, and orthography definitions.

## Current State

- `benchmark.yaml` defines the benchmark name, version, language, splits, v0 tasks, domains, default license policy, and hidden-test policy.
- `tasks/` defines task-level primary metrics and schema fields.
- `labels/` defines candidate labels for classification, sentiment, NER, and code-switching.
- `sources/` defines candidate source families.
- `orthography/variants.yaml` records spelling/normalization variants.
- `governance/decisions.yaml` provides the executable decision-status registry.

Benchmark, task, label, and source configurations include:

- `status`: one project-wide review status.
- `decision_ids`: stable references into the decision registry.
- `requires_expert_validation`: whether scientific approval is required.
- `release_candidate`: whether unresolved dependencies must fail the audit.

Source `review_status` is a separate legal/data-handling state. It must not be confused with the project-wide `status` field.

## Requirements

- Do not add labels or tasks without scientific rationale.
- Do not treat task configs as expert-validated unless explicitly marked elsewhere.
- Every source config must comply with `datasets/SOURCE_REGISTRY.md`.
- Every task config must align with `datasets/DATASET_SPECIFICATION.md` and `eval/METRICS.md`.

## Known Risks

- v0 task list may be too broad.
- Primary metrics may be provisional.
- Source licensing status may be incomplete.

## Acceptance Criteria

- Configs are parseable YAML mappings.
- Task configs specify input and target fields.
- Source configs include required registry metadata before source use.
- Scientific changes are logged in `DECISIONS.md`.
- `kreyolbench audit-governance` reports no structural errors.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial configs subsystem specification. | TO_REVIEW_LATER |
| 2026-09-08 | Added machine-readable governance metadata and decision references. | TO_REVIEW_LATER |
