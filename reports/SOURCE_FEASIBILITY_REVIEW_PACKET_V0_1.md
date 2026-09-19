# KreyolBench Source Feasibility Review Packet v0.1

## Review Record

Current status: EXPERT_VALIDATED

Project-Lead review date: 2026-09-18

Reviewer: Jeff Pierre

Role: Project Lead and Scientific Reviewer

Review independence: INTERNAL_PROJECT_LEAD

Outcome: ACCEPT WITH REQUIRED CORRECTIONS

Implementation: Codex, with AI assistance disclosed

Authorization effect: NONE

Governing decision: `KB-SRCREV-001`

## Scope of Validation

The Project Lead accepted the metadata-review methodology, strict no-authorization boundary, corrected scientific-feasibility dispositions, and planning priorities. This validates the review artifact at project-policy and prioritization level only. It does not validate source rights, ethics, representativeness, corpus composition, task suitability, or release eligibility.

This review authorizes no download, scraping, API or bulk collection, annotation, transformation, training, benchmark inclusion, redistribution, metric or split freeze, leaderboard use, release, or publication claim about dataset composition.

## Append-Only Review History

### 1. Original Codex Metadata Assessment

- Date: 2026-09-10
- Actor: Codex
- Category: `ORIGINAL_CODEX_METADATA_ASSESSMENT`
- Scope: public metadata triage for 21 non-synthetic candidates and one synthetic control
- Result under the earlier single-summary model: 12 `CONDITIONAL`, 9 `BLOCKED`
- Human scientific decision: none

### 2. Project-Lead Review Decision

- Date: 2026-09-18
- Reviewer: Jeff Pierre
- Category: `PROJECT_LEAD_REVIEW_DECISION`
- Outcome: `ACCEPT_WITH_REQUIRED_CORRECTIONS`
- Sources reviewed: 19
- Sources not reviewed in this event: `mit_ayiti_resources`, `mspp_publications`

### 3. Post-Review Implementation Evidence Checks

Codex checked authoritative public metadata needed to implement the human decisions. These checks are recorded as `IMPLEMENTATION_EVIDENCE_CHECK` events and are not attributed to Jeff Pierre. They do not constitute legal advice, independent expert review, or source approval.

## Corrected Multi-Axis Interpretation

The earlier 12/9 total used one summary label. The current model separates identity, language evidence, scientific feasibility, task fit, provenance readiness, privacy, contamination, legal review, collection, derived use, redistribution, commercial use, ethics, scientific inclusion, and release eligibility.

Among the 19 Project-Lead-reviewed sources:

| Scientific-feasibility disposition | Count | Meaning |
| --- | ---: | --- |
| `CONDITIONAL` | 14 | Scientifically worth source-specific next-stage review; not authorized. |
| `BLOCKED` | 5 | Actionable use cannot responsibly proceed; discovery value may remain. |

The 14/5 result is not directly comparable to the original 12/9 inventory total: two original sources remain pending human review, four blocked summaries were revised to conditional scientific feasibility, and authorization is now represented on independent axes.

The active registry also contains 12 later candidates outside this Project-Lead review. Their Codex metadata assessments remain provisional.

## Project-Lead Source Decisions

