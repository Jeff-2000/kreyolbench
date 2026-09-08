# Evaluation

## Purpose

`eval/` stores evaluation configs and generated result artifacts.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: Yes for primary metrics and statistical testing.

## Current State

`eval/configs/` contains evaluation configuration stubs. `eval/results/` is intended for generated result JSON files and is ignored except `.gitkeep`.

## Requirements

- Metrics must be documented before publication use.
- Result files must be machine-readable.
- Confidence intervals and uncertainty should be added for publication-grade comparisons.
- Error analysis should be planned by domain, source, register, spelling variation, code-switching, and label group.

## Dependencies

- `eval/EVALUATION_PROTOCOL.md`
- `eval/METRICS.md`
- `eval/STATISTICAL_TESTING.md`
- `eval/ERROR_ANALYSIS.md`

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial evaluation subsystem specification. | TO_REVIEW_LATER |

