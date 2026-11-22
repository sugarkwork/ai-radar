---
name: "LLMLingua"
genre: "prompt-design"
url: "https://github.com/microsoft/LLMLingua"
repo: "microsoft/LLMLingua"
stars: 6828
forks: 454
open_issues: 124
size_kb: 4061
language: "Python"
created: "2023-07-07"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 4
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:12:59.452285+00:00"
---

# LLMLingua

## 出来ること

- LLMLinguaシリーズは、プロンプトから重要度の低いトークンを取り除いて圧縮する手法を提供する。READMEでは、LLMLingua-2はタスク非依存の圧縮を行い、LLMLinguaより3〜6倍高速と説明されている。これらの効果はREADMEに記載された説明であり、ここでは独立実測していない。

## 目的・背景

- 長い入力によるコンテキスト制限や、プロンプト長に応じたコストへの対応を目的としている。READMEは、LongLLMLinguaについて長文コンテキストでの「lost in the middle」問題を軽減し、RAG性能を高めると説明している。

## 依存関係

- READMEにはGPT2-smallやLLaMA-7Bなどの小型言語モデルの例がある。必須依存パッケージの一覧は、確認したREADMEの範囲では特定できない。

## 実行条件

- READMEの範囲では、必要なPythonバージョン、ハードウェア要件、各方式の実行条件を確認できない。

## 最短手順

- READMEからは ./examples ディレクトリにあるRAG、Online Meeting、CoT、Code、LLMLingua-2などの例を手がかりにできる。具体的な導入・実行コマンドは、確認したREADMEの範囲では確認できない。

## 変更履歴

- 2026-11-22: 初回登録
