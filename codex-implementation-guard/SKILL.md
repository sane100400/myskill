---
name: codex-implementation-guard
description: "Prevents HTML/CSS generation until Wadiz long-scroll story, rhythm variation, proof integration, dated slop taxonomy, cardnews-slop detection, proof assets, section contracts, design intent, and current validation have passed. Use before implementation to avoid Codex default-component and stacked cardnews output."
---

# Codex Implementation Guard

## Purpose

Block implementation until the proof-led, long-scroll, date-aware contract is complete. If gates fail, output PASS/FAIL only; do not code.

## Required Inputs

- `reference-pack/current-codex-slop-taxonomy.md`
- `reference-pack/deprecated-slop-rules.md`
- `reference-pack/current-slop-signatures.md`
- `reference-pack/product-specific-design-language.md`
- `source/product-brief.md`
- `source/proof-assets.md`
- `artifacts/03-long-scroll-story.md` or equivalent.
- `artifacts/04-rhythm-variation-plan.json` or equivalent.
- Proof integration plan.
- `artifacts/02-section-plan.json`
- Current validator report.
- Cardnews slop detector report.

## Allowed Outputs

- Implementation permission PASS/FAIL JSON.
- Required implementation metadata contract.

Every output must include:
- `taxonomy_date`
- `evidence_sources`
- `deprecated_rules`
- `current_slop_signatures`
- `section_proof_asset_ids`
- `pass_fail_result`
- `required_fixes`

## Forbidden Behavior

- Do not write HTML/CSS when any required artifact is missing or failed.
- Do not implement sections outside the section contracts.
- Do not introduce default-component layouts absent from the design intent.
- Do not implement stacked card-news sections or repeated number/kicker/headline/panel skeletons.
- Do not use section numbers, rails, boxed panels, or ledgers as the main page rhythm unless the long-scroll story explicitly justifies them.
- Do not enforce deprecated rules.
- Do not omit section metadata.

## Workflow

1. Check all required reference, source, and artifact files exist.
2. Check long-scroll story, rhythm variation, and proof integration plans exist and passed review.
3. Check taxonomy is dated and validator has passed.
4. Check `$cardnews-slop-detector` has passed for section plan, layout spec, and any existing HTML.
5. Check every section has proof asset IDs and public proof labels.
6. If implementation is allowed, require:
   - `data-section-id`
   - `data-proof-assets`
   - `data-taxonomy-date`
   - `data-current-slop-status="pending"`
7. If implementation exists, run `$current-slop-validator` and `$cardnews-slop-detector`.

## Failure Conditions

- Current taxonomy missing or undated.
- Deprecated rules are still enforced.
- Section contracts or proof IDs are missing.
- Long-scroll story or rhythm variation plan is missing.
- Cardnews slop detector fails.
- Implementation would require invented evidence.
- HTML metadata contract is missing.
- The page can be described as stacked Instagram carousel cards.

## Validation Checklist

- Taxonomy-first workflow is complete.
- Long-scroll workflow is complete.
- Rhythm variation and proof integration gates are complete.
- Proof mapping is complete or blocked.
- Current slop validation passed.
- Cardnews slop detection passed.
- HTML/CSS is allowed only after gates pass.
- Section metadata can be machine-checked.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "implementation-permission",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": ["proof absence"],
  "section_proof_asset_ids": {},
  "required_fix": ["Create long-scroll story, rhythm variation plan, dated taxonomy, and section proof map before coding"],
  "allowed_next_skill": null
}
```

## Example Prompt

"Use `$codex-implementation-guard` to decide whether HTML/CSS is allowed. Block coding unless the long-scroll story, rhythm variation plan, proof integration plan, dated taxonomy, section contracts, proof IDs, current slop validator, and cardnews slop detector have passed."
