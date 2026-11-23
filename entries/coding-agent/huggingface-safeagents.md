---
name: "safeagents"
genre: "coding-agent"
url: "https://github.com/huggingface/safeagents"
repo: "huggingface/safeagents"
license: "Apache-2.0"
stars: 396
language: "Python"
created: "2026-10-28"
updated: "2026-11-18"
forks: 39
open_issues: 8
commits_30d: 42
commit_cadence: "daily"
commits_90d: 42
size_kb: 41799
archived: false
flags: ["unverified"]
risk_notes: "README上、mediumの検知は既定のblock-severity=highでは遮断されず、judge未設定時は呼び出しがそのまま通る。README記載の検知速度は作者の報告で、独立実測ではない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119400802389205299"]
fetched_at: "2026-11-20T04:15:08.772213+00:00"
---

# safeagents

## 出来ること

- エージェントとモデルサーバーの間にローカルプロキシを置き、ツール呼び出しを検査する。未宣言ツールや会話に現れないホストへのアクセスなどを確認し、atif-scanの検知結果や任意の判定モデルに基づいて遮断できる。--log-onlyでは遮断候補を記録する。軌跡データの資格情報や指定した秘密値などをマスクするscrub、マスク後データをHugging Face datasetへ送るpublishも備える。READMEはredactionをbest-effortと説明し、公開前にレポートを確認するよう案内している。

## 目的・背景

- モデルが生成した危険なツール呼び出しを、ハーネスが実行する前に検査するための軽量なローカルプロキシとして説明されている。判定モデルは追加の遮断に使われ、既存の遮断を解除しない。

## 依存関係

- インストールスクリプトはuvがなければ導入し、safeagentsをuv toolとしてインストールする。atif-scanの検査を利用する。判定モデルやプラグインは任意。

## 実行条件

- README記載のインストール対象はmacOS、Linux、WSL、Windows PowerShell。ハーネスはbase URLを設定できる必要があり、OpenAI Chat CompletionsまたはAnthropic Messagesに対応すると記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEのOS別インストールスクリプトを実行し、新しいターミナルを開く。まず `safeagents start https://api.anthropic.com --log-only` でプロキシを起動し、ハーネスのbase URLをプロキシに向ける。挙動を確認してから `--log-only` を外すと実際に遮断する。

## 変更履歴

- 2026-11-23: 初回登録
