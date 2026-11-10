---
repo: "MehmetGoekce/llm-wiki"
name: "llm-wiki"
genre: "rag"
url: "https://github.com/MehmetGoekce/llm-wiki"
license: "MIT"
stars: 164
language: "unknown"
created: "2026-04-08"
updated: "2026-11-07"
forks: 29
open_issues: 1
commits_30d: 33
commit_cadence: "daily"
commits_90d: 42
size_kb: 729
archived: false
flags: ["unverified"]
risk_notes: "取り込み精度、全主張の事実検証、トークン削減量、実環境での動作は未検証。公開リリース一覧ではv1.8.1にLatest表示がある一方、取得した最新リリースページはv1.7.1に転送されたため、最新タグと公開日時は未確定。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Bober_smart/status/2116978958121964030"]
fetched_at: "2026-11-10T08:12:35+00:00"
---

# llm-wiki — Claude Codeで育てる二層構成のMarkdown Wiki

## 出来ること

- 資料を取り込んでWikiページを作成・更新し、相互リンクを張る。Claude CodeからWikiを検索でき、lintで孤立ページや壊れた参照などを点検できる。

## 目的・背景

- KarpathyのLLM Wiki構想をClaude Codeで実装する。毎回必要な運用ルールはL1のClaude Codeメモリに置き、案件の経緯などはL2のWikiから必要に応じて参照する。

## 依存関係

- Claude Codeと、LogseqのグラフまたはObsidianの保管庫を使う。リポジトリはMIT。Claude Codeの利用条件と料金は別途適用される。

## 実行条件

- Wikiルートには書き込み権限が必要。READMEではセッション内の一行インストールにClaude Code 2.1.275以降が必要とし、2.1.296でのテストを報告している。Wikiはローカルに保存され、資料の内容はClaudeが処理する。

## 最短手順

- Claude Codeのセッションで `/plugin install llm-wiki --marketplace MehmetGoekce/llm-wiki` を実行し、Wikiルートを指定する。
- 同じセッションで `/llm-wiki setup` を呼び出し、利用するWiki形式と名前空間を選ぶ。
- `/llm-wiki ingest <資料>` で取り込み、`/llm-wiki query <質問>` で参照する。`/llm-wiki lint` でWikiを点検する。

## 変更履歴

- 2026-11-10: 初回登録
