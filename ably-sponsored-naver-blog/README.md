# ably-sponsored-naver-blog

에이블리 크리에이터 링크, 체험단, 제품·서비스 제공, 원고료, 수익성 링크가 포함된 한국어 네이버 블로그 원고를 작성·수정·검수하는 Codex 스킬입니다.

## 구성

```text
ably-sponsored-naver-blog/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── quick-checklist.md
│   └── style-guide.md
└── scripts/
    └── check_draft.py
```

핵심 실행 규칙은 `SKILL.md`에 두고, 전체 문체 가이드는 경계 사례에서만 읽게 했습니다. `check_draft.py`는 가짜 경험 후보, AI 상투어, 과장, 반복 CTA, 필수 문구와 키워드 횟수를 보조적으로 검사합니다.

## 전역 설치

### WSL, Linux, macOS

ZIP 파일이 있는 폴더에서:

```bash
mkdir -p ~/.agents/skills
unzip ably-sponsored-naver-blog-codex-skill.zip -d ~/.agents/skills
```

압축을 이미 풀었다면:

```bash
mkdir -p ~/.agents/skills
cp -R ./ably-sponsored-naver-blog ~/.agents/skills/
```

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Expand-Archive ".\ably-sponsored-naver-blog-codex-skill.zip" -DestinationPath "$HOME\.agents\skills" -Force
```

## 저장소 전용 설치

저장소 루트에서:

```bash
mkdir -p .agents/skills
unzip ably-sponsored-naver-blog-codex-skill.zip -d .agents/skills
```

설치 후 Codex에서 `/skills`로 확인하거나 다음처럼 호출합니다.

```text
$ably-sponsored-naver-blog 첨부한 미션 자료와 사진을 바탕으로 네이버 블로그 원고를 작성해줘. 주문은 했지만 아직 먹지는 않았어.
```

```text
$ably-sponsored-naver-blog 이 초안의 AI 티와 가짜 경험을 없애고, 필수 키워드·표시 문구·링크는 그대로 보존해줘.
```

새 스킬이 바로 보이지 않으면 Codex를 재시작합니다.

## 선택형 원고 검사

```bash
python3 ~/.agents/skills/ably-sponsored-naver-blog/scripts/check_draft.py draft.md
```

정확한 필수 문구와 키워드 횟수까지 검사:

```bash
python3 ~/.agents/skills/ably-sponsored-naver-blog/scripts/check_draft.py draft.md \
  --require "본 포스팅은 광고비를 받고 작성된 유료 컨텐츠입니다" \
  --require "https://example.com/personal-reward-link" \
  --require-count "에이블리=5"
```

`--strict`를 추가하면 경고가 하나라도 있을 때 종료 코드 1을 반환하고, `--json`을 추가하면 JSON으로 출력합니다.
