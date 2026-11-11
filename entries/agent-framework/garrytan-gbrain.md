---
name: "GBrain"
genre: "agent-framework"
url: "https://github.com/garrytan/gbrain"
repo: "garrytan/gbrain"
flags: ["unverified"]
risk_notes: "READMEは作者の説明であり、記載された機能・性能を独立に検証したものではありません。"
stars: 32488
forks: 4838
open_issues: 807
size_kb: 456904
language: "TypeScript"
created: "2026-04-05"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2119950747898974362"]
fetched_at: "2026-11-10T23:14:26.028410+00:00"
---

# GBrain

## 出来ること

- 明示的な事実とその出典を保存し、訂正や撤回を扱い、複数エージェントから同じ記憶を利用できる。キーワード検索から始め、意味検索、回答合成、バックグラウンド補強を追加できるとREADMEに記載。MCP経由の接続や、知識グラフによる関係検索も説明されている。

## 目的・背景

- 既存エージェントの個性を保ったまま、エージェント間で共有できる記憶を持たせることを目的としている。READMEでは、検索結果のページ一覧を返すだけでなく、出典付きの回答を合成し、不明点も示す使い方を例示している。

## 依存関係

- READMEによると、キーレスで基本的な記憶とキーワード検索を開始できる。意味検索、合成、抽出などでクラウドプロバイダーを設定した場合、テキストが各プロバイダーに送信されることがある。常時稼働の補強には別途コンピュートとAPI設定が必要と記載。具体的な依存パッケージは、提示されたREADME抜粋からは確認できない。

## 実行条件

- セルフホスト可能で、READMEはMITライセンスかつ無料と説明している。既存エージェントへの接続、自分のコンピューターからのMCP公開、既存のホスト済み脳への接続という構成が示されている。ホストサービスgbrain.ioは任意の有料サービス。

## 最短手順

- READMEでは既存エージェントへの追加を推奨し、Grok Bot、Muse、Codex / Claude Code向けガイドを案内している。自分のコンピューターからMCPで利用する場合は `gbrain mcp expose` を実行し、クラウドエージェント向けには `--funnel` を追加する手順が示されている。

## 変更履歴

- 2026-11-11: 初回登録
