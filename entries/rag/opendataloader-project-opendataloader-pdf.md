---
repo: "opendataloader-project/opendataloader-pdf"
name: "OpenDataLoader PDF"
genre: rag
url: "https://github.com/opendataloader-project/opendataloader-pdf"
license: "Apache-2.0"
stars: 30261
language: "Java"
created: "2025-05-13"
updated: "2026-11-09"
added: "2026-11-05"
first_seen: "2026-11-04"
source_post: "https://x.com/bkdgiffug/status/2118101482209993194"
sources: ["https://opendataloader.org"]
flags: []
risk_notes: ""
forks: 2897
open_issues: 28
size_kb: 90857
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
fetched_at: "2026-11-09T21:42:37Z"
last_release: "v2.5.20"
last_release_at: "2026-11-06"
---

# OpenDataLoader PDF

## 出来ること

- PDF を Markdown / HTML / JSON に変換する。JSON は要素ごとのバウンディングボックス付きなので、RAG のチャンクに出典位置を紐づけられる。
- 2つのモードがある。**ローカル（既定）** は決定的な処理だけで完結し、README の記載では 1ページ 0.015 秒。**ハイブリッド** は複雑な表・スキャン・数式を AI で補い、200件の実 PDF で総合 0.907・表 0.928 と主張している。
- 段組・読み順は XY-Cut++ 系のレイアウト解析で処理し、見出し・段落・表・画像を種別付きで切り出す。
- スキャン PDF 向けに OCR（80 言語以上）をハイブリッドモードで内蔵。
- 付随機能として、タグ無し PDF をタグ付き PDF に自動変換するアクセシビリティ処理がある（PDF Association の Well-Tagged PDF 仕様に沿い、veraPDF で検証。PDF/UA への書き出しは enterprise 版）。
- SDK は Python / Node.js / Java。LangChain 連携も用意されている。
- `--filter-hidden-text` で不可視の隠しテキストを除ける（v2.5.19、ネイティブ処理のみ）。README は「可視テキストも一緒に消えることがある」と注意している。

## 目的・背景

PDF をそのまま LLM に渡すと、読み順・表・座標が落ちる。ここは「AI に食わせられる構造データ」に変換することと、アクセシビリティ対応（手作業の PDF レメディエーションは1文書 $50〜200 とされる）を同じパイプラインで扱うことを狙っている。Dual Lab（veraPDF の開発元）との協働で仕様準拠を担保している、と README にある。

## 依存関係

- **Java 11 以上が必須**（`java -version` で確認。Python パッケージも内部で JVM を起動する）。Python 3.11 以上。
- `pip install -U opendataloader-pdf`、`npm` の `@opendataloader/pdf`、Maven の `opendataloader-pdf-core`。
- ハイブリッドモードは外部の AI 処理を呼ぶため、ローカルのみで完結させたい場合は既定モードを使う。

## 実行条件

- ライセンスは Apache-2.0（コア）。PDF/UA 書き出しと Accessibility Studio は enterprise の有料アドオン。
- `convert()` は呼ぶたびに JVM プロセスを起動するので、複数ファイルは1回の呼び出しにまとめる（README が明記）。
- 精度の数値（0.907 / 0.928 / 0.015 秒/page）はいずれも**作者側のベンチマーク**。第三者の追試は確認していない。

## 最短手順

```python
import opendataloader_pdf

opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json",
)
```

## 変更履歴

- 2026-11-05: 初回登録（★30,166 / Apache-2.0 / Java / 最終push 2026-11-04）
- 2026-11-05: v2.5.19 — 隠しテキスト除去の `--filter-hidden-text` を追加。段組・リスト・共有フォーム・タグ付けの読み取り修正が多数。Node 版の依存が minimatch 11 / glob 14 に上がる（6139f07）
