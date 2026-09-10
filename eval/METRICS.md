# Metrics

## Purpose

Document benchmark metrics, their limitations, and review status.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

| Task | Candidate primary metric | Secondary metrics | Current concern | Status |
| --- | --- | --- | --- | --- |
| classification | multi-label macro F1 | micro/sample F1, subset accuracy, per-label scores | prevalence, thresholding, and co-occurrence | SUBMITTED_TO_REVIEW |
| sentiment | macro F1 | accuracy, per-label F1 | label validity needs review | SUBMITTED_TO_REVIEW |
| NER | exact contiguous character-span micro F1 | per-type and boundary scores; nesting diagnostic only if activated | entity ontology and boundary policy need external review | SUBMITTED_TO_REVIEW |
| QA | exact match/F1 | unanswerable accuracy | answer normalization may bias results | SUBMITTED_TO_REVIEW |
| retrieval | nDCG@10 candidate | judged@10, bpref, MRR@10, recall@10, pooling-depth sensitivity | metric treatment of unjudged documents and pooling adequacy need external review | SUBMITTED_TO_REVIEW |
| normalization | exact match to any reference on core stratum candidate | core edit scores, auxiliary capitalization/punctuation strata, over-normalization | normative evidence, multiple valid forms, and semantic preservation | SUBMITTED_TO_REVIEW |
| code-switching | token-language macro F1 candidate | contact-status and joint scores, per-language F1, active-switch boundaries | borrowing, contact ontology, and language ambiguity | SUBMITTED_TO_REVIEW |
| translation | chrF/COMET/human eval | BLEU | current code uses placeholder exact/token style | BLOCKED |
| summarization | human eval/ROUGE/BERTScore | factuality checks | current code uses placeholder exact/token style | BLOCKED |

## Metric Rules

- Define averaging scheme.
- Report per-domain and per-label slices where relevant.
- Include uncertainty when results support claims.
- Do not interpret tiny differences as meaningful without analysis.
- Report retrieval judgment coverage and state explicitly how every metric treats unjudged documents.
- Tune classification thresholds only on validation data and report fixed and tuned results separately.
- Keep normalization auxiliary strata out of the primary score until external approval.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial metric governance specification. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Added revised multi-label, contiguous-span, incomplete-qrel, normalization-stratum, and factorized code-switching metric requirements. | SUBMITTED_TO_REVIEW |
