# Training Protocol

## Purpose

Define how supervised and transfer baselines should be trained and reported.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Required Metadata

- task
- dataset version
- split version
- training setting
- model ID and revision
- tokenizer ID and revision
- seed
- hyperparameters
- early-stopping rule
- hardware
- package versions
- training duration
- validation metric
- source of pretrained weights

## Training Settings

- zero-shot
- few-shot
- supervised fine-tuning
- cross-lingual transfer
- domain transfer
- instruction prompting

## Prohibited Shortcuts

- Do not tune on test data.
- Do not merge train and validation without logging a decision.
- Do not report only the best seed unless the protocol says so.
- Do not omit failed runs if they affect interpretation.

## Acceptance Criteria

- Results can be reproduced by another collaborator.
- Training data declaration is complete.
- Model license is compatible with release and leaderboard policy.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial training protocol. | SUBMITTED_TO_REVIEW |

