---
name: "opencode-compaction-anchor"
genre: "coding-agent"
url: "https://github.com/kylebakerio/opencode-compaction-anchor"
repo: "kylebakerio/opencode-compaction-anchor"
flags: ["unverified"]
risk_notes: "README記載の結果は限定された4タスクで各設定1回の作者報告であり、独立実測ではない。"
stars: 3
forks: 1
open_issues: 0
size_kb: 10
language: "JavaScript"
created: "2026-11-01"
updated: "2026-11-01"
archived: false
license: "MIT"
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/ai_hakase_/status/2118615006455418914"]
fetched_at: "2026-11-12T23:10:14.534880+00:00"
---

# opencode-compaction-anchor

## 出来ること

- OpenCodeの要約後、元の依頼を原文どおり次のメッセージに再挿入する`reinsert`、要約に元の依頼項目ごとのチェックリストを含めるよう促す`checklist`を提供する。任意で会話履歴を書き出して要約に保存先を示す`pointer`、自動の確認・停止案内を「タスクを続けて」と置き換える`no-stop-and-ask`もある。各機能は切り替え可能。

## 目的・背景

- READMEは、長い複数項目の作業でコンテキスト要約が繰り返されると、元の依頼や未着手項目が失われ、作業を終える前にエージェントが停止する問題を説明している。作者報告の評価では、4つの複数バグ課題・計79チェックにおいて、標準設定の57%に対し`reinsert`と`checklist`併用は94%のチェック通過だった。作者自身が各ローカル設定1回・課題4件という制約を記載している。

## 依存関係

- OpenCodeの実験的プラグインフック`experimental.session.compacting`と`experimental.chat.messages.transform`を使用する。README記載の設定例はOpenCode 1.18.34でテスト済み。OpenCode 2.xは未テスト。

## 実行条件

- README記載の設定例では、プラグインファイルの絶対パスをOpenCode設定に追加する。設定ファイルの配置先としてユーザー設定またはプロジェクトの`opencode.json`を案内している。プラグイン用ディレクトリに配置して読み込む方法もあり、その場合は既定設定で動作する。

## 最短手順

- プラグインファイルを用意し、`~/.config/opencode/opencode.json`またはプロジェクトの`opencode.json`に、絶対パスを使った`plugin`設定を追加する。READMEの例では`parts`に`reinsert`と`checklist`を指定する。プラグイン用ディレクトリから読み込む場合は既定設定で動作する。

## 変更履歴

- 2026-11-12: 初回登録
