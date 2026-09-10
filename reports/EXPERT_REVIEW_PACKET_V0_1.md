# KreyolBench v0.1 Expert Review Packet

## Purpose

This packet provides a bounded review interface for the scientific decisions that currently block a KreyolBench v0.1 task freeze, annotation campaign, and release claim. It summarizes existing proposals; it does not replace the detailed specifications linked below.

## Status

Current status: EXPERT_VALIDATED

Owner: Project lead

Requires expert validation: No at project-policy level; downstream task and source decisions require review

Review state: All project-level decisions in this packet have completed internal
project-lead review. This approval permits task specification and source-specific
feasibility work; it does not approve any task or source for release.

Outstanding downstream gates:

- final v0.1 benchmark task freeze
- source inclusion and collection authorization
- annotation campaign launch
- primary metric freeze
- train/validation/test split freeze
- publication and leaderboard claims

## Review Instructions

For each decision, mark exactly one outcome:

- `[ ] APPROVE`: accept the decision as written and change its status to `EXPERT_VALIDATED`.
- `[ ] REVISE`: provide required changes; change its status to `NEEDS_REVISION`.
- `[ ] DEFER`: retain `SUBMITTED_TO_REVIEW` and do not start dependent scientific work.

Record reviewer name, date, rationale, and any conditions. Approval applies only to the stated decision, not to every artifact that cites it.

## Decision Summary

| Decision | Subject | Current status | Principal dependency |
| --- | --- | --- | --- |
| KB-DEC-001 | Review-status policy | EXPERT_VALIDATED | All scientific governance |
| KB-DATA-001 | Multi-axis source registry and release authorization | EXPERT_VALIDATED | Collection and release |
| KB-DATA-002 | Raw/normalized text preservation | EXPERT_VALIDATED | Preprocessing and normalization |
| KB-DATA-003 | Open-world source discovery | EXPERT_VALIDATED | Registry expansion |
| KB-ANN-001 | Annotation quality control | EXPERT_VALIDATED | Annotation pilot |
| KB-EVAL-001 | Metrics and statistical testing | EXPERT_VALIDATED | Baselines and leaderboard |
| KB-SPLIT-001 | Splits, leakage, and contamination | EXPERT_VALIDATED | Dataset freeze |
| KB-PUB-001 | Publication artifact traceability | EXPERT_VALIDATED | Manuscript claims |
| KB-SCOPE-001 | v0.1 scientific pilot task scope | EXPERT_VALIDATED | Task-level feasibility work |

## KB-DEC-001: Project-Wide Review Status Policy

### Proposed Decision

Use the following statuses across major artifacts: `DRAFT`, `IN_PROGRESS`, `TO_REVIEW_LATER`, `SUBMITTED_TO_REVIEW`, `EXPERT_VALIDATED`, `NEEDS_REVISION`, `BLOCKED`, and `DEPRECATED`.

Important scientific decisions must be explicitly validated before dependent scientific work is frozen or released. Routine engineering may continue when it does not change scientific meaning.

### Evidence to Inspect

- `SCIENTIFIC_GOVERNANCE.md`
- `AGENTS.md`
- `configs/governance/decisions.yaml`

### Review Questions

- Are the eight states clear enough for international collaborators?
- Is the boundary between engineering and scientific decisions appropriate?
- Are any review gates unnecessarily strict or dangerously permissive?

### Expert Decision

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-08

Rationale or required revision:

The project-wide review-status policy is scientifically appropriate and proportionate to the intended scope of KreyolBench. The distinction between scientific decisions requiring explicit expert validation and routine engineering decisions that may proceed independently should be retained.

The status system provides sufficient traceability for research artifacts, dataset decisions, annotation protocols, experimental design, publication claims, and software implementation.

Conditions:

1. EXPERT_VALIDATED must only be assigned after explicit human review.
2. Engineering implementation must not be used to implicitly freeze an unresolved scientific decision.
3. Any material change to an EXPERT_VALIDATED scientific decision must create a new review event and decision-history entry.
4. Status changes must remain synchronized between Markdown governance documents and machine-readable governance files.

