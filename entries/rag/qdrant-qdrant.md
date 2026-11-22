---
name: "Qdrant"
genre: "rag"
url: "https://github.com/qdrant/qdrant"
repo: "qdrant/qdrant"
license: "Apache-2.0"
stars: 35598
language: "Rust"
created: "2020-05-30"
updated: "2026-11-16"
forks: 2820
open_issues: 805
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 76690
archived: false
flags: ["unverified"]
risk_notes: "README記載の量子化によるRAM使用量最大97%削減は公式資料の説明であり、独立実測値ではない。Dockerの起動例は認証なしで全ネットワークインターフェースに公開されるため、本番利用前に公式のセキュリティ手順を確認する必要がある。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119101320187560002"]
fetched_at: "2026-11-16T21:19:02.555653+00:00"
---

# Qdrant

## 出来ること

- ベクトル類似検索エンジン／ベクトルデータベースとして、ベクトルと追加ペイロードの保存・検索・管理を提供する。Dense・Sparse・Multi-vector検索、ペイロード条件によるフィルタリング、複数ベクトルのハイブリッド検索、量子化とディスク上ストレージ、シャーディングとレプリケーションによる分散配置に対応するとREADMEに記載。量子化はRAM使用量を最大97%削減すると説明されているが、これはREADMEの記載であり独立実測ではない。

## 目的・背景

- ニューラルネットワークや意味ベースのマッチング、ファセット検索などに利用するための検索基盤。埋め込みやニューラルネットワークのエンコーダーを、マッチング・検索・推薦などのアプリケーションに組み込めるとREADMEは説明している。

## 依存関係

- READMEでは、ローカルでサーバーを試す方法としてDockerコンテナの起動例を案内している。Pythonクライアントの接続例も記載されている。その他の依存関係はREADME抜粋から確認できない。

## 実行条件

- README掲載のクライアントサーバー起動例は `docker run -p 6333:6333 qdrant/qdrant`。READMEは、この例が認証なしで全ネットワークインターフェースに公開される安全でない構成だと明記し、本番デプロイ前にインストールおよびセキュリティガイドを読むよう案内している。

## 最短手順

- READMEの例に従い `docker run -p 6333:6333 qdrant/qdrant` でローカルサーバーを起動し、Qdrantクライアントから接続する。認証なしで全ネットワークインターフェースに公開される構成なので、公開環境や本番環境で使う前にREADMEが案内するセキュリティ手順を確認する。

## 変更履歴

- 2026-11-22: 初回登録
