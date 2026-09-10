# Adjudication Protocol

## Purpose

Define how annotation disagreements are resolved.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Process

1. Collect independent annotations.
2. Identify disagreements by task-specific comparison.
3. Categorize disagreement type.
4. Adjudicator reviews raw text, context, source metadata, and guideline rule.
5. Final label is recorded separately from original annotator labels.
6. Update guidelines if repeated ambiguity appears.

## Disagreement Categories

- ambiguous text
- label boundary disagreement
- entity type disagreement
- NER discontinuity or unsupported nesting
- code-switch language identity, borrowing, contact status, or tokenization
- orthographic normalization disagreement
- normalization authority or acceptable-variant disagreement
- retrieval relevance, authority, freshness, or unjudged-treatment disagreement
- source/context missing
- guideline gap
- annotator error

## Records to Preserve

Private:

- annotator IDs
- timestamps
- disagreement logs
- adjudicator notes when personally identifying

Public or release-safe:

- aggregate agreement metrics
- common disagreement categories
- guideline updates
- anonymized examples where license and privacy permit

## Acceptance Criteria

- Adjudicated labels are traceable.
- Original annotations are preserved privately.
- Guideline changes are recorded.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial adjudication protocol. | SUBMITTED_TO_REVIEW |