## KB-DATA-001: Multi-Axis Source Registry and Release Authorization Gate

### Original Proposed Decision

Require complete source metadata before collection or release. Public availability must not be interpreted as redistribution permission. Each subset must receive an explicit legal/data handling status.

### Revised Multi-Axis Source Model

The originally proposed source states mixed several independent questions. The
revision therefore records discovery, access, legal review, collection,
derived use, redistribution, commercial use, ethics, and scientific inclusion
as separate fields. Approval on one axis never implies approval on another.

| Dimension | Examples | Meaning |
| --- | --- | --- |
| Discovery | `DISCOVERED`, `ENDPOINT_VERIFIED` | Whether a candidate and its endpoint are known |
| Access | `UNKNOWN`, `ACCESSIBLE_FOR_REVIEW`, `RESTRICTED` | Whether metadata or content can currently be inspected |
| Legal review | `NOT_STARTED`, `PENDING`, `APPROVED`, `CONDITIONAL`, `REJECTED` | State of documented rights review |
| Collection | `NOT_REQUESTED`, `PERMISSION_UNKNOWN`, `APPROVED`, `PROHIBITED` | Whether acquisition is authorized |
| Derived use | `UNKNOWN`, `APPROVED`, `CONDITIONAL`, `PROHIBITED` | Whether transformations or derived artifacts are authorized |
| Redistribution | `UNKNOWN`, `APPROVED`, `LINK_ONLY`, `DERIVED_ONLY`, `CONDITIONAL`, `PROHIBITED` | What may be released publicly |
| Commercial use | `UNKNOWN`, `APPROVED`, `CONDITIONAL`, `PROHIBITED` | Whether commercial reuse is permitted |
| Ethics | `NOT_STARTED`, `PENDING`, `APPROVED`, `RESTRICTED`, `REJECTED` | Human, community, privacy, and harm review |
| Scientific inclusion | `PENDING_EXPERT_REVIEW`, `PILOT_ONLY`, `APPROVED`, `EXCLUDED` | Suitability for benchmark evidence |

### Strengthened Candidate Ecosystem

| Source candidate | Scientific role | Initial handling |
| --- | --- | --- |
| Akademi Kreyol Ayisyen | normative, formal, linguistic, terminology | critical candidate; metadata review and permission request only |
| AKA publications and bulletins | formal institutional Kreyol and language guidance | document-level permission review |
| Haitian government communication portal | civic and administrative source discovery | verify Kreyol presence and rights before collection |
| MENFP educational resources | education and school-facing language | per-asset language and legal review |
| MSPP publications | public-health language | legal, privacy, and document-level review |
| Civil Protection resources | disaster-response communication | endpoint, language, legal, and temporal review |
| MIT-Ayiti resources | education, STEM, terminology, possible parallel material | per-resource license and ownership review |
| CreoleVal | benchmark comparison and possible subset reuse | review every upstream subset independently |
| Radio Haiti archive | spoken, natural, code-switched, and diachronic language | high-priority research resource; item-level rights and ethics review |
| Radio Haiti-Inter research corpus | annotated spoken Haitian Creole | verify actual release artifacts, version, and license |
| Wikimedia Haitian Creole | general knowledge and retrieval | conditional attribution/share-alike handling with content-level exceptions |
| CMU Haitian Creole resources | speech and language resources | subset-level legal, speaker, and documentation review |
| OPUS | parallel-resource discovery | family record only; review each selected upstream corpus |
| Kreyol-MT | machine-translation research comparison | license and upstream-subset review |
| Universal Dependencies Haitian Creole | POS, syntax, and linguistic evaluation | treebank-version and upstream-text review |
| Haitian media | contemporary news and register variation | discovery-only family pending publisher records |
| Diaspora publications | diaspora usage and code-switching | discovery-only family with rights and representativeness review |
| Social media | informal language, code-switching, orthographic variation | discovery only; dedicated ethics and platform-terms review required |
| UN Haiti and eBible | civic/development and religious registers | retain as candidates without elevating current authorization |

