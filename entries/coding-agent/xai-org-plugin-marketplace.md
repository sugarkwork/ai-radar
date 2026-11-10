---
repo: "xai-org/plugin-marketplace"
name: "xAI Plugin Marketplace"
genre: "coding-agent"
url: "https://github.com/xai-org/plugin-marketplace"
stars: 325
forks: 1222
open_issues: 1287
size_kb: 3010
language: "Python"
created: "2026-05-15"
updated: "2026-11-09"
archived: false
license: "unknown"
commits_30d: 31
commits_90d: 81
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "['最新リリースのタグと公開日は未確認。プラグインの導入・実行、個別機能の有効性や安全性、料金、ライセンスおよび利用条件は未検証。README は公開 raw URL で確認した。'] GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117591176048005131"]
fetched_at: "2026-11-10T09:44:32+00:00"
---

# xAI Plugin Marketplace — Grok Build の公式プラグインカタログ

## 出来ること

- Grok Build 向けプラグインの取得元をカタログで探し、生成済みの索引でスキル、コマンド、サブエージェント、フック、MCP・LSP サーバーなどの同梱機能を導入前に確認できる。 [README](https://raw.githubusercontent.com/xai-org/plugin-marketplace/main/README.md)

## 目的・背景

- 正本の `.grok-plugin/marketplace.json` がリポジトリ内のディレクトリまたは外部リポジトリを指す。外部ソースは完全なコミット SHA に固定し、README によれば Grok Build が取得後に一致を確認する。 [README](https://raw.githubusercontent.com/xai-org/plugin-marketplace/main/README.md)

## 依存関係

- 導入には Grok Build を使う。外部ソース型のプラグインを導入するには、指定された上流リポジトリと固定コミットを取得できる必要がある。 [README](https://raw.githubusercontent.com/xai-org/plugin-marketplace/main/README.md)

## 実行条件

- 公式ガイドでは、導入して有効化したプラグインを Grok が読み込み、フックと MCP サーバーの起動にはそのプラグインを信頼する設定が必要とされる。各プラグインには個別のライセンスと利用条件が適用され、第三者製プラグインはローカルでコードを実行しデータへアクセスする場合がある。 [公式プラグインガイド](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/09-plugins.md) [README](https://raw.githubusercontent.com/xai-org/plugin-marketplace/main/README.md)

## 最短手順

- Grok Build CLI で `grok plugin marketplace add xai-org/plugin-marketplace` を使ってカタログを追加する。追加済みなら Grok の `/plugins` から Marketplace タブを開く。 [公式プラグインガイド](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/09-plugins.md)
- 目的のプラグインを選んで導入・有効化する。MCP を使う場合は内容を確認して信頼を設定し、Grok の会話で対象の MCP ツールを使うよう依頼する。具体的なツール名と利用条件は選んだプラグインの資料で確認する。 [公式プラグインガイド](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/09-plugins.md)

## 変更履歴

- 2026-11-10: 初回登録
