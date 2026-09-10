# Reproducibility

## Purpose

Define what must be recorded so KreyolBench results can be reproduced and audited.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes for publication-grade requirements.

## Required Result Metadata

Every benchmark run should eventually record:

- dataset version
- split version
- source registry version
- git commit
- model identifier
- model revision
- model license
- Python version
- package versions
- random seed
- hardware
- training setting
- prompt template where relevant
- evaluation config
- timestamp
- task version
- metric versions
- confidence intervals where available

## Current State

The current result schema records task, dataset version, model, setting, metrics, confidence interval placeholder, data hash, seed, and timestamp. It does not yet automatically record git commit, environment lockfile, hardware, model revision, or full evaluation config.

## Reproducibility Levels

| Level | Meaning | Status |
| --- | --- | --- |
| Level 0 | Manual run with visible code. | IN_PROGRESS |
| Level 1 | Configured run with structured result JSON. | IN_PROGRESS |
| Level 2 | Fully reproducible run with environment, commit, data hash, and seed. | DRAFT |
| Level 3 | Independently reproducible release with archived artifacts. | DRAFT |

## Acceptance Criteria

- Publication results must be tied to exact dataset and code versions.
- Public leaderboard entries must declare data and training setting.
- Randomness must be controlled where feasible.
- Generated results must remain machine-readable.

## Next Recommended Action

Add result-schema documentation before extending evaluation code.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial reproducibility specification. | SUBMITTED_TO_REVIEW |

