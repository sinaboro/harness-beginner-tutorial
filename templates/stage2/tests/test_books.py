"""
test_books.py - 책 등록, 목록, 저장 약속 (2단계 2장)

이 파일이 보여 주는 개념
  1) 기준(테스트)은 사람이 정한다. AI 는 이 파일을 고칠 수 없다.
  2) 저장 테스트는 임시 폴더(tmp_path)에만 파일을 쓴다. 내 진짜 파일을 건드리지 않는다.
"""

import pytest

from library import add_book, list_books, load_books, save_books


def test_add_book_creates_available_book():
    books = []
    book = add_book(books, "데미안", "헤세")
    assert book == {"id": 1, "title": "데미안", "author": "헤세", "status": "available", "borrower": None}
    assert books == [book]


def test_add_book_numbers_go_up():
    books = []
    add_book(books, "첫째", "가")
    second = add_book(books, "둘째", "나")
    assert second["id"] == 2


def test_add_book_rejects_blank_title():
    # 공백만 있는 제목은 받지 않는다.
    with pytest.raises(ValueError):
        add_book([], "   ", "헤세")


def test_list_books_filters_by_status():
    books = []
    add_book(books, "데미안", "헤세")
    assert list_books(books) == books
    assert list_books(books, "available") == books
    assert list_books(books, "lent") == []


def test_save_and_load_roundtrip(tmp_path):
    path = tmp_path / "books.json"  # 임시 폴더 안의 파일만 쓴다
    books = []
    add_book(books, "데미안", "헤세")
    save_books(books, path)
    assert load_books(path) == books


def test_load_missing_file_returns_empty_list(tmp_path):
    # 파일이 아직 없으면 빈 목록을 돌려준다. 오류를 내지 않는다.
    assert load_books(tmp_path / "없는파일.json") == []
