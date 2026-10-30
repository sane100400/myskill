#!/usr/bin/env python3
"""Lightweight linter for sponsored Korean Naver blog drafts.

The script does not decide whether an experiential claim is true. It flags
phrases that require source verification and checks exact campaign requirements.
It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Finding:
    level: str
    code: str
    line: int | None
    text: str
    message: str
    suggestion: str | None = None


PATTERN_GROUPS: tuple[tuple[str, str, str, tuple[str, ...], str], ...] = (
    (
        "warn",
        "EXPERIENCE_VERIFY",
        "실제 경험으로 확인된 표현인지 점검하세요.",
        (
            r"(?:직접\s*)?(?:사|구매)봤(?:어요|는데|더니)",
            r"(?:직접\s*)?(?:써|사용해|입어|착용해|발라|먹어|마셔|가)봤(?:어요|는데|더니)",
            r"(?:구매|주문|결제|배송받|재구매)했(?:어요|습니다|는데|더니)",
            r"장바구니에\s*(?:담|넣)",
            r"쿠폰을?\s*(?:적용|사용)해?봤",
            r"며칠(?:째|간)|몇\s*주(?:째|간)|N일\s*사용",
        ),
        "확인되지 않았다면 사진 관찰·공식 정보·기대 표현으로 낮추세요.",
    ),
    (
        "warn",
        "AI_CLICHE",
        "추상적인 광고·AI 상투어가 있습니다.",
        (
            r"핵심\s*포인트",
            r"가장\s*큰\s*장점",
            r"전반적으로",
            r"활용도(?:가)?\s*높",
            r"합리적인\s*선택",
            r"추천드립(?:니다|려요)",
            r"완성도(?:가)?\s*높",
        ),
        "수치, 형태, 사용 조건이나 구체적인 생활 장면으로 바꾸세요.",
    ),
    (
        "warn",
        "UI_NARRATION",
        "페이지나 화면을 중계하는 문장입니다.",
        (
            r"화면을\s*열",
            r"열어보니",
            r"스크롤을\s*(?:내리|올리)",
            r"내려보니",
            r"눌러보니",
            r"사진을\s*보시면",
        ),
        "독자가 새로 알 수 있는 상품 특징이나 사실을 바로 쓰세요.",
    ),
    (
        "warn",
        "OVERCLAIM",
        "근거 없는 과장 또는 단정일 수 있습니다.",
        (
            r"역대급",
            r"무조건",
            r"인생템",
            r"완벽(?:한|해|했|합니다|해요)",
            r"맛이\s*없을\s*수\s*없",
            r"최고(?:의|예요|입니다)",
            r"절대\s*놓치지",
        ),
        "검증 가능한 조건을 붙이거나 표현 강도를 낮추세요.",
    ),
    (
        "warn",
        "UNSUPPORTED_EFFECT",
        "성분·소재·재료만으로 효능이나 안전성을 단정했을 수 있습니다.",
        (
            r"건강에\s*좋",
            r"다이어트에\s*(?:좋|도움)",
            r"피부(?:가|를)?\s*(?:개선|좋아|환해)",
            r"체형\s*보정",
            r"부담\s*없이\s*먹",
            r"안심하고\s*(?:먹|사용)",
        ),
        "공식 근거가 없다면 재료·성분·형태 자체만 설명하세요.",
    ),
    (
        "warn",
        "FORCED_BALANCE",
        "확인되지 않은 단점을 억지로 추가한 문장일 수 있습니다.",
        (
            r"장점만\s*있는\s*것은\s*아니",
            r"한\s*가지\s*아쉬운\s*점",
            r"아쉬운\s*부분도\s*있",
            r"다만\s*아쉬운",
        ),
        "실제 사용에서 확인한 조건이 아니라면 삭제하세요.",
    ),
    (
        "warn",
        "HARD_CTA",
        "강한 구매 유도 문장입니다.",
        (
            r"꼭\s*(?:사|구매|확인|둘러보)",
            r"지금\s*바로\s*(?:확인|구매)",
            r"절대\s*놓치지",
            r"무조건\s*(?:사|구매|먹어|써|입어)",
        ),
        "CTA는 글 전체에서 한 번만, 가볍게 남기세요.",
    ),
)

DISCLOSURE_HINTS = (
    "광고비",
    "원고료",
    "제품을 제공",
    "제품 제공",
    "서비스를 제공",
    "서비스 제공",
    "수수료",
    "경제적 이해관계",
    "유료 광고",
    "유료광고",
)

PLACEHOLDER_PATTERNS = (
    r"\bTODO\b",
    r"\bTBD\b",
    r"\[\s*(?:링크|URL|상품명|가격|키워드|이미지|확인 필요)\s*(?:입력|삽입)?\s*\]",
    r"<\s*(?:개인 링크|표시 문구|필수 키워드|횟수|상품명|가격)\s*>",
    r"(?:링크|URL)\s*(?:입력|삽입|추가)(?:\s*필요)?",
)

ENDING_RE = re.compile(
    r"(이에요|예요|했어요|더라고요|거든요|인데요|같아요|좋아요|있어요|합니다|됩니다|드려요|추천해요|해보세요)[.!?…\s]*$"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="에이블리·체험단 네이버 블로그 초안의 위험 표현과 필수 항목을 검사합니다."
    )
    parser.add_argument("draft", type=Path, help="검사할 UTF-8 Markdown 또는 텍스트 파일")
    parser.add_argument(
        "--require",
        action="append",
        default=[],
        metavar="TEXT",
        help="원고에 반드시 정확히 포함되어야 하는 문자열. 여러 번 지정 가능",
    )
    parser.add_argument(
        "--require-count",
        action="append",
        default=[],
        metavar="TEXT=N",
        help="문자열의 정확한 출현 횟수. 예: --require-count '에이블리=5'",
    )
    parser.add_argument(
        "--max-cta",
        type=int,
        default=1,
        help="허용할 강한 CTA 패턴 총횟수. 기본값: 1",
    )
    parser.add_argument(
        "--no-disclosure-check",
        action="store_true",
        help="일반 후기 조각처럼 표시 문구가 필요 없는 입력에서 사용",
    )
    parser.add_argument("--json", action="store_true", help="결과를 JSON으로 출력")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="finding이 하나라도 있으면 종료 코드 1 반환",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"UTF-8 파일이 아닙니다: {path}") from exc
    except OSError as exc:
        raise ValueError(f"파일을 읽을 수 없습니다: {path}: {exc}") from exc


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def select_non_overlapping(
    candidates: list[tuple[int, int, Finding]],
) -> list[Finding]:
    """Keep the longest match when findings with the same code overlap."""
    selected: list[tuple[int, int, Finding]] = []
    for start, end, finding in sorted(
        candidates, key=lambda item: (item[2].code, item[0], -(item[1] - item[0]))
    ):
        overlap_index = next(
            (
                index
                for index, (old_start, old_end, old_finding) in enumerate(selected)
                if old_finding.code == finding.code
                and start < old_end
                and old_start < end
            ),
            None,
        )
        if overlap_index is None:
            selected.append((start, end, finding))
            continue
        old_start, old_end, _ = selected[overlap_index]
        if end - start > old_end - old_start:
            selected[overlap_index] = (start, end, finding)
    return [item[2] for item in selected]


def iter_pattern_findings(text: str) -> Iterable[Finding]:
    candidates: list[tuple[int, int, Finding]] = []
    for level, code, message, patterns, suggestion in PATTERN_GROUPS:
        for pattern in patterns:
            for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                candidates.append(
                    (
                        match.start(),
                        match.end(),
                        Finding(
                            level=level,
                            code=code,
                            line=line_number(text, match.start()),
                            text=match.group(0),
                            message=message,
                            suggestion=suggestion,
                        ),
                    )
                )
    yield from select_non_overlapping(candidates)


def iter_placeholder_findings(text: str) -> Iterable[Finding]:
    candidates: list[tuple[int, int, Finding]] = []
    for pattern in PLACEHOLDER_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            candidates.append(
                (
                    match.start(),
                    match.end(),
                    Finding(
                        level="warn",
                        code="PLACEHOLDER",
                        line=line_number(text, match.start()),
                        text=match.group(0),
                        message="게시 전 채워야 할 자리표시자가 남아 있습니다.",
                        suggestion="원자료로 채우거나, 확인할 수 없다면 사용자에게 명확히 표시하세요.",
                    ),
                )
            )
    yield from select_non_overlapping(candidates)


def parse_required_count(raw: str) -> tuple[str, int]:
    if "=" not in raw:
        raise ValueError(f"--require-count 형식은 TEXT=N 이어야 합니다: {raw!r}")
    text, count_raw = raw.rsplit("=", 1)
    text = text.strip()
    if not text:
        raise ValueError(f"검사 문자열이 비어 있습니다: {raw!r}")
    try:
        count = int(count_raw.strip())
    except ValueError as exc:
        raise ValueError(f"횟수는 정수여야 합니다: {raw!r}") from exc
    if count < 0:
        raise ValueError(f"횟수는 0 이상이어야 합니다: {raw!r}")
    return text, count


def requirement_findings(
    text: str, required: list[str], required_counts: list[str]
) -> list[Finding]:
    findings: list[Finding] = []
    for item in required:
        if item not in text:
            findings.append(
                Finding(
                    level="error",
                    code="REQUIRED_MISSING",
                    line=None,
                    text=item,
                    message="필수 문자열이 원고에 없습니다.",
                    suggestion="원문 그대로 삽입하고 위치 요구사항도 별도로 확인하세요.",
                )
            )
    for raw in required_counts:
        item, expected = parse_required_count(raw)
        actual = text.count(item)
        if actual != expected:
            findings.append(
                Finding(
                    level="error",
                    code="REQUIRED_COUNT",
                    line=None,
                    text=item,
                    message=f"필수 문자열 출현 횟수가 다릅니다: expected={expected}, actual={actual}",
                    suggestion="미션이 지정한 형태와 횟수로 맞추세요.",
                )
            )
    return findings


def disclosure_finding(text: str) -> Finding | None:
    if any(hint in text for hint in DISCLOSURE_HINTS):
        return None
    return Finding(
        level="warn",
        code="DISCLOSURE_NOT_DETECTED",
        line=None,
        text="",
        message="일반적인 경제적 이해관계 표시 단서를 찾지 못했습니다.",
        suggestion="미션의 정확한 표시 문구와 위치를 확인하세요. 정확한 문구는 --require로 검사하는 편이 안전합니다.",
    )


def cta_count_finding(findings: list[Finding], max_cta: int) -> Finding | None:
    count = sum(1 for finding in findings if finding.code == "HARD_CTA")
    if count <= max_cta:
        return None
    return Finding(
        level="warn",
        code="CTA_REPETITION",
        line=None,
        text=str(count),
        message=f"강한 CTA가 {count}회 감지되었습니다. 허용값은 {max_cta}회입니다.",
        suggestion="상품별 CTA를 삭제하고 글 전체에서 한 번만 남기세요.",
    )


def ending_repetition_finding(text: str) -> Finding | None:
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?。！？])\s+|\n+", text)
        if len(sentence.strip()) >= 8
    ]
    endings = [match.group(1) for sentence in sentences if (match := ENDING_RE.search(sentence))]
    if len(endings) < 6:
        return None
    ending, count = Counter(endings).most_common(1)[0]
    ratio = count / len(endings)
    if count < 4 or ratio < 0.5:
        return None
    return Finding(
        level="warn",
        code="ENDING_REPETITION",
        line=None,
        text=ending,
        message=f"감지 가능한 종결어미 중 '{ending}'가 {count}/{len(endings)}회 반복됩니다.",
        suggestion="문장 구조와 길이를 먼저 바꾸고, 의미에 맞는 종결어미를 사용하세요.",
    )


def sort_findings(findings: list[Finding]) -> list[Finding]:
    rank = {"error": 0, "warn": 1, "info": 2}
    return sorted(
        findings,
        key=lambda item: (rank.get(item.level, 9), item.line is None, item.line or 0, item.code),
    )


def print_human(path: Path, findings: list[Finding]) -> None:
    print(f"Draft: {path}")
    if not findings:
        print("OK: 자동 검사에서 문제를 찾지 못했습니다. 사실·이미지·링크의 원자료 대조는 별도로 수행하세요.")
        return
    for finding in findings:
        location = f" line {finding.line}" if finding.line is not None else ""
        excerpt = f" | {finding.text!r}" if finding.text else ""
        print(f"[{finding.level.upper()}] {finding.code}{location}{excerpt}")
        print(f"  {finding.message}")
        if finding.suggestion:
            print(f"  -> {finding.suggestion}")
    errors = sum(1 for item in findings if item.level == "error")
    warnings = sum(1 for item in findings if item.level == "warn")
    print(f"Summary: {errors} error(s), {warnings} warning(s)")


def main() -> int:
    args = parse_args()
    try:
        text = read_text(args.draft)
        findings = list(iter_pattern_findings(text))
        findings.extend(iter_placeholder_findings(text))
        findings.extend(requirement_findings(text, args.require, args.require_count))
        if not args.no_disclosure_check:
            if disclosure := disclosure_finding(text):
                findings.append(disclosure)
        if repeated_cta := cta_count_finding(findings, args.max_cta):
            findings.append(repeated_cta)
        if repeated_ending := ending_repetition_finding(text):
            findings.append(repeated_ending)
        findings = sort_findings(findings)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        payload = {
            "draft": str(args.draft),
            "ok": not findings,
            "findings": [asdict(item) for item in findings],
            "summary": {
                "errors": sum(1 for item in findings if item.level == "error"),
                "warnings": sum(1 for item in findings if item.level == "warn"),
            },
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_human(args.draft, findings)

    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
