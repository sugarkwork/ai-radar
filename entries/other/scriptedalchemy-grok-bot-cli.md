---
repo: "ScriptedAlchemy/grok-bot-cli"
name: "grok-bot-cli"
genre: "other"
url: "https://github.com/ScriptedAlchemy/grok-bot-cli"
stars: 181
forks: 37
open_issues: 8
size_kb: 26027
language: "JavaScript"
created: "2026-08-19"
updated: "2026-11-04"
archived: false
license: "MIT"
commits_30d: 31
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "README に基づく確認。CLI・MCP の実機動作、OS 別の認証互換性、最新 GitHub リリース、Grok Bot 側の料金・プラン条件は未確認。90 日コミット数の 100 は計測上限で、100 件以上を表す。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117591176048005131"]
fetched_at: "2026-11-10T09:45:32+00:00"
---

# grok-bot-cli — Grok Bot のボット・グループ操作とメッセージ連携

## 出来ること

- ボットとグループの作成・更新・削除、メッセージ送信、スレッド取得を CLI で行う。
- スレッドの取得結果を JSON で受け取り、カーソルを使って直前の取得以降の差分を確認できる。

## 目的・背景

- Grok Bot の操作を端末や AI エージェントの作業手順に組み込むためのツール。README には作成・グループ化・送信・削除のスモークテストが示されている。

## 依存関係

- Node.js 22.19.0 以上と macOS・Linux・Windows 向け Grok Bot デスクトップアプリ。Linux でセッションがシステムのキーリングに保存される構成では libsecret-tools の secret-tool を使う。

## 実行条件

- 標準の CLI 利用ではデスクトップアプリでサインイン済みのセッションを使う。MCP から同じセッションを使う場合は、ゲートウェイへの HTTPS 接続とセッションファイルの読み取りが必要。
- CLI のコードは MIT。Grok Bot 側の料金・プラン条件は未確認。

## 最短手順

- Grok Bot デスクトップアプリにサインイン済みの環境で npm install --global grok-bot-cli を実行し、gbot bots list で対象を確認する。
- AI から使う場合は、Codex・Claude Code・Cursor の対応ホストにリポジトリの Agent Bundle を導入して grok-bot MCP を有効にする。AI に gbot_send で既存のボットへ依頼させ、gbot_thread で返信を取得させる。

## 変更履歴

- 2026-11-10: 初回登録
