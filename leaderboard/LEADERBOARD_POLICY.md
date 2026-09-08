# Leaderboard Policy

## Purpose

Define how public benchmark results should be ranked and verified.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Principles

- Do not launch hidden-test submissions before evaluation infrastructure exists.
- Separate zero-shot, few-shot, fine-tuned, transfer, and API-model settings.
- Require data and compute declarations.
- Prefer task-level rankings over a single aggregate unless scientifically justified.
- Disclose uncertainty and verification status.

## Current State

`leaderboard/schema.json` defines basic submission fields. Hidden test submissions are not yet accepted.

## Acceptance Criteria

- No unverified result is presented as official.
- Leaderboard ranking policy is expert-validated before launch.
- Submission requirements align with reproducibility policy.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial leaderboard policy. | SUBMITTED_TO_REVIEW |

