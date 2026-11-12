"""
test_lending.py - 대출과 반납 약속 (2단계 3장, 1차 버전)

이 파일이 보여 주는 개념
  1) 상태 규칙: 대출 중인 책은 다시 대출할 수 없고, 대출하지 않은 책은 반납할 수 없다.
  2) 정상 경우와 잘못된 경우를 모두 약속한다.
  3) 4교시에 "반납하면 빌린 사람 이름을 지운다"는 약속이 빠져 있다는 것을 발견하게 된다.
"""

import pytest

from library import add_book, lend_book, return_book


def make_books():
    """테스트마다 책이 한 권 있는 목록을 만든다."""
    books = []
    add_book(books, "데미안", "헤세")
    return books


def test_lend_book_marks_lent():
    books = make_books()
    book = lend_book(books, 1, "철수")
    assert book == {"id": 1, "title": "데미안", "author": "헤세", "status": "lent", "borrower": "철수"}


def test_lend_lent_book_raises():
    # 이미 대출 중인 책은 다시 빌릴 수 없다.
    books = make_books()
    lend_book(books, 1, "철수")
    with pytest.raises(ValueError):
        lend_book(books, 1, "영희")


def test_lend_missing_book_raises():
    with pytest.raises(ValueError):
        lend_book(make_books(), 99, "철수")


def test_lend_blank_borrower_raises():
    with pytest.raises(ValueError):
        lend_book(make_books(), 1, "   ")


def test_return_book_marks_available():
    books = make_books()
    lend_book(books, 1, "철수")
    book = return_book(books, 1)
    assert book["status"] == "available"


def test_return_available_book_raises():
    # 대출하지 않은 책은 반납할 수 없다.
    with pytest.raises(ValueError):
        return_book(make_books(), 1)


def test_return_missing_book_raises():
    with pytest.raises(ValueError):
        return_book(make_books(), 99)
