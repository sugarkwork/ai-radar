---
repo: "nextlevelbuilder/ui-ux-pro-max-skill"
name: "UI UX Pro Max"
genre: "coding-agent"
url: "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill"
license: "MIT"
stars: 147531
forks: 15608
open_issues: 89
size_kb: 8625
language: "Python"
created: "2025-11-30"
updated: "2026-11-07"
archived: false
commits_30d: 21
commits_90d: 84
commit_cadence: "daily"
last_release: "v2.15.0"
flags: ["unverified"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
risk_notes: ""
sources: ["https://x.com/thegreatest_sv/status/2117324109478507007"]
fetched_at: "2026-11-10T08:40:33Z"
---

# UI UX Pro MaxでコーディングエージェントにUI設計案を作らせる

## 出来ること

- プロダクトの種類、業界、希望のトーンをもとに、配色、フォントの組み合わせ、レイアウトの型、避けるべき設計パターンをまとめた設計案を作れる。

## 目的・背景

- UIの実装前にデザイン方針を具体化するためのスキル。READMEではBM25による検索順位付けと業種別のルールを組み合わせる仕組みを説明している。

## 依存関係

- 検索スクリプトはPython 3.xと標準ライブラリを使用する。下記の導入経路にはClaude Codeのプラグイン機能が必要。npm CLIで導入する場合はNode.jsとnpmを使う。

## 実行条件

- READMEによれば検索スクリプトはローカルで動き、ネットワーク通信を行わない。公開リポジトリの基本版はMITライセンスで、READMEでは別途Premium版を案内している。

## 最短手順

- Claude Codeで `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` を実行し、続けて `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill` でスキルを導入する。
- Python 3.xを利用できる状態で、Claude Codeに「B2B SaaSのランディングページ向けに、落ち着いた配色と読みやすい書体で、実装前のデザインシステムを提案して」と依頼する。READMEではUI/UXの依頼をきっかけにスキルが起動し、スキル定義ではエージェントが `search.py` を `--design-system` 付きで呼び出す手順を示している。

## 変更履歴

- 2026-11-10: 初回登録
