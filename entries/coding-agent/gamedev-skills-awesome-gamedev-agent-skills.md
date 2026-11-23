---
name: "awesome-gamedev-agent-skills"
genre: "coding-agent"
url: "https://github.com/gamedev-skills/awesome-gamedev-agent-skills"
repo: "gamedev-skills/awesome-gamedev-agent-skills"
license: "Apache-2.0"
stars: 9585
language: "Python"
created: "2026-06-24"
updated: "2026-11-12"
forks: 974
open_issues: 5
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 9139
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/unclejoe_666/status/2119210003542200359"]
fetched_at: "2026-11-20T02:11:21.648534+00:00"
---

# awesome-gamedev-agent-skills

## 出来ること

- READMEによると、12のゲームエンジン向けに79個のゲーム開発用Agent Skillsとルーターを提供します。利用者が作りたいものを自然文で伝えると、ルーターがエンジンとタスクを判定し、該当するスキルを読み込む仕組みです。READMEには、Godot、Unity、Unreal、Ebitengine、Phaser、PixiJS、three.js、Bevy、pygame、LÖVE、Defold、Robloxが挙げられています。

## 目的・背景

- 利用中のゲームエンジンに合わせて、AIコーディングエージェントでゲーム開発を進めるためのスキル集です。READMEは、エンジンやタスクに合うスキルを選び、コード作成前に読み込ませる用途を説明しています。

## 依存関係

- 一括導入にはNode.js 22.20以降と`skills` CLIを使う手順がREADMEに記載されています。Claude Codeプラグインとして導入する方法も記載されています。

## 実行条件

- READMEには`npx skills add gamedev-skills/awesome-gamedev-agent-skills`による導入手順があります。`--list`で事前確認、`-g`で全プロジェクト向け、`-a <agent>`で特定エージェント向けに指定できます。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載のコマンドを実行します。

```bash
npx skills add gamedev-skills/awesome-gamedev-agent-skills
```

## 変更履歴

- 2026-11-23: 初回登録
