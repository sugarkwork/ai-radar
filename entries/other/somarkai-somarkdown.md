---
name: "SoMarkDown"
genre: "other"
url: "https://github.com/SoMarkAI/SoMarkDown"
repo: "SoMarkAI/SoMarkDown"
license: "MIT"
stars: 34
language: "JavaScript"
created: "2026-02-19"
updated: "2026-09-09"
forks: 2
open_issues: 1
commits_30d: 0
commit_cadence: "stale"
commits_90d: 2
size_kb: 489
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119370852126908922"]
fetched_at: "2026-11-19T19:14:26.546280+00:00"
---

# SoMarkDown

## 出来ること

- MarkdownソースをHTML文字列へ変換するコンパイラ。CommonMark互換をうたい、数式（KaTeX、mhchem）、SMILES化学構造（SmilesDrawer）、コードブロックの強調表示（highlight.js）、目次生成、画像表示、図表キャプションに対応するとREADMEに記載。ブラウザーとNode.jsの両方で利用できる。

## 目的・背景

- 専門的なレンダリング機能を備えたMarkdown処理と、LLMが解析しやすい簡潔で曖昧さの少ないMarkdown標準を目指している。SoMarkの文書解析製品の解析結果を扱うプロトコルとしても用いるとREADMEに記載。

## 依存関係

- READMEが挙げる統合コンポーネントはmarkdown-it、KaTeX、SmilesDrawer、highlight.js。各コンポーネントのバージョンや実行時依存の詳細はREADMEに記載なし。

## 実行条件

- npmパッケージとして導入し、JavaScriptから利用する。Node.jsサーバー側とブラウザーに対応するとREADMEに記載。READMEにはNode.jsの必要バージョンや対応ブラウザーの指定なし。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- npm install somarkdown を実行し、JavaScriptで `import SoMarkDown from 'somarkdown'` とCSSを読み込む。`new SoMarkDown({lineNumbers:{enable:true}})` で初期化し、`render(markdown)` でMarkdown文字列をHTMLに変換する。

## 変更履歴

- 2026-11-23: 初回登録
