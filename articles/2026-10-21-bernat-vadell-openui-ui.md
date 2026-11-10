---
name: "OpenUIで表データの取得をUI生成と分ける"
genre: "article"
url: "https://x.com/bernvadell/status/2112918558879449539"
author: "Bernat Vadell"
published: "2026-10-21"
flags: ["unverified"]
risk_notes: "原文は公開ミラー経由。性能や費用の実測はない。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/bernvadell/status/2112918558879449539"]
fetched_at: "2026-11-10T04:14:38Z"
---

# OpenUIで表データの取得をUI生成と分ける

## テーマ

- 生成UIとバックエンドから取得するデータを分ける構成。

## 著者の主張

- モデルはQueryにツールと引数を指定し、ランタイムが取得した結果をUIに渡す。

## 裏取り・注意点

- 公式仕様で再取得とクライアント集計を確認。取得・描画コストはデータ量に依存し得る。

## 出典

- https://www.openui.com/docs/openui-lang/queries-mutations
- https://www.openui.com/docs/openui-lang/functions

## 変更履歴

- 2026-11-10: 初回登録
