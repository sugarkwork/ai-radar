---
name: "LocalAI"
genre: "model-serving"
url: "https://github.com/mudler/LocalAI"
repo: "mudler/LocalAI"
license: "MIT"
stars: 50388
language: "Go"
created: "2023-03-18"
updated: "2026-11-16"
forks: 4610
open_issues: 186
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 233224
archived: false
flags: ["unverified"]
risk_notes: "チーム共有やアドオンなどREADMEでdevelopment buildsとされる機能は、通常の最新リリースでは利用できるか不明。README記載の版情報は取得時点の独立確認ではない。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/naka_1717/status/2119034856676159987"]
fetched_at: "2026-11-16T05:28:23.644229+00:00"
---

# LocalAI

## 出来ること

- ローカルのハードウェア上で、テキスト、視覚、音声、画像、動画、埋め込みなどのモデルをAPI経由で提供する。READMEはOpenAI、Anthropic、ElevenLabs形式のAPIと80超のバックエンドを記載している。チャット、ツール・MCPを使うエージェント、ファイルやコレクション、音声入出力、画像生成、分散モードなども説明されている。

## 目的・背景

- READMEでは「自分のAIを自分のハードウェアで」動かすプロジェクトとして紹介されている。サーバー、モデル、ファイルを利用者自身のマシンに置く構成を掲げる。

## 依存関係

- バックエンドはモデルに応じて個別のイメージとして取得される。分散モードはPostgreSQLとNATSを使用するとREADMEに記載されている。必要なバックエンドや構成要件は利用するモデル、機能、ハードウェアによって異なる。

## 実行条件

- READMEはLinuxおよびApple Silicon搭載macOS向けのインストールスクリプト、Docker・Podman等のコンテナ、Linux向けAppImageとmacOS向けDMGのデスクトップアプリを案内している。GPU利用時はNVIDIA、AMD、Intel、Apple Silicon、Vulkan、Jetson向けの構成例がある。

## 最短手順

- コンテナの場合、READMEの例は `docker run -ti --name local-ai -p 8080:8080 localai/localai:latest`。その後、モデルギャラリーの例として `local-ai run qwen3-4b` を示している。READMEにはスクリプト経由の導入例もある。

## 変更履歴

- 2026-11-16: 初回登録
