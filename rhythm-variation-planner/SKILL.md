---
name: rhythm-variation-planner
description: "Plans varied long-scroll layout rhythm for Wadiz detail pages so Codex does not repeat number, kicker, headline, paragraph, and boxed proof patterns. Use after long-scroll story composition and before layout specs."
---

# Rhythm Variation Planner

## Purpose

Prevent monotony and cardnews slop by assigning different visual roles, lengths, and transitions to each story beat.

## Required Inputs

- `artifacts/03-long-scroll-story.md` or equivalent.
- Proof asset map with public labels.
- Product-specific design language.
- Current failed screenshots or HTML when available.

## Allowed Outputs

- `artifacts/04-rhythm-variation-plan.json`.
- Beat-to-layout rhythm map.
- Repetition audit.
- PASS/FAIL handoff to `$proof-integration-designer`.

## Forbidden Behavior

- Do not use the same skeleton for every beat.
- Do not make rails, badges, rounded cards, boxed rows, or section numbers the page's main rhythm.
- Do not force every message into a panel.
- Do not create HTML/CSS.

## Workflow

1. Count repeated skeleton elements in the planned page:
   - Number marker.
   - Kicker.
   - Headline.
   - Paragraph.
   - Boxed proof.
   - Ledger row.
2. Assign each beat one rhythm type:
   - Full-bleed hook.
   - Short emotional punch.
   - Problem teardown.
   - Annotated proof spread.
   - Workbook preview.
   - Before/after scroll comparison.
   - Reward table.
   - Maker note.
   - FAQ.
   - Final CTA.
3. Require adjacent beats to differ in at least two dimensions:
   - Visual scale.
   - Density.
   - Background treatment.
   - Proof placement.
   - Text length.
   - CTA presence.
4. Mark repeated skeletons as `FAIL`.

## Failure Conditions

- Three or more adjacent beats share the same visual skeleton.
- Section numbers dominate the rhythm.
- Every beat is a boxed panel.
- Proof always appears in a card or ledger row.
- The layout reads like a stacked Instagram carousel.

## Validation Checklist

- The rhythm alternates between tension, evidence, explanation, and decision.
- At least one proof spread breaks the section grid.
- At least one short punch beat creates scroll momentum.
- At least one dense section slows the supporter down deliberately.
- No two adjacent beats reset the story in the same way.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "artifacts/04-rhythm-variation-plan.json",
  "failed_rules": ["Repeated number-kicker-headline-card skeleton"],
  "required_fix": ["Replace two adjacent card sections with a proof spread and a short emotional punch"]
}
```

## Example Prompt

"Use `$rhythm-variation-planner` to rewrite this Wadiz section plan so it cannot become cardnews. Produce varied long-scroll rhythm before layout or HTML."