The candidate registry is not a whitelist and is not a corpus manifest. These
entries authorize metadata discovery only. No candidate in this table is
approved for collection, annotation, redistribution, or benchmark inclusion by
being listed here.

### Review Questions

- Are the source-specific review states sufficient?
- Who is authorized to approve legal, ethical, and scientific inclusion?
- Should any candidate be excluded before feasibility work?

### Expert Decision

- [ ] APPROVE
- [x] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre
Date: 2026-09-08

Rationale or required revision:

The general principle is approved: public availability must never be treated as automatic authorization for collection, transformation, redistribution, benchmark release, or commercial reuse.

However, KB-DATA-001 requires revision before EXPERT_VALIDATED status because the current source registry is too narrow for the scientific objectives of KreyolBench and does not sufficiently distinguish source discovery, collection authorization, derived-use authorization, scientific inclusion, and redistribution.

The registry must support a much broader Haitian Creole data ecosystem while maintaining strict legal, ethical, provenance, and scientific controls.

At minimum, the source model must distinguish:

1. DISCOVERED
2. ACCESSIBLE_FOR_REVIEW
3. COLLECTION_PERMISSION_UNKNOWN
4. COLLECTION_APPROVED
5. DERIVED_USE_APPROVED
6. REDISTRIBUTION_APPROVED
7. REDISTRIBUTION_PROHIBITED
8. SCIENTIFICALLY_APPROVED
9. SCIENTIFICALLY_EXCLUDED
10. PENDING_LEGAL_REVIEW
11. PENDING_ETHICAL_REVIEW
12. PENDING_EXPERT_REVIEW

Scientific inclusion must remain independent of legal/redistribution status.

Required source-registry expansion:

- Akademi Kreyòl Ayisyen (AKA), including publications, bulletins, linguistic resources, terminology, dictionaries/lexicons and other official Kreyòl materials;
- Haitian government communication and ministry publications;
- MENFP educational resources;
- MSPP health resources;
- civil-protection/disaster-response materials;
- MIT-Haiti(MIT-Ayiti) educational resources;
- Radio Haiti-Inter corpus;
- additional scientifically documented Haitian Creole corpora;
- appropriate Wikimedia resources;
- selected media/news corpora subject to permission;
- diaspora Kreyòl material where scientifically justified;
- carefully governed social-media sources for informal language and code-switching research.

No newly added source is thereby approved for dataset collection or redistribution.

Conditions:

A source-discovery expansion may proceed immediately, but collection, annotation at scale, redistribution, or benchmark inclusion must wait for the corresponding legal, ethical, quality, and scientific review.

The registry must include source provenance, access date, publisher/owner, license evidence, collection method, data type, language/register, domain, temporal coverage, geographic relevance where inferable without profiling individuals, machine-generated-content risk, privacy risk, duplication risk, intended benchmark use, and review status.

### Revision Resolution

Resolution: Revised policy approved on second review

Revision completed: 2026-09-09

The source registry has been expanded and the overloaded status list has been
implemented as independent, typed governance dimensions. Source families are
discovery containers; collections and subsets remain subject to source-specific
legal, ethical, quality, and scientific review. The second review below is the
authoritative final project-policy decision.

### Second Expert Review

