# syntax = docker/dockerfile:1.5

FROM python:3.11.2-slim-buster

# メタデータを設定
LABEL maintainer="yoshi_f" \
      version="1.0" \
      description="Webアプリケーションのバックエンド。FastAPIを使用。"

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
COPY backend/pyproject.toml backend/poetry.lock /app/

# Pythonのパッケージをインストール
RUN --mount=type=cache,target=/root/.cache/pypoetry \
    pip install --no-cache-dir --upgrade pip==23.0.1 poetry==1.4.1 -q && \
    poetry config virtualenvs.create false && \
    poetry install

COPY backend/ /app/

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
