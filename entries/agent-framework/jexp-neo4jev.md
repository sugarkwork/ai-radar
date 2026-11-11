---
name: "neo4jev — Graph Navigation Demo (TypeSafe Jev + Neo4j)"
genre: "agent-framework"
url: "https://github.com/jexp/neo4jev"
repo: "jexp/neo4jev"
flags: ["unverified"]
risk_notes: "TypeSafe APIの利用にはTYPESAFE_API_KEYが必要。READMEによると、既定のベクトル埋め込みは決定論的なハッシュ由来のプレースホルダーで、意味的な検索にはならない。"
stars: 184
forks: 27
open_issues: 2
size_kb: 6655
language: "Jupyter Notebook"
created: "2026-09-16"
updated: "2026-09-18"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 39
commit_cadence: "monthly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2120147118237114757"]
fetched_at: "2026-11-11T06:10:34.954075+00:00"
---

# neo4jev — Graph Navigation Demo (TypeSafe Jev + Neo4j)

## 出来ること

- Neo4jのノードから隣接関係を1ホップずつ探索する。各ホップでTypeSafeの`system_one`構造化判定APIに関係候補を渡し、次に進む候補の確率分布を取得する。上位候補や確率しきい値を使ったビームサーチで経路を選び、`neo4j-viz`で周辺グラフとともに表示する。自由記述のゴール、特定ノード、経路パターンの3種類のゴールに対応するとREADMEは説明している。出典: https://github.com/jexp/neo4jev

## 目的・背景

- 自由文の生成ではなく構造化された選択結果を使ってNeo4jグラフを探索するデモ。`Choice`による次ホップ選択と、ゴール到達を判定する`Noul`を同じ`system_one`呼び出しで扱う設計。READMEのStatus欄では、ノートブックとアプリは`companies2`グラフに対して実行され、APIキーがない場合は明示的にラベル付けされた代替回答を使うと説明している。これは作者の報告であり、独立した動作確認ではない。出典: https://github.com/jexp/neo4jev

## 依存関係

- Python 3.12以上、`uv`が必要。READMEに記載された主な構成要素はNeo4j、TypeSafeの`system_one` API、`neo4j-viz`、Streamlit。ノートブック実行には別途Jupyter環境が必要と記載されている。出典: https://github.com/jexp/neo4jev

## 実行条件

- 依存関係をインストールし、`.env`にNeo4j接続情報を設定する。ナビゲーターのTypeSafe API呼び出しには`TYPESAFE_API_KEY`が必要。既定の接続先は公開Companies KGの`companies2`。READMEによると、探索時は1種類あたり最大10関係、合計最大60関係に制限され、上限外の関係は候補にならない。出典: https://github.com/jexp/neo4jev

## 最短手順

- READMEの手順に従い`uv sync`で依存関係をインストールし、`.env.example`を`.env`にコピーしてNeo4j接続情報と`TYPESAFE_API_KEY`を設定する。ノートブックはJupyterを追加した環境で`notebooks/`から実行する。Streamlitアプリは`app/streamlit_app.py`にある。出典: https://github.com/jexp/neo4jev

## 変更履歴

- 2026-11-11: 初回登録
