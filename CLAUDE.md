# CLAUDE.md

このプロジェクトはシンプルなTODO管理CLIです。Claude Code のベストプラクティスを試すハンズオン用の土台として使います。

## 構成

- `todo.py`: タスクの追加・一覧・完了・削除を行うコアロジックと、`tasks.json` への永続化
- `cli.py`: argparseによるCLIエントリーポイント。`todo.py` に処理を委譲する
- `tests/test_todo.py`: `todo.py` に対するpytestテスト

## セットアップ・実行

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python cli.py add "タスク内容"
python cli.py list
```

## テスト

```bash
pytest
```
