# Coupang Review Writer v3

쿠팡 상품 링크와 짧은 실사용 메모를 받아 **사용자가 원래 쓴 말투를 최대한 남긴 상품평**으로 정리하는 Codex 스킬입니다.

## v3에서 달라진 점

이전 버전의 문제는 좋은 리뷰의 요소를 체크리스트로 만들면서 결과가 더 반듯하고 비슷해졌다는 점이었습니다. v3에서는 다음을 바꿨습니다.

- 사용자 메모를 `자료`가 아니라 `초안`으로 취급
- 고정된 `구매동기 / 장점 / 단점 / 총평` 구조 삭제
- 카테고리별 항목 채우기와 문체 린터 삭제
- 사용자 표현 2~4개를 실제 결과에 남기는 방식
- 서로 구조가 다른 8개의 원문 메모 → 완성 리뷰 예시 제공
- 본인이 쓴 기존 리뷰를 넣어둘 수 있는 `my-review-samples.md` 추가
- 경험이 부족하면 스펙으로 늘리지 않고 질문하거나 짧게 종료

## 설치

기존 버전이 있으면 교체합니다.

```bash
rm -rf ~/.agents/skills/coupang-review-writer
unzip coupang-review-writer-codex-skill-v3.zip -d ~/.agents/skills
```

설치 결과:

```text
~/.agents/skills/coupang-review-writer/SKILL.md
```

## 기본 사용

```text
$coupang-review-writer
https://www.coupang.com/vp/products/...

체험단으로 받았고 책상 옆에서 이틀 써봤어.
물통 입구가 넓어서 닦기는 편했고 완전 무소음은 아닌데
낮에는 별로 안 거슬림. 밤에는 예민하면 들릴 것 같아.
내가 쓴 표현 최대한 남겨서 써줘.
```

## 내 말투를 더 정확하게 반영하기

`references/my-review-samples.md`에 본인이 직접 쓴 기존 쿠팡 리뷰를 3개 이상 붙여 넣습니다. 이후 스킬은 공개적인 일반 리뷰 문체보다 해당 샘플의 문장 길이, 줄바꿈, 종결어미를 우선합니다.

## 구성

```text
coupang-review-writer/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
└── references/
    ├── my-review-samples.md
    ├── research-notes.md
    └── voice-examples.md
```

별도의 문체 검사 스크립트는 넣지 않았습니다. 금지어와 항목 수를 세는 검사가 오히려 모델을 규칙 통과형 문장으로 몰 수 있기 때문입니다.
