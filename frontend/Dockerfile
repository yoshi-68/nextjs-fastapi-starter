# syntax = docker/dockerfile:1.5

FROM node:hydrogen-buster-slim

# メタデータを設定
LABEL maintainer="yoshi_f" \
      version="1.0" \
      description="Webアプリケーションのフロントエンド。Next.jsとTypeScriptを使用。"

# 環境変数の設定
ENV TZ=Asia/Tokyo
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP.UTF-8
ENV LC_ALL=ja_JP.UTF-8
ENV TERM=xterm-256color

# OSのパッケージをインストール
RUN apt update && \
    apt install -y --no-install-recommends tzdata locales && \
    ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# アプリケーションをコピー
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json /app/

# Node.jsのパッケージをインストール
RUN --mount=type=cache,target=/root/.npm npm \
    update -g npm -s && \
    npm ci

COPY frontend/ /app/

ENTRYPOINT ["npm"]
CMD ["run", "dev"]
