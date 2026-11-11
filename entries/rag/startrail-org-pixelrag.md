---
name: "PixelRAG"
genre: "rag"
url: "https://github.com/StarTrail-org/PixelRAG"
repo: "StarTrail-org/PixelRAG"
stars: 10889
forks: 980
open_issues: 25
size_kb: 48010
language: "Python"
created: "2026-05-29"
updated: "2026-11-05"
archived: false
license: "Apache-2.0"
commits_30d: 25
commits_90d: 54
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/dyfwsammy/status/2120128054915731961"]
fetched_at: "2026-11-10T23:11:56.259618+00:00"
---

# PixelRAG

## 出来ること

- Webページ、PDF、画像などをスクリーンショットタイルに変換し、画像を検索対象にするRAGパイプライン。READMEでは、表・チャート・レイアウトなどを画像に保ったまま検索できると説明しています。`pixelshot`によるページ撮影、Claude Code向け`pixelbrowse`スキル、独自文書のインデックス構築、FAISS検索APIの提供手順も記載されています。

## 目的・背景

- READMEによると、HTMLをテキストに変換する方式では表やレイアウトなどの視覚的構造が失われるため、文書を画像として扱い、適切な画像タイルを検索して回答に利用する構成です。

## 依存関係

- README記載の構成では、基本の`pixelshot`にPlaywright/CDPを使用します。埋め込み・インデックス・サーバー機能はそれぞれ`pixelrag[embed]`、`pixelrag[index]`、`pixelrag[serve]`として導入できます。PDF処理には`pixelrag[pdf]`とpopplerが必要です。学習用の`train/`は別のuvプロジェクトで、READMEには固定バージョンのTorch、Transformers、cuDNNが記載されています。

## 実行条件

- 独自文書のインデックス構築はREADMEにLinux（CUDA）およびmacOS（Apple Silicon/MPS）対応と記載されています。埋め込みデバイスは`auto`で選択できます。PDFの例ではPython 3.10以上、macOSまたはLinuxなどの環境とpopplerが案内されています。

## 最短手順

- ページを撮影する場合は`pip install pixelrag`の後、`pixelshot <URL> --output ./tiles`を実行します。独自文書の検索インデックスを作る場合は`pip install 'pixelrag[index]'`を行い、READMEの例に従って`pixelrag.yaml`に入力文書、埋め込みモデル、出力先を設定して`pixelrag index build`を実行し、`pixelrag serve --index-dir ./my_index --port 30001`で提供します。

## 変更履歴

- 2026-11-11: 初回登録
