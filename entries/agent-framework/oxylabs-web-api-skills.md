---
repo: "oxylabs/web-api-skills"
name: "web-api-skills"
genre: agent-framework
url: "https://github.com/oxylabs/web-api-skills"
license: "MIT"
stars: 13
language: "Python"
created: "2026-08-23"
updated: "2026-11-09"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 1
open_issues: 0
commits_30d: 11
commit_cadence: "weekly"
size_kb: 103
archived: false
commits_90d: 30
fetched_at: "2026-11-09T21:34:23Z"
last_release: ""
last_release_at: ""
---

# web-api-skills

## 出来ること

- Oxylabs の Web API をコーディングエージェントから使うためのスキル集。3本構成:
  - `oxylabs-web-api` … MCP ツール、エンドポイントのパラメータ、レイテンシ、エラー、リトライ、CLI ヘルパーの扱い。
  - `oxylabs-web-research` … 調査の進め方（検索 → 情報源の選別 → 読解 → 引用）。
  - `migrate-to-oxylabs` … Tavily、Exa、Firecrawl、Perplexity、Brave、Linkup からの移行。
- `.mcp.json` を同梱し、MCP サーバー経由の型付きツールとしても使える（任意、推奨）。
- skills 対応エージェント（Claude Code、Cursor、Codex など）で動く。Claude Code ではプラグインとしても導入可能。

## 目的・背景

検索・取得 API ベンダー自身が配布する「エージェント向けの使い方スキル」。API リファレンスを読ませる代わりに、失敗時のリトライや引用の作法まで含めて同梱する形。

## 依存関係

- Oxylabs の Web API 契約と API キー（`OXYLABS_WEB_API_KEY`）。**他製品のキーは使えない**（Web API インスタンスを作って発行する必要がある、と明記）。
- MCP サーバーは任意。使う場合は別リポジトリの `web-api-mcp` を組み合わせる。

## 実行条件

- **有料サービス前提**。Oxylabs の Web API は契約が必要で、無料枠の有無は未確認（このリポジトリに料金の記述はない）。
- スキル自体は MIT だが、API 利用は契約条件に従う。
- ★11 と知名度は低い。一次情報（ベンダー公式リポジトリ）である点以外に、第三者による評価は確認できていない。

## 最短手順

```bash
npx skills add oxylabs/web-api-skills
export OXYLABS_WEB_API_KEY=<key>
```

## 変更履歴

- 2026-11-03: 初回登録（★11 / pushed 2026-10-13 / MIT）
