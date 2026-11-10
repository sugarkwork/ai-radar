---
repo: "undefined-ui/second-brain-os"
name: "Second Brain OS"
genre: "other"
url: "https://github.com/undefined-ui/second-brain-os"
license: "MIT"
stars: 1549
forks: 265
open_issues: 7
size_kb: 671
language: "HTML"
created: "2026-09-07"
updated: "2026-11-03"
archived: false
commits_30d: 8
commits_90d: 50
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "検索精度や学習効果の比較実測、プラグインとスクリプトの実行互換性、Claude Codeの利用料金、最新リリースのタグと公開日は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Ryrenz/status/2117799503893778508"]
fetched_at: "2026-11-10T10:39:46+00:00"
---

# Second Brain OS — エージェント設計の教材とMarkdown知識ベースの演習

## 出来ること

- 全7モジュールでコンテキスト、ループ、判定、ハーネス、評価、本番運用を学べる。5冊の分野別ハンドブックと演習用のテンプレート、スキル、サブエージェントが付属する。

## 目的・背景

- READMEによると、講座はGoogleのエージェント白書を土台とする。知識ベース演習はKarpathyのLLM wikiパターンを取り入れ、原資料を保存する `raw/` と、整理したページを相互にリンクする `wiki/` を分ける。

## 依存関係

- 教材の閲覧には登録やインストールが不要。演習のクイックスタートはClaude Codeを使い、リンク検査などの補助スクリプトにはPythonが必要。READMEではObsidian連携用のMCPを任意としている。

## 実行条件

- リポジトリはMITライセンス。Claude Codeの利用条件や料金は別途確認が必要。検索スキルは参照したページと、知識ベースで回答できなかった範囲を示す設計。

## 最短手順

- 閲覧から始めるなら、READMEのGetting startedから講座の導入ページを開く。
- AIから知識ベースを引くには、READMEのクイックスタートに沿って `vault-template/` を作業フォルダにコピーし、`skills/` と `commands/` をそのフォルダの `.claude/` に配置する。サンプルのMarkdownを用意して同フォルダでClaude Codeを起動し、`/ask` でノートについて質問する。回答の参照先と未回答の範囲を確認する。

## 変更履歴

- 2026-11-10: 初回登録
