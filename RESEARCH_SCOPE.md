# Research Scope

## Purpose

Define what KreyolBench may include, what belongs later, and what requires expert review before expansion.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Current Scope

KreyolBench focuses on Haitian Creole NLP benchmark infrastructure. Current candidate tasks include:

- topic/domain classification
- sentiment
- named entity recognition
- extractive question answering
- retrieval
- summarization
- normalization
- translation evaluation
- code-switch detection
- orthographic robustness

## v0.1 Candidate Scope

The current scaffold lists classification, NER, QA, retrieval, normalization, code-switch detection, and translation metadata evaluation as v0.1 candidates.

Status: SUBMITTED_TO_REVIEW

Reason: task count, source feasibility, annotation burden, and metric validity need expert validation before freezing.

## Deferred or Conditional Scope

- sentiment: useful, but needs domain-specific label validity review.
- summarization: useful, but requires stronger metric and human evaluation design.
- orthographic robustness: scientifically important, but depends on normalization policy.
- speech/ASR: strategically important, but may belong in a companion repository or future KreyolBench track.
- TTS: not part of current NLP scaffold unless explicitly expanded.

## Expansion Policy

To add a major task or domain:

1. document the research gap
2. define the real-world use case
3. identify sources and licenses
4. define input/output schema
5. define metrics and statistical evaluation
6. estimate annotation burden
7. log a decision in `DECISIONS.md`
8. mark for expert review when scientifically material

## Acceptance Criteria

- No task is added only because it is technically easy.
- Every task has a research motivation and evaluation protocol.
- Every task has a status and expert-review state.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial research scope register. | SUBMITTED_TO_REVIEW |

