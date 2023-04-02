# 開発方法

## パッケージをインストールする

poetry.lockからパッケージのインストールする。

```shell
poetry install
```

## uvicornで起動する

```shell
uvicorn main:app --reload
```

[health](http://127.0.0.1:8000/health) が正常に表示されること。

## コードの整形等をする

フォーマッター、型チェック、コードチェッカーを行う。

```shell
isort . && black . && mypy . && flake8 .
```

## 自動テストをする

```shell
pytest
```

## データベースのテーブルを追加する

`./migrations/env.py`にインポートして、Alembicにモデルを認識させる。

```python
from models import users  # noqa: F401
```

マイグレーションスクリプトを作成する。

```shell
alembic revision --autogenerate -m "create users table"
```

マイグレーションスクリプトをデータベースに適用する。

```shell
alembic upgrade head
```

## TIPS

プロジェクトディレクトリ内に仮想環境を作成する。

```shell
poetry config virtualenvs.in-project true
```
