---
name: "AutoHarness"
genre: "agent-framework"
url: "https://github.com/tigerless-labs/autoharness"
repo: "tigerless-labs/autoharness"
license: "MIT"
language: "Python"
created: "2026-06-09"
updated: "2026-11-10"
commit_cadence: "daily"
archived: false
stars: 10940
forks: 654
open_issues: 19
size_kb: 1190
commits_30d: 100
commits_90d: 100
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/CY160909/status/2120278073715396948"]
fetched_at: "2026-11-11T04:20:28.707230+00:00"
---

# AutoHarness

## 出来ること

- Claude Codeのプラグインとして、作業セッションからスキルを作成し、同じシナリオのスキルを統合し、後続の利用状況に応じて更新・整理する。プラグインが生成したスキルだけを対象とし、セッション開始時にそれらの一覧を表示する。作成・更新の判断はスキルごとの台帳に記録される。READMEは、スキルの存続判定を後続ターンでの遵守状況に基づけ、専用評価を実行しない設計と説明している。

## 目的・背景

- 作者は、エージェントのハーネスが性能に寄与するという見立てから、スキル層を実作業に合わせて保守する構想を提示している。READMEにはCORE-Benchの42%から78%という数値が記載されているが、これはHALへのリンクを伴う作者側の説明であり、このリポジトリでの独立実測ではない。

## 依存関係

- README記載の要件はPython 3.11以降とClaude Code。外部Pythonパッケージへの依存はなく、Pythonのみで動作すると説明されている。対応プラットフォームはLinuxとmacOS。

## 実行条件

- フックとMCPサーバーの実行には、PATH上で`python3`として解決されるPython 3.11以降が必要。古いPythonが先に解決されるとフックが無効になり、その旨をstderrに出すとREADMEに記載されている。第三者マーケットプレイスの自動更新は既定で無効。

## 最短手順

- Claude Codeの入力欄で`/plugin marketplace add tigerless-labs/autoharness`、続けて`/plugin install autoharness@autoharness`を実行し、`/reload-plugins`またはClaude Codeの再起動を行う。作業中のセッションを明示的にスキル化する場合は`/learn`を使用する。

## 変更履歴

- 2026-11-11: 初回登録
