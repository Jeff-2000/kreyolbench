# External Review Evidence

## Purpose

Store dated, task-specific evidence from identifiable external human reviewers. These records support governance decisions; they do not replace the machine-readable decision registry.

## Required Record

Create one Markdown file per reviewer and decision from `REVIEW_TEMPLATE.md`. Use a stable name such as:

```text
KB-TASK-NORM-001_family-name_given-name_YYYY-MM-DD.md
```

Every review must include the reviewer's name, affiliation, relevant expertise, independence, conflict disclosure, decision, rationale, conditions, and date. The corresponding event must then be appended to `configs/governance/decisions.yaml` and summarized in `DECISIONS.md`.

## Qualification Rules

- The reviewer must be an identifiable human expert.
- External means outside the core KreyolBench drafting and implementation team at review time.
- Automated output alone cannot satisfy the external gate. The identifiable human reviewer must independently assess the specification, own the judgment, attest to it, and disclose material AI assistance.
- One reviewer may satisfy multiple expertise tags when qualifications are documented.
- Several reviewers may collectively cover required expertise.
- A disqualifying conflict cannot support approval.
- Prospective authorship, dataset ownership, institutional interests, funding relationships, and close supervisory relationships must be disclosed.

## Privacy and Publication

These evidence files are intended to be public governance records only with reviewer consent. If a reviewer requires confidential handling, store the signed record outside Git and place a redacted evidence statement here. Do not publish private contact details, signatures, or unnecessary personal data.

## Current Status

Current status: DRAFT

No external approval is currently recorded for the five v0.1 task decisions.

## Acceptance Criteria

- Evidence path exists.
- Identity and affiliation are complete.
- Expertise tags match the decision requirement.
- Conflict status and details are complete where applicable.
- The outcome and latest machine-readable decision status agree.
