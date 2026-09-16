---
description: タスクを追加し、対応する pytest テストケースの雛形も一緒に作る
argument-hint: <タスクの内容>
---

以下の手順を実行してください。

1. `python cli.py add "$ARGUMENTS"` を実行し、タスクが追加されることを確認する
2. `python cli.py list` で追加結果を確認する
3. `tests/test_todo.py` に、`add_task("$ARGUMENTS")` を呼び出して結果を検証するテストケースを追加する
4. `pytest` を実行し、追加したテストが通ることを確認する
