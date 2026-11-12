# 작업 지시서: 도서 대출 목록 완성 (2단계 7장)

## 1. 목표
`REQUIREMENTS.md` 의 R1~R5 를 모두 만족하는 `library.py` 를 완성한다. (R6 명령줄 기능은 선택)

## 2. 요구사항
`REQUIREMENTS.md` 의 **R1, R2, R3, R4, R5**. 대출 기간 `loan_days` 는 `CHANGE_요청서.md` 로 승인된 변경이다.

## 3. 범위
- 고쳐도 되는 파일: `library.py` 하나뿐이다.
- 고치면 안 되는 파일: `tests/` 폴더 전체, `verify.py`, `AGENTS.md`, `opencode.jsonc`, `REQUIREMENTS.md`

## 4. 하지 말 것
- 연체 계산, 날짜 계산, 책 삭제, 책 수정을 만들지 않는다.
- 웹 화면, 데이터베이스, 외부 패키지를 쓰지 않는다.
- 테스트 파일의 기대값을 바꾸지 않는다.

## 5. 완료 조건
- [ ] `python verify.py` 가 "검증 통과"로 끝난다.
- [ ] `tests/` 폴더는 템플릿 원본과 같다. (`Compare-Object` 로 확인)
- [ ] 대출 중인 책을 반납하면 `borrower` 가 `None` 이 되는지 내가 직접 확인했다.
- [ ] 모든 함수에 한국어 주석이 있다.

## 6. 진행 방법
`AGENTS.md` 의 작업 순서를 따른다. 먼저 계획을 말하고, 내가 "진행"이라고 하면 구현한다.
끝나면 `AGENTS.md` 의 보고 형식으로 보고한다.
