---
name: "rpn-gpt"
genre: "coding-agent"
url: "https://github.com/markab21/rpn-gpt"
repo: "markab21/rpn-gpt"
license: "MIT"
stars: 3
language: "Python"
created: "2026-11-06"
updated: "2026-11-07"
forks: 1
open_issues: 0
commits_30d: 23
commit_cadence: "daily"
commits_90d: 23
size_kb: 1117
archived: false
flags: ["unverified"]
risk_notes: "READMEの評価値や実行例は配布者の報告であり、独立に検証していない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/ai_hakase_/status/2119236467239100520"]
fetched_at: "2026-11-17T20:13:45.338326+00:00"
---

# rpn-gpt

## 出来ること

- READMEによると、言語モデルがForth形式のプログラムを生成し、モデル内のカーネルがトークン単位で実行・出力する構成。カーネルは標準的な層で構成され、重みはPythonプログラムで計算したと説明されている。モデル・LoRA・GGUF/Ollama・MLX形式・データセットへの配布リンクも掲載されている。

## 目的・背景

- 長い厳密算術で言語モデルが誤る問題に対し、通常の外部ツール呼び出しではなく、モデル内部に小さな計算機を置く方法を提示する。READMEは、容易な問題では機械の利用が性能を下げる一方、難しい問題ではスコアが上がったと報告し、学習で適切な利用を教える狙いを述べている。

## 依存関係

- READMEで確認できる構成要素は、NVIDIA Nemotron 3.5 Lightningをベースとしたモデル、LoRAアダプター、およびMamba-2等の標準層を使うカーネル。完全な依存パッケージ一覧は提示されたREADME抜粋からは確認できない。

## 実行条件

- READMEにはvLLMでの実行例として、1台のRTX PRO 6000でのライブリクエストが記載されている。また、specを外部のPythonループとして実行する評価・学習方式も説明されている。一般的な最低ハードウェア要件は確認できない。

## 最短手順

- README記載の例では、`uv run python kernel/show_stream.py '2 3 + .'` でForth入力のトークン列を表示する。モデルの配備手順はREADME内のplaybookへのリンクを参照。

## 変更履歴

- 2026-11-22: 初回登録
