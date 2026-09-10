# Assumptions Register

## Purpose

Track assumptions so future work does not silently convert them into facts.

## Status

Current status: IN_PROGRESS

Owner: Codex

Requires expert validation: Yes for high-risk assumptions.

## Format

| ID | Description | Rationale | Risk if false | Validation method | Status |
| --- | --- | --- | --- | --- | --- |
| KB-ASM-001 | Native Haitian Creole speakers and linguists can review annotation guidelines. | Benchmark quality depends on language expertise. | Labels may encode non-native assumptions. | Recruit expert reviewers and document feedback. | SUBMITTED_TO_REVIEW |
| KB-ASM-002 | Some candidate sources will permit redistribution or derived release. | Existing configs include public web and corpus sources. | Dataset release may need link-only or derived-only mode. | Complete source registry license review. | SUBMITTED_TO_REVIEW |
| KB-ASM-003 | v0.1 can focus on text NLP before speech expansion. | Current package architecture is text-first. | Strategic ASR opportunity may need separate track. | Expert roadmap review. | TO_REVIEW_LATER |
| KB-ASM-004 | Small team resources are sufficient for a pilot benchmark. | Current scaffold targets v0.1, not full-scale release. | Annotation and validation may exceed capacity. | Estimate annotation budget and sprint capacity. | TO_REVIEW_LATER |
| KB-ASM-005 | Baseline evaluation can start with open multilingual models. | Likely feasible without proprietary APIs. | Compute or licensing constraints may limit comparability. | Baseline matrix and compute policy review. | TO_REVIEW_LATER |
| KB-ASM-006 | Public-interest domains are central to publication positioning. | README and blueprint prioritize health, education, civic, disaster, search, and translation. | Overly broad domains may reduce coherence. | Expert validation of v0.1 domains. | SUBMITTED_TO_REVIEW |
| KB-ASM-007 | Apache-2.0 is appropriate for code, but not necessarily data. | Existing license separates code and data. | Contributors may mistakenly assume data inherits code license. | Data card and source registry review. | SUBMITTED_TO_REVIEW |

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial assumptions register. | IN_PROGRESS |
| 2026-09-08 | Corrected KB-ASM-007 because no explicit expert-validation record was available. | SUBMITTED_TO_REVIEW |
