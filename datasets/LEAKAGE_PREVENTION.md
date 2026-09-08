# Leakage Prevention

## Purpose

Prevent train/test contamination and invalid benchmark claims.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Leakage Types

- duplicate IDs
- exact duplicate text
- near-duplicate text
- same document split across train and test
- benchmark examples copied from public model prompts
- hidden-test leakage through examples or docs
- answer leakage in QA metadata

## Required Checks

- ID uniqueness across full dataset.
- Text hashing for exact duplicates.
- Near-duplicate detection for long text and generated examples.
- Source-document grouping before split.
- Manual review for public examples copied into prompts.

## Release Gate

No public benchmark release should proceed without a leakage report.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial leakage prevention policy. | SUBMITTED_TO_REVIEW |

