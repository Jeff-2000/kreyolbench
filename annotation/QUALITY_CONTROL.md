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
- Double annotate a defined subset, initially 20--30 percent for v0 pilots.
- Review disagreement patterns before scaling.
- Report agreement metrics appropriate to task type.
- Preserve uncertainty labels or flags.

## Agreement Measures

Candidate measures:

- classification: accuracy, Cohen's kappa, Krippendorff's alpha where suitable
- NER/code-switching: span-level agreement and token-level agreement
- retrieval: graded agreement and adjudicated qrels
- QA: exact span agreement and adjudicated acceptability
- normalization: exact agreement and edit-type agreement

Status: SUBMITTED_TO_REVIEW

## Quality Gates

- No public release without documented QC.
- No paper claims about annotation quality without agreement results.
- No final label schema without expert review.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial annotation QC policy. | SUBMITTED_TO_REVIEW |

