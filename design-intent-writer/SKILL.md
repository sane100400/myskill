---
name: design-intent-writer
description: "Defines product-specific visual language before layout and implementation. Use after section contracts to create reference-pack/product-specific-design-language.md with mood, pacing, hierarchy, image logic, typography direction, spacing logic, editorial rhythm, and non-generic design intent based on current slop taxonomy."
---

# Design Intent Writer

## Purpose

State why each visual choice exists before layout or code. This prevents Codex from replacing missing design judgment with default components.

## Required Inputs

- `artifacts/02-section-plan.json`
- `source/proof-assets.md`
- `reference-pack/current-slop-signatures.md`
- `reference-pack/accepted-modern-patterns.md`
- Wadiz reference notes.

## Allowed Outputs

- `reference-pack/product-specific-design-language.md`
- Design intent notes per section.
- PASS/FAIL JSON report.

Every output must include:
- `taxonomy_date`
- `evidence_sources`
- `deprecated_rules`
- `current_slop_signatures`
- `section_proof_asset_ids`
- `pass_fail_result`
- `required_fixes`

## Forbidden Behavior

- Do not write generic style words without section-specific intent.
- Do not define style only by color, radius, shadow, or component set.
- Do not use "premium", "crafted", "seamless", or similar smooth words unless tied to a visible proof decision.
- Do not produce HTML/CSS.

## Workflow

1. Define product-specific visual language:
   - Mood.
   - Pacing.
   - Hierarchy.
   - Image logic.
   - Typography direction.
   - Spacing logic.
   - Editorial interruption.
   - Proof-object rhythm.
2. For each section, answer:
   - Why this visual structure?
   - What proof does it foreground?
   - What should feel intentionally uneven or editorial?
   - What current slop signature does it avoid?
3. Mark unsupported visual claims as `[TODO: source needed]`.
4. Run `$current-slop-validator`.

## Failure Conditions

- Design intent could fit any product.
- It describes a component system instead of a story rhythm.
- It relies on smooth adjectives instead of visual decisions.
- It omits proof asset IDs.
- It ignores current slop taxonomy.

## Validation Checklist

- Every section has a reasoned visual intent.
- Proof objects drive hierarchy.
- Accepted modern patterns are used deliberately, not by default.
- Editorial rhythm and asymmetry are specified where useful.
- Design direction is product-specific.

## PASS/FAIL Format

```json
{
  "status": "PASS",
  "checked_artifact": "reference-pack/product-specific-design-language.md",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": [],
  "section_proof_asset_ids": {"S03_REWARD_PROOF": ["PA-01", "PA-03"]},
  "required_fix": [],
  "allowed_next_skill": "codex-implementation-guard"
}
```

## Example Prompt

"Use `$design-intent-writer` to define the product-specific visual language for this Wadiz PDF workbook before layout. Avoid component defaultness and explain the proof-object rhythm section by section."
