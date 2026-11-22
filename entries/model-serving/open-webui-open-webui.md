---
name: "Open WebUI"
genre: "model-serving"
url: "https://github.com/open-webui/open-webui"
flags: ["unverified"]
risk_notes: "READMEの説明に基づく機能情報です。実機での動作や効果は独立検証されていません。 GitHub APIでライセンスを確認できていません。"
repo: "open-webui/open-webui"
stars: 158839
forks: 23087
open_issues: 252
size_kb: 568583
language: "Svelte"
created: "2023-10-06"
updated: "2026-11-16"
archived: false
license: "unknown"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/naka_1717/status/2119034856676159987"]
fetched_at: "2026-11-16T21:57:23Z"
last_release: "v0.13.3"
last_release_at: "2026-11-08"
---

# Open WebUI

## 出来ること

- セルフホスト型のAIプラットフォーム。READMEによると、オフラインでの動作、Ollamaのローカルモデルへの接続、OpenAI互換APIを使ったローカル・クラウドモデルへの接続に対応します。

## 目的・背景

- READMEでは「a home for AI」と説明され、拡張可能で使いやすいプラットフォームとして紹介されています。

## 依存関係

- Pythonでの導入にはPython 3.12を使う手順が記載されています。Dockerの`:cuda`または`:ollama`イメージでGPUを利用する場合、Nvidia Container Toolkitが必要とされています。

## 実行条件

- README記載のPython手順は、uvを使う方法またはpipでインストールする方法です。Docker手順ではポート3000を公開し、データ用ボリュームを指定します。GPU利用時はNvidia Container Toolkitが必要です。

## 最短手順

- Python 3.12環境で`pip install open-webui`を実行し、続けて`open-webui serve`を実行します。Dockerを使う場合は、README記載の`docker run`コマンドでコンテナを起動します。

## 変更履歴

- 2026-11-16: 初回登録
