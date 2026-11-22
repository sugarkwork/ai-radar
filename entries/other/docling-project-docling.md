---
name: "Docling"
genre: "other"
url: "https://github.com/docling-project/docling"
repo: "docling-project/docling"
license: "MIT"
stars: 70669
language: "Python"
created: "2024-07-09"
updated: "2026-11-17"
forks: 5364
open_issues: 1064
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 482437
archived: false
flags: ["unverified"]
risk_notes: "個別モデルの利用条件は各モデルのライセンスに従う。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119131518920433826"]
fetched_at: "2026-11-17T02:22:22.975408+00:00"
---

# Docling

## 出来ること

- PDF、DOCX、PPTX、XLSX、HTML、画像、音声などの文書形式を解析し、Markdown、HTML、WebVTT、JSONなどへ出力する。PDFではページレイアウト、読み順、表構造、コード、数式などを扱う。OCR、音声認識、動画解析、MCPサーバー、APIサーバーもREADMEに記載されている。

## 目的・背景

- 多様な形式の文書解析と、生成AIエコシステムとの連携を簡素化することを目的としている。機微データやネットワーク隔離環境向けのローカル実行機能も記載されている。

## 依存関係

- READMEはPythonパッケージとしてのインストール方法を案内している。個別モデルを利用する場合は、モデルごとのライセンスを確認する。

## 実行条件

- READMEによるとPython 3.10以上が必要。macOS、Linux、Windowsで、x86_64とarm64の両方に対応すると記載されている。

## 最短手順

- `pip install docling` でインストールする。CLIでは `docling https://arxiv.org/pdf/2206.01062` を実行して文書をMarkdownへ変換できる。Pythonでは `DocumentConverter` を作成し、`convert(source)` の結果から `export_to_markdown()` を呼び出す例がREADMEにある。

## 変更履歴

- 2026-11-22: 初回登録
