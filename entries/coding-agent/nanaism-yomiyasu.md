---
name: "yomiyasu（よみやす）"
genre: "coding-agent"
url: "https://github.com/nanaism/yomiyasu"
repo: "nanaism/yomiyasu"
stars: 2975
forks: 78
open_issues: 1
size_kb: 5279
language: "Python"
created: "2026-09-30"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 26
commits_90d: 69
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/oga_aiichiro/status/2105309676305072437"]
fetched_at: "2026-11-11T04:18:01.512443+00:00"
---

# yomiyasu（よみやす）

## 出来ること

- AIが生成した日本語の不自然な比喩、曖昧な主述関係、不要な装飾を直し、読みやすい文章に整えるスキル。技術記事、設計書・仕様書、PR説明文、社内レポートなどの実務文書を主な対象とする。READMEでは、指示書（SKILL.md）と、直す前後で意味が変わる恐れのある箇所を示す検査ツールをまとめたものと説明されている。

## 目的・背景

- AI生成文に残りやすい主述関係の曖昧さ、情報密度の低下、定型的な表現などを、元の意味を保ちながら読みやすくすることを目的とする。README掲載のBefore/Afterは作者による使用例であり、独立した効果測定ではない。

## 依存関係

- README記載の導入方法には、npx skills、GitHub CLIのgh skill、npx openskills、Claude Codeプラグイン、登録専用ZIP、またはスキルフォルダのコピーがある。実行時に必要な依存関係の詳細は、添付READMEだけでは確認できない。

## 実行条件

- Claude Code、Codex、CursorなどのAIコーディング環境に読み込ませて使用する。Claude.ai Web版などでは登録専用ZIPを使う方法が案内されている。

## 最短手順

- READMEの推奨手順は `npx skills add nanaism/yomiyasu`。最新版への更新は `npx skills update yomiyasu`。READMEには各エージェント向けの別の導入手順も記載されている。

## 変更履歴

- 2026-11-11: 初回登録
