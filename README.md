# Next.js FastAPI, Postgresqlのスターター

Next.js、FastAPI、PostgresqlでWeb開発したい場合に使う。

# バージョン

- frontend
    - Node.js v18.15.0 (Hydrogen)
    - Next.js v13.2.4
    - React v18.2.0
    - TypeScript v5.0.2
- backend
    - Python v3.11.2
    - Poetry v1.4.1
    - FastAPI v^0.94.0
    - Alembic v1.10.2
- database
    - Postgresql v15.2

# 開発方法

### Dockerを起動する

BuildKitを有効にすること。

初めはビルドしてから起動、またはリビルドして起動したい場合。

```shell
docker compose up -d --build --force-recreate
```

次回以降のコマンドはビルドは不要。

```shell
docker compose up -d
```

### 起動を確認する

[backend](http://localhost:8000/health)にアクセスして、status:okのJSONが返ってくれば成功。

[frontend](http://localhost:3000)にアクセスして、ページが表示されれば成功。

### Dockerを終わらせる

```shell
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
