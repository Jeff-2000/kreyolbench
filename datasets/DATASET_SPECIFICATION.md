# Dataset Specification

## Purpose

Define the canonical dataset row model and task payload expectations.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes for task semantics.

## Current Row Model

Rows are JSONL objects with:

- `id`
- `task`
- `language`
- `split`
- `domain`
- `source`
- `input`
- `target`
- `metadata`

## Task Payloads

| Task | Required input | Required target | Status |
| --- | --- | --- | --- |
| classification | `text` | `label` | SUBMITTED_TO_REVIEW |
| sentiment | `text` | `label` | SUBMITTED_TO_REVIEW |
| NER | `tokens` | `tags` | SUBMITTED_TO_REVIEW |
| QA | `context`, `question` | `answers` | SUBMITTED_TO_REVIEW |
| retrieval | `query` | `relevant_docs` | SUBMITTED_TO_REVIEW |
| summarization | `document` | `summary` | BLOCKED pending metric review |
| normalization | `raw_text` | `normalized_text` | SUBMITTED_TO_REVIEW |
| translation | `source_text`, `source_lang` | `references` | BLOCKED pending metric review |
| code-switching | `tokens` | `sentence_lang` plus optional token labels | SUBMITTED_TO_REVIEW |

## Requirements

- IDs must be stable and unique.
- Source metadata must be complete.
- Splits must follow `SPLIT_POLICY.md`.
- Raw/normalized linkage must be preserved.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial dataset specification. | SUBMITTED_TO_REVIEW |

