# Source Use and Contamination Firewall

## Status

Current status: `EXPERT_VALIDATED` at project-policy level under `KB-DATA-004`.

Individual sources remain independently governed and non-authorized unless their legal, ethics, scientific, and release gates explicitly change.

## Rule

A scientific role is not permission. KreyolBench tracks source role, training eligibility, evaluation eligibility, legal status, ethics status, scientific inclusion, contamination, and release membership independently.

`configs/governance/source_use.yaml` is the machine-readable role ledger. `configs/governance/source_contamination.yaml` is the contamination and protected-split ledger.

## Eligibility Semantics

| Value | Meaning |
| --- | --- |
| `PROHIBITED` | The resource cannot enter that use under current governance. |
| `REQUIRES_REVIEW` | Use remains a proposal requiring all applicable gates. |
| `PROTECTED_REFERENCE` | Evaluation identity must be preserved; training is prohibited. |
| `REFERENCE_ONLY` | Methodology or context only; no corpus-coverage credit. |
| `NOT_APPLICABLE` | The role does not currently apply. |

No value grants collection, transformation, redistribution, publication, or release permission.

## Contamination Requirements

- Preserve canonical resource, subset, immutable revision, protected splits, parents, derivatives, and possible overlaps.
- Never use `CONTAMINATION_FREE` without affirmative, reviewable evidence; the governed vocabulary intentionally excludes it.
- Treat unknown overlap as unknown, not absent.
- Prohibit protected benchmark components from training, instruction tuning, retrieval indexing for training, or model selection.
- Require exact provenance and hashes before frozen release use.
- Keep aggregator and component lineage explicit for CreoleVal, OPUS, Kreyol-MT, and similar families.

## Acceptance Criteria

- Every registered non-synthetic source and every unresolved/reference lead has exactly one source-use and contamination record.
- Source families never back example-level provenance.
- Mirrors do not inherit upstream rights.
- Feasibility does not mutate authorization.
- Release eligibility remains false until every applicable gate is explicitly satisfied.

