# Source Discovery Expansion Review Packet

## Status and Decision Boundary

Current status: SUBMITTED_TO_REVIEW

Prepared by: Codex. AI assistance disclosed: true. Review date: 2026-09-10.

This packet expands the source inventory, not the v0.1 benchmark release. No source is approved for acquisition, annotation, transformation, training, redistribution or scientific inclusion. The five task decisions still require independent human review.

## Inventory Reconciliation

The intake contains 22 deduplicated leads: 15 registered-source references (12 new and 3 existing), four unresolved leads, and three references. The source registry now has 33 non-synthetic candidates plus one test-only synthetic control. These counts describe metadata records, not disjoint corpora or unique examples.

The [initial packet](SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md) and [archived schema-v1 ledger](source_reviews/history/source_feasibility_initial_20260910.yaml) preserve the original 21-candidate assessment. Current evidence is in the schema-v2 feasibility ledger and discovery ledger. Inferred task fit, privacy adequacy and contamination assessability formerly marked EVIDENCE_AVAILABLE are downgraded to PARTIAL unless a direct metadata claim supports them. This is evidence correction, not source authorization.

## Supplied Leads

| Lead | Disposition | Source record or reference | Evidence review |
| --- | --- | --- | --- |
| jsbeaudry continued-pretraining lead | UNVERIFIED_LEAD | No corpus registration | [Review](source_reviews/discovery/jsbeaudry_stem.md) |
| Haitian Wikipedia 20231101 snapshot | REGISTERED_SOURCE | wikimedia_htwiki_20231101 | [Review](source_reviews/wikimedia_htwiki_20231101.md) |
| FLORES+ Haitian Creole | REGISTERED_SOURCE | flores_plus_hat | [Review](source_reviews/flores_plus_hat.md) |
| xP3x Haitian Creole | REGISTERED_SOURCE | xp3x_hat | [Review](source_reviews/xp3x_hat.md) |
| Aya Collection Haitian language split | REGISTERED_SOURCE | aya_collection_haitian | [Review](source_reviews/aya_collection_haitian.md) |
| FinePDFs Haitian configuration | REGISTERED_SOURCE | finepdfs_hat | [Review](source_reviews/finepdfs_hat.md) |
| mC4 Haitian configuration | REGISTERED_SOURCE | mc4_ht | [Review](source_reviews/mc4_ht.md) |
| Kreyol-MT existing collection | REGISTERED_SOURCE | jhu_kreyol_mt | [Review](source_reviews/discovery/kreyol_mt.md) |
| CreoleVal existing family | REGISTERED_SOURCE | creoleval | [Review](source_reviews/discovery/creoleval.md) |
| MIT-Haiti corpus via CreoleVal | REGISTERED_SOURCE | creoleval_mit_haiti | [Review](source_reviews/creoleval_mit_haiti.md) |
| CMU Haitian resource family | REGISTERED_SOURCE | cmu_haitian | [Review](source_reviews/discovery/cmu_original.md) |
| phatjmo CMU Haitian mirror candidate | REGISTERED_SOURCE | cmu_haitian_phatjmo | [Review](source_reviews/cmu_haitian_phatjmo.md) |
| IARPA Babel Haitian LDC2017S03 | REGISTERED_SOURCE | babel_haitian_ldc2017s03 | [Review](source_reviews/babel_haitian_ldc2017s03.md) |
| VoxLingua107 Haitian lead | UNVERIFIED_LEAD | No corpus registration | [Review](source_reviews/discovery/voxlingua107_hat.md) |
| Corpus of Northern Haitian Creole lead | UNVERIFIED_LEAD | No corpus registration | [Review](source_reviews/discovery/northern_haitian.md) |
| UD Haitian Creole Autogramm | REGISTERED_SOURCE | ud_haitian_autogramm | [Review](source_reviews/ud_haitian_autogramm.md) |
| UD Haitian Creole Adolphe | REGISTERED_SOURCE | ud_haitian_adolphe | [Review](source_reviews/ud_haitian_adolphe.md) |
| Haitian Disaster Response SMS research collection | REGISTERED_SOURCE | haitian_disaster_sms_munro | [Review](source_reviews/haitian_disaster_sms_munro.md) |
| APiCS Haitian Creole survey chapter 49 | REFERENCE_ONLY | No corpus registration | [Review](source_reviews/discovery/apics_survey49.md) |
| APiCS Haitian Creole structure contribution 49 | REFERENCE_ONLY | No corpus registration | [Review](source_reviews/discovery/apics_structure49.md) |
| XM3600 multimodal methodology reference | REFERENCE_ONLY | No corpus registration | [Review](source_reviews/discovery/xm3600.md) |
| Translated VICR release lead | UNVERIFIED_LEAD | No corpus registration | [Review](source_reviews/discovery/vicr_translated.md) |

