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


def test_add_task_defaults_to_medium_priority(storage_path):
    task = todo.add_task("牛乳を買う", storage_path)

    assert task["priority"] == "medium"


def test_add_task_accepts_high_priority(storage_path):
    task = todo.add_task("牛乳を買う", storage_path, priority="high")

    assert task["priority"] == "high"


def test_add_task_accepts_medium_priority(storage_path):
    task = todo.add_task("牛乳を買う", storage_path, priority="medium")

    assert task["priority"] == "medium"


def test_add_task_accepts_low_priority(storage_path):
    task = todo.add_task("牛乳を買う", storage_path, priority="low")

    assert task["priority"] == "low"


def test_list_tasks_returns_added_tasks(storage_path):
    todo.add_task("牛乳を買う", storage_path)
    todo.add_task("洗濯する", storage_path)

    tasks = todo.list_tasks(storage_path)

    assert [task["title"] for task in tasks] == ["牛乳を買う", "洗濯する"]


def test_list_tasks_exposes_priority(storage_path):
    todo.add_task("牛乳を買う", storage_path, priority="high")
    todo.add_task("洗濯する", storage_path, priority="low")

    tasks = todo.list_tasks(storage_path)

    assert [task["priority"] for task in tasks] == ["high", "low"]


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


def test_count_done_counts_only_completed_tasks(storage_path):
    first = todo.add_task("牛乳を買う", storage_path)
    todo.add_task("洗濯する", storage_path)
    todo.complete_task(first["id"], storage_path)

    assert todo.count_done(storage_path) == 1


def test_count_done_returns_zero_when_no_tasks_done(storage_path):
    assert todo.count_done(storage_path) == 0

    todo.add_task("牛乳を買う", storage_path)

    assert todo.count_done(storage_path) == 0


def test_count_pending_counts_only_incomplete_tasks(storage_path):
    first = todo.add_task("牛乳を買う", storage_path)
    todo.add_task("洗濯する", storage_path)
    todo.complete_task(first["id"], storage_path)

    assert todo.count_pending(storage_path) == 1


def test_count_pending_returns_zero_when_no_tasks(storage_path):
    assert todo.count_pending(storage_path) == 0
