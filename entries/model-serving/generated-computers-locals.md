---
name: "Locals"
genre: "model-serving"
url: "https://github.com/Generated-Computers/Locals"
repo: "Generated-Computers/Locals"
license: "Apache-2.0"
stars: 647
language: "Python"
created: "2026-10-12"
updated: "2026-11-12"
forks: 43
open_issues: 8
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 4202
archived: false
flags: ["unverified"]
risk_notes: "速度・処理性能に関する数値はREADME記載の作者による測定報告です。READMEに示された機種・メモリ・比較条件の範囲での報告であり、独立実測ではありません。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/Ryrenz/status/2118555228756639888"]
fetched_at: "2026-11-12T16:17:04.035226+00:00"
---

# Locals

## 出来ること

- AIモデルをMac上で動かし、複数エージェントからの要求、会話の継続、ツール呼び出しやスキーマに沿ったJSON応答を扱うローカルサーバーです。READMEではOpenCode、Cline、Aider、OpenHands、Claude Codeなどとの連携を説明しています。速度の数値はREADMEに記載された作者の測定報告です。

## 目的・背景

- READMEによると、コーディングエージェントの並列要求、長い会話、ツール呼び出しに合わせて、Mac上でのモデル推論と応答形式の制御を行う目的で作られています。

## 依存関係

- READMEの基本導入方法はインストールスクリプトまたはPython 3.12を指定したuv経由のPyPIインストールです。初回起動時にMacに適したモデル（README記載では約3 GB）をダウンロードすると説明されています。

## 実行条件

- READMEが示す対応環境はApple silicon搭載Macです。必要なメモリ量はモデルにより異なり、READMEではFlintに24 GB以上が必要と記載されています。

## 最短手順

- README記載の手順は、`uv tool install --python 3.12 locals`で導入し、新しいTerminalで`locals code ~/my-project`を実行する方法です。初回起動時にモデルを取得し、OpenCodeアシスタントをプロジェクトで開くと説明されています。

## 変更履歴

- 2026-11-12: 初回登録
