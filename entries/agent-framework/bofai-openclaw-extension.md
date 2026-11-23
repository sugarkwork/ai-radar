---
name: "OpenClaw Extension"
genre: "agent-framework"
url: "https://github.com/BofAI/openclaw-extension"
repo: "BofAI/openclaw-extension"
license: "unknown"
stars: 14
language: "Shell"
created: "2026-03-02"
updated: "2026-10-22"
forks: 4
open_issues: 0
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 2
size_kb: 1667
archived: false
flags: ["low-quality", "unverified"]
risk_notes: "READMEの「Use at your own risk」で、実験段階、厳密なテスト未実施、保証なしと説明されている。 インストーラーは通常モードでもAgentWalletの初期化やMCP・スキル設定を行い、クリーンモードは既存のAgentWalletデータ、MCP設定、導入済みスキルを削除するとREADMEに記載。bnbchain-mcpはPRIVATE_KEYを必要とし、AgentWallet非対応。秘密鍵をAIエージェントに扱わせる危険性と資産損失の可能性がREADMEで明記されている。ライセンスはGitHub API上でunknown。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/joejossy_12/status/2119201345802490283"]
fetched_at: "2026-11-19T05:10:23.077064+00:00"
---

# OpenClaw Extension

## 出来ること

- OpenClawに、TRONやBNB Chainなどのブロックチェーン操作用MCPサーバーと、ウォレット、取引、ステーキング、DEX、x402決済などのスキルを設定する。スキルは導入時に選択でき、README記載のスナップショットはskillsリポジトリのv1.5.15。READMEは各コンポーネントの機能を説明しているが、独立した動作検証結果は示していない。

## 目的・背景

- AIエージェントが標準プロトコルで報酬を受け取り、計算資源などに支払い、エージェント間取引やDeFi・スマートコントラクトを扱えるようにすることを目指すとREADMEに記載。

## 依存関係

- README記載の前提条件は、OpenClaw、Node.js ^22.23.4 || ^24.22.1 || >=26.12.1、スキルリポジトリ取得用Git、AgentWallet CLI v2.3.1。WindowsではPowerShell 5.1以降が必要。MCP設定にはmcporterを使う。bnbchain-mcpはPRIVATE_KEYを必要とし、AgentWalletには未対応と記載されている。

## 実行条件

- Linux/macOSではinstall.sh、Windowsではinstall.ps1またはinstall.batを使う手順がREADMEにある。OpenClawを先に導入する必要がある。READMEによると、インストーラーは通常・クリーンのモードを選択させ、クリーンモードは既存AgentWalletデータ、MCPエントリー、導入済みスキルを削除して再導入する。通常モードではagent-wallet start --save-runtime-secrets、クリーンモードではagent-wallet start --override --save-runtime-secretsを実行すると説明されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載のLinux/macOS手順は `curl -fsSL https://raw.githubusercontent.com/BofAI/openclaw-extension/refs/heads/main/install.sh | bash`。WindowsはPowerShellで `irm https://raw.githubusercontent.com/BofAI/openclaw-extension/refs/heads/main/install.ps1 | iex`。どちらも取得したスクリプトをその場で実行する形式。READMEはまずOpenClawの導入を求め、テストネットで検証してからメインネットを使うよう勧めている。

## 変更履歴

- 2026-11-23: 初回登録
