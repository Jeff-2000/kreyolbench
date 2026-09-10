# Baselines

## Purpose

`baselines/` documents model families and protocols used to establish reproducible benchmark baselines.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: Yes for baseline matrix and comparison policy.

## Current State

The repository has baseline family directories for classical, transformer, and generative approaches. Code modules also exist under `src/kreyolbench/baselines/`.

## Requirements

- Separate random/majority, classical, fine-tuned, zero-shot, few-shot, cross-lingual, and frontier-model settings.
- Do not compare incompatible training settings as if equivalent.
- Record model IDs, revisions, prompts, seeds, compute, dataset versions, and licenses.
- Document failures and limitations.

## Dependencies

- `baselines/BASELINE_MATRIX.md`
- `baselines/TRAINING_PROTOCOL.md`
- `baselines/COMPUTE_POLICY.md`
- `eval/EVALUATION_PROTOCOL.md`

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial baselines subsystem specification. | TO_REVIEW_LATER |

