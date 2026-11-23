---
name: "Cybernetic Meadow agent skill"
genre: "agent-framework"
url: "https://github.com/CyberneticMeadow/Skill"
repo: "CyberneticMeadow/Skill"
license: "MIT"
stars: 0
language: "JavaScript"
created: "2026-11-17"
updated: "2026-11-17"
forks: 0
open_issues: 0
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 1
size_kb: 1381
archived: false
flags: ["unverified"]
risk_notes: "READMEの説明に基づく登録で、機能や安全性を独立検証していない。単一運営者がブロック生成・署名サービス等を担い、fraud proofは未提供とREADMEが説明している。トークンの凍結・停止可能性も記載されている。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Cyber_Meadow/status/2122900231725502631"]
fetched_at: "2026-11-18T05:11:20.121716+00:00"
---

# Cybernetic Meadow agent skill

## 出来ること

- READMEによると、Node.js CLIとMCPサーバーを通じてAIエージェント用ウォレットの作成・ペアリング、残高確認、入出金、エージェント間送金、マイニング、トークンやプール操作を行う。署名サービスは公開ポリシーに従って要求を承認し、ポリシー外の送金や操作を拒否すると説明されている。これらはREADMEの記載であり、独立検証ではない。

## 目的・背景

- READMEはCybernetic Meadowを、AIエージェントのみが取引できるSolana L2と説明している。所有者のSolanaウォレットでエージェントをペアリングし、日次上限の設定、停止、所有者宛ての出金ができるとしている。

## 依存関係

- READMEはCLIとMCPサーバーが依存パッケージなしのNode.js実装であると記載している。

## 実行条件

- READMEの記載ではNode.js 18以降が必要。CLIはスキルのフォルダーから `node ai-tools/cli.mjs <command>` で実行する。MCPクライアントでは `node <path-to-repository>/skills/cybernetic-meadow/ai-tools/mcp.mjs` を登録する手順が示されている。

## 最短手順

- READMEは `npx skills add CyberneticMeadow/skill` でスキルを導入し、エージェントにスキルを読むよう指示した後、`https://cyberneticmeadow.network/pair` でSolanaウォレットを接続してペアリングコードを入力する手順を示している。ANTHROPICを移動する操作の前に確認を求める例も掲載されている。

## 変更履歴

- 2026-11-23: 初回登録
