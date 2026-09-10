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

The current `task` value is a runtime compatibility alias resolved through `configs/tasks/`. It is not the stable scientific identity or an exhaustive task universe. Task-instance identity and release membership live in the task and release registries.

## Task Payloads

| Task | Required input | Required target | Status |
| --- | --- | --- | --- |
| classification | `text` | non-empty multi-label `labels` | SUBMITTED_TO_REVIEW |
| sentiment | `text` | `label` | SUBMITTED_TO_REVIEW |
| NER | raw `text` | typed character-span `entities` | SUBMITTED_TO_REVIEW |
| QA | `context`, `question` | `answers` | SUBMITTED_TO_REVIEW |
| retrieval | separate `queries.jsonl` | separate corpus and graded qrels | SUBMITTED_TO_REVIEW |
| summarization | `document` | `summary` | BLOCKED pending metric review |
| normalization | `raw_text` | orthography-only `references` and typed `edits` | SUBMITTED_TO_REVIEW |
| translation | `source_text`, `source_lang` | `references` | BLOCKED pending metric review |
| code-switching | `tokens` | aligned `token_langs` and `token_types` | SUBMITTED_TO_REVIEW |

## Requirements

- IDs must be stable and unique.
- Source metadata must be complete.
- Splits must follow `SPLIT_POLICY.md`.
- Raw/normalized linkage must be preserved.
- Example provenance must follow `EXAMPLE_PROVENANCE.md`.
- Retrieval uses linked corpus, query, and qrel artifacts rather than the general row model.
- The five task-specific contracts in `datasets/tasks/` remain provisional until independent review.
- Future roadmap task families may be registered without creating dataset rows or implemented payload contracts.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial dataset specification. | SUBMITTED_TO_REVIEW |
