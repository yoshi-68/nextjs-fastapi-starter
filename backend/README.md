# 開発方法

## tips

tips: プロジェクトディレクトリ内に仮想環境を作成する。

```shell
poetry config virtualenvs.in-project true
```

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

テーブルを追加する。

```shell
alembic revision --autogenerate -m "create users table"
```

マイグレーションスクリプトをデータベースに適用する。

```shell
alembic upgrade head
```
