---
name: "Composio"
genre: "agent-framework"
url: "https://github.com/ComposioHQ/composio"
repo: "ComposioHQ/composio"
license: "MIT"
stars: 31014
language: "TypeScript"
created: "2024-02-23"
updated: "2026-11-10"
forks: 4935
open_issues: 141
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 484550
archived: false
flags: ["unverified"]
risk_notes: "利用にはCOMPOSIO_API_KEYが必要とREADMEに記載。README記載の機能や規模について独立した検証はしていない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118043980420030914"]
fetched_at: "2026-11-10T16:22:48.093539+00:00"
---

# Composio

## 出来ること

- 1000以上の事前認証済みツールキット、ユーザー単位のセッション、認証、トリガー、サンドボックスをAIエージェントに提供する。TypeScript・Python SDK、CLI、およびOpenAI Agents、Claude Agent SDK、Vercel AI SDK、LangChainなどのプロバイダーアダプターを含む。各セッションはMCPエンドポイントも公開できる。

## 目的・背景

- エージェントがユーザーの意図に応じて複数のアプリで操作できるよう、ツール連携とセッションの仕組みを提供するSDKモノレポ。

## 依存関係

- READMEのTypeScript QuickstartではNode.js向けに@composio/core、@composio/openai-agents、@openai/agentsをインストールする。Python Quickstartではcomposio、composio-openai-agents、openai-agentsをインストールする。

## 実行条件

- Quickstartの利用にはCOMPOSIO_API_KEYが必要。READMEによるとTypeScript SDKはNode 22以上、Python SDKはPython 3.11以上を対象とする。

## 最短手順

- TypeScriptでは依存パッケージをインストールし、ComposioにOpenAIAgentsProviderを設定してユーザーIDでセッションを作成し、session.tools()で得たツールをAgentへ渡す。Pythonでは対応パッケージをインストールし、ComposioとOpenAIAgentsProviderを初期化、ユーザーIDでセッションを作成してtoolsをAgentに渡す。

## 変更履歴

- 2026-11-11: 初回登録
