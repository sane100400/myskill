---
name: product-proof-mapper
description: "Maps each Wadiz section to concrete product proof asset IDs such as ebook cover, PDF spread, checklist, prompt template, before/after example, reward bundle, maker process, and delivery guide. Use before section contracts so missing proof becomes TODO instead of hallucinated content."
---

# Product Proof Mapper

## Purpose

Anchor every section in concrete evidence. If an asset does not exist or is not sourced, mark it as `[TODO: source needed]` rather than inventing.

## Required Inputs

- `source/product-brief.md`
- `source/proof-assets.md`
- `reference-pack/current-good-wadiz-pages.md`
- `reference-pack/current-slop-signatures.md`
- Product files or asset paths.

## Allowed Outputs

- Updated `source/proof-assets.md`
- Section-to-proof map.
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

- Do not invent proof assets, screenshots, page counts, reviews, results, or before/after examples.
- Do not use a decorative mockup as evidence.
- Do not let a section proceed without at least one proof asset ID or TODO.
- Do not create copy or layout yet.

## Workflow

1. Register stable IDs: `PA-01`, `PA-02`, etc.
2. For each asset, define status:
   - `available`
   - `needed`
   - `blocked`
   - `not_allowed`
3. Map proof IDs to likely sections.
4. Mark cannot-fake assets.
5. If proof is missing, keep it visible as `[TODO: source needed]`.
6. Run `$current-slop-validator` to catch proof absence and mockup fakeness.

## Failure Conditions

- A section has no proof ID.
- A proof asset is marked available without a source.
- A fake or generated asset is used as evidence.
- Missing proof is hidden in polished language.
- Proof assets are not specific to the product.

## Validation Checklist

- Every asset has ID, status, source, and usage.
- Every section has proof IDs or TODO.
- Cannot-fake evidence is labeled.
- Decorative mockups are separated from proof.
- Missing proof blocks downstream production.

## PASS/FAIL Format

```json
{
  "status": "FAIL",
  "checked_artifact": "source/proof-assets.md",
  "taxonomy_date": "2026-06-06",
  "evidence_sources": [],
  "deprecated_rules": [],
  "current_slop_signatures": ["proof absence"],
  "section_proof_asset_ids": {"S01_HERO": ["PA-01", "[TODO: source needed]"]},
  "required_fix": ["Provide PA-04 before/after source or keep S01 blocked"],
  "allowed_next_skill": null
}
```

## Example Prompt

"Use `$product-proof-mapper` to map each Wadiz section to proof asset IDs. Do not invent missing proof; mark it `[TODO: source needed]`."
