---
name: "Skill Recorder"
genre: "coding-agent"
url: "https://github.com/microsoft/skill-recorder"
repo: "microsoft/skill-recorder"
stars: 5816
forks: 658
open_issues: 48
size_kb: 6130
language: "TypeScript"
created: "2026-07-29"
updated: "2026-11-12"
archived: false
license: "MIT"
commits_30d: 8
commits_90d: 35
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/ruyi3699/status/2118984802250498379"]
fetched_at: "2026-11-15T16:08:21.184927+00:00"
---

# Skill Recorder

## 出来ること

- 画面上の作業セッションを記録し、GitHub Copilot CLIで全体の意図と順序付きの手順を再構成する。承認した分析から、オンデマンドで実行するSKILL.md形式のSkill、またはスケジュールやトリガーで実行するAutomationを作成できる。生成物はUIクリックの再生より、gh CLIやweb_fetchなどエージェントのネイティブツールを優先する。

## 目的・背景

- READMEによると、実際の作業を一度記録し、エージェントが再利用できる手順へ変換することを目的とする。単一の作業例から一般化する設計として説明されている。

## 依存関係

- 解析にはアプリに同梱されるGitHub Copilot CLIを使用する。利用にはCopilotアクセスのあるGitHubアカウント、または対応モデルプロバイダーのAPIキーが必要。

## 実行条件

- macOSを主対象とし、Windows 11 x64/ARM64も対応対象として記載。Ubuntu向けインストール手順も記載されている。インストールはリリースページのコミット固定コマンドで、必要なNode.jsランタイムをダウンロードして端末上でビルドする方式。解析時には選択したフレーム、文字起こし、追加詳細が選択中のAIプロバイダーへ送られる。

## 最短手順

- 公式リリースページで対象OSの「Commit-pinned installation」コマンドをコピーし、WindowsではPowerShell、macOSまたはUbuntuではTerminalで実行する。完了後、Windowsは通知に従って起動し、macOSまたはUbuntuはインストーラーが起動する。アプリで作業を記録してAnalyzeを実行し、分析結果を確認・編集してSkillまたはAutomationを作成する。

## 変更履歴

- 2026-11-15: 初回登録
