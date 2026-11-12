"""
test_todo.py - 할 일 목록 프로그램(todo.py)이 지켜야 할 약속

6교시에 AI 에이전트는 이 테스트를 통과하도록 todo.py 를 만든다.
이 파일은 사람이 쓴 "기준"이다. AI 는 이 파일을 고칠 수 없다(opencode.jsonc 에서 막는다).

이 파일이 보여 주는 개념
  1) 기준(테스트)은 사람이 정하고, 구현(todo.py)은 AI 가 맡는다.
  2) 정상 경우와 잘못된 경우를 모두 약속한다.
  3) 파일 저장은 임시 폴더(tmp_path)에서만 한다. 내 진짜 파일을 건드리지 않는다.
"""

import pytest

from todo import add_task, complete_task, delete_task, load_tasks, save_tasks


def test_add_task_creates_new_task():
    tasks = []
    task = add_task(tasks, "우유 사기")
    assert task == {"id": 1, "title": "우유 사기", "done": False}
    assert tasks == [task]  # 목록에도 들어가야 한다


def test_add_task_numbers_go_up():
    tasks = []
    add_task(tasks, "첫째")
    second = add_task(tasks, "둘째")
    assert second["id"] == 2


def test_add_task_rejects_blank_title():
    # 공백만 있는 제목은 받지 않는다.
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_complete_task_marks_done():
    tasks = []
    add_task(tasks, "운동하기")
    complete_task(tasks, 1)
    assert tasks[0]["done"] is True


def test_complete_task_not_found():
    with pytest.raises(ValueError):
        complete_task([], 99)


def test_delete_task_removes_it():
    tasks = []
    add_task(tasks, "지울 일")
    delete_task(tasks, 1)
    assert tasks == []


def test_delete_task_not_found():
    with pytest.raises(ValueError):
        delete_task([], 99)


def test_save_and_load_roundtrip(tmp_path):
    path = tmp_path / "tasks.json"  # 임시 폴더 안의 파일만 쓴다
    tasks = []
    add_task(tasks, "저장할 일")
    save_tasks(tasks, path)
    assert load_tasks(path) == tasks


def test_load_missing_file_returns_empty_list(tmp_path):
    # 파일이 아직 없으면 빈 목록을 돌려준다(오류가 나지 않는다).
    assert load_tasks(tmp_path / "없는파일.json") == []
