---
repo: "n8n-io/n8n"
name: "n8n"
genre: "agent-framework"
url: "https://github.com/n8n-io/n8n"
license: "unknown"
stars: 209990
language: "TypeScript"
created: "2019-06-22"
updated: "2026-11-10"
forks: 61430
open_issues: 1225
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 803402
archived: false
last_release: "n8n@2.47.3"
last_release_at: "2026-11-09"
flags: ["unverified"]
risk_notes: "公式資料で機能と設定手順を確認。Docker起動、MCP接続、ワークフロー実行は未試験。発見投稿のGrok Botとの接続や節約効果は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117960732184633699"]
fetched_at: "2026-11-10T11:13:28+00:00"
---

# n8n — AIエージェントとアプリ連携のワークフロー自動化

## 出来ること

- アプリ連携、分岐、カスタムコードを組み合わせてワークフローを構築できる。MCP対応のAIクライアントから、アクセスを許可したワークフローを呼び出せる。 [公式MCPドキュメント](https://docs.n8n.io/connect/connect-to-n8n-mcp-server.md)

## 目的・背景

- ビジュアルキャンバスを使い、定型処理とAIモデルによる処理を同じフローに組み込む。 [公式README](https://github.com/n8n-io/n8n/blob/master/README.md)

## 依存関係

- セルフホストのクイックスタートではDockerを使用する。外部AIからの呼び出しには、n8nに到達できるMCP対応クライアントと接続認証が必要。 [公式README](https://github.com/n8n-io/n8n/blob/master/README.md) [公式MCPドキュメント](https://docs.n8n.io/connect/connect-to-n8n-mcp-server.md)

## 実行条件

- Dockerの起動例はポート5678を使い、n8nのデータをボリュームに保存する。セルフホストと公式クラウドが選べる。 [公式README](https://github.com/n8n-io/n8n/blob/master/README.md)
- Sustainable Use Licenseの対象部分は、社内業務、非商用または個人利用に使用・変更が限られ、再配布は非商用かつ無償に限られる。一部のEnterpriseコードには別ライセンスが適用される。 [ライセンス原文](https://raw.githubusercontent.com/n8n-io/n8n/master/LICENSE.md)

## 最短手順

- READMEの手動Docker手順で起動し、http://localhost:5678 のエディターでテストデータを返すワークフローを作る。 [公式README](https://github.com/n8n-io/n8n/blob/master/README.md)
- AIから呼ぶには、管理者またはインスタンス所有者が Settings → Instance-level MCP でMCPを有効にし、対象ワークフローの Available in MCP をオンにする。Connectに表示されるサーバーURLを対応クライアントに設定してOAuthで接続し、実行権限を付与したうえで、クライアントから対象フローをテスト実行する。 [公式MCPドキュメント](https://docs.n8n.io/connect/connect-to-n8n-mcp-server.md)

## 変更履歴

- 2026-11-10: 初回登録
