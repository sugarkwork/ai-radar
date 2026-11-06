---
type: "repo"
name: "pagesift（Webと文書をMarkdown/JSONに落とすAGPLの自前ホスト型パーサ）"
genre: "rag"
url: "https://github.com/YOLOW92/pagesift"
repo: "YOLOW92/pagesift"
license: "AGPL-3.0（商用ライセンスあり）"
stars: 244
language: "Rust"
created: "2026-10-20"
updated: 2026-11-04
added: "2026-11-06"
first_seen: "2026-11-05"
sources: ["https://x.com/Ryrenz/status/2118161886894080121"]
flags: []
risk_notes: "ライセンスは AGPL-3.0。自前ホストしてネットワーク越しにサービスとして提供すると AGPL のソース開示義務が及びうるため、製品に組み込む場合は商用ライセンス（docs/COMMERCIAL.md）の検討が要る。速度・メモリの数値はすべてベンダー自身のベンチマークで、比較条件は docs/benchmarks.md にある。投稿の『PDF処理のピークメモリ32MB、Doclingは3.6GB以上』は README の『ブラウザ無しでワーカーあたり18〜377MB（OCRで式モデルを使う場合は約1.7GB）』という表記と水準が異なるので、数値は条件依存と見るべき。投稿も認めるとおり高速クロールは spider などに劣る。既定で robots.txt とレート制限に従うが、対象サイトの規約・著作権は利用者の責任。"
forks: 32
open_issues: 0
commits_30d: 100
commit_cadence: daily
size_kb: 41314
archived: false
fetched_at: "2026-11-06T09:14:17Z"
last_release: v1.1.2
last_release_at: 2026-11-04
commits_90d: 100
---

# pagesift — URL・PDF・Office・メール・アーカイブを、エージェントが読めるMarkdown/JSONに変換する単体バイナリ

## 出来ること

- 入力は URL、HTML、**スキャンPDF（OCR）**、画像（OCR）、Word（.docx/.doc）、Excel（.xlsx/.xlsb/.xls）、PowerPoint（.pptx/.ppt）、OpenDocument、RTF、WordPerfect、HWP、EPUB、MOBI、FB2、メール（.eml/.mbox/.msg）、圧縮ファイル（zip/tar/gz/bz2/xz/7z）、SQLite、dBASE、CSV、Markdown、**373種のソースコード/設定言語**、WARC
- 出力は Markdown、HTML、生HTML、リンク、画像、メタデータ、スキーマ準拠のJSON。**結果が不完全なときは警告を付ける**
- OCR は PP-OCRv6（スキャン頁）と PP-FormulaNet（表示式）を pure Rust で回す。CPU でも動き、NVIDIA GPU があれば速くなる
- 構造化抽出：CSSセレクタによるJSON抽出（サイト構造が変わるとセレクタを自動で引き直す）、またはモデルに一度スキーマを書かせてキャッシュする方式
- ブラウザ操作：クリック・入力・スクロール、セッションを保持したまま続行
- クロール：サイトマップ対応、目標に寄与しなくなったら止まる「クエリ指向クロール」（`--adaptive`）、トラップ回避、robots.txt とホスト単位のレート制限
- 変更監視：日付・カウンタ・広告を除いた実質的な変更だけを検出し、webhook で通知
- **エージェント連携（本命）**：MCPサーバ（stdio / HTTP）、Python・Node.js/TypeScript・Rust・C ABI（Go/Java/Kotlin/C#/Ruby/PHP/Lua/Perl/Dart/Swift/Zig）、LangChain・LlamaIndex
- **既存コードをほぼ変えずに移行できる**：Firecrawl v1/v2 API と Jina Reader（`/r/`、`/s/`）に互換。Firecrawl のSDKは接続先URLを変えるだけで動く
- `/v2/agent`：自前のモデルで「質問＋スキーマ」から1ステップずつ計画し、検索・map・scrape・extract を実行する。各フィールドは根拠の頁と突き合わせて検証され、JSON＋出典＋警告で返る
- 運用向けにゲートウェイ／ワーカー／スタンバイ構成、ジョブ永続化、監査ログ、メトリクスも持つ

