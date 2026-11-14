---
name: "MiniMind"
genre: "other"
url: "https://github.com/jingyaogong/minimind"
repo: "jingyaogong/minimind"
stars: 65230
forks: 8542
open_issues: 63
size_kb: 39476
language: "Python"
created: "2024-07-27"
updated: "2026-10-27"
archived: false
license: "Apache-2.0"
commits_30d: 10
commits_90d: 59
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118880615348969714"]
fetched_at: "2026-11-14T20:10:32.337669+00:00"
---

# MiniMind

## 出来ること

- READMEでは、Dense・MoEモデルの構造、Tokenizer、事前学習、SFT、LoRA、RLHF/RLAIF、Tool Use、Agentic RL、蒸留などのコードと学習手順を提供すると説明しています。評価用コード、OpenAI API互換サーバー、StreamlitチャットUIも記載されています。

## 目的・背景

- 大規模モデルの高い計算資源や抽象化された第三者ライブラリに頼らず、LLMの構造と学習過程をコードから理解し、小規模モデルの学習を試せるようにすることを目的としています。

## 依存関係

- READMEのクイックスタートではPython依存パッケージをrequirements.txtからインストールします。説明では主要アルゴリズムをPyTorchで実装し、transformers、trl、peftなどとの互換性も挙げています。個別の手順で必要となる依存関係は対象機能により異なります。

## 実行条件

- README記載の作者環境はUbuntu 20.04、Python 3.10.16、CUDA 12.2、RTX 3090×8、RAM 128 GBです。これは参考環境としての記載です。SFTの1 epochを単一RTX 3090で約2時間・GPUレンタル約3元とする記述は作者の報告で、一般的な実行条件や独立実測を示すものではありません。

## 最短手順

- READMEの例では、リポジトリをcloneし、requirements.txtから依存パッケージを導入します。推論を試す場合はModelScopeまたはHugging Faceからモデルを取得し、eval_llm.pyにモデルの場所を指定します。READMEに記載されたコマンドは手順の紹介であり、ここでは実行していません。

## 変更履歴

- 2026-11-14: 初回登録
