---
name: cardnews-slop-detector
description: "Detects cardnews slop in Wadiz detail pages: vertical stacks of standalone social-slide-like sections, repeated number-kicker-headline-paragraph-card skeletons, rails, boxed panels, and rhythm resets. Use after section plans, layout specs, HTML, or screenshots before implementation approval."
---

# Cardnews Slop Detector

## Purpose

Fail outputs that look like a stack of square card-news slides instead of a continuous Wadiz long-scroll funding story.

## Required Inputs

- Section plan, layout spec, HTML, CSS, or screenshots.
- Long-scroll story plan when available.
- Rhythm variation plan when available.

## Allowed Outputs

- PASS/FAIL JSON only.
- Failed cardnews signatures.
- Required fixes.

## Script

Use the deterministic script when an implementation exists:

```bash
python $HOME/.codex/skills/cardnews-slop-detector/scripts/detect_cardnews_slop.py /path/to/index.html --css /path/to/styles.css
```

The script checks repeated section skeletons, section rails, kicker/header repetition, boxed-panel density, section count, and known cardnews class signatures. It is intentionally conservative: it catches structural risk, not final taste.

## Forbidden Behavior

- Do not approve a page because each individual section is tidy.
- Do not treat one-message-per-mobile-screen as sufficient.
- Do not ignore repeated section skeletons.
- Do not require every page to remove all sections; require continuity and rhythm variation.

## Failure Conditions

- Each section can be screenshotted as a standalone square card.
- The page repeats number -> kicker -> headline -> paragraph -> card/image.
- Visual rhythm resets at every section.
- The design feels like an Instagram carousel stacked vertically.
- Every section has the same spacing, border, radius, and header hierarchy.
- Section numbers, rails, boxed panels, ledgers, or isolated proof cards dominate.
- Proof assets are displayed as neat cards instead of persuasive evidence.
- Mobile scrolling feels monotonous.

## Validation Checklist

- Does each section depend on the previous one?
- Are there varied beat lengths and proof treatments?
- Are repeated rails or number markers subordinate to the story?
- Does the page include full-bleed, punch, proof spread, comparison, reward, note, FAQ, and CTA rhythms?
- Is the page compliant but not compelling?

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "index.html",
  "cardnews_score": 9,
  "failed_rules": ["Repeated section rail", "Repeated kicker/headline skeleton", "High boxed panel density"],
  "required_fix": ["Remove section rail as the primary rhythm", "Merge adjacent beats into a continuous proof spread"]
}
```

## Example Prompt

"Use `$cardnews-slop-detector` to validate this Wadiz HTML/CSS. Fail it if it looks like stacked cardnews, even if the copy and proof IDs are valid."