| Source ID | Decision | Scientific role or restriction | Exact next action |
| --- | --- | --- | --- |
| `aka_official` | RETAIN CONDITIONAL | Institutional and normative discovery family; never final example provenance. | Select exact normative documents and obtain document-specific rights and Haitian Creole orthographic review. |
| `aka_publications` | RETAIN CONDITIONAL | High-priority orthographic/normative collection; variation must not be erased. | Register only selected title/version children with supersession, rights, provenance, and linguistic review. |
| `haiti_civil_protection_resources` | RETAIN BLOCKED | High future disaster-retrieval value; current actionable source unresolved. | Resolve authoritative endpoint, publisher, Haitian content, temporal validity, and public-alert boundary. |
| `cmu_haitian` | REVISE TO CONDITIONAL | Family identity and release history verified; artifact and rights unresolved. | Locate authoritative surviving artifacts and register exact children only. |
| `creoleval` | RETAIN CONDITIONAL | Prior art, comparison, source discovery, and contamination reference. | Audit every Haitian component, upstream origin, license, split, hash, and overlap separately. |
| `ebible_hat_1985` | RETAIN CONDITIONAL | Provider-stated public-domain 1985 edition; narrow religious register and high contamination risk. | Verify edition-specific rights and provenance; prioritize controlled linguistic or contamination analysis. |
| `diaspora_publications` | RETAIN BLOCKED | Important open-world research family, not an actionable corpus. | Register bounded publisher/country/community/medium/date children with community and privacy review. |
| `haiti_government_communication_portal` | REVISE TO CONDITIONAL | Accessible civic portal with portal-level CC0 notice; asset inheritance unresolved. | Register bounded publisher/content-type assets and verify language, revision, third-party status, and license applicability. |
| `haiti_government_publications` | RETAIN BLOCKED | Heterogeneous discovery family without a uniform rights or language regime. | Register ministry- or institution-specific children; never use the family as example provenance. |
| `jhu_kreyol_mt` | RETAIN CONDITIONAL | Confirmed Haitian language-pair directories; aggregate license and upstream rights vary. | Register each selected language pair/upstream component and audit origin, duplicates, license, split, and contamination. |
| `menfp_educational_resources` | REVISE TO CONDITIONAL | Scientifically relevant education resource family; authorization unresolved. | Resolve authoritative copies and register curriculum, syllabus, guide, exam, information, and third-party textbook assets separately. |
| `haitian_news_candidates` | RETAIN BLOCKED | Important contemporary-language family without publisher-level authorization. | Register publisher-specific children and document editorial, copyright, syndication, corrections, sampling, and sensitive-person risks. |
| `opus` | RETAIN CONDITIONAL | Aggregation/discovery family, never final example provenance. | Register corpus/version/language-pair/upstream children; resolve license, origin, alignment, duplication, and contamination. |
| `radio_haiti_duke_archive` | RETAIN CONDITIONAL | Very-high-value spoken, historical, sociolinguistic, and code-switching archive. | Resolve item-level audio, transcript, metadata, participant, sensitivity, and derived-corpus rights while preserving Duke identifiers. |
| `radio_haiti_inter_lrec2026` | REVISE TO CONDITIONAL | Scientific identity and claimed 50-hour release verified in the primary paper. | Locate the exact artifact and resolve version, license, archive rights chain, annotation rights, ethics, and contamination. |
| `social_media_candidates` | RETAIN BLOCKED | Informal-language relevance cannot override platform and research ethics. | Approve a platform-specific terms, access, consent/waiver, deletion, PII, minors, quote, retention, and redistribution protocol first. |
| `un_haiti_ht` | RETAIN CONDITIONAL | High civic/development/retrieval relevance; route membership does not prove document language. | Select dated assets and verify entity, language, origin, authority, temporal validity, duplication, and exact terms. |
| `universal_dependencies_haitian` | RETAIN CONDITIONAL | Linguistic infrastructure family containing distinct Autogramm and Adolphe children. | Pin exact UD release and commit/hash and review each treebank's upstream-text rights and conversion history. |
| `wikimedia_htwiki` | RETAIN CONDITIONAL | High scalable-text value and high contamination risk. | Use only an immutable snapshot child with page/revision provenance, attribution, imported-content exceptions, and contamination analysis. |

## Pending Project-Lead Review

- `mit_ayiti_resources`
- `mspp_publications`

These sources preserve their prior state. This review supplies no Jeff Pierre decision for them.

## Implementation Evidence Checks

Codex implementation evidence checks identified:

- a CMU institutional page documenting the Haitian Creole spoken/text resource history and 2010 public release;
- an official Haitian government portal-level CC0 1.0 notice, without asset-level inheritance;
- eBible's HAT/HATPDS identity and provider-stated public-domain rationale for the 1985 edition only;
- Kreyol-MT repository directories for several `hat-*` language pairs under an aggregate `other` license;
- item-level Radio Haiti rights notices and third-party-content caveats in the Duke archive;
- the LREC 2026 paper's explicit claimed release of 50 hours with ASR-derived transcription, POS, alignment, confidence, and manual evaluation;
- general UN web terms that can restrict redistribution and derivative works unless specific terms apply;
- distinct UD Autogramm and Adolphe pages, versions, genres, conversion histories, and CC BY-SA 4.0 treebank-level notices.

## Planning Priorities

Planning tiers are recorded in `configs/governance/source_prioritization.yaml`. They are not authorization states.

- High-priority next-stage review: AKA selected publications, Wikimedia immutable snapshot, Radio Haiti archive/corpus, bounded government communications, selected UN Haiti assets, and selected MENFP assets.
- Comparison, contamination, and future infrastructure: CreoleVal, Kreyol-MT, OPUS, UD Haitian treebanks, CMU resources, and eBible HAT 1985.
- Discovery/future governance: Haitian news, diaspora publications, social media, broad government publications, and Civil Protection.

## Completion Gate

Every selected asset must independently satisfy legal, ethical, linguistic, provenance, contamination, scientific-inclusion, and release gates. `release_eligible` remains false. The next permitted work is human review of the two pending sources and source-specific rights, ethics, linguistic, and provenance clarification for bounded high-priority candidates.

## Revision History

| Date | Change | Attribution | Status |
| --- | --- | --- | --- |
| 2026-09-10 | Original 21-candidate metadata-only packet. | Codex, AI-assisted | SUBMITTED_TO_REVIEW |
| 2026-09-18 | Accepted methodology with required corrections and adopted 19 source-specific dispositions. | Jeff Pierre, Project Lead and Scientific Reviewer | EXPERT_VALIDATED |
| 2026-09-18 | Implemented evidence checks and multi-axis synchronization. | Codex, AI-assisted | IMPLEMENTATION_EVIDENCE_CHECK |
