---
name: "unstructured"
genre: "rag"
url: "https://github.com/Unstructured-IO/unstructured"
repo: "Unstructured-IO/unstructured"
license: "Apache-2.0"
stars: 15750
language: "HTML"
created: "2022-09-26"
updated: "2026-11-17"
forks: 1402
open_issues: 446
commits_30d: 83
commit_cadence: "daily"
commits_90d: 100
size_kb: 242024
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119131518920433826"]
fetched_at: "2026-11-17T02:22:33.897292+00:00"
---

# unstructured

## 出来ること

- PDF、HTML、Word文書などの画像・テキスト文書を取り込み、LLM向けデータ処理ワークフローのために前処理し、非構造化データを構造化出力へ変換する。出典: https://github.com/Unstructured-IO/unstructured

## 目的・背景

- データ取り込みと前処理を簡素化し、さまざまなプラットフォームに適応できるようにすることを目的としている。READMEはオープンソース版とTransform v2 APIのベンチマーク比較も掲載しているが、その比較はREADME記載の評価条件に基づく。出典: https://github.com/Unstructured-IO/unstructured

## 依存関係

- README記載の導入例ではPythonパッケージを使用する。処理する文書形式に応じて追加依存が必要となり、例としてlibmagic-dev、poppler-utils、tesseract-ocr、libreofficeが挙げられている。

## 実行条件

- Python環境で利用できる。プレーンテキスト、HTML、XML、JSON、メールは追加依存なしの例として `pip install unstructured` が示されている。ほかの形式では対応するextrasやシステム依存が必要な場合がある。

## 最短手順

- プレーンテキスト等を処理する場合は `pip install unstructured` を実行し、`from unstructured.partition.auto import partition` を読み込んで `partition(filename="example-docs/eml/fake-email.eml")` を呼び出す。README記載の手順。

## 変更履歴

- 2026-11-22: 初回登録
