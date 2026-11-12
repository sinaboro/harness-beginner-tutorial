# 요구사항: 도서 대출 목록 (2단계 7장, 최종 버전)

## 한 문장 요약
책을 등록하고, 대출하고, 반납하고, 목록을 보는 명령줄 프로그램. 책 목록은 JSON 파일에 저장되어 프로그램을 껐다 켜도 남는다.

## 책 한 권의 모양
| 항목 | 설명 |
|---|---|
| `id` | 1, 2, 3 … 순서대로 붙는 번호. 지워지는 기능이 없으므로 항상 새 번호를 쓴다. |
| `title` | 책 제목. 공백만 있으면 안 된다. |
| `author` | 지은이. 비워 둘 수 있다. |
| `status` | `"available"`(대출 가능) 또는 `"lent"`(대출 중). 처음에는 `"available"`. |
| `borrower` | 빌려 간 사람 이름. 대출 중이면 이름이, 대출 가능하면 `None`. |
| `loan_days` | 대출 기간(일). 대출 중일 때만 `14` 가 들어 있다. 반납하면 이 칸을 지운다. |

## 기능 요구사항

### R1. 책 등록
- `add_book(books, title, author)` 을 부르면 새 책을 목록 끝에 넣고, 그 책을 돌려준다.
- 제목이 공백뿐이면 `ValueError` 를 일으킨다.

### R2. 목록 보기
- `list_books(books)` 은 모든 책을 돌려준다.
- `list_books(books, "available")` 또는 `list_books(books, "lent")` 은 그 상태의 책만 돌려준다.

### R3. 대출
- `lend_book(books, book_id, borrower)` 을 부르면 그 책의 `status` 를 `"lent"`, `borrower` 를 빌리는 사람 이름으로 바꾸고, `loan_days` 를 `14` 로 넣는다.
- 없는 번호면 `ValueError`.
- 이미 대출 중인 책이면 `ValueError`.
- 빌리는 사람 이름이 공백뿐이면 `ValueError`.

### R4. 반납
- `return_book(books, book_id)` 을 부르면 그 책의 `status` 를 `"available"` 로 바꾸고, `borrower` 를 `None` 으로, `loan_days` 칸을 지운다.
- 없는 번호면 `ValueError`.
- 대출 중이 아닌 책이면 `ValueError`.

### R5. 파일 저장과 읽기
- `save_books(books, path)` 은 책 목록을 JSON 파일로 저장한다. 한글이 깨지지 않는다.
- `load_books(path)` 은 JSON 파일을 읽어 목록을 돌려준다.
- 파일이 없으면 빈 목록 `[]` 을 돌려준다.

### R6. 명령줄에서 쓰기 (선택)
- `python library.py` 뒤에 `add`, `list`, `lend`, `return` 을 붙여 쓸 수 있다.
- 목록은 번호, 상태, 제목, 지은이, 빌린 사람을 한 줄씩 보여 준다.

## 만들지 않는 것
- 연체 계산, 날짜 계산 (대출 기간은 숫자 14 로만 기록한다)
- 회원 관리, 여러 사람이 동시에 쓰는 기능
- 책 삭제, 책 정보 수정
- 웹 화면, 데이터베이스
