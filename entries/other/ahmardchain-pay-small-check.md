---
name: "Pay Small Check"
genre: "other"
url: "https://github.com/ahmardchain/pay-small-check"
repo: "ahmardchain/pay-small-check"
license: "MIT"
stars: 1
language: "TypeScript"
created: "2026-11-06"
updated: "2026-11-07"
forks: 0
open_issues: 0
commits_30d: 32
commit_cadence: "daily"
commits_90d: 32
size_kb: 2839
archived: false
flags: ["unverified"]
risk_notes: "判定の正確さや詐欺被害を防ぐ効果は確認できない。README記載の購入者価格は1チェックあたり$0.08。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/RoundtableSpace/status/2118834560280690699"]
fetched_at: "2026-11-14T12:13:38.610332+00:00"
---

# Pay Small Check

## 出来ること

- READMEでは、XまたはInstagramのハンドルを入力すると、有料の読み取り結果をもとにSafe／Caution／Riskyと理由・根拠投稿を返すと説明されている。Xは6種類の読み取り、Instagramは5種類と、投稿ショートコードがある場合のコメント読み取りを記載。Facebookはcoming soonで、チェック対象ではない。出典: https://github.com/ahmardchain/pay-small-check

## 目的・背景

- 購入前に販売者のアカウント情報、投稿、返信などを確認し、判定の根拠と決済記録を公開レシートから追えるようにする目的がREADMEに記載されている。判定による被害防止の実効性は示されていない。出典: https://github.com/ahmardchain/pay-small-check

## 依存関係

- README記載のスタックはCloudflare Workers、Hono、D1、viem、@x402/*、@celo/attribution-tags。X・Instagramのデータ読み取りはbuy gateway経由と説明されている。出典: https://github.com/ahmardchain/pay-small-check

## 実行条件

- README記載では、購入者価格は1チェックあたり$0.08で、Celo mainnetを使用する。USDT、USDC、USA₮でのx402決済、またはUSDT／cUSDのtransferを案内している。実行に必要な開発環境や認証情報の詳細は、提供されたREADME抜粋から確認できない。出典: https://github.com/ahmardchain/pay-small-check

## 最短手順

- READMEのデモ手順では、アプリでXまたはInstagramを選択し、ハンドルを入力、通貨を選んで支払い、結果と公開レシートを確認する。ライブアプリの利用・支払いは行っていない。出典: https://github.com/ahmardchain/pay-small-check

## 変更履歴

- 2026-11-14: 初回登録
