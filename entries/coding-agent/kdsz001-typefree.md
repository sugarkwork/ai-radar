---
name: "Typefree"
genre: "coding-agent"
url: "https://github.com/kdsz001/typefree"
repo: "kdsz001/typefree"
license: "unknown"
stars: 398
language: "Swift"
created: "2026-06-05"
updated: "2026-10-28"
forks: 70
open_issues: 4
commits_30d: 4
commit_cadence: "weekly"
commits_90d: 47
size_kb: 18535
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/ruyi3699/status/2118639527069696057"]
fetched_at: "2026-11-13T07:19:29.656015+00:00"
---

# Typefree

## 出来ること

- macOS上でショートカットキーまたはマウスを押して話し、離すと音声認識した内容をAIが整理して、カーソル位置に入力する。空白部分でマウスを押してAIに質問する機能、音声翻訳、修正した固有名詞などを次回の認識に反映する機能、履歴のローカル保存・エクスポートがある。README記載の機能説明であり、独立した動作検証ではない。

## 目的・背景

- 話し言葉から不要語を除き、文を整えて句読点や段落を加え、入力先アプリに直接テキストを入力する音声入力アプリ。

## 依存関係

- ソースからのビルドにはmacOS 14以降とXcode 26.3が必要。音声認識には火山引擎、文章整理には通義千問を利用するとREADMEに記載。自分のAPI Keyを使う場合、音声は選択したモデル提供元へ直接送られ、作者のサーバーを経由しない。

## 実行条件

- 無料試用と会員機能は公式署名版でのみ利用可能。ソースからビルドした場合は自分のAPI Keyを設定する。自分のKeyはローカルのキーチェーンに保存される。

## 最短手順

- macOS 14以降とXcode 26.3の環境でリポジトリを取得し、`cd typefree/mac`、`./build.sh`を実行する。成果物は`dist/`に生成される。インストールする場合は`bash scripts/install_app.sh`を実行する。

## 変更履歴

- 2026-11-13: 初回登録
