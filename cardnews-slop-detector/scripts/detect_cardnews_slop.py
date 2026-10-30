#!/usr/bin/env python3
"""Detect cardnews slop in Wadiz long-scroll pages.

This is a structural risk detector. It intentionally fails pages that repeat
isolated section skeletons even when metadata, proof IDs, and copy are valid.
"""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


REPEATED_CLASS_SIGNATURES = {
    "rail",
    "side-index",
    "section-index",
    "kicker",
    "section-header",
    "artifact-row",
    "fit-panel",
    "reward-ledger",
    "faq-list",
    "story-section",
}

BOXED_PANEL_CLASSES = {
    "artifact-row",
    "fit-panel",
    "paper-page",
    "note-board",
    "image-sheet",
    "faq-list",
    "reward-ledger",
    "final-layout",
    "proof-frame",
    "proof-card",
    "card",
    "panel",
    "ledger",
}


class SectionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sections: list[dict] = []
        self._stack: list[str] = []
        self._current: dict | None = None
        self._section_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v or "" for k, v in attrs}
        classes = set(attrs_dict.get("class", "").split())
        if tag == "section":
            self._current = {
                "classes": sorted(classes),
                "class_text": attrs_dict.get("class", ""),
                "data_section_id": attrs_dict.get("data-section-id", ""),
                "tags": [],
                "classes_seen": [],
                "text": "",
                "headings": 0,
                "paragraphs": 0,
                "figures": 0,
                "articles": 0,
                "links": 0,
                "has_number": False,
            }
            self._section_depth = 1
            return
        if self._current is None:
            return
        self._section_depth += 1
        self._current["tags"].append(tag)
        self._current["classes_seen"].extend(classes)
        if tag in {"h1", "h2", "h3"}:
            self._current["headings"] += 1
        elif tag == "p":
            self._current["paragraphs"] += 1
        elif tag == "figure":
            self._current["figures"] += 1
        elif tag == "article":
            self._current["articles"] += 1
        elif tag == "a":
            self._current["links"] += 1

    def handle_endtag(self, tag: str) -> None:
        if self._current is None:
            return
        if tag == "section":
            text = self._current["text"]
            self._current["has_number"] = bool(re.search(r"\b(?:0[1-9]|1[0-9]|[1-9])\b", text[:80]))
            self.sections.append(self._current)
            self._current = None
            self._section_depth = 0
            return
        self._section_depth = max(0, self._section_depth - 1)

    def handle_data(self, data: str) -> None:
        if self._current is not None:
            self._current["text"] += data.strip() + " "


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ratio(count: int, total: int) -> float:
    return count / total if total else 0.0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", help="HTML file to inspect")
    parser.add_argument("--css", help="Optional CSS file to inspect")
    parser.add_argument("--threshold", type=int, default=6, help="Score at or above this value fails")
    args = parser.parse_args()

    html_path = Path(args.html).resolve()
    html = read(html_path)
    css = read(Path(args.css).resolve()) if args.css else ""

    p = SectionParser()
    p.feed(html)
    sections = p.sections
    section_count = len(sections)
    failed_rules: list[str] = []
    score = 0

    if section_count >= 8:
        score += 1
        failed_rules.append("Many isolated section blocks")

    repeated = {}
    for cls in REPEATED_CLASS_SIGNATURES:
        repeated[cls] = sum(1 for s in sections if cls in set(s["classes_seen"]) or cls in set(s["classes"]))

    if ratio(repeated.get("rail", 0) + repeated.get("side-index", 0) + repeated.get("section-index", 0), section_count) >= 0.7:
        score += 2
        failed_rules.append("Section numbers or rails dominate the rhythm")

    if ratio(repeated.get("kicker", 0), section_count) >= 0.7:
        score += 2
        failed_rules.append("Repeated kicker on most sections")

    if ratio(repeated.get("section-header", 0), section_count) >= 0.5:
        score += 1
        failed_rules.append("Repeated section-header skeleton")

    boxed_count = 0
    for section in sections:
        classes = set(section["classes_seen"]) | set(section["classes"])
        if classes & BOXED_PANEL_CLASSES or section["articles"] >= 2 or section["figures"] >= 1:
            boxed_count += 1
    if ratio(boxed_count, section_count) >= 0.75:
        score += 2
        failed_rules.append("High boxed panel or isolated proof density")

    skeleton_sections = 0
    for section in sections:
        classes = set(section["classes_seen"]) | set(section["classes"])
        if (
            ("kicker" in classes or section["has_number"])
            and section["headings"] >= 1
            and section["paragraphs"] >= 1
            and (section["figures"] >= 1 or section["articles"] >= 1 or classes & BOXED_PANEL_CLASSES)
        ):
            skeleton_sections += 1
    if ratio(skeleton_sections, section_count) >= 0.65:
        score += 3
        failed_rules.append("Repeated number/kicker/headline/paragraph/proof skeleton")

    css_repetition_hits = [
        name for name in REPEATED_CLASS_SIGNATURES | BOXED_PANEL_CLASSES
        if len(re.findall(rf"\.{re.escape(name)}\b", css)) >= 2
    ]
    if len(css_repetition_hits) >= 5:
        score += 1
        failed_rules.append("CSS reinforces repeated cardnews components")

    status = "FAIL" if score >= args.threshold else "PASS"
    required_fix = []
    if status == "FAIL":
        required_fix = [
            "Remove section numbers or rails as the primary visual rhythm.",
            "Replace repeated section skeletons with a continuous long-scroll story arc.",
            "Vary adjacent beats by scale, density, proof placement, and pacing.",
            "Integrate proof assets into claims instead of boxing every proof object.",
        ]

    report = {
        "status": status,
        "checked_artifact": str(html_path),
        "cardnews_score": score,
        "threshold": args.threshold,
        "section_count": section_count,
        "repeated_class_counts": repeated,
        "boxed_section_count": boxed_count,
        "skeleton_section_count": skeleton_sections,
        "css_repetition_hits": sorted(css_repetition_hits),
        "failed_rules": failed_rules,
        "required_fix": required_fix,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if status == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
