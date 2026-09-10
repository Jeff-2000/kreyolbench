# Ethics and Data Governance

## Purpose

Unify ethical principles, data governance, and public-interest constraints for KreyolBench.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Core Principles

- Haitian Creole speakers are stakeholders, not merely data sources.
- Do not publish private, sensitive, or non-redistributable material.
- Do not use KreyolBench for surveillance, exclusion, or harmful profiling.
- Preserve linguistic variation unless a task explicitly studies normalization.
- Document uncertainty, limitations, source skew, and domain skew.
- Attribute upstream sources and community contributors.

## Data Governance Requirements

Every source must have:

- source ID
- source name
- source URL
- provider
- language
- domain
- data type
- license
- redistribution status
- commercial-use status where known
- collection method
- expected tasks
- quality notes
- privacy risk
- review status

## Human Data

Speech, interviews, annotator records, consent forms, and private communications require controlled access. Completed consent forms and identifying data must not be committed to Git.

## Release Gate

Before public release:

- complete source review
- complete PII review
- document deduplication
- freeze and hash splits
- update dataset card
- document limitations
- confirm out-of-scope use policy

## Dependencies

See `DATA_ACCESS_POLICY.md`, `docs/data_governance.md`, `docs/ethics.md`, and `datasets/SOURCE_REGISTRY.md`.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial consolidated ethics and data governance policy. | SUBMITTED_TO_REVIEW |

