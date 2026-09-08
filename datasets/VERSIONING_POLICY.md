# Dataset Versioning Policy

## Purpose

Define dataset versioning and release expectations.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Version Types

- scaffold version: code/config structure without real release data
- pilot version: small reviewed dataset for method testing
- benchmark version: frozen release with documented splits and metrics
- patch version: metadata or documentation correction without changed examples

## Requirements

- Dataset versions must identify source registry version, split version, and task versions.
- Changing examples or labels requires a new dataset version.
- Public releases need changelog entries and dataset-card updates.
- Deprecated versions remain documented.

## Current State

`v0.1` currently describes scaffold intent and should not be treated as a validated benchmark release unless expert review and release gates are complete.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial dataset versioning policy. | SUBMITTED_TO_REVIEW |

