import pytest

import todo


@pytest.fixture
def storage_path(tmp_path):
    return tmp_path / "tasks.json"


def test_add_task_assigns_incrementing_id(storage_path):
    first = todo.add_task("牛乳を買う", storage_path)
    second = todo.add_task("洗濯する", storage_path)

    assert first["id"] == 1
    assert second["id"] == 2
    assert first["done"] is False


def test_list_tasks_returns_added_tasks(storage_path):
    todo.add_task("牛乳を買う", storage_path)
    todo.add_task("洗濯する", storage_path)

    tasks = todo.list_tasks(storage_path)

    assert [task["title"] for task in tasks] == ["牛乳を買う", "洗濯する"]


def test_complete_task_marks_task_done(storage_path):
    task = todo.add_task("牛乳を買う", storage_path)

    updated = todo.complete_task(task["id"], storage_path)

    assert updated["done"] is True


def test_complete_task_raises_for_unknown_id(storage_path):
    with pytest.raises(ValueError):
        todo.complete_task(999, storage_path)


def test_remove_task_deletes_task(storage_path):
    task = todo.add_task("牛乳を買う", storage_path)

    todo.remove_task(task["id"], storage_path)

    assert todo.list_tasks(storage_path) == []


def test_remove_task_raises_for_unknown_id(storage_path):
    with pytest.raises(ValueError):
        todo.remove_task(999, storage_path)
