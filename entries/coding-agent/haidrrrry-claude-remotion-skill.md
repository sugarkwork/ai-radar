---
name: "Claude Remotion Skill"
genre: "coding-agent"
url: "https://github.com/haidrrrry/claude-remotion-skill"
repo: "haidrrrry/claude-remotion-skill"
license: "MIT"
stars: 960
language: "TypeScript"
created: "2026-06-13"
updated: "2026-08-12"
forks: 131
open_issues: 2
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 14826
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:12:26.325213+00:00"
---

# Claude Remotion Skill

## 出来ること

- Claude向けのエージェントスキルとしてRemotionの動画・モーショングラフィックス制作を支援する。READMEは、スプリングやベジェ曲線、段階的なアニメーション、カラーグレーディング、字幕、効果音設計などのルールを示し、ReactとTypeScriptによる動画制作を説明している。

## 目的・背景

- 作者は、スキルにモーションデザインのルールを持たせ、レンダー後にフレームを抽出・確認して修正し、再レンダーする手順を説明している。README内の品質比較や効果の評価は作者の説明であり、独立した実測ではない。

## 依存関係

- READMEではRemotion（React + TypeScript）を使用する。例のレンダー手順ではexamplesディレクトリでnpm installを実行し、音声生成にnpm run audio、各動画のレンダーにnpm run render:*を使う。

## 実行条件

- READMEによると、Claude CodeまたはClaude DesktopのSonnetまたはOpusで利用でき、agent skills対応のClaudeを対象としている。RemotionとClaudeのサブスクリプションまたはAPIアクセスが必要と記載されている。

## 最短手順

- Claude Codeではリポジトリをcloneし、remotion-motion-graphicsフォルダをユーザーまたはプロジェクトの.claude/skills/へコピーする。Claude DesktopまたはClaude.aiではremotion-motion-graphics.skillをSettings → Capabilities → Skillsからアップロードする。利用時は動画を依頼し、レンダー後にフレームを確認・修正して再レンダーする手順がREADMEに示されている。

## 変更履歴

- 2026-11-12: 初回登録
