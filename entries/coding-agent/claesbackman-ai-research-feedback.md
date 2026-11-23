---
name: "AI tools for research"
genre: "coding-agent"
url: "https://github.com/claesbackman/AI-research-feedback"
repo: "claesbackman/AI-research-feedback"
license: "MIT"
stars: 569
language: "Python"
created: "2026-03-01"
updated: "2026-11-15"
forks: 107
open_issues: 0
commits_30d: 12
commit_cadence: "weekly"
commits_90d: 18
size_kb: 3473
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/bkdgiffug/status/2119346182950355149"]
fetched_at: "2026-11-19T12:19:01.756546+00:00"
---

# AI tools for research

## 出来ること

- Claude Code向けスキルを提供する。論文、事前分析計画、助成金申請書、論文と分析コードの整合性などをレビューし、構造化した報告を作成する。論文の政策向け要約やスライド作成、PDFからMarkdownへの変換、論文の静的Webサイト化などのスキルも含む。

## 目的・背景

- 学術研究の作業を支援するスキル集。READMEでは、論文へのフィードバックと研究成果の異なる読者向けの伝達を主な用途として説明している。

## 依存関係

- Claude Code用のスキルとして説明されている。explorable-deck、explorable-beamer、paper-websiteはテンプレート、参考資料、補助スクリプトを含むフォルダ単位での導入が必要とされる。

## 実行条件

- グローバル導入またはプロジェクト単位の導入が可能。README記載の一括導入手順はmacOS、Linux、WSL向け。WindowsではZIPを展開してスキルフォルダをコピーする手順が記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- WindowsではリポジトリのZIPを取得して展開し、Skills/内の各スキルフォルダを ~/.claude/skills/ にコピーしてClaude CodeまたはVS Codeを再起動する。macOS、Linux、WSLではREADME記載のgit cloneとコピーの一行コマンドで全スキルを導入できる。

## 変更履歴

- 2026-11-23: 初回登録
