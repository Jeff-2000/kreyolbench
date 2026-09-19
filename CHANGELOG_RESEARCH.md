# Research Changelog

## 2026-09-19

- Implemented Jeff Pierre's 2026-09-18 expanded source-review decisions with explicit human attestation and AI-assisted evidence-synthesis disclosure.
- Added `KB-SRCREV-002`, `KB-DATA-004`, `KB-DATA-005`, and `KB-ENG-010` to both decision registries.
- Added complete source-use and contamination-firewall ledgers covering registered sources and unresolved/reference leads.
- Registered metadata-only VoxLingua107 Haitian and Northern Haitian records, and separated Mission 4636 open/non-sensitive and restricted/sensitive children.
- Added canonical content-origin and typed multimodal-provenance contracts while preserving the native Haitian vision-language evidence gap.
- Protected FLORES+ and CreoleVal evaluation material from training use; no source authorization, task status, or release membership changed.

## Purpose

Track scientific and governance evolution separately from software release notes.

## Status

Current status: IN_PROGRESS

Owner: Codex

Requires expert validation: No for logging; Yes for scientific decisions referenced here.

## 2026-09-18

Status: IN_PROGRESS

Changes:

- Recorded `KB-SRCREV-001`, Jeff Pierre's Project-Lead acceptance of the source-feasibility methodology with required corrections.
- Migrated source feasibility to schema v3 with independent scientific axes, append-only attribution, and structured external-evidence gates.
- Revised CMU, government portal, MENFP, and Radio Haiti-Inter summaries to conditional scientific feasibility without changing authorization.
- Added complete categorical prioritization, source-diversity, and contamination ledgers for all 33 non-synthetic source records.
- Preserved MIT-Ayiti and MSPP as pending Project-Lead review and kept 12 later candidates outside the 2026-09-18 human review.

Scientific implications:

- No source acquisition, annotation, training, scientific inclusion, release membership, or release authorization occurred.

## 2026-09-01

Status: IN_PROGRESS

Changes:

- Added project knowledge architecture plan.
- Added formal review-status system.
- Added initial decision, assumption, and risk registers.
- Identified current scaffold as not yet a validated benchmark release.
- Marked v0.1 task freeze, source inclusion, metrics, split policy, and publication claims as requiring expert review.

Scientific implications:

- Current results and sample data must not be represented as benchmark findings.
- Translation and summarization metrics require stronger design before publication use.

## 2026-09-08

Status: SUBMITTED_TO_REVIEW

Implemented:

- machine-readable decision registry and typed eight-state review model
- governance metadata on benchmark, task, label, and source configurations
- deterministic `audit-governance` CLI output for maintainers and CI
- source redistribution consistency checks
- sample-data checks for identifiers, split contamination, source resolution, labels, and raw/normalized linkage
- explicit synthetic-fixture source provenance
- v0.1 expert-review packet

Scientific state:

- all seven scientific governance decisions remain `SUBMITTED_TO_REVIEW`
- translation and summarization evaluation remain `BLOCKED`
- structural audit success does not confer scientific approval
- no datasets were downloaded, no models were trained, and no benchmark task was frozen

Validation:

- 43 tests passed
- the governance audit returned `PASS` with `release_eligible: false`
- lint passed for all files introduced or modified by this implementation

## 2026-09-09

Status: SUBMITTED_TO_REVIEW

Implemented:

- reconciled six approved governance policies with the human review record
- added expert-validated open-world source discovery (`KB-DATA-003`)
- recorded the expert-validated five-task v0.1 pilot scope (`KB-SCOPE-001`)
- revised and resubmitted the multi-axis source authorization policy (`KB-DATA-001`)
- migrated all committed source records to schema version 2
- expanded the source inventory with institutional, government, educational,
  archival, linguistic, media, diaspora, and social-media candidate families
- added typed source gates, hierarchy checks, release checks, and legacy adapter compatibility

Scientific state:

- `KB-DATA-001` remains the only unresolved project-level decision in the packet
- candidate registration authorizes metadata discovery only
- task-level labels, metrics, split details, source inclusion, and annotation campaigns remain provisional
- no source content was downloaded, scraped, annotated, or redistributed

