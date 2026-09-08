# Compute Policy

## Purpose

Define practical compute expectations for fair, reproducible baseline evaluation.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: Yes for leaderboard tiers.

## Principles

- Prefer baselines feasible for small research teams.
- Record hardware and approximate compute budget.
- Separate low-compute baselines from frontier/API-based evaluations.
- Do not require expensive training for basic contribution.

## Compute Tiers

| Tier | Description | Status |
| --- | --- | --- |
| CPU/basic | classical models and validation checks | DRAFT |
| Single GPU | small transformer fine-tuning | DRAFT |
| API model | closed or hosted model evaluation | SUBMITTED_TO_REVIEW |
| Large compute | expensive training or large-scale sweeps | BLOCKED pending justification |

## Acceptance Criteria

- Every reported run declares compute tier.
- Leaderboards can filter by compute tier.
- Expensive experiments require clear publication value.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial compute policy. | TO_REVIEW_LATER |

