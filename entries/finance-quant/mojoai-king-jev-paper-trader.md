---
repo: "MojoAI-King/jev-paper-trader"
name: "Jev Paper Trader"
genre: "finance-quant"
url: "https://github.com/MojoAI-King/jev-paper-trader"
license: "unknown"
stars: 3
language: "Python"
created: "2026-09-27"
updated: "2026-11-10"
forks: 1
open_issues: 0
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 260686
archived: false
flags: ["unverified"]
risk_notes: "GitHub上の表示版READMEを確認。現在の成績、動作の再現性、外部サービスの現行料金、最新リリースは未確認。コードの再配布・改変を許諾するライセンスは確認できていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115461838607659474"]
fetched_at: "2026-11-10T12:20:27+00:00"
---

# Jev Paper Trader — 予測市場でClaudeの調査が予測精度に効くかを比較する

## 出来ること

- PolymarketとKalshiの公開価格を読み取り、仮想資金10万ドルで模擬取引する。予測には市場価格を見せず、決着後にBrierスコアと模擬損益を集計する。

## 目的・背景

- 調査付きJev、調査なしJev、Claude単独の予測を比較し、同じ決着済み市場で市場価格も基準にする。READMEの2026年10月9日付報告では、約2週間の時点で全予測器の精度が市場価格を下回り、戦略は損失を出していた。

## 依存関係

- Python 3.9以上。調査にはClaudeプランで認証済みのClaude Code、Jevの呼び出しにはTypeSafe APIキーを使う。市場データはPolymarketとKalshiの公開フィードを参照する。

## 実行条件

- 実注文や実資金を伴わない。Claudeプランの利用枠を消費し、Jevの利用料がかかるとREADMEに記載がある。GitHub APIのライセンス値はunknown。

## 最短手順

- READMEのCLI手順では、端末を使えるAIエージェントからリポジトリ直下で `python3 -m papertrade markets` を呼び、Jevを使わず公開市場データを確認できる。
- 利用者が必要な認証を用意した環境では、同じ端末から `python3 -m papertrade ping` で接続を確認し、`python3 -m papertrade scan --limit 3` で少数の市場を試す。

## 変更履歴

- 2026-11-10: 初回登録
