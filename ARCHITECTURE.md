# Architecture

## Purpose

Describe the repository architecture and its scientific responsibilities.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: No for engineering structure; Yes for scientific task semantics.

## Current State

KreyolBench uses a Python package under `src/kreyolbench/` with config-driven benchmark behavior. The repository distinguishes the long-term research program and ecosystem from task instances and versioned release membership.

Major components:

- `configs/`: ecosystem, taxonomy, domain, release, task, label, source, and orthography configuration.
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
- Use stable task-instance IDs for scientific traceability.
- Treat current CLI task names as compatibility aliases, not the global task universe.
- Keep scientific review status independent from planning and release scope status.
- Store release membership in versioned release records rather than duplicated booleans.

## Scientific Hierarchy

```text
Research Program
  -> Benchmark Ecosystem
    -> Task Family
      -> Task Type
        -> Task Variant
          -> Task Instance
            -> Release Membership
```

`configs/task_taxonomy.yaml` registers open-world task families. `configs/tasks/` defines concrete implemented or roadmap instances. `configs/releases/` controls version membership. `configs/domains.yaml` registers candidate and roadmap domains without authorizing corpus use.

## Weaknesses

- Evaluation metrics are scaffold-level for some tasks.
- Result metadata does not yet capture git commit, package lockfile, hardware, model revision, or full run config.
- No CI policy is currently documented.
- Hidden-test evaluation server does not exist.
- Current dataset-row and metric dispatch code supports only implemented adapters. This is an implementation boundary, not a scientific scope boundary.
- Future modality interfaces remain undesigned and require separate review.

## Engineering Requirements

- Preserve config-driven design.
- Avoid hard-coded dataset assumptions.
- Permit roadmap family registration without extending a permanent Python task enum.
- Keep CLI operations reproducible.
- Add tests when schemas, metrics, or runners change.

## Scientific Requirements

- Task configs must resolve to a registered family, type, variant, and stable instance ID.
- Release records must not include roadmap, discovery, feasibility-only, or deferred tasks.
- Task-instance decisions must not become task-family definitions.
- Source configs must align with the source registry policy.
- Evaluation code must not imply publication-grade validity before review.

## Next Recommended Action

Recruit independent reviewers for the five v0.1 task instances and conduct metadata-only source feasibility reviews before any task freeze or real-data pilot.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial architecture overview. | TO_REVIEW_LATER |
| 2026-09-09 | Added open-world task taxonomy and explicit release-membership architecture. | TO_REVIEW_LATER |
| 2026-09-09 | Reconciled the validated open-world scope policy with independently governed task and release artifacts. | TO_REVIEW_LATER |
