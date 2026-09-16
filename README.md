# my-project

Claude Code のベストプラクティスを試すためのハンズオン用プロジェクト。シンプルなTODO管理CLIを題材にしています。

## セットアップ

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 使い方

新しいタスクを追加したいとき:

```bash
python cli.py add "牛乳を買う"
```

優先度を指定してタスクを追加したいとき（省略時は medium）:

```bash
python cli.py add "資料を提出する" --priority high
```

登録されているタスクを一覧で確認したいとき:

```bash
python cli.py list
```

タスクが完了したときに、完了済みとしてマークしたいとき:

```bash
python cli.py done 1
```

不要になったタスクを削除したいとき:

```bash
python cli.py remove 1
```

完了済みタスクの件数だけを知りたいとき（進捗確認など）:

```bash
python cli.py count-done
```

未完了タスクの件数だけを知りたいとき（残タスクの把握など）:

```bash
python cli.py count-pending
```

## テスト

```bash
pytest
```
