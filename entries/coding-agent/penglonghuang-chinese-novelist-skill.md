---
name: "chinese-novelist skill"
genre: "coding-agent"
url: "https://github.com/PenglongHuang/chinese-novelist-skill"
repo: "PenglongHuang/chinese-novelist-skill"
license: "MIT"
stars: 4766
language: "JavaScript"
created: "2026-01-25"
updated: "2026-11-01"
forks: 646
open_issues: 15
commits_30d: 21
commit_cadence: "daily"
commits_90d: 30
size_kb: 1088
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/0xGky/status/2120065171347640759"]
fetched_at: "2026-11-11T06:07:45.327293+00:00"
---

# chinese-novelist skill

## 出来ること

- README では、中文小说の企画から完稿までを支援する Claude Code Skill と説明されています。題材・主役・中心となる葛藤を質問し、人物档案・章別大纲・写作计划を生成した後、章ごとの執筆、润色、字数检查、全稿校验と不合格章の修复を行います。偏好记忆、中断位置の検出と续写、串行・子Agent并行・Agent Teams の三つの写作模式も記載されています。

## 目的・背景

- 物語の構想があっても続きを組み立てにくい利用者向けに、人物と大纲を先に定め、章ごとに執筆して完稿へ進む手順を提供します。

## 依存関係

- README は Claude Code Skill として紹介し、インストール手順に `npx skills add PenglongHuang/chinese-novelist-skill` を示しています。その他の依存関係は添付READMEから確認できません。

## 実行条件

- Skill をインストールし、対応する Agent で「使用 chinese-novelist 帮我写一部小说」と依頼する手順がREADMEに記載されています。READMEは Claude Code を明示し、Coding Agent、Personal Agent などを対象として挙げています。

## 最短手順

- 1. `npx skills add PenglongHuang/chinese-novelist-skill` でSkillをインストールします。
2. Agent に「使用 chinese-novelist 帮我写一部小说」と依頼します。
3. 質問に回答して企画を確認し、執筆モードを選びます。

## 変更履歴

- 2026-11-11: 初回登録
