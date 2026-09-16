# my-project

Claude Code のベストプラクティスを試すためのハンズオン用プロジェクト。シンプルなTODO管理CLIを題材にしています。

## セットアップ

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 使い方

```bash
python cli.py add "牛乳を買う"
python cli.py list
python cli.py done 1
python cli.py remove 1
```

## テスト

```bash
pytest
```
