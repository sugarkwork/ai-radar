---
name: "Prefect"
genre: "other"
url: "https://github.com/PrefectHQ/prefect"
repo: "PrefectHQ/prefect"
license: "Apache-2.0"
stars: 24173
language: "Python"
created: "2018-06-29"
updated: "2026-11-17"
forks: 2667
open_issues: 876
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 254610
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:16:01.623437+00:00"
---

# Prefect

## 出来ること

- Pythonのデータパイプラインをワークフローとして構築・実行し、スケジュール、キャッシュ、リトライ、イベント連動の自動化を利用できます。ワークフローの活動はセルフホストのPrefect serverまたはPrefect Cloudで監視できます。

## 目的・背景

- 既存のスクリプトを本番運用可能なワークフローへ発展させるためのオーケストレーション基盤として紹介されています。

## 依存関係

- READMEの導入要件としてPython 3.11以上が記載されています。

## 実行条件

- PrefectをインストールしたPython環境で実行します。UIで活動を確認する例では `prefect server start` でサーバーを起動します。

## 最短手順

- `pip install -U prefect` または `uv add prefect` で導入します。Pythonファイルで `from prefect import flow, task` を読み込み、関数に `@task` と `@flow` を付けてワークフローを定義し、`flow` 関数を呼び出します。READMEにはGitHub APIからスター数を取得する例があります。

## 変更履歴

- 2026-11-22: 初回登録
