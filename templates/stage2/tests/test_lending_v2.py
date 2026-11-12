"""
test_lending_v2.py - 대출과 반납 약속 (2단계 5장, 2차 버전: 대출 기간 추가)

5장 요구사항 변경: "대출하면 대출 기간 14일(loan_days)이 함께 기록된다.
반납하면 대출 기간 기록은 지운다."

이 파일은 사람이 승인한 뒤에만 test_lending.py 대신 쓴다.
AI 는 이 파일을 고칠 수 없다(권한 설정으로 막는다).
"""

import pytest

from library import add_book, lend_book, return_book


def make_books():
    books = []
    add_book(books, "데미안", "헤세")
    return books


def test_lend_book_marks_lent_with_loan_days():
    books = make_books()
    book = lend_book(books, 1, "철수")
    assert book == {
        "id": 1, "title": "데미안", "author": "헤세",
        "status": "lent", "borrower": "철수", "loan_days": 14,
    }


def test_return_book_removes_loan_days():
    books = make_books()
    lend_book(books, 1, "철수")
    book = return_book(books, 1)
    assert book == {"id": 1, "title": "데미안", "author": "헤세",
                    "status": "available", "borrower": None}


def test_lend_lent_book_raises():
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


def test_return_available_book_raises():
    with pytest.raises(ValueError):
        return_book(make_books(), 1)


def test_return_missing_book_raises():
    with pytest.raises(ValueError):
        return_book(make_books(), 99)
