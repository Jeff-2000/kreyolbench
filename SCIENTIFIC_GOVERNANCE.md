# Scientific Governance

## Purpose

Define review statuses, expert-validation rules, and the boundary between engineering decisions and scientific decisions.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Review Status Values

| Status | Meaning |
| --- | --- |
| DRAFT | The artifact or decision exists but is preliminary. |
| IN_PROGRESS | Implementation or scientific work is actively underway. |
| TO_REVIEW_LATER | Acceptable for temporary continuation but requires later expert review. |
| SUBMITTED_TO_REVIEW | Codex has completed the current artifact or decision and dependent scientific work should pause for expert review. |
| EXPERT_VALIDATED | The human expert explicitly reviewed and accepted the artifact or decision. |
| NEEDS_REVISION | Expert or audit review found issues that must be corrected. |
| BLOCKED | Work cannot proceed because of missing data, unresolved dependencies, licensing constraints, scientific ambiguity, or required expert input. |
| DEPRECATED | Artifact or decision should no longer be used but remains documented for traceability. |

## Engineering Decisions

Engineering decisions may usually proceed without expert interruption:

- package layout
- function decomposition
- test framework
- configuration parser
- linting
- CI configuration
- typed Python style

## Scientific Decisions

Scientific decisions must be documented and may require expert validation:

- benchmark task definitions
- corpus inclusion/exclusion
- annotation labels
- normalization policy
- train/test split strategy
- primary metrics
- statistical testing
- leaderboard ranking
- paper claims

## Expert Validation Rule

If a decision changes scientific meaning, mark it `SUBMITTED_TO_REVIEW` unless it has already been explicitly validated.

Do not over-block routine engineering work. Do block downstream work when final claims, releases, or data collection depend on unvalidated scientific choices.

## Acceptance Criteria

- Major scientific choices have decision IDs.
- Knowledge files clearly show status and review needs.
- Future agents can identify what is provisional.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial scientific governance policy. | SUBMITTED_TO_REVIEW |

