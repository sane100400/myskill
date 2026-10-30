---
name: outdated-rule-filter
description: "Filters anti-slop rules before they are enforced. Use after Current Slop Taxonomy Builder to mark old rules as deprecated when they no longer match current Codex/v0/Lovable outputs, block valid human design styles, focus on surface aesthetics instead of structural genericness, or cause overcorrection into another generic style."
---

# Outdated Rule Filter

## Purpose

Prevent stale anti-slop rules from steering Codex into a newer form of generic design. A rule must be current, evidence-backed, and structural before it can be enforced.

## Required Inputs

- `reference-pack/current-codex-slop-taxonomy.md`
- Candidate anti-slop rules.
- Current reference examples and dates.
- Product context and Wadiz platform context.

## Allowed Outputs

- `reference-pack/deprecated-slop-rules.md`
- Updated `reference-pack/current-slop-signatures.md`
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

- Do not enforce a rule because it sounds familiar.
- Do not ban a visual style if the issue is actually proof absence, weak hierarchy, or generic information design.
- Do not keep a rule that causes the model to overcorrect into another default style.
- Do not delete a useful rule without stating why it is outdated or replaced.

## Workflow

1. Read the current taxonomy.
2. For each candidate rule, decide:
   - `enforce`
   - `revise_to_structural_signal`
   - `deprecated`
   - `needs_more_evidence`
3. A rule is deprecated if:
   - It describes an older AI design cliché absent from current examples.
   - It blocks a style current human designers can use well.
   - It focuses on surface aesthetics instead of structural genericness.
   - It causes overcorrection into another generic style.
4. Rewrite surviving rules as symptoms:
   - "Reject component defaultness" instead of "ban cards."
   - "Reject proof-free mockups" instead of "ban laptop mockups."
5. Run `$current-slop-validator`.

## Failure Conditions

- Deprecated rules are still enforced.
- Current rules lack evidence sources.
- Surface rules are not translated into structural failure signals.
- The filter ignores product-specific Wadiz needs.
- The output has no PASS/FAIL status.

## Validation Checklist

- Every enforced rule has current evidence.
- Every deprecated rule has a reason.
- Surface-style bans are converted into symptom tests.
- The validator receives only current, structural signatures.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "reference-pack/deprecated-slop-rules.md",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": ["[DEPRECATED_RULE] avoid purple gradients unless current references prove relevance"],
  "current_slop_signatures": [],
  "section_proof_asset_ids": {},
  "required_fix": ["Move stale rule out of enforced validator"],
  "allowed_next_skill": null
}
```

## Example Prompt

"Use `$outdated-rule-filter` to review these anti-slop rules against the current taxonomy. Mark old surface bans as `[DEPRECATED_RULE]` and rewrite useful ones as structural failure signals."
