# 송우진 수의사 개인 홈페이지

시그니처 동물의료센터 내과 원장 송우진(한국수의내과전문의, 전 제주대학교 수의과대학 교수)의 개인 홈페이지.
이태호(`~/leetaeho-homepage`)·안운찬(`~/ahn-woonchan-homepage`) 홈페이지와 같은 구조(정적 HTML 1장, Vercel 배포)다.

- 배포: GitHub `growingtiger/songwoojin-homepage` → Vercel 자동 배포 (`git push`)
- 공개 주소: https://songwoojin.co.kr (2026-10-02 도메인 연결; songwoojin.vercel.app과 www는 영구 리다이렉트)

## 구조

```
public/index.html      페이지 전체 (CSS·JS 포함)
public/portrait.*.jpg  대표 사진 (병원 의료진 프로필 사진, 파일명에 콘텐츠 해시)
public/press/          기사 인용 사진 (뉴스1·데일리벳, 출처 표기 필수)
public/yt/             유튜브 썸네일 (수의사 이태호 채널 출연분)
data/papers.json       논문 서지 데이터 (PubMed + ORCID + Crossref 대조)
tools/build_papers.py  papers.json → index.html 의 PAPERS:LIST 블록 재생성
```

## 갱신 방법

- 논문 추가: `data/papers.json`에 항목 추가 → `python3 tools/build_papers.py` → 커밋.
  `role`은 `first`(제1저자) / `last`(마지막 저자=교신저자 표기) / `co`.
- 언론 보도: `index.html`의 `PRESS:LIST:START ~ END` 블록에 최신순으로 항목 추가.
- 강의·학회: `#lectures` 섹션의 연도별 목록. 예정 항목은 `<span class="tag soon">예정</span>`을 붙이고, 지난 뒤 태그를 뗀다.
- 상단 수치(논문 80편 이상, 발표 60건 이상, 강연 40건 이상)는 2026년 6월 병원 제출 프로필 기준. 근거가 바뀌면 `facts-note`의 기준 시점도 함께 고친다.

## 출처 메모

- 약력: 2026년 6월 병원 제출 프로필(`26년수의사프로필/송우진.docx`), 병원 의료진 소개 페이지, 베토퀴놀 웨비나 포스터(학위 연도)
- 한국수의내과전문의 제1회(2022) 합격: 데일리벳 2025-11-07 기사
- 논문 수치(SCIE 56 · Scopus 19 · KCI 8): 병원 의료진 소개 페이지
- 인터뷰 인용: 뉴스1 2026-05-05, 데일리개원 2022-11-25
- 사진: 병원 프로필(자체), 뉴스1(ⓒ 한송아 기자), 데일리벳 — 인용 시 출처 표기 유지
