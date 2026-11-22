---
name: "Mem0"
genre: "agent-framework"
url: "https://github.com/mem0ai/mem0"
flags: ["unverified"]
risk_notes: "ベンチマーク値はMem0の管理プラットフォームでの結果で、READMEはオープンソース版では同一の数値にならないと説明している。"
repo: "mem0ai/mem0"
stars: 69090
forks: 8224
open_issues: 959
size_kb: 69585
language: "Python"
created: "2023-06-20"
updated: "2026-11-17"
archived: false
license: "Apache-2.0"
commits_30d: 7
commits_90d: 85
commit_cadence: "weekly"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119161717586366650"]
fetched_at: "2026-11-17T06:30:38.950239+00:00"
---

# Mem0

## 出来ること

- AIアシスタントやエージェントに記憶レイヤーを追加し、ユーザー、セッション、エージェントの状態を保持する。READMEは、ユーザーの好みの記憶や、過去の会話・サポート履歴を用いた応答などを用途として挙げている。

## 目的・背景

- パーソナライズされたAIとのやりとりを可能にするため、ユーザーの好みなどを記憶し、時間とともに適応するメモリレイヤーを提供する。

## 依存関係

- ライブラリ利用にはPythonのmem0aiパッケージまたはnpmのmem0aiパッケージを使う。ハイブリッド検索とエンティティ抽出向けのNLP追加機能にはmem0ai[nlp]とspaCyの英語モデルが必要。

## 実行条件

- READMEはMem0の動作にLLMが必要と説明している。利用形態としてライブラリ、セルフホスト型サーバー、クラウドプラットフォームを案内している。

## 最短手順

- Pythonライブラリは `pip install mem0ai` で導入し、READMEのBasic Usageにある例に沿って利用する。セルフホスト型サーバーは `cd server && make bootstrap` で起動・初期設定する手順が示されている。

## 変更履歴

- 2026-11-22: 初回登録
