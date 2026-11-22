---
name: "Celery"
genre: "other"
url: "https://github.com/celery/celery"
repo: "celery/celery"
license: "unknown"
stars: 29219
language: "Python"
created: "2009-04-24"
updated: "2026-11-17"
forks: 5265
open_issues: 813
commits_30d: 76
commit_cadence: "daily"
commits_90d: 100
size_kb: 38346
archived: false
flags: ["unverified"]
risk_notes: "README上の最新版5.7.xの実行条件はPython 3.11+またはPyPy 3.11+（v8+）。Windowsはサポート対象外と記載。API計測ではlicenseがunknownのため、ライセンスはREADME本文から確認できず。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:19:25.633344+00:00"
---

# Celery

## 出来ること

- タスクキューを使ってスレッドやマシン間に作業を配布する。クライアントがタスクのメッセージをブローカーへ送り、ワーカープロセスがキューを監視して処理する。複数のワーカーとブローカーで高可用性や水平スケーリングを構成できる。

## 目的・背景

- 分散したワーカーに単位作業（タスク）を配布する仕組みとして説明されている。

## 依存関係

- 通常はメッセージブローカーを使用する。READMEではRabbitMQとRedisのトランスポートを機能対応済みとして挙げ、SQLiteをローカル開発向けの実験的サポートとして記載している。

## 実行条件

- Celery 5.7.xはPython 3.11+またはPyPy 3.11+（v8+）で動作。READMEではWindowsをサポートしていないが、動作する可能性はあるとしている。

## 最短手順

- READMEの最小例では、`from celery import Celery`、`app = Celery('hello', broker='amqp://guest@localhost//')`でアプリを作り、`@app.task`を付けた関数をタスクとして定義する。実行にはブローカー接続が必要。

## 変更履歴

- 2026-11-22: 初回登録
