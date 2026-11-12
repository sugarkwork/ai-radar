---
name: "Axion 1.0"
genre: "agent-framework"
url: "https://github.com/bytedance/axion1_0"
repo: "bytedance/axion1_0"
stars: 72
forks: 6
open_issues: 4
size_kb: 4045
language: "Python"
created: "2026-11-02"
updated: "2026-11-11"
archived: false
license: "Apache-2.0"
commits_30d: 39
commits_90d: 39
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/ai_hakase_/status/2118569827044360253"]
fetched_at: "2026-11-12T19:08:45.737408+00:00"
---

# Axion 1.0

## 出来ること

- 科学・数学の自己完結型推論問題とツール依存型推論問題のデータ構築、2段階の教師あり微調整（SFT）、非同期GRPOによる強化学習、ベンチマークの準備と採点のコードを提供する。READMEは、ツール利用時の検索・ウェブページ閲覧・学術情報取得・Pythonとのエージェント対話をRLの対象として記載している。

## 目的・背景

- READMEは、基盤モデルの能力を活用して推論問題を強化し、ツールを要するタスクでは公開データから参照回答をプログラムで構成・検証する学習レシピを説明している。Axionモデルのベンチマーク結果も掲載されているが、ここでは独立実測ではなくREADMEに記載された報告値として扱う。

## 依存関係

- READMEによると、SFTはSwiftとMegatron-FSDP、RLはverlを使用する。データ構築と評価用にはPython 3.11以上の別環境を用意し、`python -m pip install -e ".[data,evaluation]"`を実行する手順が示されている。

## 実行条件

- 学習ガイドは単一ホスト・複数ホストの構成、必要なサービス、チェックポイントのエクスポート、実行時要件を扱う。README記載の122B SFTレシピは32 GPU、128Kコンテキストウィンドウ、global batch 8。報告されている学習コストは35Bで約90 GPU時間、122Bで240 GPU時間であり、READMEは122Bレシピのmicro-batch sizeについて、保存された引数は1、技術レポート本文は2と食い違うと明記している。

## 最短手順

- README記載の開始手順は、`git clone https://github.com/bytedance/axion1_0.git`、`cd axion1_0`。続けて学習ガイドに従って環境を構築する。データ構築・評価コードを使う場合はPython 3.11以上の別環境で`python -m pip install -e ".[data,evaluation]"`を実行する。

## 変更履歴

- 2026-11-12: 初回登録