## Scientific Corrections

- Aya Collection is not equivalent to the entirely human-annotated Aya Dataset. Its parent metadata reports 4,120,342 Haitian translated entries, not millions of native multi-turn conversations. [Official card](https://huggingface.co/datasets/CohereLabs/aya_collection)
- xP3x is an instruction-training mixture. Prompt variants and inherited tasks are not independent evaluation examples; audit original FLORES lineage before using overlapping resources as test evidence. No Haitian overlap rate is claimed. [Card](https://huggingface.co/datasets/CohereLabs/xP3x)
- Wikipedia's 70,159 rows are reported for the 20231101.ht train snapshot. Size and structure do not establish factual accuracy or native authorship. [Snapshot metadata](https://huggingface.co/datasets/wikimedia/wikipedia/blob/main/README.md)
- MIT-Haiti's README identifies ht-en, ht-fr and ht-es parallel children's stories, distinct from monolingual lesson plans and blog posts. Educational parallel data must not all be relabeled STEM text. [Subset documentation](https://github.com/hclent/CreoleVal/tree/main/nlg/mit_haiti)
- Adolphe and Autogramm are distinct treebanks; the old family report describes Adolphe only. Versioned counts and conversion quality need review. [Adolphe](https://universaldependencies.org/treebanks/ht_adolphe/index.html), [Autogramm](https://universaldependencies.org/treebanks/ht_autogramm/index.html)
- The CMU mirror's MIT badge does not settle the reproduced CMU notice conditions or uploader authority. Babel is a cataloged access-controlled resource, not an openly authorized corpus. [CMU mirror](https://huggingface.co/datasets/phatjmo/cmu_haitian), [Babel catalog](https://catalog.ldc.upenn.edu/LDC2017S03)
- The Northern Haitian link redirects to a general university page; VoxLingua Haitian duration and translated VICR Haitian coverage remain unverified. APiCS is linguistic reference material, not a substitute for natural corpus sampling.
- XM3600 is retained for methodology, not represented as a confirmed Haitian dataset. No claim that native Haitian vision-language resources do not exist is supported here.

## Human Review Queue

1. Confirm identity, granularity and evidence corrections; select bounded subsets by scientific need rather than size.
2. Review rights and upstream provenance for Wikipedia, MIT-Haiti, UD and instruction mixtures; keep evaluation partitions separate from training proposals.
3. Request specialist ethics scoping before any speech or emergency-SMS access. Public interest does not replace consent or justify disclosure.
4. Resolve inaccessible or underspecified leads through metadata or custodian clarification. Do not fetch data to establish feasibility.
5. Record each outcome with reviewer, date, evidence and limitations. Permission and task validation remain separate gates.

## Open Questions

No language-quality sampling, corpus deduplication, content-origin audit, regional balance measurement or license opinion has been completed. Domain mappings in the [coverage matrix](SOURCE_DOMAIN_MODALITY_MATRIX_V0_1.md) are hypotheses. Broad collections cannot fill every domain gap merely by being large.

## Acceptance and Next Action

Structural validation must pass with no source gate elevated and release eligibility false. Human review of this packet is next; acquisition and pilots remain blocked until every applicable source and task gate passes.

## Revision History

- 2026-09-10: Added expanded intake and corrected metadata evidence without rewriting the initial review history.
