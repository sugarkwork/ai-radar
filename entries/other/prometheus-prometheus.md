---
name: "Prometheus"
genre: "other"
url: "https://github.com/prometheus/prometheus"
repo: "prometheus/prometheus"
stars: 67664
forks: 11031
open_issues: 1107
size_kb: 297194
language: "Go"
created: "2012-11-24"
updated: "2026-11-16"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119139068374290493"]
fetched_at: "2026-11-17T03:14:18.349839+00:00"
---

# Prometheus

## 出来ること

- 設定したターゲットから一定間隔でメトリクスを収集し、ルール式を評価して結果を表示し、指定条件に応じてアラートを発生させる。PromQLによるクエリ、サービスディスカバリまたは静的設定、グラフ・ダッシュボード、フェデレーションにも対応する。出典: https://github.com/prometheus/prometheus

## 目的・背景

- Prometheusは、システムとサービスの監視システムとして説明されている。時系列データはメトリクス名とキー・値の次元で定義され、単一サーバーノードは分散ストレージに依存せず自律して動作する。出典: https://github.com/prometheus/prometheus

## 依存関係

- ソースからビルドする場合、READMEはGo（go.mod指定バージョン以上）、NodeJS（web/ui/.nvmrc指定バージョン以上）、npm 10以上を必要条件としている。出典: https://github.com/prometheus/prometheus

## 実行条件

- READMEには、リリース版の事前コンパイル済みバイナリを使う方法と、Dockerイメージを使う方法が記載されている。ソースからビルドした場合、go installで作成した実行ファイルはWeb資産をリポジトリ内から読むため、リポジトリのルートから起動する必要がある。出典: https://github.com/prometheus/prometheus

## 最短手順

- README記載のDockerで試す手順は `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`。この候補の評価ではコマンドの実行は行っていない。出典: https://github.com/prometheus/prometheus

## 変更履歴

- 2026-11-22: 初回登録
