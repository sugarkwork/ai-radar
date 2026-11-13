---
name: "AI SDK"
genre: "agent-framework"
url: "https://github.com/Anil-matcha/ai"
flags: ["unverified"]
risk_notes: "READMEにライセンスの記載がなく、利用条件は確認できません。 GitHub APIでライセンスを確認できていません。"
repo: "Anil-matcha/ai"
stars: 18
forks: 4
open_issues: 0
size_kb: 265635
language: "unknown"
created: "2026-06-17"
updated: "2026-08-06"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/I_am_Aiabir/status/2118731208578478546"]
fetched_at: "2026-11-13T04:09:25.273794+00:00"
---

# AI SDK

## 出来ること

- Node.jsやNext.js、React、Svelte、Vue、AngularなどでAIアプリやエージェントを構築するためのTypeScriptツールキット。複数のモデルプロバイダーを統一APIまたは各プロバイダーのSDK経由で利用でき、テキスト生成、構造化データ生成、ツールを使うエージェント、チャットUIを実装できる。

## 目的・背景

- READMEでは、複数のモデルプロバイダーやUIフレームワークでAI機能を構築するためのprovider-agnosticなツールキットとして説明されている。

## 依存関係

- README記載の基本導入にはNode.js 22以降とnpmまたは別のパッケージマネージャーが必要。基本パッケージは`ai`。利用するプロバイダーに応じて`@ai-sdk/openai`、`@ai-sdk/anthropic`、`@ai-sdk/google`などを追加する。React UIには`@ai-sdk/react`の例がある。

## 実行条件

- モデルプロバイダーの利用には、READMEに示されたVercel AI Gatewayまたは各プロバイダーのSDKとの接続が必要。Gateway利用例ではモデル文字列を指定し、直接接続例ではプロバイダーSDKのモデルを指定する。料金や認証情報の設定条件はREADMEに記載されていない。

## 最短手順

- Node.js 22以降の環境で`npm install ai`を実行し、`generateText`にモデルとプロンプトを渡す。例では`import { generateText } from 'ai'`の後、`generateText({ model: 'openai/gpt-5.4', prompt: 'What is an agent?' })`を呼び出している。

## 変更履歴

- 2026-11-13: 初回登録
