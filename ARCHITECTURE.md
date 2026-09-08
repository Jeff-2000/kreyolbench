# Architecture

## Purpose

Describe the repository architecture and its scientific responsibilities.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: No for engineering structure; Yes for scientific task semantics.

## Current State

KreyolBench uses a Python package under `src/kreyolbench/` with config-driven benchmark behavior.

Major components:

- `configs/`: benchmark, task, label, source, and orthography configuration.
- `data/`: ignored raw/interim/processed data plus committed sample fixtures.
- `datasets/`: Hugging Face loader and dataset documentation.
- `annotation/`: guidelines, examples, and annotation tool templates.
- `baselines/`: baseline family docs and placeholder model modules.
- `eval/`: evaluation configs and generated result location.
- `leaderboard/`: public submission schema and generated table.
- `scripts/`: wrappers for CLI workflows.
- `src/kreyolbench/`: package code.
- `tests/`: automated tests.
- `reports/`: datasheets, baseline reports, and publication artifacts.

## Design Decisions

- Use JSONL rows validated by Pydantic schemas.
- Keep task/source/label definitions in YAML configs.
- Avoid automatic external dataset downloads before source review.
- Store generated benchmark results as structured JSON.
- Keep raw external data out of Git unless redistribution is explicitly approved.

## Weaknesses

- Evaluation metrics are scaffold-level for some tasks.
- Result metadata does not yet capture git commit, package lockfile, hardware, model revision, or full run config.
- No CI policy is currently documented.
- Hidden-test evaluation server does not exist.

## Engineering Requirements

- Preserve config-driven design.
- Avoid hard-coded dataset assumptions.
- Keep CLI operations reproducible.
- Add tests when schemas, metrics, or runners change.

## Scientific Requirements

- Task configs must align with documented task specifications.
- Source configs must align with the source registry policy.
- Evaluation code must not imply publication-grade validity before review.

## Next Recommended Action

Create formal task, source, metric, split, and result-schema specifications before expanding code.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial architecture overview. | TO_REVIEW_LATER |