Validation:

- 62 tests passed
- governance audit returned `PASS` with `release_eligible: false`
- the only unresolved decision reported was `KB-DATA-001`

### Task Specification and Feasibility Phase

Status: SUBMITTED_TO_REVIEW

Implemented:

- recorded the second approval of `KB-DATA-001` and synchronized project-policy status
- added append-only machine-readable review events and evidence-path validation
- established the independent external task-review gate `KB-GOV-002`
- added detailed specifications for classification, NER, retrieval, normalization, and code-switching
- added Markdown and YAML feasibility matrices without unsupported numerical readiness scores
- added example-level provenance, content-origin, and derivation-step contracts
- migrated synthetic fixtures to multi-label classification, character-span NER,
  orthography-only normalization, direct token language IDs, and separate retrieval artifacts

Scientific state:

- project-policy review is complete
- all five task decisions remain `SUBMITTED_TO_REVIEW`
- all five tasks remain `CONDITIONAL` because source authorization,
  representativeness, and pilot evidence are incomplete
- no source content was downloaded, scraped, annotated, or redistributed

Validation target:

- governance audit must return `PASS` with `release_eligible: false`
- unresolved decisions must be the five task decisions, not `KB-DATA-001`
- task specifications require independent external review before freeze

### Open-World Scope Architecture

Policy status: EXPERT_VALIDATED

Registry-content status: SUBMITTED_TO_REVIEW

Implemented:

- separated the research program, benchmark ecosystem, task families, task types, variants, instances, and release membership
- added open-world task and domain registries without adding future task implementations
- assigned stable identifiers to all current task instances
- replaced task-level `v0`, `scope_tier`, and `release_candidate` fields with independent scientific and scope statuses
- added an authoritative v0.1 release record containing five pilot candidates, QA feasibility work, deferred translation, and no included tasks
- added `KB-SCOPE-002` for expert review and `KB-ENG-005` for engineering traceability
- revised task specifications, publication planning, and public documentation so v0.1 choices do not define permanent task families
- added audit enforcement for taxonomy resolution, domain registration, release membership, and prohibited automatic inclusion

Scientific state:

- the five v0.1 task instances remain unchanged and `SUBMITTED_TO_REVIEW`
- `KB-SCOPE-002` was approved through internal project-lead scientific review at project-scope governance level
- the approval does not validate taxonomy contents, task instances, sources, datasets, metrics, or release expansion
- roadmap families and domains are registered possibilities, not validated or implemented components
- no task is `INCLUDED_IN_RELEASE`
- no data were acquired, scraped, annotated, or redistributed

Validation:

- 103 tests passed
- Ruff passed
- text and JSON governance audits returned `PASS` with zero errors and warnings
- release eligibility remains false with five unresolved task decisions

### Pre-External Task Specification Revision

Status: SUBMITTED_TO_REVIEW

Implemented:

- recorded a public AI-assisted internal audit adopted by Jeff Pierre, without representing it as independent review
- established `KB-GOV-003`, requiring identifiable external human reviewers, affiliations, relevant expertise, conflicts, dates, and evidence
- revised classification ontology and agreement rules, NER offset and span rules, retrieval judgment methodology, normalization construct boundaries, and code-switching contact semantics
- added machine-readable review requirements and reviewer qualification checks
- added reusable external-review evidence templates
- retained all five task instances as `PILOT_CANDIDATE` and `CONDITIONAL`

Scientific state:

- each task has an internal `REVISED` event and a corrected specification
- all five decisions are resubmitted as `SUBMITTED_TO_REVIEW`
- no external approval, pilot authorization, source inclusion, metric freeze, or release inclusion exists
- source review remains metadata-only

Validation target:

- governance audit returns `PASS` with zero errors and warnings
- exactly the five task decisions remain unresolved
- release eligibility remains false

### Metadata-Only Source Feasibility Review

Status: SUBMITTED_TO_REVIEW

Implemented:

- added a typed feasibility ledger with eight non-numeric evidence dimensions
- reviewed all 21 non-synthetic source candidates and the synthetic test control
- added public source-specific evidence reports, a consolidated review packet,
  and a provisional source-to-task matrix
