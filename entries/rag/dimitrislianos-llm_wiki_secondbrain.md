---
repo: "DimitrisLianos/LLM_Wiki_SecondBrain"
name: "LLM_Wiki_SecondBrain"
genre: "rag"
url: "https://github.com/DimitrisLianos/LLM_Wiki_SecondBrain"
license: "MIT"
stars: 18
forks: 3
open_issues: 0
size_kb: 3870
language: "Python"
created: "2026-04-10"
updated: "2026-04-17"
archived: false
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "最新リリースの確認先は取得時にタイムアウトした。ページ生成数は著者報告。回答の正確性、全主張の検証機能、処理速度、メモリ使用量、オフライン動作は独立に確認していない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Bober_smart/status/2116978958121964030"]
fetched_at: "2026-11-10T08:13:07+00:00"
---

# LLM_Wiki_SecondBrain — ローカルLLMで資料をObsidian互換Wikiに変換

## 出来ること

- PDFやMarkdownなどからエンティティと概念を抽出し、相互リンク付きのMarkdownページを生成する。CLIでWikiへの質問やリンク構造の点検ができる。
- READMEでは、ローカル推論に関する約25件の資料から500ページ超を生成したと著者が報告している。

## 目的・背景

- KarpathyのLLM Knowledge Baseパターンを実装した概念実証。資料を取り込む段階でWikiを構築・更新し、質問時には蓄積したページを検索する。検索はSQLite FTS5とWikiリンクを組み合わせる。

## 依存関係

- 取り込み・質問のPythonコードは標準ライブラリで動く。推論にはGemma 4のGGUF重みとTurboQuant対応のllama.cppフォークを使い、PDFのテキスト抽出にはPopplerを使う。Web UIのFastAPI、検索拡張のddgs、閲覧用のObsidianは任意。コードはMIT。

## 実行条件

- Python 3.12以上。基準環境はApple Silicon搭載macOS。READMEはLinuxとWindows上のWSL 2の手順も示す。推奨RAMは32 GB以上で、16 GBはスループットが低下する場合の下限とされる。初期セットアップでモデル重みなどを取得した後、取り込みと質問の中核はオフラインで動く設計。

## 最短手順

- READMEのQuick Startに沿ってGGUF重みを配置し、CMakeでllama.cppフォークをビルドして `bash scripts/start_server.sh` でローカル推論サーバーを起動する。
- README記載のVaultディレクトリを作成し、資料を `obsidian_vault/raw/` に置いて `python3 scripts/ingest.py --all` を実行する。
- 端末実行権限のあるAIエージェントから、リポジトリのルートで `python3 scripts/query.py '質問'` を呼び、標準出力の回答を受け取る。

## 変更履歴

- 2026-11-10: 初回登録
