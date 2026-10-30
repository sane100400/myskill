---
name: wadiz-editorial-pacing-reviewer
description: "Reviews Wadiz detail pages for editorial pacing, emotional buildup, long-scroll continuity, proof timing, and funding-story persuasion. Use after screenshots or layout specs, before final approval."
---

# Wadiz Editorial Pacing Reviewer

## Purpose

Judge whether the page feels like a Wadiz funding story rather than a SaaS landing page, technical report, or stacked cardnews deck.

## Required Inputs

- Desktop and mobile screenshots.
- Long-scroll story plan.
- Rhythm variation plan.
- Proof integration plan.
- Public copy deck.

## Allowed Outputs

- `artifacts/06-editorial-pacing-review.md`.
- PASS/FAIL summary.
- Required fixes.

## Forbidden Behavior

- Do not approve a page because it is neat.
- Do not approve a page that only satisfies metadata.
- Do not rely on old surface bans.
- Do not redesign the page directly unless explicitly asked.

## Workflow

1. Review the full mobile screenshot before desktop.
2. Check the emotional arc:
   - Sting.
   - Recognition.
   - Cause.
   - Promise.
   - Proof.
   - Usage.
   - Trust.
   - Reward.
   - Decision.
3. Check whether proof arrives at the right time.
4. Check whether section rhythm varies.
5. Check whether repeated motifs carry over rather than reset.
6. Run `$cardnews-slop-detector` when HTML or screenshots exist.

## Failure Conditions

- The page feels like a vertical Instagram carousel.
- Every section is equally important.
- There is no tension, release, or curiosity gap.
- Proof arrives as inventory instead of evidence.
- CTA appears before desire and offer clarity.
- FAQ and caution flatten the page before the supporter wants the reward.

## Validation Checklist

- Long-scroll continuity is visible.
- Mobile scroll momentum is stronger than section neatness.
- There are deliberate fast and slow moments.
- Proof is integrated with claims.
- The final decision feels earned.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "mobile screenshot",
  "failed_rules": ["Cardnews rhythm", "No emotional buildup"],
  "required_fix": ["Remove repeated section rails and rebuild the first five beats as one continuous story"]
}
```

## Example Prompt

"Use `$wadiz-editorial-pacing-reviewer` to review this Wadiz mobile screenshot for long-scroll persuasion. Do not fix the page; report pacing failures and required changes."
