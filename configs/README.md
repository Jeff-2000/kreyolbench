# Configs

## Purpose

`configs/` is the source of configuration truth for ecosystem metadata, task taxonomy, domains, releases, task instances, labels, sources, and orthographic variants.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: Yes for scientific task, label, source, and orthography definitions.

## Current State

- `benchmark.yaml` identifies the research program, ecosystem, language, and registry locations. It must not contain release-specific task lists.
- `task_taxonomy.yaml` registers open-world task families and task types.
- `domains.yaml` registers current candidate and roadmap domains without authorizing data use.
- `releases/` defines explicit version membership, splits, and release policy.
- `tasks/` defines stable task instances, runtime aliases, variants, primary metrics, and schema fields.
- `labels/` defines candidate labels for classification, sentiment, NER, and code-switching.
- `sources/` defines candidate source families.
- `orthography/variants.yaml` records spelling/normalization variants.
- `governance/decisions.yaml` provides the executable decision-status and review-event registry.
- `governance/task_feasibility.yaml` records evidence-based readiness without numerical scoring.
- `governance/source_feasibility.yaml` separates scientific feasibility, evidence, attribution, and external-evidence gates from authorization.
- `governance/source_prioritization.yaml`, `source_diversity.yaml`, and `source_contamination.yaml` provide complete non-authoritative planning coverage for registered non-synthetic sources.

Most governed configurations include:

- `status`: one project-wide review status.
- `decision_ids`: stable references into the decision registry.
- `requires_expert_validation`: whether scientific approval is required.
- `release_candidate`: whether unresolved dependencies must fail the audit.

Task configurations use `scientific_status` separately from `scope_status` and include `task_instance_id`, `task_family_id`, `task_type_id`, and `task_variant`. The runtime `task` slug is a compatibility alias, not the global task identity.

Allowed scope states are `ROADMAP`, `DISCOVERY`, `FEASIBILITY_ONLY`, `PILOT_CANDIDATE`, `RELEASE_CANDIDATE`, `DEFERRED`, and `INCLUDED_IN_RELEASE`. Version membership is authoritative only in `releases/`; task-level `v0`, `scope_tier`, and `release_candidate` fields are prohibited.

Source records use `source_schema_version: 2` and a typed
`source_governance` block. Discovery, access, legal review, collection,
derived use, redistribution, commercial use, ethics, and scientific inclusion
are independent. These fields must not be confused with the project-wide
`status` field. The legacy source `review_status` is deprecated and rejected in
committed configuration.

The decision registry uses schema version 3. Human review events are append-only
and record outcome, reviewer, role, date, independence, and an evidence path.
The latest event must agree with the decision status.

## Source Discovery and Feasibility

`governance/source_discovery.yaml` records deduplicated intake, separate source/lead/reference dispositions, claimed origin, reported sizes and non-authorizing provenance relationships. `governance/source_feasibility.yaml` uses schema v3 with independent feasibility axes, claim-level evidence, append-only review events, and external-evidence requirements. Source configs retain schema v2 and their independent authorization gates. See `datasets/SOURCE_DISCOVERY.md` before editing either ledger.

## Requirements

- Do not add labels or tasks without scientific rationale.
- Do not treat task configs as expert-validated unless explicitly marked elsewhere.
- Every source config must comply with `datasets/SOURCE_REGISTRY.md`.
- Source families are discovery containers and must not be referenced by dataset rows.
- Registering a source does not authorize collection or scientific inclusion.
- Every task config must align with `datasets/DATASET_SPECIFICATION.md` and `eval/METRICS.md`.
- Every task family and type must resolve through `task_taxonomy.yaml`.
- Roadmap registration must not create release membership or authorize implementation.

## Known Risks

- The five-task v0.1 pilot may still exceed available review or annotation capacity.
- Primary metrics may be provisional.
- Source licensing status may be incomplete.
- Roadmap breadth may be misread as implemented capability.

## Acceptance Criteria

- Configs are parseable YAML mappings.
- Task configs specify input and target fields.
- Stable task-instance IDs are unique and release memberships resolve.
- Scope and scientific statuses are validated independently.
- Source configs include required registry metadata before source use.
- Scientific changes are logged in `DECISIONS.md`.
- `kreyolbench audit-governance` reports no structural errors.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial configs subsystem specification. | TO_REVIEW_LATER |
| 2026-09-08 | Added machine-readable governance metadata and decision references. | TO_REVIEW_LATER |
| 2026-09-09 | Migrated committed source records to the multi-axis schema v2. | TO_REVIEW_LATER |
| 2026-09-09 | Added decision review history and the v0.1 task feasibility matrix. | TO_REVIEW_LATER |
| 2026-09-09 | Added open-world task/domain registries and versioned release membership. | TO_REVIEW_LATER |
