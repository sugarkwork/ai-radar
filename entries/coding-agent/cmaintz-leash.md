---
repo: "CMaintz/leash"
name: "Leash"
genre: "coding-agent"
url: "https://github.com/CMaintz/leash"
license: "MIT"
stars: 0
language: "TypeScript"
created: "2026-09-30"
updated: "2026-11-06"
forks: 0
open_issues: 6
commits_30d: 21
commit_cadence: "daily"
commits_90d: 93
size_kb: 314
archived: false
flags: ["unverified"]
risk_notes: "最新GitHubリリース、npmの配布版、現行のJev料金と送信データの保持条件は未確認。READMEの約300 msと約68%は作者の記載で、測定条件や対象リポジトリでの再現性は未確認。CLI、フック、MCPは未実行。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116142322543198271"]
fetched_at: "2026-11-10T12:54:52Z"
---

# Leash — コーディングエージェントの変更差分をプロジェクトのルールで判定

## 出来ること

- Claude CodeやCodexのターン終了時に変更差分を調べ、修正閾値を超えた新規違反のルールをエージェントに返す。stdio MCPからも差分を検査できる。

## 目的・背景

- CLAUDE.mdやAGENTS.mdにあるリンターで判定しづらいルールを、エージェントが `.leash/rubric.json` に整理する。既存違反を基準に登録し、新規違反に絞る。決定的な検査で扱えるルールはモデル判定から外す。

## 依存関係

- Node.js上で動くnpmパッケージ `@cmaintz/leash`。モデル判定にはJevとAPIキーが必要。Leash本体はMITライセンス。

## 実行条件

- 判定対象のテキスト差分をJevに送信する。キーやルールがなければ判定を省略し、タイムアウトでもターンを通す。モデル判定は助言として扱い、作者が記載した速度や精度は導入先での性能を保証しない。

## 最短手順

- READMEの手順では `npm install -g @cmaintz/leash` で導入し、`JEV_API_KEY` を設定する。Claude Codeでは `leash init --project` の後に `/leash-rubric` でエージェントにルール表を作らせ、`leash compile` で検証する。以後はターン終了時のフックが判定を呼ぶ。
- AIから任意の時点で呼ぶ場合は、Codexに `leash init --mcp --codex` でMCPを登録し、エージェントに `check` ツールで作業ツリーの差分を調べるよう依頼する。

## 変更履歴

- 2026-11-11: 初回登録
