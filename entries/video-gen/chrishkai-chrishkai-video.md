---
name: "ChrisHKAI-Video"
genre: "video-gen"
url: "https://github.com/ChrisHKAI/ChrisHKAI-Video"
repo: "ChrisHKAI/ChrisHKAI-Video"
license: "MIT"
stars: 150
language: "JavaScript"
created: "2026-10-28"
updated: "2026-11-14"
forks: 45
open_issues: 1
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 62331
archived: false
flags: ["unverified"]
risk_notes: "Codexによる完全な映像制作の品質はREADME時点で未検証。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/ganfanren_ai/status/2118963364907094088"]
fetched_at: "2026-11-15T10:09:39.337687+00:00"
---

# ChrisHKAI-Video

## 出来ること

- XのプロフィールURLを入力し、プロフィール画像や投稿、数値を題材にした短編映像を制作する。READMEは、画像を3Dトイ化し、投稿を壁のように配置し、数値を映像内に表現する例を説明している。映像はBlenderで描画し、音声はPythonで作成する。

## 目的・背景

- 作者がコーディングエージェントとコードで制作した映像から抽出したスキル。READMEによるとClaudeで制作・映像検証されており、Codex向け設定もある。

## 依存関係

- README記載の制作要件はBlender、Node、Python、ffmpeg、Chrome。Codexのスキル導入スクリプト自体はPython 3.9以上を必要とし、Blenderなどの描画依存関係は導入しない。

## 実行条件

- Codexはシェル実行、画像表示、ブラウザーまたは検索へのアクセスが可能なローカルセッションで使用する。描画要件は別途必要。Codexでの完全な映像制作は未検証とREADMEに記載されている。

## 最短手順

- README記載の手順でリポジトリを取得し、`python3 scripts/install-codex.py`を実行してスキルを導入する。Codexを別の書き込み可能な映像作業フォルダーで開き、`$creator-toy-intro Make a self-intro film for https://x.com/yourhandle`を入力する。

## 変更履歴

- 2026-11-15: 初回登録
