# Notebooks

## Purpose

`notebooks/` contains exploratory and reproducible analysis notebooks.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: No for exploration; Yes for publication claims.

## Rules

- Notebooks are not the source of truth for library code.
- Move reusable logic into `src/kreyolbench/`.
- Do not store secrets, private data, or large outputs.
- Record dataset version and source subset.
- Clear or minimize large notebook outputs before commit.

## Publication Use

Notebook outputs may inform papers only if the underlying data, code, config, and result artifacts are reproducible.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial notebooks specification. | TO_REVIEW_LATER |

