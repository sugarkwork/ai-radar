---
name: "Volta sPLIt: DeepSeek-V4.1-Flash-1017 on eight V100-SXM2 32 GB cards"
genre: "model-serving"
url: "https://github.com/ProprietaryLegal/Volta-sPLIt-DeepSeek-V4.1-Flash-1017-8xV100-SXM2-PP2xTP4"
repo: "ProprietaryLegal/Volta-sPLIt-DeepSeek-V4.1-Flash-1017-8xV100-SXM2-PP2xTP4"
license: "Apache-2.0"
stars: 36
language: "Python"
created: "2026-11-03"
updated: "2026-11-19"
forks: 4
open_issues: 0
commits_30d: 14
commit_cadence: "weekly"
commits_90d: 14
size_kb: 1380
archived: false
flags: ["unverified"]
risk_notes: "READMEの速度・遅延・品質に関する結果は作者が記載した測定値で、独立検証は確認できていません。公開ツリーは1スロット構成と説明されており、3チャットスロットの実装は公開ツリーに含まれないとREADMEにあります。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119384922762674183"]
fetched_at: "2026-11-19T23:09:16.512645+00:00"
---

# Volta sPLIt: DeepSeek-V4.1-Flash-1017 on eight V100-SXM2 32 GB cards

## 出来ること

- READMEによると、DeepSeek-V4.1-Flash-1017を8枚のV100-SXM2-32GBで、2段のパイプライン並列と各段4枚のテンソル並列でサービングする構成です。ルーティング対象の全エキスパートをGPUメモリに置き、EngramテーブルはホストRAMに置く設計、DSparkによる投機的デコード、vLLMのOpenAI互換サーバーとMessagesエンドポイント、ツール呼び出しを説明しています。速度などの数値はREADMEに記載された作者の測定報告です。

## 目的・背景

- READMEは、限られた8枚のV100でDeepSeek-V4.1-Flash-1017を動かすためのビルド記録としています。1Cat-vLLMのSM70向けフォークを基盤に、2段構成への移植、エンジンパッチ、サービング設定、測定方法・記録をまとめています。

## 依存関係

- README記載の構成では、1CatAIの1Cat-vLLM（SM70対応フォーク）、DeepSeek-V4.1-Flash-1017とISTA-DASLabのGSQ-RCO GGUF、DeepSeekのFP8 DSpark drafter、CUDAおよびNCCLを使用します。重みはこのリポジトリに含まれず、READMEはこのリポジトリが重み・wheel・コンパイル済みライブラリを含まず、ダウンロードもしないと説明しています。

## 実行条件

- README記載の構成は8枚のV100-SXM2-32GBと2枚のNVLinkボードを前提とし、各ボードに4枚を割り当てます。サーバー設定はループバックのみで待ち受け、APIキーなしと説明されています。重みや実行環境の用意を含む手順はREADMEからリンクされたRUNNING.mdに案内されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの「How to run it」からRUNNING.mdを参照してください。READMEは重みをリポジトリに含まず、自動ダウンロードもしないと記載しています。実行前にREADMEが示すV100構成、モデルファイル、エンジン設定を確認してください。

## 変更履歴

- 2026-11-23: 初回登録
