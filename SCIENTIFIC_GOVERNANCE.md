# Scientific Governance

## Purpose

Define review statuses, expert-validation rules, and the boundary between engineering decisions and scientific decisions.

## Status

Current status: EXPERT_VALIDATED

Owner: Codex

Requires expert validation: No for the current policy; material changes require a new review

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

## Scope Status Values

Scope status is independent of review status. Allowed values are `ROADMAP`, `DISCOVERY`, `FEASIBILITY_ONLY`, `PILOT_CANDIDATE`, `RELEASE_CANDIDATE`, `DEFERRED`, and `INCLUDED_IN_RELEASE`.

Roadmap or discovery registration is not implementation. Pilot or feasibility placement is not scientific approval. `RELEASE_CANDIDATE` and `INCLUDED_IN_RELEASE` require resolved scientific decisions and explicit versioned release membership.

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

Review events must be append-only in the machine-readable decision registry and
record outcome, reviewer, role, date, independence, and evidence path.

Under `KB-GOV-002`, internal project-lead review may authorize specification
work, but each v0.1 task requires independent external review before freeze.

Under `KB-GOV-003`, externally gated task approval additionally requires an identifiable human reviewer, affiliation, relevant expertise tags, conflict disclosure, human attestation, dated evidence, and task-specific qualification coverage. Several reviewers may collectively cover expertise requirements. Internal review and automated output without external human ownership cannot satisfy an external minimum. A disqualifying conflict cannot support approval.

`KB-SCOPE-002` establishes the validated open-world project-scope policy. This project-level approval permits extensible registration, but it does not validate any task family, taxonomy entry, source, dataset, annotation protocol, metric, evaluation paradigm, or release membership. Every downstream component remains subject to its independent governance gates.

## Acceptance Criteria

- Major scientific choices have decision IDs.
- Knowledge files clearly show status and review needs.
- Future agents can identify what is provisional.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial scientific governance policy. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Recorded validated status and independent task-review requirements. | EXPERT_VALIDATED |
| 2026-09-09 | Documented the independent scope-status dimension and open-world proposal. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Recorded project-scope approval of the open-world policy without validating downstream components. | EXPERT_VALIDATED |
| 2026-09-10 | Added qualified external human review evidence and conflict requirements. | EXPERT_VALIDATED |
