"""TODO CLI エントリーポイント。argparseでコマンドを解釈しtodo.pyに委譲する。"""

import argparse

import todo


def main():
    parser = argparse.ArgumentParser(description="シンプルなTODO管理CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="タスクを追加する")
    add_parser.add_argument("title", help="タスクの内容")
    add_parser.add_argument(
        "--priority",
        choices=todo.PRIORITIES,
        default=todo.DEFAULT_PRIORITY,
        help="優先度 (high/medium/low, デフォルト: medium)",
    )

    subparsers.add_parser("list", help="タスク一覧を表示する")

    done_parser = subparsers.add_parser("done", help="タスクを完了にする")
    done_parser.add_argument("task_id", type=int, help="タスクID")

    remove_parser = subparsers.add_parser("remove", help="タスクを削除する")
    remove_parser.add_argument("task_id", type=int, help="タスクID")

    subparsers.add_parser("count-done", help="完了済みタスクの数を表示する")

    subparsers.add_parser("count-pending", help="未完了タスクの数を表示する")

    args = parser.parse_args()

    if args.command == "add":
        task = todo.add_task(args.title, priority=args.priority)
        print(f"追加しました: [{task['id']}] {task['title']} (優先度: {task['priority']})")
    elif args.command == "list":
        tasks = todo.list_tasks()
        if not tasks:
            print("タスクはありません")
        for task in tasks:
            status = "x" if task["done"] else " "
            priority = task.get("priority", todo.DEFAULT_PRIORITY)
            print(f"[{status}] {task['id']}: {task['title']} (優先度: {priority})")
    elif args.command == "done":
        task = todo.complete_task(args.task_id)
        print(f"完了にしました: [{task['id']}] {task['title']}")
    elif args.command == "remove":
        todo.remove_task(args.task_id)
        print(f"削除しました: {args.task_id}")
    elif args.command == "count-done":
        print(todo.count_done())
    elif args.command == "count-pending":
        print(todo.count_pending())


if __name__ == "__main__":
    main()
