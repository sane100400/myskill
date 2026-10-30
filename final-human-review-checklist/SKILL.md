---
name: final-human-review-checklist
description: "Creates the final human visual judgment checklist for Wadiz detail pages after automated validators pass. Use to review proof density, editorial intent, mobile readability, long-scroll momentum, cardnews slop, Wadiz story fit, and subtle current AI slop that cannot be fully automated."
---

# Final Human Review Checklist

## Purpose

Create the final review checklist for a human operator. Some 2026-style slop is a judgment problem, so this skill defines what a person must inspect after automated validation.

## Required Inputs

- Current slop taxonomy and evidence sources.
- Deprecated rule file.
- Product-specific design language.
- Proof asset map.
- Section contracts.
- Long-scroll story plan.
- Rhythm variation plan.
- Cardnews slop detector report.
- Implementation screenshots or page preview when available.

## Allowed Outputs

- `artifacts/06-final-review.md`
- Human review checklist.
- PASS/FAIL JSON summary.

Every output must include:
- `taxonomy_date`
- `evidence_sources`
- `deprecated_rules`
- `current_slop_signatures`
- `section_proof_asset_ids`
- `pass_fail_result`
- `required_fixes`

## Forbidden Behavior

- Do not claim automated validation is enough.
- Do not approve a page whose proof is present but visually unconvincing.
- Do not reintroduce outdated style bans.
- Do not accept a page that looks like a SaaS landing page instead of a Wadiz story.
- Do not accept a page that looks like a vertical stack of cardnews slides.

## Workflow

1. Confirm automated validators passed.
2. Build a human checklist:
   - Can the reviewer identify why each visual choice exists?
   - Does the proof feel real and specific?
   - Is there editorial rhythm and intentional pacing?
   - Does the mobile page read as a funding story?
   - Does the page avoid stacked cardnews rhythm?
   - Does emotion carry over from one scroll beat to the next?
   - Do proof assets interrupt and support claims instead of sitting in neat cards?
   - Are modern patterns used deliberately?
   - Are deprecated rules absent from judgment?
3. Run `$cardnews-slop-detector` if HTML/CSS exists.
4. Mark each item PASS, FAIL, or NEEDS HUMAN DECISION.
5. Output final fixes before launch or implementation approval.

## Failure Conditions

- No screenshots or preview when visual review is requested.
- Human checklist is generic.
- Proof density is not inspected.
- Cardnews slop is not inspected.
- Current taxonomy is missing.
- The page is approved despite unresolved slop signatures.

## Validation Checklist

- Review is tied to current taxonomy.
- Checklist covers judgment issues automation misses.
- Section proof IDs are visible.
- Final fixes are concrete.
- Deprecated rules are not used as final judgment criteria.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "final-human-review",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": ["human intent gap"],
  "section_proof_asset_ids": {},
  "required_fix": ["Add section-level visual rationale and inspect screenshot again"],
  "allowed_next_skill": null
}
```

## Example Prompt

"Use `$final-human-review-checklist` to create the final human review checklist for this Wadiz page screenshot after current slop validation passes."
