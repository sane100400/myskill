---
name: current-slop-validator
description: "Validates Wadiz artifacts and implementations against the current dated slop taxonomy, not hardcoded old rules. Use after every artifact to reject component defaultness, section sameness, proof absence, context collapse, overly smooth copy, fake mockups, design-system overfit, startup-landing-page mismatch, missing human intent, and hand off to cardnews-slop detection for stacked social-slide rhythms."
---

# Current Slop Validator

## Purpose

Judge outputs against the current taxonomy and product-specific design intent. This is a PASS/FAIL validator, not a style preference list.

This validator is not sufficient for final approval. For Wadiz pages, always run `$cardnews-slop-detector` after this validator when a section plan, layout spec, HTML, CSS, or screenshot exists.

## Required Inputs

- Artifact or implementation to validate.
- `reference-pack/current-codex-slop-taxonomy.md`
- `reference-pack/current-slop-signatures.md`
- `reference-pack/deprecated-slop-rules.md`
- `reference-pack/product-specific-design-language.md`
- `source/proof-assets.md`
- `artifacts/02-section-plan.json` when validating sections or implementation.

## Allowed Outputs

- PASS/FAIL JSON only.
- Failed current signatures.
- Deprecated rules found.
- Required fixes.

## Script

Use `scripts/validate_current_wadiz_artifacts.py` when a project folder exists:

```bash
python $HOME/.codex/skills/current-slop-validator/scripts/validate_current_wadiz_artifacts.py /path/to/project
python $HOME/.codex/skills/current-slop-validator/scripts/validate_current_wadiz_artifacts.py /path/to/project --html dist/index.html
```

The script checks dated reference-pack files, proof asset IDs, section proof references, deprecated-rule markers, required HTML metadata, and optional code signatures read from the current taxonomy. It does not use hardcoded old style bans.

Every output must include:
- `taxonomy_date`
- `evidence_sources`
- `deprecated_rules`
- `current_slop_signatures`
- `section_proof_asset_ids`
- `pass_fail_result`
- `required_fixes`

## Forbidden Behavior

- Do not validate from memory.
- Do not enforce deprecated rules.
- Do not give aesthetic opinions without tying them to taxonomy signatures.
- Do not approve proof-free polish.
- Do not rewrite the artifact except for required fix suggestions.

## Workflow

1. Confirm taxonomy date and evidence sources.
2. Check for the 2026-style symptoms if present in the taxonomy:
   - Component defaultness.
   - Section sameness.
   - Proof absence.
   - Context collapse.
   - Editorial weakness.
   - Copy smoothness.
   - Mockup fakeness.
   - Design-system overfit.
   - Detail-page mismatch.
   - Human intent gap.
3. Check every section has proof asset IDs.
4. Check deprecated rules are not enforced.
5. For HTML, check required metadata:
   - `data-section-id`
   - `data-proof-assets`
   - `data-taxonomy-date`
   - `data-current-slop-status`
6. Return PASS or FAIL JSON.
7. Run `$cardnews-slop-detector` for repeated section skeletons and long-scroll continuity risk.

## Failure Conditions

- Taxonomy missing, undated, or source-free.
- Output fails current slop signatures.
- Output enforces deprecated rules.
- Section lacks proof asset IDs.
- Implementation lacks metadata.
- Visual polish hides lack of proof or intent.
- Output passes metadata checks but looks like stacked cardnews.

## Validation Checklist

- Current taxonomy exists and is dated.
- Deprecated rules are ignored.
- Product proof is visible or reserved.
- Layout and copy are product-specific.
- PASS/FAIL result has concrete required fixes.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "artifacts/02-section-plan.json",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": ["component defaultness", "proof absence"],
  "section_proof_asset_ids": {"S01_HERO": []},
  "required_fix": ["Add proof asset IDs to S01_HERO", "Replace component rhythm with product-specific proof sequence"],
  "allowed_next_skill": null
}
```

## Example Prompt

"Use `$current-slop-validator` to validate this layout spec against the dated taxonomy. Return PASS/FAIL JSON only and do not enforce deprecated style bans."
