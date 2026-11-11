---
name: "ComfyArt"
genre: "image-gen"
url: "https://github.com/jtydhr88/ComfyArt"
repo: "jtydhr88/ComfyArt"
license: "MIT"
stars: 504
language: "TypeScript"
created: "2026-10-13"
updated: "2026-11-09"
forks: 87
open_issues: 0
commits_30d: 70
commit_cadence: "daily"
commits_90d: 70
size_kb: 41572
archived: false
flags: ["unverified"]
risk_notes: "一部の生成ワークフローが必要とするモデルやカスタムノードのローカル環境への導入条件は、READMEだけでは全て確認できない。Comfy Cloud APIキーには有料Comfyプランが必要と記載されている。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/bfl_ai/status/2120281089709363685"]
fetched_at: "2026-11-11T06:13:30.781899+00:00"
---

# ComfyArt

## 出来ること

- READMEでは、ComfyUI上で動く無限キャンバス型のデザイン環境として、画像・動画・音声・3Dの生成、画像編集、書き出し、MCP経由のエージェント操作を説明している。これらはREADMEに記載された機能であり、独立した実機検証結果ではない。出典: https://github.com/jtydhr88/ComfyArt

## 目的・背景

- READMEは、ローカルのComfyUIでAIデザインキャンバスを動かし、キャンバス上の作業をエージェントから操作できるプロジェクトとして説明している。出典: https://github.com/jtydhr88/ComfyArt

## 依存関係

- README記載の導入要件はComfyUIと、その環境へのPython requirementsのインストール。PDFアップロード用にpypdfium2、Edit Elements用にrapidocrを挙げている。生成ワークフローはモデルやカスタムノードを利用する。Comfy Cloudを使う場合はCOMFY_API_KEYが必要で、APIキーには有料Comfyプランが必要と記載されている。出典: https://github.com/jtydhr88/ComfyArt

## 実行条件

- READMEでは、リポジトリをComfyUI/custom_nodes/に配置し、ComfyUIの環境でpip install -r requirements.txtを実行してから再起動する手順を案内している。ビルド済みdist/が含まれるため通常の導入にビルドは不要と記載。Comfy Cloud利用時はComfyUI起動前にCOMFY_API_KEYを設定する。出典: https://github.com/jtydhr88/ComfyArt

## 最短手順

- READMEの手順: 1) リポジトリをComfyUI/custom_nodes/に配置し、ComfyUI環境でpip install -r requirements.txtを実行。2) ComfyUIを再起動。3) ComfyUI上部のComfyArtを開く。出典: https://github.com/jtydhr88/ComfyArt

## 変更履歴

- 2026-11-11: 初回登録
