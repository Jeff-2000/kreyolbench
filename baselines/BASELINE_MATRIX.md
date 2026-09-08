# Baseline Matrix

## Purpose

Define candidate baseline families and comparison settings.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

| Family | Examples | Setting | Tasks | Status |
| --- | --- | --- | --- | --- |
| Random/majority | label prior, random ranker | trivial baseline | classification, sentiment, retrieval | DRAFT |
| Classical | TF-IDF + logistic regression/SVM | supervised | classification, sentiment, retrieval | DRAFT |
| Sequence tagging | CRF, BiLSTM-CRF if justified | supervised | NER, code-switching | DRAFT |
| Multilingual encoders | mBERT, XLM-R, AfroXLM-R if justified | fine-tuned or transfer | classification, NER, QA | SUBMITTED_TO_REVIEW |
| Sentence embeddings | multilingual sentence transformers | retrieval | retrieval, clustering | DRAFT |
| MT models | NLLB, M2M, Marian where appropriate | zero-shot/fine-tuned | translation | SUBMITTED_TO_REVIEW |
| Instruction LLMs | open multilingual instruct models | zero-shot/few-shot | QA, summarization, classification | SUBMITTED_TO_REVIEW |

## Rules

- Report results by training setting.
- Do not blend public-test and hidden-test results.
- Include compute and data declarations.
- Treat proprietary frontier-model results as non-reproducible unless full run metadata is recorded.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial baseline matrix. | SUBMITTED_TO_REVIEW |

