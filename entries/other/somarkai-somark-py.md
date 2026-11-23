---
name: "somark-py"
genre: "other"
url: "https://github.com/SoMarkAI/somark-py"
repo: "SoMarkAI/somark-py"
license: "unknown"
stars: 1
language: "Python"
created: "2026-05-20"
updated: "2026-05-20"
forks: 1
open_issues: 1
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 15929
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119370852126908922"]
fetched_at: "2026-11-19T19:15:14.192504+00:00"
---

# somark-py

## 出来ること

- SoMark向けのPython SDKとCLIを提供する。READMEが挙げる公式ドキュメントの対象は、認証、CLI利用、SDK例、非同期タスク、ローカルプレビュー、PDFユーティリティ、APIパラメーター、エラー処理。

## 目的・背景

- READMEによると、SoMark共通のSDK・CLI仕様に沿ったPython実装で、JavaScript/TypeScript実装は別リポジトリにある。

## 依存関係

- リモート解析と利用状況の照会にはSoMark APIキーが必要。ローカルPDFユーティリティとSoMarkDownプレビューにはAPIキー不要。

## 実行条件

- Python 3.10以上。Docker/UbuntuでPDFをレンダリングする場合、libxcb1、libgl1、libglib2.0-0のシステムライブラリが必要になることがある。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- `pip install somark` でインストールする。利用方法や認証、CLI・SDKの詳細はREADMEが案内する公式ドキュメントを参照。

## 変更履歴

- 2026-11-23: 初回登録
