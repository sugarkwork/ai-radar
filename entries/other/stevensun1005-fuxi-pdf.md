---
name: "fuxi-pdf · 复习pdf"
genre: "other"
url: "https://github.com/stevensun1005/fuxi-pdf"
repo: "stevensun1005/fuxi-pdf"
license: "unknown"
stars: 201
language: "Python"
created: "2026-10-21"
updated: "2026-10-22"
forks: 3
open_issues: 0
commits_30d: 12
commit_cadence: "weekly"
commits_90d: 12
size_kb: 8214
archived: false
flags: ["unverified"]
risk_notes: "READMEはSkill指示と構築・検証コードをMITと記載する一方、同梱の授業デモ、派生PDF、プレビューはCC BY-NC-SA 4.0と明記。第三者授業素材はコードのMITライセンスに含まれない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Ryrenz/status/2118283446736851080"]
fetched_at: "2026-11-11T15:18:10.287441+00:00"
---

# fuxi-pdf · 复习pdf

## 出来ること

- Codex skillとして、提供された授業資料から逐頁解説PDF、指定ページ数のcheatsheet、概念別の詳細な復習資料を作る。原ページ、説明、公式・条件、出典の対応を整理し、編集可能な原稿も残す。ページ数や言語の希望に応じて学習冊子、参考資料などの形式を選べる。

## 目的・背景

- 授業資料の内容を理解し、印刷や復習に使える形へ整理する。READMEは、原ページの追跡、式の適用条件、出典の記録を重視し、限られたページ数で省略した内容も記録すると説明している。

## 依存関係

- Codexなどローカルskillsに対応したホスト環境が必要。PDF生成には資料の読み取り、コンパイル、レンダリング機能と適切なフォントが必要で、LaTeXを優先し、Typstや明示されたMarkdown出力にも対応するとREADMEに記載。skillのインストールだけではPDFツール一式は導入されない。

## 実行条件

- 利用者がPDF/PPTXなどの資料を提供し、ページ数や言語を指定する。未指定なら希望を確認する。スキャン資料はホスト側のOCR等に依存し、読み取りや視覚確認ができない箇所は未決として扱う。

## 最短手順

- README記載の手順では、GitでリポジトリをCodexのskills/fuxi-pdfへ配置し、必要に応じて新しい会話を開始する。資料を添付し、「$fuxi-pdfを使って資料をcheatsheetにして」などと依頼する。

## 変更履歴

- 2026-11-11: 初回登録
