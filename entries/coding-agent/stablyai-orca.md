---
repo: "stablyai/orca"
name: "Orca"
genre: "coding-agent"
url: "https://github.com/stablyai/orca"
flags: ["unverified"]
risk_notes: ["最新安定版のタグと公開日時は未確認。並列実行時の速度、作業品質、リソース消費、既存契約での利用可否は実機で検証していない。"]
stars: 120836
forks: 7653
open_issues: 8268
size_kb: 2664805
language: "TypeScript"
created: "2026-03-17"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2117504564941508613"]
fetched_at: "2026-11-10T09:16:19Z"
---

# Orca — コーディングエージェントをGit worktreeごとに並列管理

## 出来ること

- Claude CodeやCodexを個別のworktreeで並列に動かし、セッションや変更差分を同じアプリで確認できる。

## 目的・背景

- 複数の変更タスクを別々の作業ツリーに分け、エージェントの操作とレビューを一か所にまとめる。並列化による時間短縮は未測定。

## 依存関係

- Gitリポジトリと、利用するコーディングエージェントのCLIを用意する。Orca本体はMITライセンスで、エージェント側の認証・料金・利用枠は各提供元の契約に従う。

## 実行条件

- デスクトップ版はmacOS、Windows、Linux向け。Orca CLIは稼働中のOrcaランタイムに接続する。LinuxでのCLI名はorca-ide。

## 最短手順

- 公式インストールページからデスクトップ版を導入し、手元のGitリポジトリを追加する。タスクごとにworktreeを作り、使うエージェントを起動する。
- AIから呼ぶには、Settings → General → Orca CLIでCLIを登録し、シェルを使えるエージェントに `orca status --json` で接続を確認させる。続けて `orca repo list --json` で登録済みリポジトリを取得できる。Linuxでは両コマンドの `orca` を `orca-ide` に置き換える。

## 変更履歴

- 2026-11-10: 初回登録
