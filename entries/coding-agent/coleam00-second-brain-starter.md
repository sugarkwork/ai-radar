---
repo: "coleam00/second-brain-starter"
name: "Second Brain Starter"
genre: "coding-agent"
url: "https://github.com/coleam00/second-brain-starter"
license: "unknown"
stars: 885
language: "unknown"
created: "2026-03-29"
updated: "2026-06-09"
forks: 188
open_issues: 1
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 614
archived: false
flags: ["unverified"]
risk_notes: "スキルは未実行。生成PRDの品質、連携先ごとの動作、対応バージョン、運用費用、ライセンス条件は未確認。GitHubの公開リリース一覧の取得結果にはリリースが表示されず、最新リリースへの直接アクセスはタイムアウトした。READMEは公開raw URLおよびGitHubの表示から確認した。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Bober_smart/status/2117619229465641097"]
fetched_at: "2026-11-10T10:03:12Z"
---

# Second Brain Starter — Claude Codeで個人向けAIアシスタントの構築計画を作る

## 出来ること

- 利用ツール、優先タスク、自律度、許可範囲を記入した要件から、実装順と段階間の依存関係を含む9段階のPRDを生成する。各機能の実装はPRD生成後の工程になる。

## 目的・背景

- Markdownの記憶層を軸に、セッションフック、キーワードとベクトルを併用する検索、外部連携、定期チェック、チャット、セキュリティ強化、デプロイを段階的に設計する。

## 依存関係

- PRD生成にはClaude Codeと同梱の要件テンプレートを使う。READMEの構築例はClaude Agent SDK、Python、Obsidian vaultを用いる。外部サービスの組み合わせは利用者の要件で決まる。

## 実行条件

- スキルを配置したプロジェクトでClaude Codeを開く。READMEのフローでは、要件と設計資料の読解に加え、利用ツールやAPIをWeb検索で調べ、プロジェクト内にPRDを書き出す。

## 最短手順

- リポジトリの `.claude/skills/create-second-brain-prd/` をプロジェクトの同じ相対パスにコピーする。
- 同梱の `my-second-brain-requirements.md` をプロジェクト直下にコピーし、利用ツール、優先タスク、許可範囲を記入する。
- プロジェクトでClaude Codeを開き、`/create-second-brain-prd ./my-second-brain-requirements.md` を呼び出す。READMEが示す出力先は `.agent/plans/second-brain-prd.md`。

## 変更履歴

- 2026-11-10: 初回登録