* [x] APPROVE
* [ ] REVISE
* [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-09

Decision status after second review: `EXPERT_VALIDATED`

Rationale:

The revised `KB-DATA-001` adequately resolves the concerns raised during the
first expert review.

The multi-axis source-governance model appropriately separates discovery,
access, legal review, collection authorization, derived use, redistribution,
commercial use, ethical review, and scientific inclusion. These dimensions
must remain independent: approval on one axis must never be interpreted as
approval on another.

The expanded source ecosystem is sufficiently open-ended for the current
project-policy level. The registry now supports institutional, governmental,
educational, public-health, disaster-response, research, archival, media,
diaspora, social-media, parallel-corpus, linguistic, and other future source
families without treating the current candidate list as exhaustive.

The distinction between source families, collections, and subsets is also
approved. Broad source-family registration is appropriate for discovery and
governance, but benchmark examples must ultimately be traceable to the
specific collection, subset, document, or other provenance unit from which
they originate.

The revised policy is therefore approved as the project-level source
governance framework for KreyolBench v0.1.

This approval authorizes progression to source-specific feasibility and review.
It does NOT authorize any candidate source for collection, scraping,
annotation, transformation, redistribution, benchmark inclusion, or
publication use.

Conditions:

1. Source-specific authorization remains mandatory.

   Every candidate collection or subset intended for actual use must undergo
   its own legal, ethical, quality, provenance, and scientific assessment
   before content acquisition or benchmark inclusion.

2. Scientific suitability must remain independent from legal availability.

   A legally reusable source may still be rejected because of poor linguistic
   quality, weak representativeness, excessive duplication, contamination,
   domain imbalance, translation artifacts, machine-generated content, or
   other threats to benchmark validity.

3. Legal accessibility must remain independent from scientific importance.

   High-value sources such as Akademi Kreyòl Ayisyen materials may remain
   discovery/reference candidates even where collection or redistribution
   permission has not yet been established.

4. Heterogeneous source families must never receive blanket authorization.

   OPUS, media collections, government portals, archives, social-media
   platforms, and similar families require collection-, subset-, document-,
   or platform-specific review as appropriate.

5. Social-media data require an elevated review path.

   Any future social-media collection must receive explicit platform-terms,
   privacy, identifiability, ethics, redistribution, quotation, deletion, and
   research-necessity review before acquisition.

6. Sensitive-domain sources require proportional safeguards.

   Health, humanitarian, disaster-response, archival speech, and other
   potentially sensitive sources must receive privacy and ethical review
   appropriate to their content and provenance.

7. Provenance must remain granular and persistent.

   Dataset examples must retain stable linkage to the most specific permitted
   provenance unit. Discovery-family identifiers alone must never serve as
   final example-level provenance.

8. Machine-generated and translated content must be explicitly tracked.

   Where determinable, provenance should distinguish naturally authored
   Kreyòl, human translation, machine translation, LLM-generated text,
   ASR-derived text, OCR-derived text, and unknown or mixed origins.

9. Source discovery remains open-world.

   Approval of `KB-DATA-001` does not freeze the current source inventory.
   New sources may continue to enter the registry under `KB-DATA-003`, subject
   to the same downstream gates.

10. Future changes that weaken these independent authorization gates require a
    new expert review. Adding new candidate sources under the validated
    open-world discovery policy does not by itself require reopening
    `KB-DATA-001`.

Expert conclusion:

`KB-DATA-001` is approved at the project-policy level and may be changed from
`SUBMITTED_TO_REVIEW` to `EXPERT_VALIDATED`.

The next scientific phase may therefore begin with source-specific assessments
and task-level feasibility/specification work. Dataset acquisition,
large-scale annotation, task-level metric/split freezes, and release claims
remain subject to their applicable downstream approvals.


## KB-DATA-002: Raw and Normalized Text Preservation

### Proposed Decision

Whenever normalization is performed, preserve the source form and an explicit raw-to-normalized linkage. Do not overwrite orthographic, register, dialectal, or code-switching evidence merely to simplify modeling.

### Review Questions

- What transformations qualify as normalization rather than correction?
- Which metadata must accompany each transformation?
- Should multiple acceptable normalized forms be permitted?
- Which transformations require native-speaker or linguist approval?

### Expert Decision

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-08

Rationale or required revision:

Raw/source text preservation is a mandatory scientific requirement.
Normalization must be represented as an explicit derived representation and must never overwrite the original source form.

Conditions:

Every transformation must record:
- transformation_id
- raw_text
- normalized_text
- normalization_version
- transformation_type
- transformation_rule
- automatic_or_human
- reviewer if human-reviewed
- confidence/uncertainty where applicable
- timestamp/version
- reversible linkage to the source example

Multiple acceptable normalized forms must be permitted where linguistic variation makes a single canonical target scientifically unjustified.

Native-speaker/linguistic review is required for transformations involving lexical substitution, grammatical reinterpretation, code-switch boundaries, ambiguous segmentation, or competing accepted forms.

## KB-DATA-003: Open-World Source Discovery and Corpus Expansion Policy

### Proposed Decision

KreyolBench shall maintain an open-world source discovery process. The source
registry is not a fixed whitelist. New source families, collections, and subsets
may be discovered and registered continuously, provided their provenance and
uncertainties are documented.

Registration authorizes metadata discovery only. It does not authorize
collection, annotation, transformation, derived use, redistribution, commercial
use, scientific inclusion, or publication claims.

### Expert Decision

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-09

Rationale or required revision:

An extensible discovery process is required because Haitian Creole resources
are distributed across institutions, archives, public agencies, publishers,
research releases, and communities, and new resources will continue to emerge.

Conditions:

1. Every discovered source must receive a stable identifier and provenance.
2. Broad source families must not be used as dataset-row provenance.
3. Each downstream action must pass its own legal, ethical, quality, and
   scientific gate.
4. Discovery must not be presented publicly as endorsement, partnership, or
   permission.
5. Duplicate, superseded, inaccessible, and excluded records remain traceable
   rather than being silently deleted.


## KB-ANN-001: Annotation Quality-Control Policy

### Proposed Decision

Require a pilot, written guidelines, gold examples, double annotation of a defined subset, adjudication, agreement reporting, and explicit uncertainty handling before a task is frozen.

### Candidate v0.1 Tasks Requiring Annotation Review

| Task instance | Candidate label/output structure | Scope status | Scientific status |
| --- | --- | --- | --- |
| Multi-label topic classification | multi-label topics | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| Named entity recognition | typed character spans; optional nesting support | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| Question answering | extractive answers and unanswerable cases | FEASIBILITY_ONLY | SUBMITTED_TO_REVIEW |
| Retrieval | separate corpus, query, and graded qrel artifacts | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| Orthographic normalization | orthography-only references and edit records | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| Token language identification | direct token language IDs with derived sentence composition | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| Translation | one or more references | DEFERRED | BLOCKED |

Sentiment and summarization have configuration/sample scaffolds but are not in the current v0.1 task list.

### Review Questions

- What minimum double-annotation proportion is feasible?
- Which agreement statistic is appropriate for each task?
- Who may adjudicate linguistic disagreements?
- How should annotator uncertainty and alternate valid answers be represented?

### Expert Decision

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-08

Rationale or required revision:

The annotation quality-control architecture is scientifically appropriate and
is approved as a project-wide requirement.

Conditions:

No universal double-annotation percentage or agreement threshold is frozen at
this stage.

Each task must undergo a pilot from which task-specific decisions will be made
regarding:
- double-annotation proportion;
- agreement metric;
- minimum acceptable agreement;
- adjudication procedure;
- uncertainty representation;
- label-guideline revision.

Native Haitian Creole expertise must participate in adjudication of linguistic
ambiguity.

Statistical agreement metrics must be selected according to the structure of each task rather than applying Cohen's kappa mechanically across all tasks.

## KB-EVAL-001: Metrics and Statistical Testing

### Proposed Decision

Every metric must document definition, averaging, limitations, uncertainty, and appropriateness. Model comparisons must report effect size or uncertainty and must not treat small point-estimate differences as scientifically meaningful by default.

### Candidate Metric Matrix

| Task | Candidate primary metric | Secondary evidence | Current status |
| --- | --- | --- | --- |
| Classification | multi-label macro F1 | micro/sample F1, subset accuracy, per-label F1 | SUBMITTED_TO_REVIEW |
| Sentiment | macro F1 | accuracy, per-label F1 | SUBMITTED_TO_REVIEW; not v0.1 |
| NER | exact character-span micro F1 | per-type, boundary, and nested-span analysis | SUBMITTED_TO_REVIEW |
| QA | token F1 | exact match, unanswerable accuracy | SUBMITTED_TO_REVIEW |
| Retrieval | nDCG@10 | MRR@k, recall@k | SUBMITTED_TO_REVIEW |
| Normalization | exact match to any reference | character/word, edit-type, and over-normalization analysis | SUBMITTED_TO_REVIEW |
| Code-switching | token-language macro F1 | per-language, boundary, and derived sentence metrics | SUBMITTED_TO_REVIEW |
| Translation | chrF candidate | BLEU, COMET, human evaluation | BLOCKED |
| Summarization | ROUGE-L candidate | ROUGE-1/2, chrF, human evaluation | BLOCKED; not v0.1 |

### Review Questions

- Which metric is primary for each retained v0.1 task?
- Which confidence-interval or paired-test procedure is required?
- How should multiple comparisons across models and tasks be handled?
- Which tasks require human evaluation before publication claims?

### Expert Decision

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-08

Rationale or required revision:

The evaluation principle is approved: metric selection must be justified, uncertainty must be reported, and small point-estimate differences must not automatically be interpreted as scientifically meaningful.

Conditions:

The current metric matrix remains CANDIDATE rather than EXPERT_VALIDATED at task level.

Each task specification must subsequently validate:
- primary metric;
- secondary metrics;
- confidence-interval procedure;
- paired comparison method where appropriate;
- effect-size reporting;
- multiple-comparison strategy where applicable;
- human evaluation requirements.

Normalization evaluation must explicitly account for multiple linguistically acceptable outputs rather than relying on exact match alone.

## KB-SPLIT-001: Split, Leakage, and Contamination Policy

### Proposed Decision

Use stable example identifiers, deterministic split generation, source/document-aware grouping, exact and near-duplicate checks, frozen hashes, and hidden-test protection.

### Unresolved Split Questions

- Should split proportions vary by task and source size?
- Which tasks need source-held-out or domain-held-out robustness sets?
- What near-duplicate representation and threshold should be used per task?
- How should parallel translations and document-derived examples be grouped?
- What minimum hidden-test size is defensible?
- When should a time-based split replace or supplement a random/grouped split?

### Expert Decision

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-09

Rationale or required revision:

The split, leakage, and contamination policy is approved at project-policy
level. Task-specific split proportions, grouping keys, held-out designs, and
near-duplicate thresholds remain provisional and require task-level evidence.

Conditions:

No universal split ratio or universal near-duplicate threshold is approved.

Every task must define its split policy from:
- corpus structure;
- source structure;
- document provenance;
- temporal structure;
- entity overlap;
- translation relationships;
- sample size;
- domain structure.

Whenever feasible, KreyolBench should include robustness evaluation beyond the standard IID test set, including source-held-out, domain-held-out, temporal, or other scientifically justified challenge sets.

Parallel or derived examples from the same underlying content must never cross train/test boundaries in ways that create leakage.

## KB-PUB-001: Publication Artifact Traceability

### Proposed Decision

Associate planned tables, figures, datasets, experiments, and claims with stable artifact identifiers, evidence requirements, implementation dependencies, and review status.

### Review Questions

- Is the burden proportionate for a small research team?
- Which artifacts require independent reproduction before submission?
- Who may approve a result or claim for manuscript inclusion?
- Should preprint, workshop, and archival submissions use different evidence gates?

### Expert Decision

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Date: 2026-09-08

Rationale or required revision:

Artifact-to-paper and claim-to-evidence traceability are mandatory for
KreyolBench's publication workflow.

Every material empirical manuscript claim must be traceable to a versioned artifact or externally verifiable source.

Conditions:

Headline findings, benchmark rankings, annotation-quality claims,
state-of-the-art claims, dataset statistics, and robustness conclusions require independent rerun or reproduction before archival submission whenever practicable.

## KB-SCOPE-001: KreyolBench v0.1 Scientific Pilot Task Scope

### Pre-Review Candidate Task List (Historical)

1. Classification
2. Named entity recognition
3. Question answering
4. Retrieval
5. Normalization
6. Code-switching
7. Translation

This was the candidate list presented before the scope decision below. It is
retained for traceability and is not the current v0.1 task commitment.

### Candidate Corpus Domains (Not Classification Labels)

- health
- education
- civic administration
- disaster response
- religion
- news
- culture
- other

### Scope Recommendation for Expert Consideration

Do not validate the entire seven-task list as one indivisible package. Review task readiness individually using scientific value, source feasibility, annotation cost, evaluation validity, collaborator capacity, and 12-month publication feasibility.

### Scope Decision

- [ ] APPROVE CURRENT CANDIDATE LIST FOR PILOT FEASIBILITY ONLY
- [x] REVISE TASK LIST
- [ ] DEFER SCOPE FREEZE

Reviewer: Jeff Pierre
Date: 2026-09-08

Tasks retained for v0.1 scientific pilot:

1. Text classification
2. Named entity recognition
3. Information retrieval
4. Text normalization
5. Code-switching

Tasks retained for feasibility investigation but not yet committed to v0.1:

6. Question answering

Tasks deferred from the core v0.1 release:

7. Translation

Sentiment analysis and summarization remain roadmap tasks rather than v0.1 commitments.

Rationale:

The long-term KreyolBench scope should remain broad. However, the first publication-quality release should prioritize tasks that jointly offer scientific novelty, Haitian-specific linguistic relevance, feasible annotation, strong real-world applicability, and defensible evaluation.

Normalization and code-switching should receive particular attention as potential KreyolBench signature contributions rather than treating v0.1 as only another collection of conventional multilingual NLP tasks.

Translation should remain supported by the architecture and investigated for
future integration. Prior Haitian Creole MT resources exist, but their domain
coverage, quality, licenses, overlap, and suitability for KreyolBench evaluation
still require audit. Translation is deferred primarily to keep the v0.1 pilot
feasible and because its publication-grade evaluation protocol remains
unresolved; the deferral is not a claim that existing resources provide
sufficient coverage.

## Final Review Record

Review completed by: Jeff Pierre

Affiliation/role: Project Lead and Scientific Reviewer

Review independence: Internal project-lead review. Independent external review
is required before any v0.1 task specification is frozen.

Review date: 2026-09-09

Decision IDs approved:

- KB-DEC-001
- KB-DATA-001
- KB-DATA-002
- KB-ANN-001
- KB-EVAL-001
- KB-SPLIT-001
- KB-PUB-001
- KB-DATA-003
- KB-SCOPE-001

Decision IDs requiring revision:

- None at project-policy level

Decision IDs deferred:

- None at project-policy level

Authorized next scientific step:

1. Maintain open-world source discovery under validated `KB-DATA-003`.
2. Expand the source registry in discovery/pending-review states only.
3. Maintain the completed provisional task specifications and feasibility
   analysis without treating them as frozen.
4. Obtain independent external review before freezing any task specification.
5. Do not launch large-scale collection or annotation until source-level and
   task-level approvals are complete.

Limitations or conditions:

Approval of the governance framework does not constitute approval of any specific source for acquisition, redistribution, annotation, or release.

The KreyolBench long-term benchmark scope remains broader than the v0.1 pilot.
Task deferral from v0.1 must not be interpreted as removal from the overall research roadmap.

## Current Status and Next Action

Current status: EXPERT_VALIDATED

All project-level scientific governance decisions in this review packet have
completed expert review.

Next action:

Proceed to independent task-specification review and metadata-only source
feasibility review for the five provisional task instances selected by the
validated v0.1 pilot-scope decision:

1. Text classification
2. Named entity recognition
3. Information retrieval
4. Text normalization
5. Code-switching

In parallel, conduct source-specific legal, ethical, provenance, quality, and
scientific assessments for candidate collections and subsets.

Project-level approval does not authorize dataset acquisition, large-scale
annotation, source redistribution, task-level metric or split freezing, or
release claims. Those actions remain subject to their applicable downstream
review gates.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-08 | Initial v0.1 expert-review packet. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Reconciled expert decisions, expanded source candidates, added open-world discovery and v0.1 scope records, and resubmitted revised KB-DATA-001. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Recorded the second KB-DATA-001 approval and closed project-policy review; downstream task and source gates remain open. | EXPERT_VALIDATED |
| 2026-09-09 | Clarified stable task-instance and bounded-release language without changing the approved v0.1 selection. | EXPERT_VALIDATED |
