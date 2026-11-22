---
name: "Semantic Router"
genre: "agent-framework"
url: "https://github.com/aurelio-labs/semantic-router"
repo: "aurelio-labs/semantic-router"
stars: 4033
forks: 396
open_issues: 102
size_kb: 117032
language: "Python"
created: "2023-10-30"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 21
commits_90d: 100
commit_cadence: "daily"
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:23:46.086073+00:00"
---

# Semantic Router

## 出来ること

- READMEによると、入力文を定義済みルートと照合してLLMやエージェントの判断を振り分ける。`IndexedRouter`による埋め込み検索、`DecisionRouter`による判断モデルの利用、複数ルーターの`Chain`や`Merge`、キーワードを併用するハイブリッド検索、画像ルーティングが紹介されている。READMEは判断がミリ秒単位で行われ、信頼度を確率として調整できると説明しているが、性能や精度の独立した実測値はここでは確認していない。

## 目的・背景

- READMEでは、遅いLLM生成を待ってツール利用などを決める代わりに、ルートへの振り分けを担う判断レイヤーとして説明されている。

## 依存関係

- READMEのローカルQuickstartは`semantic-router[fastembed]`とFastEmbedのローカル埋め込みモデルを使う。OpenAI、Cohere、Hugging Faceなどのエンコーダーも利用できると記載されている。

## 実行条件

- README記載のローカルQuickstartではAPIキーなしで実行できる。Pythonからパッケージを導入し、ルートとエンコーダーを定義して`IndexedRouter`を作成する。

## 最短手順

- READMEの例に沿って、`pip install -qU "semantic-router[fastembed]"`で導入する。`Route`に名前と発話例を設定し、`FastEmbedEncoder(name="BAAI/bge-small-en-v1.5")`と`IndexedRouter(encoder=encoder, routes=routes)`を作成する。`router("how's the weather today?").name`のように入力を渡してルート名を得る。該当ルートなしを許容する例では、未見のラベル付きクエリで`router.fit(...)`を行い、`confidence_threshold`を設定する。

## 変更履歴

- 2026-11-22: 初回登録
