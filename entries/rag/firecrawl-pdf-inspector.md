---
repo: "firecrawl/pdf-inspector"
name: "pdf-inspector"
genre: rag
url: "https://github.com/firecrawl/pdf-inspector"
license: "MIT"
stars: 19820
language: "Rust"
created: "2026-02-06"
updated: 2026-10-22
added: "2026-11-04"
first_seen: "2026-11-04"
sources: []
flags: []
risk_notes: ""
forks: 1335
open_issues: 255
size_kb: 14138
archived: false
commits_30d: 1
commits_90d: 0
commit_cadence: weekly
last_release: "v1.25.2"
---

# pdf-inspector

## 出来ること

- PDF が「テキスト型 / スキャン画像型 / 画像のみ / 混在」のどれかを 10〜50ms で判定し、信頼度とページ単位の OCR ルーティングを返す。テキスト型なら OCR を省ける。
- 位置情報つきのテキスト抽出（フォント、X/Y 座標、多段組の読み順、回転した文字の角度）。
- Markdown 変換: 見出し（フォントサイズ比で H1〜H4）、箇条書き・番号付きリスト、コードブロック（等幅フォント判定）、表（罫線ベース＋ヒューリスティック）、強調、URL リンク、ページ区切り。
- Rust ライブラリ本体に加え、CLI、Python / Node.js バインディング、ブラウザ用 WebAssembly を同梱。Rust と CLI では選択的な OCR も呼べる。
- Firecrawl の主張では、テキスト型 PDF の約54% を OCR サービスに送らずに済ませられる。

## 目的・背景

RAG の前処理で「とりあえず全部 OCR」に掛かるコストを削るための判定器兼抽出器。Firecrawl が自社パイプライン用に作り、MIT で公開している。README では 200ms 未満でテキスト型 PDF を処理するとしている。

## 依存関係

- Rust 1.7x 以降（クレート `pdf-inspector`）、または `pip install pdf-inspector` / `npm i @firecrawl/pdf-inspector`。
- ブラウザ利用は WASM ビルド。OCR を併用する場合は別途 OCR エンジンが必要。

## 実行条件

- ライセンスは MIT。
- **直近30日のコミットは1件**で、更新は落ち着いている（v1.25.2）。
- 画像のみの PDF は当然 OCR が必要。判定は誤る場合があるので、信頼度を見て分岐させる前提の設計。

## 最短手順

```bash
pip install pdf-inspector
```

```python
import pdf_inspector

result = pdf_inspector.process_pdf("document.pdf")
print(result.pdf_type, result.confidence, result.page_count)   # text_based / 0.0-1.0 / ページ数
```

- OCR を併用するページがある場合のみ PDFium と ONNX Runtime の共有ライブラリが必要（`PDFIUM_LIB_PATH` / `ORT_DYLIB_PATH`）。モデルは初回に取得してチェックサム検証される。
- README 掲載のベンチマーク（opendataloader-bench 200件、OCR 無効）では総合 0.875 で、pymupdf4llm 0.735 / markitdown 0.589 を上回るとしている。ベンダー自身の計測で、第三者による追試は確認していない。

## 変更履歴

- 2026-11-04: 初回登録（★19,820 / MIT / Rust / 最終push 2026-10-22 / v1.25.2）
