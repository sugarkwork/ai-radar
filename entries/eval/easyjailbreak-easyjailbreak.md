---
name: "EasyJailbreak"
genre: "eval"
url: "https://github.com/EasyJailbreak/EasyJailbreak"
repo: "EasyJailbreak/EasyJailbreak"
flags: ["malicious", "unverified"]
risk_notes: "README explicitly describes generating adversarial jailbreak prompts and using them to attack a target model. This capability can facilitate bypassing model safeguards. 一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
stars: 945
forks: 95
open_issues: 17
size_kb: 8916
language: "Python"
created: "2024-01-31"
updated: "2026-09-01"
archived: false
license: "GPL-3.0"
commits_30d: 0
commits_90d: 2
commit_cadence: "stale"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/mingzi206/status/2118628554883883348"]
fetched_at: "2026-11-13T00:12:58.574194+00:00"
---

# EasyJailbreak

## 出来ること

- 複数の手法を組み合わせて敵対的なjailbreakプロンプトを生成するPythonフレームワーク。READMEでは、Selector、Mutator、Constraint、Evaluatorを使う複数の攻撃レシピを紹介している。出典: https://github.com/EasyJailbreak/EasyJailbreak — “An easy-to-use Python framework to generate adversarial jailbreak prompts by assembling different methods”

## 目的・背景

- LLMセキュリティの研究者・開発者向けに、jailbreakの工程を反復可能な段階に分け、研究や試行のための環境を提供する。出典: https://github.com/EasyJailbreak/EasyJailbreak — “EasyJailbreak is an easy-to-use Python framework designed for researchers and developers focusing on LLM security.”

## 依存関係

- READMEに記載された実行環境の条件はPython 3.9以上。追加の依存パッケージやモデル要件の詳細は、このREADMEの確認範囲では特定できない。出典: https://github.com/EasyJailbreak/EasyJailbreak — “All those methods need python>=3.9 installed.”

## 実行条件

- READMEの手順では、収録済みの手法を使う場合はeasyjailbreakをpipでインストールする。コンポーネントを追加する場合はリポジトリを取得してeditable installする。ワークフローにはQueries、Config、Models、Seedの準備と、対象モデルへの問い合わせが含まれる。出典: https://github.com/EasyJailbreak/EasyJailbreak

## 最短手順

- 収録済み手法を使う場合のREADME記載手順は `pip install easyjailbreak`。追加コンポーネントの開発には `git clone https://github.com/EasyJailbreak/EasyJailbreak.git`、`cd EasyJailbreak`、`pip install -e .` を案内している。出典: https://github.com/EasyJailbreak/EasyJailbreak

## 変更履歴

- 2026-11-13: 初回登録
