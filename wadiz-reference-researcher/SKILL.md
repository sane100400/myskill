---
name: wadiz-reference-researcher
description: "Researches current high-quality Wadiz story pages and extracts dated reference patterns for story flow, proof density, visual rhythm, reward clarity, mobile readability, and funding-story persuasion. Use after slop taxonomy and before section contracts."
---

# Wadiz Reference Researcher

## Purpose

Build a current Wadiz reference pack so production is based on platform-specific story evidence, not generic landing-page assumptions.

## Required Inputs

- Current date.
- Product category and reward type.
- Comparable Wadiz links or search access.
- Current slop taxonomy and deprecated rule file.
- Product brief when available.

## Allowed Outputs

- `reference-pack/current-good-wadiz-pages.md`
- `reference-pack/current-visual-vocabulary.md`
- Wadiz story pattern notes.
- PASS/FAIL JSON report.

Every output must include:
- `taxonomy_date`
- `evidence_sources`
- `current_slop_signatures`
- `deprecated_rules`
- `section_proof_asset_ids` when known
- `pass_fail_result`
- `required_fixes`

## Forbidden Behavior

- Do not use generic SaaS landing references as Wadiz references.
- Do not copy proprietary page content.
- Do not infer reward policy from memory when it is current and checkable.
- Do not create a page or section plan yet.

## Workflow

1. Collect current Wadiz references for similar digital rewards.
2. Extract:
   - Story flow.
   - Proof density.
   - Reward clarity.
   - Mobile layout rhythm.
   - Maker credibility treatment.
   - FAQ/caution placement.
3. Compare references against current slop taxonomy.
4. Identify patterns that are acceptable modern Wadiz patterns, not generic AI defaults.
5. Mark missing or unverifiable policy details as `[TODO: verify current Wadiz guidance]`.
6. Hand off to `$product-proof-mapper`.

## Failure Conditions

- References are undated.
- References are not Wadiz or not comparable.
- Notes are generic design preferences.
- The output lacks proof-density observations.
- The output ignores current slop taxonomy.

## Validation Checklist

- Evidence sources are listed with dates.
- Wadiz story flow is separated from SaaS landing flow.
- Proof and reward clarity patterns are explicit.
- Mobile readability notes are actionable.
- Outdated anti-slop rules are not reintroduced.

## PASS/FAIL Format

```json
{
  "status": "PASS",
  "checked_artifact": "reference-pack/current-good-wadiz-pages.md",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": [],
  "section_proof_asset_ids": [],
  "required_fix": [],
  "allowed_next_skill": "product-proof-mapper"
}
```

## Example Prompt

"Use `$wadiz-reference-researcher` to study current high-quality Wadiz digital reward pages and extract story flow, proof density, visual rhythm, reward clarity, and mobile readability patterns."
