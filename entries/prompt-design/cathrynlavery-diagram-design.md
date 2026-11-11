---
name: "Diagram Design"
genre: "prompt-design"
url: "https://github.com/cathrynlavery/diagram-design"
repo: "cathrynlavery/diagram-design"
flags: ["unverified"]
risk_notes: "README内の機能説明に基づく登録。生成品質や各ホストでの動作は独立検証していない。依存関係、実行条件、料金についてREADMEから確認できる情報は限定的。"
stars: 66245
forks: 4400
open_issues: 48
size_kb: 38503
language: "HTML"
created: "2026-04-16"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/opensourcelab9/status/2116500497469472871"]
fetched_at: "2026-11-10T13:46:19.068997+00:00"
---

# Diagram Design

## 出来ること

- READMEでは、45種類の図をブランドに合わせ、単一のHTML+SVGファイルとして作成するAgent Skillと説明されている。作成したHTMLはダブルクリックで開ける。

## 目的・背景

- 図の種類を選び、ブランドの色やフォントに合わせた図を作る用途。READMEには、アーキテクチャ図、インパクト対労力の四象限、401時のトークン更新を含むシーケンス図などの例がある。

## 依存関係

- READMEにはAgent Skills対応ホストとしてCursor、Claude Code、Codex、Qoder、GitHub Copilot、Gemini CLI、Cline、Windsurf、Ampなどが挙げられている。クロスエージェント導入例は `npx skills add cathrynlavery/diagram-design`。

## 実行条件

- READMEでは、エージェントに自然文で図の作成を依頼する方法を案内している。必要な環境条件や依存関係の全容は、取得したREADMEの範囲では確認できない。

## 最短手順

- Agent Skills対応ホストでは `npx skills add cathrynlavery/diagram-design` で導入し、エージェントに作りたい図を自然文で依頼する。READMEによると、エージェントが図の種類を選び、計画を示してHTMLファイルを作成する。

## 変更履歴

- 2026-11-11: 初回登録
