---
name: "PyBreaker"
genre: "other"
url: "https://github.com/danielfm/pybreaker"
repo: "danielfm/pybreaker"
license: "BSD-3-Clause"
stars: 702
language: "Python"
created: "2010-10-17"
updated: "2026-09-25"
forks: 97
open_issues: 29
commits_30d: 0
commit_cadence: "stale"
commits_90d: 1
size_kb: 186
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:22:20.934365+00:00"
---

# PyBreaker

## 出来ること

- 危険な外部連携処理をCircuit Breakerで保護するPython実装。失敗閾値とリセット時間の設定、例外の除外、イベントリスナー、ジェネレーター関数の保護、状態の監視・管理に対応するとREADMEに記載されています。Redisによる状態保存とTornado非同期呼び出しはオプションです。

## 目的・背景

- READMEでは、連携先の障害がシステム全体へ波及するのを防ぐため、障害中の呼び出しを回避するCircuit Breakerパターンの実装と説明しています。

## 依存関係

- README記載の基本要件はPython 3.10以降です。Redis保存を使う例ではredisクライアント、Tornado非同期対応ではTornadoを使用しています。

## 実行条件

- Redis保存を使う場合、READMEはRedis接続のdecode_responsesをTrueにしないよう注意しています。外部サービスへの接続では、API側で対応していればタイムアウトを設定するよう推奨しています。

## 最短手順

- READMEの手順は `pip install pybreaker`。`import pybreaker` の後、例では `pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)` を作成し、デコレーター、`call()`、または `calling()` で保護対象を呼び出します。

## 変更履歴

- 2026-11-22: 初回登録
