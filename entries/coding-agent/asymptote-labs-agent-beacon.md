---
repo: "Asymptote-Labs/agent-beacon"
name: "Beacon"
genre: "coding-agent"
url: "https://github.com/Asymptote-Labs/agent-beacon"
license: "MIT"
stars: 3410
language: "Go"
created: "2026-05-12"
updated: "2026-11-09"
forks: 302
open_issues: 13
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 71397
archived: false
flags: ["unverified"]
risk_notes: "最新版のタグ・公開日時、投稿にある beacon handoff resume の具体的な挙動、エージェント間の再利用による時間短縮や成功率、Beacon Cloudの料金は未確認。対話セットアップではBeacon Cloudが事前選択され、確定すると収集した履歴の転送が始まる。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/PayneL_AI/status/2117477229563445735"]
fetched_at: "2026-11-10T09:10:12+00:00"
---

# BeaconでClaude CodeやCodexの作業知識を再利用する

## 出来ること

- Claude Code、Codex、Cursor、OpenCodeなどの作業履歴を共通のイベント形式に正規化し、ローカルのJSONLに記録する。レビュー済みの知識はMCPやAgent Skillsを通じて後続のエージェントが参照できる。

## 目的・背景

- ツールを切り替えても、過去の修正手順やリポジトリ固有の作業ルールを再利用できるようにする。READMEは履歴から知識を抽出し、レビュー・承認を経て再利用する流れを説明している。改善効果は実測していない。

## 依存関係

- Beacon CLIと対応するエージェント環境を使う。収集方法は環境ごとに異なり、Claude CodeとCodex CLIではOTLP・フック・ポーリングが対応表に記載されている。

## 実行条件

- READMEにはmacOS向けのHomebrewとLinux向けのdeb・rpmが案内されている。対話セットアップで端末内に履歴を留めるにはLocalを選ぶ。クラウド転送はBeacon Cloudを確定すると始まる。公開リポジトリはMITライセンス。

## 最短手順

- READMEのOS別手順でCLIを導入する。対話セットアップを使う場合はLocalを選び、対象エージェントで作業してから `beacon traces` で履歴が記録されたことを確認する。
- 利用するエージェントのMCP設定で `beacon mcp serve` をローカルサーバーとして登録し、エージェントに『BeaconのMCPを使い、このリポジトリの過去の修正手順を探して』と依頼する。

## 変更履歴

- 2026-11-10: 初回登録
