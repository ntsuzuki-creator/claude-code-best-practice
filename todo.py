"""TODOタスク管理のコアロジック。JSONファイルへの永続化とタスク操作を行う。"""

import json
from pathlib import Path

DEFAULT_STORAGE_PATH = Path("tasks.json")
PRIORITIES = ["high", "medium", "low"]
DEFAULT_PRIORITY = "medium"


def load_tasks(storage_path=DEFAULT_STORAGE_PATH):
    storage_path = Path(storage_path)
    if not storage_path.exists():
        return []
    with storage_path.open(encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, storage_path=DEFAULT_STORAGE_PATH):
    storage_path = Path(storage_path)
    with storage_path.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(title, storage_path=DEFAULT_STORAGE_PATH, priority=DEFAULT_PRIORITY):
    tasks = load_tasks(storage_path)
    next_id = max((task["id"] for task in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "done": False, "priority": priority}
    tasks.append(task)
    save_tasks(tasks, storage_path)
    return task


def list_tasks(storage_path=DEFAULT_STORAGE_PATH):
    return load_tasks(storage_path)


def complete_task(task_id, storage_path=DEFAULT_STORAGE_PATH):
    tasks = load_tasks(storage_path)
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks, storage_path)
            return task
    raise ValueError(f"task id {task_id} not found")


def remove_task(task_id, storage_path=DEFAULT_STORAGE_PATH):
    tasks = load_tasks(storage_path)
    remaining = [task for task in tasks if task["id"] != task_id]
    if len(remaining) == len(tasks):
        raise ValueError(f"task id {task_id} not found")
    save_tasks(remaining, storage_path)


def count_done(storage_path=DEFAULT_STORAGE_PATH):
    tasks = load_tasks(storage_path)
    return sum(1 for task in tasks if task["done"])


def count_pending(storage_path=DEFAULT_STORAGE_PATH):
    tasks = load_tasks(storage_path)
    return sum(1 for task in tasks if not task["done"])
