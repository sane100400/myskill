---
name: section-contract-planner
description: "Creates Wadiz section or story-beat contracts with proof asset IDs, supporter question, continuity, scroll momentum, rhythm role, public copy role, visual role, CTA, and failure conditions. Use after long-scroll story composition, rhythm variation planning, and proof mapping so every beat is proof-led without becoming cardnews."
---

# Section Contract Planner

## Purpose

Define evidence-based story-beat contracts before copy, visuals, layout, or HTML/CSS. The contract prevents Codex from filling unknowns with generic UI components or isolated cardnews sections.

## Required Inputs

- `source/product-brief.md`
- `source/proof-assets.md`
- `artifacts/03-long-scroll-story.md` or equivalent.
- `artifacts/04-rhythm-variation-plan.json` or equivalent.
- `reference-pack/current-slop-signatures.md`
- `reference-pack/deprecated-slop-rules.md`
- Wadiz reference notes.

## Allowed Outputs

- `artifacts/02-section-plan.json`
- PASS/FAIL JSON report.

Every section contract must include:
- `section_id`
- `section_role`
- `section_goal`
- `supporter_question`
- `supporter_state_before`
- `carry_over_from_previous`
- `curiosity_gap_to_next`
- `mobile_scroll_job`
- `rhythm_role`
- `core_message`
- `required_proof_asset_ids`
- `public_proof_labels`
- `copy_role`
- `visual_role`
- `layout_role`
- `cta_role`
- `failure_conditions`

Every output must include:
- `taxonomy_date`
- `evidence_sources`
- `deprecated_rules`
- `current_slop_signatures`
- `section_proof_asset_ids`
- `pass_fail_result`
- `required_fixes`

## Forbidden Behavior

- Do not create a full page.
- Do not design each section as a standalone card or social slide.
- Do not repeat number -> kicker -> headline -> paragraph -> proof panel as the default skeleton.
- Do not use proof-free sections.
- Do not invent missing evidence.
- Do not use current or deprecated anti-slop rules without the reference pack.
- Do not write HTML/CSS.

## Workflow

1. Start from the long-scroll story arc, not from a section list.
2. Create story-beat contracts with carry-over and curiosity gaps.
3. Attach proof IDs and public proof labels to each beat.
4. Assign rhythm roles from the rhythm variation plan.
5. Translate current slop and cardnews slop signatures into failure conditions.
6. Mark blocked beats when proof is missing.
7. Keep output strict JSON.
8. Run `$current-slop-validator` and `$cardnews-slop-detector`.

## Failure Conditions

- Any section lacks proof IDs or TODO.
- Any section could fit any unrelated product.
- Any section is described as generic component layout only.
- Three or more adjacent sections share the same skeleton.
- Any section can stand alone without continuity from previous or to next.
- Section numbers or rails become the main visual rhythm.
- Deprecated anti-slop rules are enforced.
- JSON is invalid.

## Validation Checklist

- Section IDs are stable.
- Proof IDs are valid.
- Public proof labels are present.
- Continuity from previous and curiosity to next are present.
- Rhythm roles vary across adjacent beats.
- Failure conditions are current-taxonomy-based.
- Copy, visual, layout, and CTA roles are separated.
- Blocked sections stay blocked.

## PASS/FAIL Format

```json
{
  "status": "PASS",
  "checked_artifact": "artifacts/02-section-plan.json",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": [],
  "section_proof_asset_ids": {"S01_HERO": ["PA-01"]},
  "required_fix": [],
  "allowed_next_skill": "design-intent-writer"
}
```

## Example Prompt

"Use `$section-contract-planner` to create long-scroll story-beat contracts for this Wadiz ebook. Every beat must include proof asset IDs, public proof labels, carry-over, curiosity gap, mobile scroll job, rhythm role, and cardnews failure conditions."
