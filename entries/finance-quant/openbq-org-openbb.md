---
name: "Open Data Platform by OpenBB (ODP)"
genre: "finance-quant"
url: "https://github.com/openbq-org/OpenBB"
repo: "openbq-org/OpenBB"
license: "unknown"
stars: 75488
language: "Python"
created: "2020-12-20"
updated: "2026-11-15"
forks: 7898
open_issues: 114
commits_30d: 17
commit_cadence: "weekly"
commits_90d: 25
size_kb: 2439947
archived: false
flags: ["unverified"]
risk_notes: "README記載の通り、データが正確とは限らず、金融商品の取引には損失リスクがある。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/ruyi3699/status/2119220353964691525"]
fetched_at: "2026-11-17T15:14:02.841301+00:00"
---

# Open Data Platform by OpenBB (ODP)

## 出来ること

- READMEによると、ODPは独自・ライセンス付き・公開データソースを統合し、Python環境、OpenBB Workspace、Excel、MCPサーバー、REST APIなどから利用できるようにするデータ統合基盤。データ統合機能の一覧はPythonリファレンスに案内されている。

## 目的・背景

- データエンジニアが複数のデータソースを下流のアプリケーション、AIコパイロット、リサーチダッシュボードに接続するための「connect once, consume everywhere」基盤として説明されている。

## 依存関係

- README記載のWorkspace連携用バックエンドはPython 3.11〜3.14環境での利用を案内している。APIサーバーはFastAPIとUvicornで起動すると記載されている。

## 実行条件

- READMEのWorkspace連携手順ではPython 3.11〜3.14環境を用意し、`pip install openbb`の後に`openbb-api`を実行する。APIは`127.0.0.1:6900`で起動すると記載されている。

## 最短手順

- Pythonで`pip install openbb`を実行し、`from openbb import obb`で読み込み、例として`obb.equity.price.historical("AAPL")`を呼び出して`to_dataframe()`でデータフレームに変換する。ローカルAPIを使う場合はインストール後に`openbb-api`を起動する。

## 変更履歴

- 2026-11-22: 初回登録
