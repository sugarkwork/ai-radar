---
name: "shodan-python"
genre: "other"
url: "https://github.com/achillean/shodan-python"
flags: ["unverified"]
risk_notes: "READMEにはライセンス情報がなく、ライセンスは確認できていない。利用にはShodan APIキーが必要。 GitHub APIでライセンスを確認できていません。"
repo: "achillean/shodan-python"
stars: 3487
forks: 785
open_issues: 64
size_kb: 448
language: "Python"
created: "2010-09-07"
updated: "2024-08-05"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118713263290741015"]
fetched_at: "2026-11-13T20:10:45.297706+00:00"
---

# shodan-python

## 出来ること

- READMEは、Shodanの検索、IP情報の高速・一括照会、リアルタイムのストリーミングAPI、ネットワークアラート管理、Exploit検索API、データの一括ダウンロード、Shodan DNS DBのドメイン情報参照、およびコマンドラインインターフェースを機能として挙げている。これらはREADMEの説明であり、独立した性能測定ではない。

## 目的・背景

- READMEによると、Shodanはインターネットに接続されたデバイスを検索するサービスで、このライブラリはShodanに保存されたデータへプログラムからアクセスし、タスクの自動化や既存ツールとの統合を行うためのもの。

## 依存関係

- READMEには依存パッケージの一覧は記載されていない。インストール方法としてpipおよびeasy_installを案内している。

## 実行条件

- READMEの例ではPythonから`shodan`をインポートし、Shodan APIキーを渡して利用する。APIキーの取得先として`https://account.shodan.io`を案内している。サービス側の料金や利用条件はREADMEに記載されていない。

## 最短手順

- README記載の手順は、`pip install shodan`でインストールし、ShodanからAPIキーを取得したうえで、`from shodan import Shodan`、`api = Shodan('MY API KEY')`のように初期化すること。IP照会例は`api.host('8.8.8.8')`。

## 変更履歴

- 2026-11-14: 初回登録
