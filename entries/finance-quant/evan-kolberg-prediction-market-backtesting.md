---
name: "prediction-market-backtesting"
genre: "finance-quant"
url: "https://github.com/evan-kolberg/prediction-market-backtesting"
repo: "evan-kolberg/prediction-market-backtesting"
license: "unknown"
stars: 1267
language: "Python"
created: "2026-02-13"
updated: "2026-05-16"
forks: 201
open_issues: 5
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 164736
archived: false
flags: ["unverified"]
risk_notes: "READMEには開発中とある。Limitless.exchangeとOpinion.tradeは今後の予定で、Kalshiは公開実行可能なバックテスト経路ではないと記載。ライセンスはAPI上unknownだが、READMEのバッジはMIT + LGPL-3.0-or-laterを示すため、適用範囲は確認が必要。README抜粋にある情報のみを記載。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116886377698578543"]
fetched_at: "2026-11-10T14:08:08.079008+00:00"
---

# prediction-market-backtesting

## 出来ること

- Polymarketの予測市場戦略をNautilusTrader上でバックテストする。READMEでは、Rustネイティブのデータ変換、段階的なデータ読み込み、キャッシュ、実験オブジェクトを使うランナー、統計的最適化のサポート、複数市場のチャート機能を紹介している。

## 目的・背景

- 予測市場戦略のバックテスト用フレームワークとして説明されている。Polymarket向けのカスタム取引所アダプターを備える。Limitless.exchangeとOpinion.tradeは今後の対応予定。Kalshi関連コンポーネントは調査・手数料モデル用で、公開された実行可能なバックテスト経路ではない。

## 依存関係

- README記載の基盤はNautilusTrader 1.226.0。READMEのバッジはPython 3.12以上、Rust 1.93.1、Rust Edition 2024を示している。

## 実行条件

- README抜粋には詳細な環境構築条件やデータ取得条件が含まれていないため、具体的な実行要件は未確認。

## 最短手順

- README抜粋内に具体的なインストール・実行コマンドはない。詳細ガイドはREADMEからSetupとFirst Runのドキュメントへ案内されている。

## 変更履歴

- 2026-11-11: 初回登録
