---
repo: "karpathy/minbpe"
name: "minbpe"
genre: "other"
url: "https://github.com/karpathy/minbpe"
flags: ["unverified"]
risk_notes: "最新リリース、対応するPython・依存ライブラリのバージョン範囲、cl100k_baseとの出力一致、実行時間は未検証。互換性と所要時間はREADMEの著者報告に基づく。"
stars: 11021
forks: 1150
open_issues: 59
size_kb: 256
language: "Python"
created: "2024-02-16"
updated: "2024-07-01"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115051970251628961"]
fetched_at: "2026-11-10T11:50:52+00:00"
---

# minbpe — バイトレベルBPEを学ぶPython実装

## 出来ること

- 手持ちのテキストから語彙とマージ規則を学習し、文字列をトークンID列へ変換して復号できる。BasicTokenizerとRegexTokenizerで事前分割の影響を比較できる。

## 目的・背景

- UTF-8の256種類のバイトを初期語彙とし、学習テキストで最頻の隣接ペアを順にマージする。RegexTokenizerはマージの前にテキストを分割するため、分割境界をまたぐマージが生じない。

## 依存関係

- Pythonで動作する。RegexTokenizerはregex、GPT4Tokenizerはtiktokenを使う。READMEのテスト手順にはpytestが必要。ライセンスはMIT。

## 実行条件

- BasicTokenizerで学習する際は入力テキストと256以上の目標語彙サイズを指定する。READMEのデモは同梱テキストで2種類のトークナイザーを学習し、語彙をファイルへ保存する。

## 最短手順

- リポジトリのルートで `python -m pip install -r requirements.txt` を実行し、`python train.py` で同梱テキストの学習例を試す。
- AIエージェントから試す場合は、Python実行環境で `from minbpe import BasicTokenizer` とし、インスタンスの `train(text, vocab_size)`、`encode(text)`、`decode(ids)` を順に呼ぶ。まず反復を含む短文と語彙サイズ257で、復号結果を元の文字列と比較する。

## 変更履歴

- 2026-11-10: 初回登録
