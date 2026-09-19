# Source Contamination Registry

## Purpose

Track evidence about overlap and model-exposure risk without claiming that a source or example is contamination-free.

## Status

Current status: SUBMITTED_TO_REVIEW

Authorization effect: NONE

Machine-readable registry: `configs/governance/source_contamination.yaml`

## States

| State | Meaning |
| --- | --- |
| `KNOWN_OVERLAP` | A documented relationship establishes overlap with another registered source. |
| `ELEVATED_RISK` | Wide distribution, benchmark reuse, aggregation, or likely pretraining exposure requires enhanced review. |
| `CONTAMINATION_NOT_ESTABLISHED` | Investigation did not establish contamination; this is not evidence of absence. |
| `NOT_ASSESSED` | No adequate contamination assessment exists. |
| `NOT_APPLICABLE` | The record cannot serve as scientific evidence. |

`CONTAMINATION_FREE` is prohibited unless a future validated policy defines and supports that claim.

## Required Provenance

Future test candidates must retain source, source unit, item locator, version, content hash, origin, and derivation history. Reviews must check registered sources, benchmark test sets, common multilingual corpora, and documented model-training sources. Unknown model training data remains `EXTERNAL_EVIDENCE_REQUIRED`.

## Acceptance Criteria

- Every non-synthetic registered source has exactly one contamination record.
- Overlap references resolve to registered sources.
- No contamination state changes a legal, ethics, scientific-inclusion, or release gate.
- Split and release reports state unresolved contamination limitations.

## Next Action

Define exact- and near-overlap procedures only after bounded source artifacts are legally available for analysis.

