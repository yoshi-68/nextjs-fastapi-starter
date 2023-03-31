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
RUN apt-get -q update && \
    apt-get -yq install --no-install-recommends tzdata locales && \
    ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 新しいユーザーとグループを追加
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
RUN mkdir -p /home/appuser && chown -R appuser:appgroup /home/appuser

# アプリケーションをコピー
WORKDIR /app
COPY frontend/ /app/
RUN chown -R appuser:appgroup /app

# Node.jsのパッケージをインストール
RUN npm update -g npm -s && \
    npm ci -s

USER appuser

ENTRYPOINT ["npm"]
CMD ["run", "dev"]
