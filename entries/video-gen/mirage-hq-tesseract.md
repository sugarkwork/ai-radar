---
name: "Tesseract"
genre: "video-gen"
url: "https://github.com/mirage-hq/Tesseract"
repo: "mirage-hq/Tesseract"
license: "unknown"
stars: 367
language: "Python"
created: "2026-09-16"
updated: "2026-11-13"
forks: 27
open_issues: 0
commits_30d: 12
commit_cadence: "weekly"
commits_90d: 26
size_kb: 7526
archived: false
flags: ["unverified"]
risk_notes: "READMEにライセンスの説明がなく、API/MCPや製品の利用条件はリンク先未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/naka_1717/status/2118899440715276357"]
fetched_at: "2026-11-14T23:09:28.355148+00:00"
---

# Tesseract

## 出来ること

- READMEによると、AIエージェント向けのスキルとCLI（tsrct）で、動画編集、モーショングラフィックス、3Dシーン、デザインを扱い、編集可能な.tsrctプロジェクトを作成・編集・レンダリングできる。

## 目的・背景

- 動画編集、モーション、サウンドを一つのローカルプロジェクトにまとめ、エージェントとの対話で作成・反復編集するためのクリエイティブスイートとして紹介されている。

## 依存関係

- 手動のCLI取得手順は、OS別のZIPをReleasesから取得する方法。READMEにはターミナル経由のスキル導入にはNode.jsが必要とある。詳細な依存関係はREADME本文では確認できない。

## 実行条件

- READMEにはmacOS、Windows、Linux対応とあり、ChatGPT、Codex、Claude Code、Cursorでの利用を案内している。CLIの手動取得はApple Silicon/Intel Mac、64-bit Windows、Linuxまたはクラウドエージェント向けに記載。

## 最短手順

- README記載の他エージェント向け手順は、新しいチャットに「Install the latest Tesseract skills from https://github.com/mirage-hq/Tesseract and finish any setup they need.」と入力する方法。ターミナルを使う場合は `npx skills add mirage-hq/Tesseract`（Node.jsが必要）。

## 変更履歴

- 2026-11-14: 初回登録