- added audit checks for complete coverage, evidence paths, task references,
  source-family restrictions, non-authorizing conclusions, and unchanged gates
- reconciled only directly observed public metadata without elevating permissions

Scientific state:

- 12 candidates are `CONDITIONAL` for further human review and 9 are `BLOCKED`
- these are metadata-triage conclusions, not readiness or authorization states
- all legal, ethical, collection, derived-use, redistribution, scientific, and
  release gates remain non-approved
- the synthetic control remains excluded from scientific evidence
- no source content was downloaded, scraped, annotated, transformed, or redistributed

Validation target:

- exactly 21 candidate reviews and one synthetic-control review resolve
- governance audit returns `PASS` with exactly five unresolved task decisions
- release eligibility remains false

### Expanded Source Discovery

Status: SUBMITTED_TO_REVIEW

Implemented 22 deduplicated leads across text, speech, linguistic and multimodal research: 15 registered-source references, four unresolved leads and three references. Twelve metadata-only source registrations extend the active ledger to 33 candidates plus the synthetic control. Preserved the initial 21-candidate assessment and every existing source authorization state.

Added claim-level feasibility evidence, attributed size records, cross-source provenance relationships, domain/modality hypotheses and engineering decision KB-ENG-008. Corrected Aya origin claims, separated UD treebanks and preserved source-specific rights uncertainty. Inferred task fit and risk assessments remain PARTIAL, not direct evidence. No dataset content was acquired or benchmark scope frozen. Validation results are recorded in the implementation handoff.

### Project-Lead Source-Feasibility Review

Status: EXPERT_VALIDATED for methodology and Project-Lead prioritization only

Implemented:

- recorded Jeff Pierre's 2026-09-18 review as `KB-SRCREV-001`, with internal Project-Lead independence and an explicit no-authorization boundary
- preserved the original Codex assessment, appended 19 Project-Lead source decisions, and separated later Codex implementation evidence checks
- represented 14 reviewed sources as conditionally feasible and five as blocked for actionable use
- retained `mit_ayiti_resources` and `mspp_publications` in a dedicated pending Project-Lead queue
- kept 12 subsequently registered source candidates outside the scope of this human review
- introduced feasibility schema v3 with independent assessment axes and structured external-evidence requirements
- added complete source-prioritization, representativeness, and contamination ledgers without numerical readiness scores
- strengthened evidence for CMU, Haitian government communications, eBible, Kreyol-MT, Radio Haiti, UN assets, UD treebanks, and Wikimedia provenance

Scientific and authorization state:

- `CONDITIONAL` means only that bounded next-stage review is scientifically worthwhile
- no legal, collection, derived-use, redistribution, commercial-use, ethics, scientific-inclusion, or release gate was elevated
- no new content-bearing child record was created
- no source content was acquired, scraped, annotated, transformed, trained on, or redistributed
- release eligibility remains false and the five task decisions remain unresolved

Validation:

- Ruff passed
- 174 tests passed
- deterministic text and JSON governance audits returned `PASS` with zero errors and warnings
- source attribution, pending-review, hierarchy, contamination, and no-authorization invariants passed

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial research changelog. | IN_PROGRESS |
| 2026-09-08 | Operationalized scientific governance and added expert-review gate. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Reconciled expert decisions and implemented open-world source governance schema v2. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Validated KB-SCOPE-002 at project-scope level while preserving all downstream scientific gates. | EXPERT_VALIDATED |
| 2026-09-09 | Added task specifications, feasibility evidence, external review gates, and example provenance. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Added open-world task/domain taxonomy and bounded release membership. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Revised all five task specifications after the AI-assisted internal audit and added qualified external human review enforcement. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Added complete metadata-only source feasibility evidence and enforcement without authorizing source use. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Expanded open-world source discovery while preserving all source authorization gates. | SUBMITTED_TO_REVIEW |
| 2026-09-18 | Implemented the Project-Lead source-feasibility review, multi-axis evidence model, and planning ledgers without authorizing source use. | EXPERT_VALIDATED |
