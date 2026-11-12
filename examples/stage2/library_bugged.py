"""
library.py - 도서 대출 목록 (AI 가 만든 초안, 아직 검증 전)

4장에서 이 파일을 프로젝트 폴더의 library.py 로 복사해서 검증합니다.
"""

import json
from pathlib import Path


def add_book(books, title, author):
    """책을 등록한다. 번호는 1, 2, 3 ... 순서대로 붙는다."""
    new_id = max((b["id"] for b in books), default=0) + 1
    book = {"id": new_id, "title": title.strip(), "author": author.strip(),
            "status": "available", "borrower": None}
    books.append(book)
    return book


def list_books(books, status=None):
    """책 목록을 돌려준다. status 를 주면 그 상태의 책만 돌려준다."""
    if status is None:
        return books
    return [b for b in books if b["status"] == status]


def _find(books, book_id):
    """번호로 책을 찾는다. 없으면 ValueError 를 일으킨다."""
    for b in books:
        if b["id"] == book_id:
            return b
    raise ValueError("책을 찾을 수 없습니다.")


def lend_book(books, book_id, borrower):
    """책을 대출한다. 빌리는 사람 이름을 기록한다."""
    book = _find(books, book_id)
    if not borrower.strip():
        raise ValueError("빌리는 사람 이름을 입력하세요.")
    book["status"] = "lent"
    book["borrower"] = borrower.strip()
    return book


def return_book(books, book_id):
    """책을 반납한다."""
    book = _find(books, book_id)
    if book["status"] != "lent":
        raise ValueError("대출 중이 아닌 책입니다.")
    book["status"] = "available"
    return book


def save_books(books, path):
    """책 목록을 JSON 파일로 저장한다."""
    Path(path).write_text(json.dumps(books, ensure_ascii=False, indent=2), encoding="utf-8")


def load_books(path):
    """JSON 파일을 읽는다. 파일이 없으면 빈 목록을 돌려준다."""
    p = Path(path)
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))
