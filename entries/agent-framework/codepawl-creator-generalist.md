---
name: "creator-generalist"
genre: "agent-framework"
url: "https://github.com/codepawl/creator-generalist"
repo: "codepawl/creator-generalist"
license: "MIT"
stars: 119
language: "Python"
created: "2026-11-06"
updated: "2026-11-10"
forks: 7
open_issues: 0
commits_30d: 28
commit_cadence: "daily"
commits_90d: 28
size_kb: 7122
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/CY160909/status/2119983884934734211"]
fetched_at: "2026-11-10T23:20:27.907597+00:00"
---

# creator-generalist

## 出来ること

- 2D・3Dの画像や映像、キャラクター、地図、図表、背景、アニメーション、動画編集、音声制作などに使うエージェント向けスキルを提供する。READMEには、3D制作にBlender、Three.js、67jsを使う手順や、2D制作に無料ツールを使う手順などが記載されている。

## 目的・背景

- エージェントにスキルパックを一度導入し、依頼内容に応じたスキルを呼び出して2D・3Dコンテンツや動画を制作することを目的としている。READMEによると、依頼の目的・掲載先・形式・見た目などが未指定の場合は質問し、プレビューを提示する設計。

## 依存関係

- READMEでは、用途に応じてBlender、Three.js、67js、Krita、FFmpeg、Node.js、Pythonなどを扱うと説明している。すべてのスキルで必要となる依存関係やバージョン要件は、提示されたREADMEの範囲では特定されていない。

## 実行条件

- README記載の導入方法は、Claude Codeのプラグイン、skills CLI、またはスキルフォルダへの手動コピー。手動導入ではエージェントのskillsフォルダへ指定されたスキル群をコピーする。具体的な環境要件は提示されたREADMEの範囲では特定されていない。

## 最短手順

- READMEはClaude Code向けに`/plugin marketplace add codepawl/creator-generalist`の後、各プラグインを`/plugin install`する手順を記載している。任意のエージェント向けには`npx skills add codepawl/creator-generalist`を案内している。

## 変更履歴

- 2026-11-11: 初回登録
