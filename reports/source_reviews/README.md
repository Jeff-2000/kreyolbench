# Source Feasibility Reviews

## Purpose

This directory records public, metadata-only evidence about registered KreyolBench source candidates. It supports prioritization of later legal, ethical, linguistic, and scientific review; it does not authorize source use.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex, with AI assistance disclosed

Review date: 2026-09-10

## Method

1. Match each report to exactly one schema-v2 source registry record.
2. Prefer an official provider page, license or terms page, archival catalog, dataset card, repository, or primary paper.
3. Separate direct facts from reviewer inference and preserve `UNKNOWN` where evidence is absent.
4. Assess endpoint identity, metadata access, rights evidence, language/register evidence, provenance/versionability, ethics/privacy, task fit, and duplication/contamination.
5. Recommend only a next review action. Public availability, an API, `robots.txt`, or a download link never establishes permission.

No corpus files, dumps, documents, audio, models, or archives were downloaded. No source was collected, annotated, transformed, redistributed, scientifically included, or made release-eligible.

## Evidence States

| State | Meaning |
| --- | --- |
| `EVIDENCE_AVAILABLE` | Authoritative public evidence directly supports the limited metadata claim. |
| `PARTIAL` | Some evidence exists, but material facts remain unresolved. |
| `MISSING` | No adequate evidence was identified in this review. |
| `BLOCKED` | The dimension cannot currently proceed, for example because the endpoint is unavailable or ethics scoping is undefined. |

`CONDITIONAL` means scientific feasibility warrants bounded next-stage review. It is not approval. `BLOCKED` means actionable use cannot responsibly progress, although discovery value may remain.

Schema v3 separates scientific feasibility from identity, Haitian-language evidence, task fit, provenance readiness, privacy, contamination, and every authorization axis. Review history distinguishes `ORIGINAL_CODEX_METADATA_ASSESSMENT`, `PROJECT_LEAD_REVIEW_DECISION`, and `IMPLEMENTATION_EVIDENCE_CHECK`.

## Review Groups

- Pilot-facing: institutional, government, health, education, civic, Wikimedia, and Radio Haiti records.
- Research-resource: CMU, CreoleVal, Kreyol-MT, MIT-Ayiti, OPUS, Universal Dependencies, and eBible.
- Discovery: broad institutional, government, media, diaspora, and social-media families.

## Acceptance Gate

Every non-synthetic registered source must have one ledger record and one evidence report. The synthetic `sample` record is reviewed separately and remains excluded from scientific evidence. Human reviewers must confirm or revise findings before permission requests or source use proceeds. Under KB-DATA-003, metadata-only child registration may proceed with documented identity and language evidence; it grants no authorization.

## Discovery Expansion

See `datasets/SOURCE_DISCOVERY.md` and `reports/SOURCE_DISCOVERY_EXPANSION_REVIEW_PACKET_V0_1.md`. The initial 21-candidate packet and schema-v1 ledger are historical snapshots. Active feasibility schema v3 requires direct claim-level evidence, independent assessment axes, attributed review events, and external-evidence gates; inferred suitability remains `PARTIAL`. Discovery reports include unresolved leads and references that are not registered research corpora. No source count is a corpus-size or coverage measure.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-10 | Added methodology and first complete metadata-only review set. | SUBMITTED_TO_REVIEW |
| 2026-09-18 | Recorded the Project-Lead review, required corrections, and append-only evidence attribution. | SUBMITTED_TO_REVIEW |
