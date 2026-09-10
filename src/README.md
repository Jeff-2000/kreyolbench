# Source Package

## Purpose

`src/kreyolbench/` contains the installable Python package.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: No for software structure; Yes when code encodes scientific meaning.

## Current Modules

- `schemas.py`: Pydantic JSONL row schemas.
- `sources.py`: conservative source-plan helpers.
- `registry.py`: YAML loading and registry helpers.
- `io.py`: JSONL and hash utilities.
- `cli.py`: command-line entry points.
- `governance.py`: typed statuses, configuration audit, release gates, and scientific-invariant checks.
- `preprocessing/`: text cleaning, PII, dedupe, orthography, OCR helpers.
- `evaluation/`: metrics, runner, reporting.
- `baselines/`: baseline scaffolds.

## Engineering Requirements

- Keep functions small and typed.
- Avoid hidden network access.
- Do not hard-code scientific decisions that belong in configs.
- Add tests when behavior changes.

## Scientific Requirements

- Code that encodes labels, metrics, splits, or source handling must align with knowledge specs.
- Scaffold metrics must not be presented as validated publication methods.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial source package specification. | TO_REVIEW_LATER |
| 2026-09-08 | Added machine-readable governance audit infrastructure. | TO_REVIEW_LATER |
