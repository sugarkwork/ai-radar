---
name: "Moyu（摸鱼）"
genre: "prompt-design"
url: "https://github.com/uucz/moyu"
repo: "uucz/moyu"
license: "MIT"
language: "Python"
commit_cadence: "stale"
archived: false
flags: ["unverified"]
risk_notes: "過度なエンジニアリングを抑える効果としてREADMEに記載された説明・数値は、独立した検証結果として確認されていない。"
stars: 307
forks: 13
open_issues: 1
size_kb: 1307
created: "2026-03-23"
updated: "2026-07-30"
commits_30d: 0
commits_90d: 0
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118747739769151562"]
fetched_at: "2026-11-14T01:12:43.921560+00:00"
---

# Moyu（摸鱼）

## 出来ること

- READMEは、コーディングエージェント向けのルール集「摸鱼」を説明している。ルールは、依頼されたコードだけを変更する、最も簡潔な案を優先する、不明点は質問する、の3点。過剰な変更を検出する4段階の基準も記載されている。Claude Code、Codex、Cursor、Copilot、Windsurf、Cline、Kiro、CodeBuddy、Antigravity、OpenCode、Aider、Continue向けの設定ファイルや手順が案内されている。

## 目的・背景

- READMEは、コーディング助手が依頼範囲を超えてコード、抽象化、依存関係などを追加しがちだという問題意識から、変更を必要最小限に抑えるルールを提案している。READMEにある「1460回の対照実験」やコード削減率は作者の記載であり、独立検証された事実としては扱えない。

## 依存関係

- READMEに明示された外部ライブラリやランタイム依存関係は確認できない。Claude Code向けの例では `claude skill install` を使う。各プラットフォーム向けには対応するルールファイルを配置する手順が記載されている。

## 実行条件

- README記載の導入先は各対応エージェントの設定ディレクトリまたは指示ファイル。手動配置する場合のパスはプラットフォームごとに異なる。READMEは導入後にルールが自動適用されると説明しているが、適用方法はプラットフォーム設定に依存する。

## 最短手順

- Claude Code向けのREADME記載例は `claude skill install --url https://github.com/uucz/moyu --skill moyu`。他の対応環境ではREADMEの該当節に記載されたルールファイルを配置する。

## 変更履歴

- 2026-11-14: 初回登録