## 目的・背景

- RAG やエージェントの「餌やり」工程が、Web用クローラ・PDF用パーサ・OCR・Office変換とバラバラの道具の寄せ集めになり、遅くて壊れやすい。pagesift はそこを1つの Rust バイナリに畳む
- 既存のクラウド（Firecrawl など）の置き換えを狙っており、API互換を前面に出している。月額を止めたいが書き直しはしたくない、という移行経路を用意している
- ベンダーの計測（README 記載）：PDF→Markdown 2.4ms/頁（pypdf は 50.0ms、20.49倍）、HTML→Markdown 0.24ms/頁（Turndown は 1.9ms、8.12倍）、本文抽出 1.0ms/頁、Office 91.7ファイル/秒。olmOCR-bench 1,269頁の公式スコアは 0.645（pymupdf4llm は 0.484）

## 依存関係

- 配布形態は単体バイナリ：`cargo install pagesift --locked`、`pip install pagesift`、`npm install @pagesift/node`、Docker イメージ `ghcr.io/yolow92/pagesift`
- HTTP・PDF・Office の処理には**追加インストール不要**
- 任意：JavaScript ページ用のブラウザ、OCR 用の NVIDIA GPU、`/v2/agent` 用の自前モデル
- 対応プラットフォーム：Linux x86_64/aarch64（glibc 2.28以上と musl）、macOS arm64、Windows x86_64

## 実行条件

- メモリはブラウザ無しでワーカーあたり 18〜377MB（ベンチマーク1.1の範囲）。OCR で式モデルを使うと約1.7GB。容量は cgroup の制限から自動で見積もる
- robots.txt・レート制限・プライベートネットワーク/DNSリバインディングのガードは全ページに適用される。`/v2/agent` でモデルが選べるのは URL とクエリだけで、取得オプションは選べない
- **AGPL-3.0**。ネットワーク越しに第三者へ提供する形で使うなら、商用ライセンスかソース開示の判断が必要
- HTTP サーバ運用時は `PAGESIFT_API_KEYS` で認証を有効にする（例に `sk-test` が載っているが、これは例示であって既定値ではない）
- 高速クロールは専用クローラに劣る（README にも記載）

## 最短手順

```bash
# 1) 入れる（いずれか）
cargo install pagesift --locked
# pip install pagesift
# npm install @pagesift/node

# 2) 単発変換
pagesift scrape https://example.com
pagesift scrape report.pdf
pagesift --ocr scrape scan.pdf              # スキャンPDF。モデルは初回に取得される

# 3) まとめて取る
pagesift crawl https://docs.rs --limit 500 --out ./data/
pagesift crawl https://www.example.edu --query "graduate admission" --adaptive

# 4) 環境の点検（ブラウザ・GPU・モデル）
pagesift doctor

# 5) MCPサーバとしてエージェントに繋ぐ
pagesift mcp                                 # stdio（1エージェント向け）
pagesift mcp http --port 3003                # 共有サービス
claude mcp add --scope user --transport http pagesift http://127.0.0.1:3003/mcp

# 6) Firecrawl 互換のHTTPサーバを自前ホスト
docker run -d -p 3002:3002 -v pagesift-data:/data \
  -e PAGESIFT_API_KEYS=sk-xxxx ghcr.io/yolow92/pagesift:1.1.2
curl -s localhost:3002/v2/scrape -H 'Authorization: Bearer sk-xxxx' \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","formats":["markdown"]}'
```

MCPツール名：`pagesift_scrape` / `pagesift_batch_scrape` / `pagesift_crawl` / `pagesift_crawl_status` / `pagesift_map` / `pagesift_interact` / `pagesift_interact_stop`、モデル設定時は `pagesift_agent` / `pagesift_agent_status`。

## 変更履歴

- 2026-11-06: 初回登録
