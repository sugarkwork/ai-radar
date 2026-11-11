---
name: "Second Brain"
genre: "coding-agent"
url: "https://github.com/NicholasSpisak/second-brain"
repo: "NicholasSpisak/second-brain"
flags: ["unverified"]
risk_notes: "READMEに記載された機能と手順に基づく。個別の効果、利用条件、費用は確認できていない。 GitHub APIでライセンスを確認できていません。"
stars: 775
forks: 116
open_issues: 1
size_kb: 3586
language: "Shell"
created: "2026-04-06"
updated: "2026-04-07"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Bober_smart/status/2116978958121964030"]
fetched_at: "2026-11-10T14:14:37.834658+00:00"
---

# Second Brain

## 出来ること

- raw/フォルダの素材をエージェントが構造化Wikiページにまとめ、相互参照とインデックスを維持する。Obsidianで閲覧し、クエリやWikiの健全性確認を行うための4つのスキルを提供する。

## 目的・背景

- READMEでは、LLM Wikiパターンに基づく個人知識ベースとして説明されている。素材を取り込み、エージェントがWikiを整備し、人がキュレーションする構成。

## 依存関係

- README記載の前提はObsidian、Agent Skills対応のAIコーディングエージェント、スキル導入用のNode.js。summarize、qmd、agent-browserは任意ツールとして記載されている。

## 実行条件

- READMEによると、利用するエージェントがAgent Skillsに対応している必要がある。ObsidianでVaultフォルダを開いてWikiを閲覧する。

## 最短手順

- README記載の手順: `npx skills add NicholasSpisak/second-brain` でスキルを導入し、エージェントで `/second-brain` を実行してVaultを設定する。素材を `raw/` に入れ、`/second-brain-ingest` で取り込み、Obsidianで閲覧する。

## 変更履歴

- 2026-11-11: 初回登録
