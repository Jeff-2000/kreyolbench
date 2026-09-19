# Reports

## Current Source Governance

- `SOURCE_DISCOVERY_EXPANSION_REVIEW_PACKET_V0_1.md`: Project-Lead-validated metadata discovery and reconciliation packet; authorization effect `NONE`.
- `CREOLEVAL_HAITIAN_COMPONENT_MATRIX_V0_1.md`: component-level license and overlap backlog for CreoleVal.
- `EXPANDED_SOURCE_REVIEW_IMPLEMENTATION_HANDOFF.md`: implementation state, validation, and remaining external gates.

## Purpose

`reports/` contains research outputs, datasheets, baseline summaries, and publication-facing artifacts.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: Yes for publication claims.

## Current State

Current reports are scaffold-level and must not be treated as final benchmark evidence.

`EXPERT_REVIEW_PACKET_V0_1.md` records completed project-policy review.
`TASK_SPEC_REVIEW_PACKET_V0_1.md` is the controlled interface for independent
review of the five provisional v0.1 task specifications.
`INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md` records the AI-assisted internal
pre-review and cannot satisfy the external task-review gate.
`reviews/` contains reusable external-review evidence requirements and forms.
`V0_1_TASK_FEASIBILITY_MATRIX.md` records evidence gaps and source-to-task fit.
`SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md` consolidates metadata-only reviews
for all registered source candidates. `SOURCE_TO_TASK_MATRIX_V0_1.md` records
provisional relevance without authorization, and `source_reviews/` contains
the methodology, template, and source-specific public evidence reports.
The master paper outline covers the first controlled release only; it does not define the global KreyolBench task universe. Long-term scope is governed by `datasets/TASK_TAXONOMY.md` and `KB-SCOPE-002`.

Source governance reports include the Project-Lead feasibility packet, categorical prioritization, domain/modality accounting, and append-only per-source evidence reports. Feasibility and priority never authorize source use. See `SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md`, `SOURCE_PRIORITIZATION_V0_1.md`, and `SOURCE_DOMAIN_MODALITY_MATRIX_V0_1.md`.

## Expanded Discovery Review

`SOURCE_DISCOVERY_EXPANSION_REVIEW_PACKET_V0_1.md` is the current source-review entry point; the original packet describes its initial 21-candidate snapshot. `SOURCE_DOMAIN_MODALITY_MATRIX_V0_1.md` records candidate domains and roadmap-family fit, not measured coverage. `source_reviews/discovery/` holds unresolved leads and references, and `source_reviews/history/` preserves prior ledger and authorization evidence.

## Rules

- Separate scaffold reports from publication-ready reports.
- Link publication artifacts to `reports/PAPER_OUTLINE.md`.
- Do not publish benchmark claims without validated data, metrics, and reproducible runs.
- Include limitations and source-review status.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial reports subsystem specification. | TO_REVIEW_LATER |
| 2026-09-08 | Added the v0.1 expert-review packet. | TO_REVIEW_LATER |
| 2026-09-09 | Added the task review packet and evidence-based feasibility matrix. | TO_REVIEW_LATER |
| 2026-09-10 | Added the internal audit record and qualified external-review evidence templates. | TO_REVIEW_LATER |
| 2026-09-10 | Added complete metadata-only source feasibility reports and a source-to-task matrix. | SUBMITTED_TO_REVIEW |
