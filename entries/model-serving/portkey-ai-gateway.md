---
name: "Portkey AI Gateway"
genre: "model-serving"
url: "https://github.com/Portkey-AI/gateway"
repo: "Portkey-AI/gateway"
license: "MIT"
stars: 13394
language: "TypeScript"
created: "2023-08-23"
updated: "2026-05-25"
forks: 1383
open_issues: 344
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 67695
archived: false
flags: ["unverified"]
risk_notes: "READMEは「250+ LLM」と「1600+ language, vision, audio, and image models」の両方を記載しており、対象数の数え方は確認できない。README記載の機能・性能値は独立検証していない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:17:43.944784+00:00"
---

# Portkey AI Gateway

## 出来ること

- READMEによると、複数のLLMを単一のAPIで利用するゲートウェイ。自動リトライ、フォールバック、ロードバランシング、条件付きルーティング、ガードレール、マルチモーダル機能を掲げ、MCPサーバーの管理機能も説明している。機能や性能の独立検証はしていない。

## 目的・背景

- 言語・視覚・音声・画像モデルへの接続を統一し、AIアプリケーションのルーティングや信頼性設定をまとめることを目的とする。

## 依存関係

- READMEのローカル起動例ではNode.jsとnpmが必要。Pythonの呼び出し例ではportkey-aiクライアントを使う。

## 実行条件

- README記載の最短起動例は `npx @portkey-ai/gateway`。モデルへのリクエストにはプロバイダーのAPIキーが必要。

## 最短手順

- 1. Node.jsとnpmを用意し、`npx @portkey-ai/gateway` でゲートウェイを起動する。2. Python例では `portkey-ai` をインストールし、`Portkey` クライアントにプロバイダーとAPIキーを設定して、`client.chat.completions.create(...)` を呼び出す。

## 変更履歴

- 2026-11-22: 初回登録
