"""
test_calc.py - calc.py 가 약속대로 동작하는지 확인하는 테스트

이 파일이 보여 주는 개념
  1) 테스트는 "이 값을 넣으면 이 값이 나와야 한다"를 코드로 적은 약속이다.
  2) assert 뒤의 식이 참이면 통과, 거짓이면 실패다.
  3) 정상 경우뿐 아니라 잘못된 경우(0으로 나누기)도 약속에 넣는다.
"""

import pytest

from calc import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide():
    assert divide(9, 3) == 3


def test_divide_by_zero_raises_error():
    # 0 으로 나누면 ValueError 가 나와야 한다.
    with pytest.raises(ValueError):
        divide(1, 0)


def test_multiply():
    # 5교시에 AI 가 multiply 를 추가하면 이 테스트가 통과한다.
    assert multiply(4, 5) == 20
