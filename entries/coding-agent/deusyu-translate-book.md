---
name: "Rainman Translate Book"
genre: "coding-agent"
url: "https://github.com/deusyu/translate-book"
repo: "deusyu/translate-book"
license: "MIT"
stars: 2425
language: "Python"
created: "2026-03-15"
updated: "2026-11-07"
forks: 279
open_issues: 2
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 16
size_kb: 11578
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/bkdgiffug/status/2118920628938088657"]
fetched_at: "2026-11-16T21:43:49Z"
last_release: ""
last_release_at: ""
---

# Rainman Translate Book

## 出来ること

- PDF/DOCX/EPUBまたはMarkdownの書籍をチャンクに分け、既定で8並列のサブエージェントに翻訳させる。隣接チャンクの短い抜粋を参照でき、マニフェストのハッシュ検証、再開・選択的な再翻訳、結合後のHTML・DOCX・EPUB・PDF出力に対応するとREADMEに記載されている。

## 目的・背景

- READMEによると、書籍全体を単一セッションで翻訳する際のコンテキスト蓄積と出力切り詰めを避けるため、各チャンクを独立したサブエージェントで処理する。

## 依存関係

- Codex、Claude Code、OpenClawのいずれかのエージェント実行環境、Calibreのebook-convert、Pandoc、Python 3、必須のpypandocが必要。beautifulsoup4は目次生成改善用の任意依存。数式・表が多いPDFを先にMarkdown化する場合はMinerUまたはMarkerを任意で利用する。

## 実行条件

- Calibreのebook-convertコマンドが利用可能で、PandocとPython 3がインストールされていること。各エージェント環境でスキルを利用可能にし、翻訳対象の書籍ファイルを指定する。

## 最短手順

- README記載のCodex向け導入例は `npx skills add deusyu/translate-book -a codex -g`。導入後、Codexに `$translate-book Translate /path/to/book.pdf into Chinese.` のように依頼する。処理後のファイルは `{book_name}_temp/` に保存される。

## 変更履歴

- 2026-11-15: 初回登録
