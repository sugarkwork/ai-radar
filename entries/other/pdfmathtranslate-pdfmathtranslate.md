---
repo: "PDFMathTranslate/PDFMathTranslate"
name: "PDFMathTranslate"
genre: "other"
url: "https://github.com/PDFMathTranslate/PDFMathTranslate"
flags: ["unverified"]
risk_notes: "翻訳精度、レイアウトの保持度、実行速度、実験的OCRの品質、CLIとMCPの動作は独立検証していない。mainブランチの記載と配布版の機能差、最新リリースのタグと公開日時、翻訳サービスごとの料金とデータ取扱条件は未確認。"
stars: 38342
forks: 3433
open_issues: 171
size_kb: 185522
language: "Python"
created: "2024-09-06"
updated: "2026-11-10"
archived: false
license: "AGPL-3.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2114967848775041508"]
fetched_at: "2026-11-10T11:46:50+00:00"
---

# PDFMathTranslate — 論文PDFのレイアウトに配慮した翻訳CLI

## 出来ること

- 科学論文などのPDFを翻訳する。公式READMEでは数式、図表、目次、注釈を保持する設計としており、翻訳先のサービスにはGoogle、DeepL、Ollama、OpenAIなどを選べる。

## 目的・背景

- 本文の翻訳とPDFのレイアウト処理を組み合わせ、翻訳後も論文の構造を追えるようにする。公式READMEはレイアウト解析にDocLayout-YOLOを挙げている。

## 依存関係

- パッケージ名はpdf2zh。主な依存関係にはPyMuPDF、pdfminer-six、ONNX Runtimeがある。MCPはオプション依存で、翻訳サービスに応じて接続設定が必要になる。

## 実行条件

- 公式のローカル導入手順はPython 3.11〜3.12を指定する。リポジトリのライセンスはAGPL-3.0で、外部翻訳サービスの料金と利用条件はサービスごとに異なる。

## 最短手順

- Python 3.11または3.12の環境で `pip install pdf2zh` を実行し、作業ディレクトリで `pdf2zh document.pdf` を実行する。
- AIエージェントからは、シェルツールで同じCLIに入力PDFのパスを渡す。MCP対応クライアントでは `pip install 'pdf2zh[mcp]'` で追加依存を導入し、stdioサーバーのコマンドに `pdf2zh`、引数に `--mcp` を指定する。

## 変更履歴

- 2026-11-10: 初回登録
