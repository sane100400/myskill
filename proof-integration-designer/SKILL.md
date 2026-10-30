---
name: proof-integration-designer
description: "Integrates proof assets into the persuasive flow of Wadiz pages instead of displaying them as neat isolated cards. Use before image direction, layout specs, or HTML when digital rewards need tangible evidence without cardnews slop."
---

# Proof Integration Designer

## Purpose

Make proof act as evidence inside the story, not as decorative boxed assets.

## Required Inputs

- Proof asset map with private IDs and public labels.
- Long-scroll story beats.
- Rhythm variation plan.
- Product brief and source facts.

## Allowed Outputs

- Proof integration plan.
- Public proof labels.
- Evidence placement rules.
- Missing-proof blocking decisions.

## Forbidden Behavior

- Do not expose private proof IDs publicly.
- Do not put every proof object inside a card, row, or framed panel.
- Do not use decorative mockups as evidence.
- Do not invent screenshots, reviews, statistics, results, delivery dates, or maker photos.
- Do not create HTML/CSS.

## Workflow

1. For each proof asset, define:
   - `private_proof_id`
   - `public_label`
   - `supporter_takeaway`
   - `story_moment`
   - `integration_mode`
2. Choose varied integration modes:
   - Inline annotation.
   - Large spread.
   - Scroll comparison.
   - Margin note.
   - Tear-down overlay.
   - Workbook page excerpt.
   - Reward table.
   - Final proof reminder.
3. For missing proof, choose only:
   - Block the beat.
   - Move to private launch checklist.
   - Use explicitly approved public pending copy.
4. Reject proof that could be removed without changing the story.

## Failure Conditions

- Proof appears as a neat inventory only.
- Proof labels are internal IDs.
- Proof does not answer a supporter objection.
- Missing proof appears as TODO in public copy.
- Evidence is visually separated from the claim it supports.

## Validation Checklist

- Every major claim has nearby proof.
- Every proof object has a supporter takeaway.
- Proof placement changes rhythm, not just decoration.
- Missing proof is blocked or privately tracked.
- Public labels are human-readable Korean.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "proof-integration-plan",
  "failed_rules": ["Proof assets are isolated inventory cards"],
  "required_fix": ["Move workbook preview into the promise beat and annotate the before/after comparison in the problem beat"]
}
```

## Example Prompt

"Use `$proof-integration-designer` to integrate this ebook cover, PDF spread, checklist, and before/after example into a continuous Wadiz story. Do not display proof as isolated cards."
