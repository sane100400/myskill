---
name: current-slop-taxonomy-builder
description: "Builds a dated, evidence-based taxonomy of current AI/Codex web and Wadiz detail-page slop before production. Use first for Wadiz story page work to research current Codex, v0, Lovable, Bolt, Cursor, and similar AI-generated patterns, separate current slop signatures from outdated stereotypes, and create reference-pack/current-codex-slop-taxonomy.md."
---

# Current Slop Taxonomy Builder

## Purpose

Build a current, dated slop taxonomy from fresh references. Do not define AI slop from memory. Do not hardcode old surface rules unless the current reference set proves they still matter.

## Required Inputs

- Current date.
- Target platform: Wadiz story detail page.
- Tool context: Codex, Cursor, v0, Lovable, Bolt, Claude Code, or similar.
- Current references:
  - 10 strong Wadiz/detail-page examples when available.
  - 10 weak AI-generated or failed examples when available.
  - User's failed outputs, screenshots, HTML, or class names.
  - Current design trend notes or cited sources.

## Allowed Outputs

- `reference-pack/current-codex-slop-taxonomy.md`
- `reference-pack/current-slop-signatures.md`
- `reference-pack/current-bad-ai-pages.md`
- `reference-pack/accepted-modern-patterns.md`
- PASS/FAIL JSON report.

Every output must include:
- `taxonomy_date`
- `evidence_sources`
- `current_slop_signatures`
- `deprecated_rule_candidates`
- `section_proof_asset_ids`
- `accepted_modern_patterns`
- `pass_fail_result`
- `required_fixes`

## Forbidden Behavior

- Do not use anti-slop rules from memory.
- Do not treat old clichés such as one color, one framework, or one visual style as automatically current.
- Do not ban styles that can be used well by human designers unless the current taxonomy shows structural genericness.
- Do not let missing evidence become a rule.
- Do not produce a page, copy deck, layout, or image prompt.

## Workflow

1. Gather current references with dates and links/files.
2. Separate observations into:
   - Current slop signatures.
   - Outdated slop stereotypes.
   - Accepted modern patterns.
   - Dangerous modern defaults.
3. Prefer symptom-based rules over style bans:
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
4. Mark uncertain items as `[TODO: current reference needed]`.
5. Hand off deprecated candidates to `$outdated-rule-filter`.
6. Run `$current-slop-validator` on the taxonomy artifact.

## Failure Conditions

- No taxonomy date.
- No evidence sources.
- Rules are based on memory instead of references.
- Surface style bans replace structural failure signals.
- The taxonomy would overcorrect into another generic style.
- It cannot explain why an output fails beyond "looks AI."

## Validation Checklist

- Taxonomy is dated.
- Every current signature has evidence.
- Old stereotypes are separated from current signatures.
- Current signatures describe judgment failure, not just aesthetics.
- The artifact can update the validator without hardcoded assumptions.

## PASS/FAIL Format

```json
{
  "status": "PASS",
  "checked_artifact": "reference-pack/current-codex-slop-taxonomy.md",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": [],
  "section_proof_asset_ids": {},
  "required_fix": [],
  "allowed_next_skill": "outdated-rule-filter"
}
```

## Example Prompt

"Use `$current-slop-taxonomy-builder` to build a 2026-06-06 Wadiz/Codex slop taxonomy from my failed HTML, 10 current good Wadiz references, and 10 weak AI-generated examples. Do not rely on old rules unless the references support them."
