---
name: "SoPDF"
genre: "other"
url: "https://github.com/SoMarkAI/SoPDF"
repo: "SoMarkAI/SoPDF"
license: "unknown"
stars: 20
language: "Python"
created: "2026-03-30"
updated: "2026-04-14"
forks: 3
open_issues: 1
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 176
archived: false
flags: ["unverified"]
risk_notes: "README記載の性能値と精度比較は配布者による報告で、独立した実測ではない。GitHub APIでライセンスはunknownと確認した一方、READMEはApache 2.0と記載しているため、ライセンスファイルの内容は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119370852126908922"]
fetched_at: "2026-11-19T19:14:51.650421+00:00"
---

# SoPDF

## 出来ること

- PDFを開いてPNG/JPEGに描画し、テキストや座標付きテキストブロックを抽出、全文検索できます。ページの分割・複数PDFの結合、圧縮保存、ページ回転、文書メタデータの読み書き、目次の取得、暗号化PDFの読み書き、破損PDFの自動修復にも対応するとREADMEに記載されています。

## 目的・背景

- READMEは、PDFの描画・テキスト処理と構造編集を一つのPython APIで扱うライブラリとして説明しています。描画とテキスト抽出にpypdfium2、構造の読み書きにpikepdfを使う構成です。性能比較の数値はREADMEに掲載された配布者のベンチマーク報告です。

## 依存関係

- READMEによると、描画とテキスト処理にpypdfium2、構造編集と書き込みにpikepdfを使用します。画像エンコードにはopencv-pythonを使用すると記載されています。

## 実行条件

- README記載の条件はPython 3.10以上です。macOS、Linux、Windows向けにネイティブ依存関係のビルド済みwheelがあるとされています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- `pip install sopdf` で導入し、Pythonコードで `import sopdf`、`with sopdf.open("document.pdf") as doc:` として開きます。ページ描画は `doc[0].render(dpi=150)`、テキスト抽出は `doc[0].get_text()`、検索は `doc[0].search("invoice", match_case=False)` の例がREADMEにあります。

## 変更履歴

- 2026-11-23: 初回登録
