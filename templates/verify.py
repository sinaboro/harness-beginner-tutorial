"""
verify.py - 검증 스크립트 (하네스의 "검증" 담당)

사용법 (프로젝트 폴더에서):  python verify.py
  - 테스트가 모두 통과하면 "검증 통과"를 출력하고 끝난다.
  - 하나라도 실패하면 "검증 실패"를 출력하고, 종료 코드 1 로 끝난다.

커밋 직전에 이 파일이 자동으로 실행된다(.githooks/pre-commit).
실패하면 커밋이 취소된다. 그래서 "테스트를 통과한 것만 저장된다"는 규칙이 사람의 기억이 아니라 도구로 지켜진다.
"""

import subprocess
import sys

# 파이썬으로 pytest 를 실행한다. 결과(통과/실패)는 pytest 가 정한다.
result = subprocess.run([sys.executable, "-m", "pytest", "-q"])

if result.returncode != 0:
    print("")
    print("검증 실패: 위의 오류를 고친 뒤 다시 실행하세요.")
    sys.exit(1)  # 0 이 아닌 값으로 끝나야 커밋이 취소된다

print("")
print("검증 통과: 이제 저장(commit)해도 됩니다.")
