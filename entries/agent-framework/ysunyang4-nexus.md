---
name: "Nexus"
genre: "agent-framework"
url: "https://github.com/ysunyang4/Nexus"
repo: "ysunyang4/Nexus"
license: "AGPL-3.0"
stars: 375
language: "TypeScript"
created: "2026-11-13"
updated: "2026-11-15"
forks: 65
open_issues: 2
commits_30d: 10
commit_cadence: "weekly"
commits_90d: 10
size_kb: 14758
archived: false
flags: ["low-quality", "unverified"]
risk_notes: "READMEは「Zero Hallucination Guarantee」といった強い保証表現を含みますが、提示された資料内にその保証を裏付ける独立した根拠はありません。 READMEはサンドボックス、トークン保護、クラッシュ復旧などのセキュリティ・信頼性機能を主張していますが、この資料だけでは実装や効果を独立に確認できません。リリースページの配布物やチェックサムの有無もREADMEでは確認していません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/shenxiankk/status/2122521103381745949"]
fetched_at: "2026-11-18T00:37:13.372068+00:00"
---

# Nexus

## 出来ること

- READMEによると、NexusはChatGPT、DeepSeekなどのAIアシスタントとローカルワークステーションをMCP経由で接続するデスクトップアプリ、サーバー、実行デーモンからなる構成です。ローカルファイル操作、コマンド実行、Git、ブラウザー操作、Windowsのコンピューター操作、LSP連携などの機能を掲げています。これらの機能・安全性はREADMEの説明であり、独立検証はしていません。

## 目的・背景

- READMEでは、AIエージェントがローカルの開発作業を行えるようにし、サンドボックス境界を設けてクラウド仲介先へのコード送信を避けることを目的として説明しています。

## 依存関係

- ソースビルドの前提条件として、Node.js 24以上、pnpm 10以上、Rust stableがREADMEに記載されています。

## 実行条件

- READMEの手順は、依存関係をインストールし、ワークスペースをビルドした後にデスクトップ開発サーバーを起動する構成です。対象コマンドは `pnpm install`、`pnpm run build`、`pnpm --filter @localbridge/desktop dev` です。

## 最短手順

- README記載のソースビルド手順：`git clone https://github.com/ysunyang4/Nexus.git`、`cd Nexus`、`pnpm install`、`pnpm run build`、`pnpm --filter @localbridge/desktop dev`。Node.js 24以上、pnpm 10以上、Rust stableが必要です。

## 変更履歴

- 2026-11-22: 初回登録
