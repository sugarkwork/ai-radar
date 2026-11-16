---
name: "/brag"
genre: "video-gen"
url: "https://github.com/latent-spaces/brag"
repo: "latent-spaces/brag"
license: "MIT"
stars: 21613
language: "Python"
created: "2026-06-16"
updated: "2026-11-15"
forks: 1680
open_issues: 8
commits_30d: 40
commit_cadence: "daily"
commits_90d: 58
size_kb: 50282
archived: false
flags: []
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/ganfanren_ai/status/2119002572552052995"]
fetched_at: "2026-11-16T00:23:18.274181+00:00"
---

# /brag

## 出来ること

- プロジェクトの内容をもとに、音楽・モーション・共有用コピーを含む短いローンチ動画を作るエージェントスキル。READMEでは、通常版はHyperframesに動画の構築・タイミング調整・レンダリングを任せ、対応モデル向けのbrag-slimはHyperframesや同梱素材を使わない構成と説明している。出力先は `brag-output/`。

## 目的・背景

- 「You built it. Now brag.」を掲げ、作成したプロジェクトを共有可能なローンチ動画にする。READMEには、リポジトリのローンチサイトにあるループ動画もこのスキルで作成したとの作者の説明がある。

## 依存関係

- 通常版の要件として、Agent Skills対応エージェント、Node.js 22以上、PATH上のFFmpeg、Hyperframes CLI（`npx hyperframes`）が記載されている。音声ナレーションを有効にした場合はHyperframes経由でKokoroを使う。

## 実行条件

- エージェントがAgent Skillsに対応していること。通常版ではNode.js 22以上、FFmpegがPATH上にあり、Hyperframes CLIを利用できること。READMEはHyperframesの確認に `npx hyperframes doctor` を案内している。

## 最短手順

- Codexでは `codex plugin marketplace add latent-spaces/brag` の後に `codex plugin add brag@brag`。インストール後、プロジェクトのディレクトリでエージェントに `let's /brag` と依頼する。README記載の手順であり、ここでは実行確認していない。

## 変更履歴

- 2026-11-16: 初回登録
