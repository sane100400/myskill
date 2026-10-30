---
name: mobile-scroll-momentum-architect
description: "Designs and reviews mobile Wadiz scroll momentum so mobile-first does not become cardnews-first. Use when a page needs one-screen readability with carry-over, curiosity, pacing changes, and a reason to keep scrolling."
---

# Mobile Scroll Momentum Architect

## Purpose

Make mobile scrolling feel continuous and persuasive. One mobile viewport can have one main message, but it must pull the supporter into the next viewport instead of becoming a standalone card.

## Required Inputs

- Long-scroll story plan.
- Rhythm variation plan.
- Mobile screenshots or target viewport sizes.
- Public copy deck.
- Proof integration plan.

## Allowed Outputs

- Mobile viewport momentum map.
- Scroll hooks.
- PASS/FAIL review.
- Required fixes before implementation or launch.

## Forbidden Behavior

- Do not interpret mobile-first as one card per section.
- Do not make every viewport self-contained.
- Do not repeat the same opening pattern on each screen.
- Do not use section numbers as the primary mobile navigation.
- Do not approve mobile screenshots with monotone section rhythm.

## Workflow

1. Review each target viewport, usually 390px and 412px wide.
2. For each visible screen, record:
   - `emotional_job`
   - `current_question`
   - `proof_or_tension`
   - `carry_over_from_previous`
   - `reason_to_continue`
   - `rhythm_change`
3. Check whether the next screen answers or intensifies the previous one.
4. Require alternation:
   - short punch
   - proof
   - explanation
   - decision
   - caution
5. FAIL if the mobile page feels like vertical cards.

## Failure Conditions

- Each viewport can be screenshotted as a standalone social slide.
- The emotional state resets at every section.
- There is no curiosity gap.
- Same spacing/header/panel rhythm repeats three times.
- The page has one message per screen but no scroll momentum.
- Proof appears too late or only as inventory.

## Validation Checklist

- Each mobile screen has a reason to continue.
- Adjacent screens depend on each other.
- Pacing alternates between fast and slow.
- Proof and CTA timing match supporter readiness.
- Repetition is intentional, not default.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "viewport": "390x844",
  "failed_rules": ["Every screen resets with number + kicker + headline"],
  "required_fix": ["Remove repeated rails and combine two screens into one continuous proof spread"]
}
```

## Example Prompt

"Use `$mobile-scroll-momentum-architect` to review this 390px Wadiz screenshot. Fail it if mobile-first has become cardnews-first."
