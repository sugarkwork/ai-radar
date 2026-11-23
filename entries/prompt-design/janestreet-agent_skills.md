---
name: "Jane Street Agent Skills — Socratic Tutor"
genre: "prompt-design"
url: "https://github.com/janestreet/agent_skills"
repo: "janestreet/agent_skills"
stars: 10268
forks: 705
open_issues: 1
size_kb: 7
language: "unknown"
created: "2026-11-03"
updated: "2026-11-17"
archived: false
license: "MIT"
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/RoundtableSpace/status/2119380660288999692"]
fetched_at: "2026-11-19T21:12:31.738757+00:00"
---

# Jane Street Agent Skills — Socratic Tutor

## 出来ること

- トピックを指定すると、LLMをSocratic methodに基づく個人チューターとして使うスキル。診断、レベル0〜5のスキルマップ、一度に一つの質問、間隔を空けた復習、最終評価を行うとREADMEは説明している。

## 目的・背景

- Jane Streetが内部で日々使っているスキルを公開したもの。READMEによると、既存のチューター用プロンプトやスキルはあるが、このスキルは社内で作成され、他の実装を意図的に派生元としたものではない。

## 依存関係

- READMEでは、共通のSKILL.md形式に対応したコーディングエージェント、または通常のチャットボットで利用する方法を案内している。個別のソフトウェア依存関係は記載されていない。

## 実行条件

- 共通のSKILL.md形式に対応するコーディングエージェントでは、スキルのディレクトリをエージェントのスキルフォルダーにコピーし、「teach me X」のように利用を指示する。通常のチャットボットでは、SKILL.mdの本文をチャットまたはカスタム／システムプロンプトに貼り、その後に実行したい内容を続ける。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- 1. リポジトリからsocratic-tutorのSKILL.mdを取得する。
2. 対応するコーディングエージェントのスキルフォルダーへスキルディレクトリをコピーするか、本文をチャットボットに貼る。
3. 学びたいトピックを指定する。

## 変更履歴

- 2026-11-23: 初回登録
