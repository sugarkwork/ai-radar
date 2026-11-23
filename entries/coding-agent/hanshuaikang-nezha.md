---
name: "Nezha"
genre: "coding-agent"
url: "https://github.com/hanshuaikang/nezha"
repo: "hanshuaikang/nezha"
license: "GPL-3.0"
stars: 1901
language: "TypeScript"
created: "2026-03-22"
updated: "2026-09-17"
forks: 174
open_issues: 52
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 11
size_kb: 19163
archived: false
flags: ["low-quality", "unverified"]
risk_notes: "READMEは未署名パッケージの警告に対し、`xattr -rd com.apple.quarantine /Applications/nezha.app` の実行を案内している。OSの隔離属性を削除する手順だが、リスク説明は記載されていない。 READMEでは未署名のmacOSインストールパッケージに対し、隔離属性を再帰的に削除する手順を案内している。この操作による安全性への影響はREADMEでは説明されていない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/BIGMayrr/status/2119203067925053448"]
fetched_at: "2026-11-19T07:10:16.787365+00:00"
---

# Nezha

## 出来ること

- READMEによると、Nezhaは複数プロジェクトのClaude Code／Codexセッション管理、タスク通知、会話内容の閲覧とResume、Git操作、Git Worktree、コード・Markdown編集、Skill管理を一つの画面にまとめるデスクトップIDE。これらはREADMEの説明であり、個別機能の実機動作や「5倍」の効率向上は独立検証されていない。

## 目的・背景

- READMEは、複数のプロジェクトや並行タスクを切り替え、ターミナルや編集・Gitツール間の移動を減らすことを目的としていると説明している。

## 依存関係

- READMEは使用前にClaude CodeまたはCodexをインストールするよう案内している。

## 実行条件

- READMEはNezhaをクロスプラットフォームの軽量IDEと説明している。macOSでは、未署名のアプリを開く際の手順として隔離属性の削除コマンドを掲載している。対応OSの詳細はこのREADME抜粋では確認できない。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- 先にClaude CodeまたはCodexをインストールし、Nezhaを導入する。README記載のmacOS手順では、未署名アプリの隔離属性を外すため `xattr -rd com.apple.quarantine /Applications/nezha.app` を実行する。隔離属性の削除はOSの保護機能に関わるため、配布物の出所を確認してから実施すること。

## 変更履歴

- 2026-11-23: 初回登録
