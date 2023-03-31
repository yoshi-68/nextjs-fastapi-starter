# 開発方法

## バージョン
- frontend
    - Next.js v13.2.4
    - React v18.2.0
    - TypeScript v5.0.2
- backend
    - Python v3.11.2
    - FastAPI v^0.94.0
    - Poetry
- database
    - Postgresql v15.2

### Dockerを起動する

初めはビルドしてから起動、またはリビルドして起動する。

```shell
docker compose up -d --build --force-recreate
```

次回以降のコマンドはビルドは不要。

```shell
docker compose up -d
```

### 起動を確認する
[front](http://localhost:3000)にアクセスして、ページが表示されれば成功。

[health](http://localhost:8000/health)にアクセスして、status:okのJSONが返ってくれば成功。

### Dockerを終わらせる

```shell
「シェル
docker compose down
```

# TIPS

## コンテナにBashで接続する

```shell
# frontendに接続する
docker compose exec frontend bash

# backendに接続する
docker compose exec backend bash
```
