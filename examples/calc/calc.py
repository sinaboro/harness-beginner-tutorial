"""
calc.py - 아주 작은 계산 함수 모음 (1단계 연습용)

이 파일이 보여 주는 개념
  1) 함수는 "입력 → 계산 → 결과"에 이름을 붙인 것이다.
  2) 잘못된 입력(0으로 나누기)은 조용히 틀린 답을 내지 않고 오류로 알린다.

5교시 연습: multiply(곱하기) 함수가 아직 없다. 테스트를 먼저 실행하면 실패한다(빨강).
          AI 에게 multiply 를 추가하게 해서 테스트를 통과시킨다(초록).
"""


def add(a: float, b: float) -> float:
    """두 수를 더한다."""
    return a + b


def subtract(a: float, b: float) -> float:
    """a 에서 b 를 뺀다."""
    return a - b


def divide(a: float, b: float) -> float:
    """a 를 b 로 나눈다. b 가 0 이면 ValueError 오류를 일으킨다."""
    # 0 으로 나누면 계산할 수 없으므로 미리 막는다. 이 검사가 없으면 프로그램이 멈춘다.
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
