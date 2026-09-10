# Annotation Quality Control

## Purpose

Define quality-control requirements for annotation campaigns.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Minimum QC Requirements

- Pilot at least one small batch before full annotation.
- Include gold examples for annotator calibration.
- Use pilot evidence to define a task-specific double-annotation proportion; no universal percentage is approved.
- Review disagreement patterns before scaling.
- Report agreement metrics appropriate to task type.
- Preserve uncertainty labels or flags.

## Agreement Measures

Candidate measures:

- classification: per-label binary agreement, set precision/recall/F1, and bootstrapped chance-adjusted multi-label agreement; ordinary Cohen's kappa alone is insufficient
- NER: exact span/type agreement, boundary-only agreement, and per-type agreement
- code-switching: separate agreement for language identity, token type, contact status, uncertainty, and derived boundaries
- retrieval: graded agreement, assessor overlap, adjudicated qrels, judgment coverage, and pooling sensitivity
- QA: exact span agreement and adjudicated acceptability
- normalization: reference acceptability, decision-class agreement, edit-type agreement, and over-normalization review

Status: SUBMITTED_TO_REVIEW

## Quality Gates

- No public release without documented QC.
- No paper claims about annotation quality without agreement results.
- No final label schema without expert review.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial annotation QC policy. | SUBMITTED_TO_REVIEW |
