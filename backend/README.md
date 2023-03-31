# 開発方法

## tips

tips: プロジェクトディレクトリ内に仮想環境を作成する

```shell
poetry config virtualenvs.in-project true
```

## インストール

poetry.lockからパッケージのインストールする

```shell
poetry install
```

## コードの整形など

フォーマッター、型チェック、コードチェッカーを行う

```shell
isort . && black . && mypy . && flake8 .
```

## 自動テスト

```shell
pytest
```

## 起動

```shell
uvicorn main:app --reload
```

[health](http://127.0.0.1:8000/health) が正常に表示されること。
