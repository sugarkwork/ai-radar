---
repo: "jarrodwatts/jev-trader"
name: "jev-trader"
genre: "finance-quant"
url: "https://github.com/jarrodwatts/jev-trader"
license: "MIT"
stars: 3135
language: "TypeScript"
created: "2026-09-16"
updated: "2026-10-13"
forks: 601
open_issues: 3
commits_30d: 4
commit_cadence: "weekly"
commits_90d: 16
size_kb: 69
archived: false
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "README の遅延値は作者によるモック推論のドライラン計測。実コードの起動、Jev 使用時の遅延・精度、実注文の約定率・収益性、Jev API の料金・利用条件は未検証。発見投稿の Nasdaq 先物成績は別リポジトリの実験。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115461838607659474"]
fetched_at: "2026-11-10T12:20:57+00:00"
---

# jev-trader — Monad のブロックごとに板を読み、Jev で売買方向を判定する実装

## 出来ること

- Kuru の MON-USDC 板を読み、売買方向の推論に応じて post-only 指値注文を差し替える。スナップショット、履歴、SSE で判断や約定イベントを取得できる。

## 目的・背景

- 板取得・推論・注文送信をブロックの時間予算に収める実装例。README による作者のモック使用時の計測では、板取得の中央値は 18 ms、ループ全体の中央値は 100 ms。

## 依存関係

- Bun と Monad RPC を使用する。package.json に AI SDK、TypeSafe AI プロバイダー、Kuru SDK、ethers 5 を記載。リポジトリは MIT。

## 実行条件

- PRIVATE_KEY を設定しない場合は実際の板を読み、約定をシミュレートする。既定の推論はモメンタムベースのモックで、Jev を使うには MODEL=jev と TYPESAFE_AI_API_KEY が必要。

## 最短手順

- README の手順に沿って .env.example を .env にコピーし、PRIVATE_KEY を設定せず bun install、bun run start の順に実行する。
- AI エージェントの HTTP ツールから GET / で最新状態を取得する。時系列を読む場合は GET /history、継続購読には GET /events を使う。これらはボットの観測用エンドポイント。

## 変更履歴

- 2026-11-10: 初回登録
