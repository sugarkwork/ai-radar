---
name: "Knowledge Work Plugins"
genre: "agent-framework"
url: "https://github.com/anthropics/knowledge-work-plugins"
repo: "anthropics/knowledge-work-plugins"
stars: 35663
forks: 3945
open_issues: 169
size_kb: 6859
language: "Python"
created: "2026-01-23"
updated: "2026-11-13"
archived: false
license: "Apache-2.0"
commits_30d: 75
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/awe0_io/status/2118739120206045238"]
fetched_at: "2026-11-13T23:19:15.427574+00:00"
---

# Knowledge Work Plugins

## 出来ること

- 職務別プラグインを通じて、Claudeにスキル、外部ツール接続、スラッシュコマンドを提供する。READMEでは、生産性、営業、カスタマーサポート、製品管理、マーケティング、法務、財務、データ、企業内検索、バイオ研究、プラグイン管理の11種類を紹介している。

## 目的・背景

- READMEによると、プラグインはClaudeの作業方法、参照するツールやデータ、重要なワークフロー、利用可能なコマンドを職務や組織に合わせるための出発点として公開されている。会社固有の用語、ツール、プロセスに合わせてカスタマイズできる。

## 依存関係

- Claude Cowork向けに構築され、Claude Codeにも対応するとREADMEに記載されている。コネクタはMCPサーバー経由で外部ツールと接続する。接続先はプラグインごとに異なる。

## 実行条件

- READMEでは、Coworkはclaude.com/pluginsからプラグインをインストールし、Claude Codeはマーケットプレイスを追加してから個別プラグインをインストールする手順を案内している。個別の接続先サービスを使う場合の認証や契約条件はREADMEに記載されていない。

## 最短手順

- Claude Codeでは、まず `claude plugin marketplace add anthropics/knowledge-work-plugins` を実行し、続けて `claude plugin install sales@knowledge-work-plugins` のように対象プラグインを指定してインストールする。READMEにはCoworkではclaude.com/pluginsからインストールする方法も記載されている。

## 変更履歴

- 2026-11-14: 初回登録
