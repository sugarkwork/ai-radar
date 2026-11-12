---
name: "Motion.dev Animations Skill"
genre: "coding-agent"
url: "https://github.com/199-biotechnologies/motion-dev-animations-skill"
repo: "199-biotechnologies/motion-dev-animations-skill"
license: "MIT"
stars: 231
language: "TypeScript"
created: "2025-11-07"
updated: "2026-03-30"
forks: 36
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 76
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:17:27.762824+00:00"
---

# Motion.dev Animations Skill

## 出来ること

- READMEでは、Claude Codeが自然言語の指示からMotion.devを使ったTypeScript/JSXのアニメーションコードを生成するスキルと説明されています。例として、ヒーロー要素の登場、スクロール効果、ホバー、ドラッグ並べ替え、ボタンのマイクロインタラクションが挙げられています。README記載の性能目標は60fps以上（120fpsを理想）、バンドルサイズ50KB未満、reduced motion・キーボード操作への対応などです。これらはREADME上の目標であり、独立検証結果ではありません。

## 目的・背景

- READMEは、spring physics、GPU向けプロパティ、prefers-reduced-motion対応などを含むアニメーション実装のパターンをClaude Codeに提供し、自然言語の依頼からコードを生成することを目的として説明しています。コア指示に加え、例・API参照・テンプレートを必要時に読み込む構成とされています。

## 依存関係

- READMEではMotion.devを利用すると説明されています。Vueではmotion-vパッケージを使う案内があります。その他の具体的な依存パッケージ一覧やバージョンは、提示されたREADME本文には記載されていません。

## 実行条件

- README記載の対応対象はReact 19+、Next.js 15+（App Router）、Svelte 5+、Astro 4+、Vue 3（motion-vを使用）、Vanilla JS ES2020+（motionパッケージ）です。Claude Codeのskillsディレクトリへの追加、またはプロジェクトへのgit submodule追加が案内されています。

## 最短手順

- READMEの案内では、リポジトリをClaude Codeのskillsディレクトリへ追加するか、プロジェクトの.claude/skills/motion-dev-animationsへgit submoduleとして追加します。その後、アニメーションしたい内容を自然言語で依頼します。README例では、Claude Codeがフレームワークなどを確認し、方針を立ててコードを生成・検証すると説明されています。

## 変更履歴

- 2026-11-12: 初回登録
