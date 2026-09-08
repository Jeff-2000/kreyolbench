# Metrics

## Purpose

Document benchmark metrics, their limitations, and review status.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

| Task | Candidate primary metric | Secondary metrics | Current concern | Status |
| --- | --- | --- | --- | --- |
| classification | macro F1 | accuracy, weighted F1 | class imbalance and domain skew | SUBMITTED_TO_REVIEW |
| sentiment | macro F1 | accuracy, per-label F1 | label validity needs review | SUBMITTED_TO_REVIEW |
| NER | span F1 | precision, recall, token accuracy | entity taxonomy needs expert review | SUBMITTED_TO_REVIEW |
| QA | exact match/F1 | unanswerable accuracy | answer normalization may bias results | SUBMITTED_TO_REVIEW |
| retrieval | nDCG@k | MRR@k, recall@k | qrel quality and pooling needed | SUBMITTED_TO_REVIEW |
| normalization | exact match | token accuracy, edit distance | multiple valid normalizations possible | SUBMITTED_TO_REVIEW |
| code-switching | macro F1 or token F1 | sentence accuracy | language-boundary ambiguity | SUBMITTED_TO_REVIEW |
| translation | chrF/COMET/human eval | BLEU | current code uses placeholder exact/token style | BLOCKED |
| summarization | human eval/ROUGE/BERTScore | factuality checks | current code uses placeholder exact/token style | BLOCKED |

## Metric Rules

- Define averaging scheme.
- Report per-domain and per-label slices where relevant.
- Include uncertainty when results support claims.
- Do not interpret tiny differences as meaningful without analysis.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial metric governance specification. | SUBMITTED_TO_REVIEW |

