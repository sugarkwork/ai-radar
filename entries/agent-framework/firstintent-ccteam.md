---
name: "ccteam"
genre: "agent-framework"
url: "https://github.com/firstintent/ccteam"
repo: "firstintent/ccteam"
flags: ["unverified"]
risk_notes: "README excerpt does not specify the complete dependency list or installation requirements."
stars: 649
forks: 29
open_issues: 8
size_kb: 30247
language: "Rust"
created: "2026-05-04"
updated: "2026-11-14"
archived: false
license: "MIT"
commits_30d: 37
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/ruyi3699/status/2119097797081501791"]
fetched_at: "2026-11-16T21:15:45.726390+00:00"
---

# ccteam

## 出来ること

- READMEによると、Claude Code、Codex、Grok、Kimi、Deepseek Harnessなどのコーディングエージェントをまとめ、セッションの作成・振り分け・結果収集を行う。Telegram、Lark、Slack、Webコンソールから操作でき、APIとJavaScriptで記述するFlowも提供する。

## 目的・背景

- READMEは、各コーディングCLIが単独のターミナルとコンテキストに閉じていることを背景に挙げ、エージェント間の連携、ルーティング、ガードレール、コスト記録を提供すると説明している。

## 依存関係

- READMEに明記された連携対象はClaude Code、Codex、Grok、Kimi、Deepseek Harness、Pi。Claudeアカウント切替には任意のcswap連携が記載されている。完全な依存関係一覧は提示されたREADME抜粋から確認できない。

## 実行条件

- READMEのバッジにはmacOS、Linux、WSL対応とある。FlowはJavaScriptスクリプトとしてccteam runnerが実行する。必要なランタイムやバージョンの詳細は提示された抜粋にない。

## 最短手順

- README記載の例では、`ccteam flow new branch-review`でFlowのひな形を作り、`ccteam flow run branch-review.flow.js --args '{"base":"main"}' --budget 5`で実行する。通常のセットアップ手順は提示された抜粋に含まれていない。

## 変更履歴

- 2026-11-22: 初回登録
