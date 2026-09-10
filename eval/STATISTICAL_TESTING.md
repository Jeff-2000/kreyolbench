# Statistical Testing

## Purpose

Define statistical methods for comparing systems and quantifying uncertainty.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Requirements

- Report confidence intervals for primary metrics when sample size allows.
- Prefer paired tests for paired model comparisons.
- Use effect sizes, not only p-values.
- Correct or disclose multiple comparisons where many systems/tasks are tested.
- Treat low-resource small-sample results cautiously.

## Candidate Methods

- bootstrap confidence intervals
- paired bootstrap tests
- permutation tests
- approximate randomization
- stratified bootstrap by domain/source where feasible

## Known Risks

- Small test sets can produce unstable intervals.
- Domain imbalance can hide subgroup failures.
- Multiple tasks and models increase false discovery risk.

## Acceptance Criteria

- Publication tables include uncertainty or explain why not.
- Leaderboards disclose whether differences are statistically meaningful.
- Statistical method choices are logged in `DECISIONS.md`.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial statistical testing policy. | SUBMITTED_TO_REVIEW |

