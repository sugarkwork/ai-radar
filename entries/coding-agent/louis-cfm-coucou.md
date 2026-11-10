---
repo: "Louis-CFM/coucou"
name: "Coucou"
genre: "coding-agent"
url: "https://github.com/Louis-CFM/coucou"
license: "MIT"
stars: 7102
language: "Swift"
created: "2026-09-27"
updated: "2026-11-06"
forks: 1166
open_issues: 460
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 30519
archived: false
last_release: "v0.5.8"
last_release_at: "2026-10-31"
flags: ["unverified"]
risk_notes: ["公開資料による確認。通知の到達や遅延、端末移動、Face ID承認は実機未検証。CodexでClaude Codeと同じ承認操作ができるか、およびTestFlightの参加可否は未確認。"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2115692620999725338"]
fetched_at: "2026-11-10T12:28:52+00:00"
---

# Coucou — MacのノッチにAIコーディングエージェントの進捗と許可要求を表示

## 出来ること

- Claude Code、Codex、Cursor、Gemini CLIなどのセッションをMacのノッチで確認できる。Claude Codeの許可要求にはノッチから応答できると公式READMEに記載されている。
- 公式iPhoneガイドでは、通知やロック画面から許可・拒否でき、許可時にFace IDを求めると説明している。 [iPhoneガイド](https://github.com/Louis-CFM/coucou/blob/main/docs/IPHONE.md)

## 目的・背景

- エージェントごとのターミナルを切り替えずに、進行中の作業や人の判断を待っているセッションを見つけるためのデスクトップUI。コードはMIT。Coucouの名称、キャラクターのMochi、効果音は著作権者に権利が留保される。 [公式README](https://github.com/Louis-CFM/coucou/blob/main/README.md)

## 依存関係

- 実セッションを表示するには対象エージェントと連携設定が必要。Claude Code、Codex、Gemini CLIは設定からフックを導入する。iPhone連携には同じApple AccountのiCloudと通知許可が必要。 [公式README](https://github.com/Louis-CFM/coucou/blob/main/README.md)

## 実行条件

- macOS 15以降のApple siliconまたはIntel。CodexやGemini CLIの連携はMacのGitHub配布版を使用する。iPhone連携はiOS 18以降。公式READMEではTestFlightベータを無料と案内している。 [macOSリリース](https://github.com/Louis-CFM/coucou/releases/tag/v0.5.8) [公式README](https://github.com/Louis-CFM/coucou/blob/main/README.md)

## 最短手順

- GitHub ReleasesのCoucou.zipを展開し、Coucou.appをApplicationsに移して起動する。 [公式リリース](https://github.com/Louis-CFM/coucou/releases/tag/v0.5.8)
- Coucouの設定でClaude CodeのInstall hooksを選び、提示される設定差分を確認する。ターミナルでClaude Codeを起動すると、エージェントのフックを通じてセッションのイベントがCoucouに届く。Codexを表示する場合は設定のCodexから専用フックを導入する。 [公式README](https://github.com/Louis-CFM/coucou/blob/main/README.md)

## 変更履歴

- 2026-11-10: 初回登録
