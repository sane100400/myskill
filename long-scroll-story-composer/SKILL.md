---
name: long-scroll-story-composer
description: "Composes Wadiz detail pages as continuous long-scroll funding stories, not isolated card-news sections. Use before section planning or layout when a Korean Wadiz page needs emotional buildup, carry-over, curiosity gaps, proof integration, and scroll momentum across sections."
---

# Long-scroll Story Composer

## Purpose

Design the page as one continuous vertical persuasion flow. Do not design isolated slides, square card-news blocks, or self-contained sections.

## Required Inputs

- Product brief and source facts.
- Supporter psychology and objections.
- Proof asset map with public proof labels.
- Wadiz reference notes.
- Any failed page, screenshot, or HTML that looked like cardnews.

## Allowed Outputs

- `artifacts/03-long-scroll-story.md` or JSON equivalent.
- Story beat sequence.
- Continuity notes between beats.
- Curiosity gaps and emotional buildup.
- PASS/FAIL handoff to `$rhythm-variation-planner`.

## Forbidden Behavior

- Do not create HTML/CSS.
- Do not make every beat a section with number, kicker, headline, paragraph, and card.
- Do not use section numbers as the main visual rhythm.
- Do not reset emotion at each beat.
- Do not let proof assets sit as neat cards when they should interrupt, overlap, annotate, or carry the story.

## Workflow

1. Define the continuous emotional arc:
   - Sting.
   - Recognition.
   - Cause.
   - Promise.
   - Proof.
   - Usage.
   - Trust.
   - Reward.
   - Decision.
2. For each beat, define:
   - `beat_id`
   - `supporter_state_before`
   - `story_action`
   - `proof_or_tension`
   - `carry_over_from_previous`
   - `curiosity_gap_to_next`
   - `must_not_be_card`
3. Use varied beat lengths:
   - Some beats are one-line punches.
   - Some are long proof spreads.
   - Some are tables or comparison strips.
   - Some are quiet notes.
4. Mark any beat that can be screenshotted as a standalone card as `FAIL`.
5. Hand off to `$rhythm-variation-planner`.

## Failure Conditions

- The output reads like a list of independent slides.
- Each beat can stand alone without depending on the previous beat.
- Every beat uses the same header hierarchy.
- Proof assets appear only inside neat boxes.
- The emotional state does not change across the scroll.
- There is no explicit carry-over or curiosity gap.

## Validation Checklist

- The page has one continuous arc, not a deck.
- Every beat either answers or creates a supporter question.
- Visual motifs carry over across beats.
- Short emotional beats and long evidence beats alternate.
- The reward appears as part of the story, not only as a final table.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "artifacts/03-long-scroll-story.md",
  "failed_rules": ["Beat sequence reads as standalone card deck", "No carry-over between beats"],
  "required_fix": ["Rewrite beats as sting -> recognition -> cause -> promise -> proof -> usage -> trust -> reward -> decision"]
}
```

## Example Prompt

"Use `$long-scroll-story-composer` to plan this Wadiz ebook page as a continuous long-scroll funding story. Do not create section cards. Define emotional carry-over and curiosity gaps before any layout."
