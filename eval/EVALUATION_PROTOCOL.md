# Evaluation Protocol

## Purpose

Define the minimum protocol for evaluating systems on KreyolBench.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Protocol

1. Confirm dataset version and split version.
2. Confirm task spec and metric spec.
3. Declare model, model revision, training data, compute, seed, and prompt where relevant.
4. Run evaluation with fixed config.
5. Save machine-readable result JSON.
6. Add confidence intervals where available.
7. Run error analysis for publication claims.
8. Submit only verified results to leaderboard.

## Current Limitation

The current evaluation runner is scaffold-level and does not yet capture full reproducibility metadata.

## Acceptance Criteria

- Evaluation can be rerun by another contributor.
- Results include enough metadata to audit.
- Test data remains protected from tuning.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial evaluation protocol. | SUBMITTED_TO_REVIEW |

