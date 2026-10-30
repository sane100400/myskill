#!/usr/bin/env python3
"""Validate date-aware Wadiz artifacts against the current reference pack.

This script avoids hardcoded old anti-slop rules. It checks that a dated
taxonomy exists, proof asset IDs are traceable, section metadata is present,
and optional code signatures come from reference-pack/current-slop-signatures.md.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_REFERENCE_FILES = (
    "reference-pack/current-codex-slop-taxonomy.md",
    "reference-pack/current-slop-signatures.md",
    "reference-pack/deprecated-slop-rules.md",
    "reference-pack/accepted-modern-patterns.md",
    "reference-pack/product-specific-design-language.md",
)

REQUIRED_SOURCE_FILES = (
    "source/product-brief.md",
    "source/proof-assets.md",
    "source/design-constitution.md",
    "source/wadiz-story-rules.md",
)

REQUIRED_ARTIFACT_FILES = (
    "artifacts/02-section-plan.json",
)

REQUIRED_HTML_ATTRS = (
    "data-section-id",
    "data-proof-assets",
    "data-taxonomy-date",
    "data-current-slop-status",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> tuple[object | None, list[str]]:
    try:
        return json.loads(read(path)), []
    except FileNotFoundError:
        return None, [f"Missing file: {path}"]
    except json.JSONDecodeError as exc:
        return None, [f"Invalid JSON: {path}: {exc}"]


def dates_in(text: str) -> set[str]:
    return set(re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", text))


def proof_ids_from_markdown(path: Path) -> tuple[set[str], list[str]]:
    if not path.exists():
        return set(), [f"Missing file: {path}"]
    text = read(path)
    ids = set(re.findall(r"\bPA-\d{2,}\b", text))
    if not ids:
        return ids, [f"No PA IDs found in {path}"]
    return ids, []


def section_proof_ids(section: dict) -> list[str]:
    for key in ("required_proof_asset_ids", "proof_asset_ids", "proof_assets"):
        value = section.get(key)
        if isinstance(value, list):
            return [str(item) for item in value]
        if isinstance(value, str):
            return value.split()
    return []


def optional_code_signatures(reference_pack: Path) -> set[str]:
    path = reference_pack / "current-slop-signatures.md"
    if not path.exists():
        return set()
    text = read(path)
    marker = "## Optional Code Signatures"
    if marker not in text:
        return set()
    section = text.split(marker, 1)[1]
    next_heading = re.search(r"\n##\s+", section)
    if next_heading:
        section = section[: next_heading.start()]
    signatures: set[str] = set()
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("-"):
            continue
        signatures.update(re.findall(r"`([^`]+)`", stripped))
    return signatures


def validate_required_files(project: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_REFERENCE_FILES + REQUIRED_SOURCE_FILES + REQUIRED_ARTIFACT_FILES:
        if not (project / rel).exists():
            errors.append(f"Missing file: {project / rel}")
    return errors


def validate_taxonomy(project: Path) -> tuple[str | None, list[str]]:
    errors: list[str] = []
    taxonomy = project / "reference-pack" / "current-codex-slop-taxonomy.md"
    signatures = project / "reference-pack" / "current-slop-signatures.md"
    deprecated = project / "reference-pack" / "deprecated-slop-rules.md"

    taxonomy_dates = dates_in(read(taxonomy)) if taxonomy.exists() else set()
    signature_dates = dates_in(read(signatures)) if signatures.exists() else set()

    if not taxonomy_dates:
        errors.append(f"No taxonomy date found in {taxonomy}")
    if not signature_dates:
        errors.append(f"No taxonomy date found in {signatures}")
    if deprecated.exists() and "[DEPRECATED_RULE]" not in read(deprecated):
        errors.append(f"No [DEPRECATED_RULE] marker found in {deprecated}")

    date = sorted(taxonomy_dates)[-1] if taxonomy_dates else None
    return date, errors


def validate_sections(project: Path, proof_ids: set[str]) -> tuple[dict[str, list[str]], list[str]]:
    errors: list[str] = []
    section_map: dict[str, list[str]] = {}
    data, json_errors = load_json(project / "artifacts" / "02-section-plan.json")
    errors.extend(json_errors)
    if not isinstance(data, dict):
        return section_map, errors

    sections = data.get("sections", [])
    if not isinstance(sections, list):
        return section_map, errors + ["artifacts/02-section-plan.json: sections must be a list"]

    for index, section in enumerate(sections):
        if not isinstance(section, dict):
            errors.append(f"Section #{index + 1} must be an object")
            continue
        section_id = str(section.get("section_id", f"#{index + 1}"))
        ids = section_proof_ids(section)
        section_map[section_id] = ids
        has_todo = "[TODO: source needed]" in json.dumps(section, ensure_ascii=False)
        if not ids and not has_todo:
            errors.append(f"{section_id}: missing proof asset IDs or [TODO: source needed]")
        for proof_id in ids:
            if proof_id not in proof_ids:
                errors.append(f"{section_id}: undefined proof asset ID {proof_id}")
    return section_map, errors


def validate_html(paths: list[Path], signatures: set[str]) -> list[str]:
    errors: list[str] = []
    section_pattern = re.compile(r"<section\b(?P<attrs>[^>]*)>", re.IGNORECASE)
    class_pattern = re.compile(r'class=["\']([^"\']+)["\']', re.IGNORECASE)
    for path in paths:
        if not path.exists():
            errors.append(f"Missing HTML file: {path}")
            continue
        text = read(path)
        for class_match in class_pattern.finditer(text):
            classes = set(class_match.group(1).split())
            flagged = sorted(classes & signatures)
            if flagged:
                errors.append(f"{path}: current taxonomy code signature(s): {', '.join(flagged)}")
        for match in section_pattern.finditer(text):
            attrs = match.group("attrs")
            for required in REQUIRED_HTML_ATTRS:
                if required not in attrs:
                    errors.append(f"{path}: section missing {required}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", nargs="?", default=".", help="Project root with reference-pack/, source/, and artifacts/")
    parser.add_argument("--html", nargs="*", default=[], help="HTML files to validate")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    errors: list[str] = []
    errors.extend(validate_required_files(project))

    taxonomy_date, taxonomy_errors = validate_taxonomy(project)
    errors.extend(taxonomy_errors)

    proof_ids, proof_errors = proof_ids_from_markdown(project / "source" / "proof-assets.md")
    errors.extend(proof_errors)

    section_map, section_errors = validate_sections(project, proof_ids)
    errors.extend(section_errors)

    signatures = optional_code_signatures(project / "reference-pack")
    errors.extend(validate_html([Path(p).resolve() for p in args.html], signatures))

    status = "FAIL" if errors else "PASS"
    report = {
        "status": status,
        "checked_artifact": str(project),
        "taxonomy_date": taxonomy_date,
        "evidence_sources": [],
        "deprecated_rules": [],
        "current_slop_signatures": sorted(signatures),
        "section_proof_asset_ids": section_map,
        "failed_rules": errors,
        "required_fix": ["Fix failed_rules before moving to the next skill"] if errors else [],
        "allowed_next_skill": None if errors else "next-contract-step",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
