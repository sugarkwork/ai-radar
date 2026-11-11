---
name: "Y2A-Auto"
genre: "other"
url: "https://github.com/fqscfqj/Y2A-Auto"
repo: "fqscfqj/Y2A-Auto"
flags: ["unverified"]
risk_notes: "The supplied README does not establish what permissions or platform terms apply to reposting videos; verify these before use."
stars: 4749
forks: 797
open_issues: 13
size_kb: 54396
language: "Python"
created: "2025-05-10"
updated: "2026-10-28"
archived: false
license: "GPL-3.0"
commits_30d: 4
commits_90d: 37
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/superfang119/status/2118323026576253399"]
fetched_at: "2026-11-11T19:04:09.729471+00:00"
---

# Y2A-Auto

## 出来ること

- READMEによると、YouTube動画のダウンロード、音声認識による字幕生成、字幕翻訳・質疑・焼き込み、メタデータ生成、内容审核、AcFun／bilibiliへのアップロードを自動化する。Web管理画面でタスク確認や手動审核を行えるほか、YouTubeチャンネル・キーワード監視、通知、CookieCloud連携、CPU・各社GPUの動画エンコードに対応すると説明されている。

## 目的・背景

- YouTube動画をAcFun／bilibiliへ移す一連の処理をまとめて自動化するツールとして説明されている。

## 依存関係

- Docker利用時はREADMEでDocker対応と説明されている。本地运行ではPython 3.11+、FFmpeg、yt-dlpが前提。字幕処理などのAI機能には設定に応じてOpenAI互換API等の設定が必要。YouTubeダウンロードではYouTube Cookieが必要で、投稿先のAcFun／bilibili認証情報も用意する。

## 実行条件

- Dockerまたはローカルで実行できる。ローカル実行はPython 3.11+、FFmpeg、yt-dlpが必要。READMEではFFmpeg 5.1以上を要求し、古い版ではソフトウェアエンコードの字幕焼き込みが失敗すると説明されている。YouTube監視機能にはYouTube Data API v3キーが必要。

## 最短手順

- README記載のDocker手順では、必要なYouTube Cookieと投稿先アカウントのCookieを準備し、リポジトリの compose 設定で `docker compose up -d` を実行する。起動後にWeb画面を開き、ログイン保護、投稿先アカウント、YouTube Cookieなどを設定する。READMEは初期設定でログイン保護が無効と記載している。

## 変更履歴

- 2026-11-11: 初回登録
