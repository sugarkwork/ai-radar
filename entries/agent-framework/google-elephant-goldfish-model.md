---
name: "Elephant-Goldfish Model (EGM)"
genre: "agent-framework"
url: "https://github.com/google/elephant-goldfish-model"
repo: "google/elephant-goldfish-model"
stars: 19014
forks: 1414
open_issues: 105
size_kb: 15142
language: "Python"
created: "2026-09-13"
updated: "2026-11-14"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ganfanren_ai/status/2118875956089856189"]
fetched_at: "2026-11-14T18:07:06.457626+00:00"
---

# Elephant-Goldfish Model (EGM)

## 出来ること

- AIアシスタント向けプラグインとして、プロジェクトの文脈をもとに仕様書を作成し、別の新規レビュアーが仕様書と参照資料を確認する設計レビューを提供する。既存の設計文書やPR計画をコードと照合するレビュー、文書とコードのドリフト報告、アイデアの検討、仕様書の草案作成にも使える。レビューはテストや人の判断の代替ではない。出典: README https://github.com/google/elephant-goldfish-model

## 目的・背景

- READMEでは、Elephantがプロジェクトの文脈を保持して仕様書を作成し、Goldfishが先行会話なしで草案と参照資料を確認することで、明示されていない前提や見落としを見つける構成として説明されている。設計上の選択と仕様の承認は利用者が担う。組み込みの草案・設計レビューはソフトウェア仕様向けで、他の文書ではレビュー担当者と基準をReview loopで選ぶ。出典: README https://github.com/google/elephant-goldfish-model

## 依存関係

- READMEには、ブレインストーミングとレビューに新規のサブエージェントを作成できるセッションが必要とある。必要なランタイム、その他の依存関係はREADMEでは確認できない。出典: README https://github.com/google/elephant-goldfish-model

## 実行条件

- ChatGPT/Codexデスクトップ、Antigravity、Claude Code、Codex CLI向けの導入方法がREADMEに記載されている。各環境の対応状況には制限があり、レビュー機能は新規サブエージェントのコンテキストを作成できない場合に停止する。出典: README https://github.com/google/elephant-goldfish-model

## 最短手順

- 対象のコーディングエージェントにプラグインを導入して新しいセッションを開始する。既存文書のレビューは、例として `/egm:egm-review docs/designs/webhooks.md` を実行する。Codexでは対応するEGMスキルをスキルピッカーから選ぶ。出典: README https://github.com/google/elephant-goldfish-model

## 変更履歴

- 2026-11-14: 初回登録
