---
repo: Panniantong/Agent-Reach
name: Agent-Reach
genre: agent-framework
url: https://github.com/Panniantong/Agent-Reach
license: MIT
stars: 108885
language: Python
created: 2026-02-24
updated: 2026-11-04
added: 2026-11-05
first_seen: 2026-11-04
source_post: https://x.com/thegreatest_sv/status/2117687388214272339
sources: []
flags: []
risk_notes: "ログイン必須プラットフォームの利用は各サイトの規約に従う。初回利用時にChromeの該当サイトのログインを専用ブラウザへ複製する仕様のため、小号（サブアカウント）の利用が推奨されている。"
forks: 9726
open_issues: 276
commits_30d: 98
size_kb: 3209
archived: false
commits_90d: 100
commit_cadence: daily
fetched_at: "2026-11-05T04:39:45Z"
last_release: v1.6.1
last_release_at: 2026-11-01
---

# Agent Reach

## 出来ること

- CLIエージェント（Claude Code、Codex、Hermes Agent、OpenClaw など）から**ログイン壁の向こう側**へ届かせるためのツール群。チャネル単位のコマンドで、検索・読み取り・字幕取得などを行う。
  ```bash
  agent-reach channels                    # 使えるチャネルと機能の一覧
  agent-reach bilibili search "大模型"     # agent-reach <チャネル> <動作> [引数]
  agent-reach read https://www.v2ex.com/t/123   # URLからチャネルを自動判定
  ```
- 既定で使えるチャネル: bilibili（検索・動画情報・人気・字幕／字幕はログイン要）、v2ex（人気・ノード・投稿と返信・ユーザー）、github（リポジトリ検索・README・issue/PRとコメント）、youtube（動画情報・検索・字幕・音声の文字起こし／Groq または OpenAI のキーが必要）、web（検索・読み取りのフォールバック）。
- 任意チャネル: xiaohongshu（ログイン）、xueqiu（行情はログイン不要、人気投稿は要ログイン）、boss（求人・JD、ログイン）、xiaoyuzhou（ポッドキャスト文字起こし、Groq キー）、linkedin（公開求人はログイン不要、サイト内検索は要ログイン）、reddit（ログイン）。
- 実験枠: twitter、facebook、instagram（いずれもログイン）。
- 動画・ポッドキャストの音声を文字起こしできるため、字幕のないYouTubeや小宇宙（Xiaoyuzhou）の内容もテキストで扱える。

## 目的・背景

汎用のWeb検索では届きにくい「ログイン後」「動画の中」「中国語プラットフォーム」「構造化データ」を、エージェントが1コマンドで扱えるようにするのが目的。各プラットフォーム向けのツールを利用者側で個別に設定・検証する代わりに、動作確認済みの構成を配布している。GitHub Trending 1位（Trendshift）を取得したとREADMEに記載。

## 依存関係

- Python 3.10 以上。導入には `uv` を使う（無ければインストーラが先に入れる）。
- チャネルごとに追加要件がある: 字幕・文字起こしはログインまたは Groq/OpenAI のAPIキー、ブラウザ系チャネルは専用ブラウザ。
- **PyPI の `agent-reach` は別プロジェクト**。README に「PyPI から入れず、install.md の GitHub 手順だけを使う」と明記されている。

## 実行条件

- ログインが要るサイトは、Agent Reach 専用のブラウザをバックグラウンドで動かす。初回にChromeの該当サイトのログイン状態を複製する（パスワードストアは読まない、元ブラウザは変更しない）。複製されるのは通常メインアカウントのため、小号への切り替えが推奨されている。
- 各プラットフォームの規約・レート制限に従う。アカウント停止リスクは利用者側。
- 導入・更新はエージェントに install.md のURLを渡す方式が正式:
  `https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md`

## 最短手順

```bash
# エージェントにこのURLを渡して導入させる（uv ベース、管理者権限不要）
# https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md

agent-reach channels
agent-reach github search "agent framework"
agent-reach read https://www.v2ex.com/t/123
```

## 変更履歴

- 2026-11-05: 初回登録（★108,882 / pushed 2026-11-04 / MIT / v1.6.1）
