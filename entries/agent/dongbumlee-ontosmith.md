---
type: "repo"
repo: "Dongbumlee/ontosmith"
name: "ontosmith"
genre: "agent"
url: "https://github.com/Dongbumlee/ontosmith"
license: "MIT"
stars: 223
language: "Python"
created: "2026-10-22"
updated: "2026-11-08"
forks: 23
open_issues: 1
commits_30d: "100+"
commits_90d: "100+"
commit_cadence: "daily"
size_kb: 32035
archived: false
added: "2026-11-09"
fetched_at: "2026-11-09T03:42:27Z"
flags: ["unverified"]
risk_notes: "MIT。引用が実在しても関係が真とは限らず、出典付き記録は数学的証明ではない。モデル判定や費用を実データで検証する必要がある。 実行・品質は未検証。"
sources: ["https://x.com/i/status/2119417274314396148", "https://github.com/Dongbumlee/ontosmith"]
---

# ontosmith

## 出来ること

文書からエンティティと関係を候補化し、原文の根拠・型チェックと別モデルの判定を経て知識グラフを構築する。

## 目的・背景

人間が承認する型定義を先に作り、候補生成と採否判定を分離。結果に出典と根拠テキストを保持する。

## 依存関係

Python 3.11以上。実データのグラフ構築にはNeo4jとLLM接続、Jev判定モデルが必要。

## 実行条件

Linuxで開発・テスト、WindowsはWSL2。デモの一部はAPIキー不要だが実構築は別。

## 最短手順

`pip install ontosmith`。公式READMEのkeylessデモから始め、独自データではスキーマを承認して接続を設定する。

## 注意点

MIT。引用が実在しても関係が真とは限らず、出典付き記録は数学的証明ではない。モデル判定や費用を実データで検証する必要がある。 実行・品質は未検証。

## 出典

- [公式リポジトリ](https://github.com/Dongbumlee/ontosmith)
- [紹介投稿](https://x.com/i/status/2119417274314396148)
