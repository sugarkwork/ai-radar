---
name: "AI Office"
genre: "agent-framework"
url: "https://github.com/EngChooN/ai-office"
repo: "EngChooN/ai-office"
license: "MIT"
stars: 36
language: "TypeScript"
created: "2026-10-25"
updated: "2026-11-16"
forks: 9
open_issues: 3
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 231121
archived: false
flags: ["unverified"]
risk_notes: "Windowsでは通知、アプリ外で開始したスタッフへの質問処理、画面キャプチャは未対応。タスク結果の確認にはGit for WindowsとGitHub CLIが必要で、実運用で未検証。Mac版はApple Silicon専用で署名・公証されていない。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/dextune/status/2119074897087570318"]
fetched_at: "2026-11-16T21:37:47Z"
last_release: "v1.4.2"
last_release_at: "2026-11-16"
---

# AI Office

## 出来ること

- Claude と GPT のスタッフを従業員として選び、チャットで作業を依頼できます。チームリードによる作業分割、重要な操作の承認、変更ファイルの取り消し、完了報告、Androidアプリからの承認・チャットに対応するとREADMEに記載されています。

## 目的・背景

- スタッフへの指示、承認、報告を一つのオフィスのような画面で扱う、無料のオープンソースElectronデスクトップアプリです。

## 依存関係

- 開発スタックは Electron Forge、Vite、React 19、Zustand、Tailwind 4、shadcn/ui、Phaser 4、SQLite（node:sqlite）、Claude Agent SDK、Codex app-server（GPTスタッフ）です。

## 実行条件

- 利用には、そのPCでClaude CodeまたはChatGPT（Codex）のいずれかにサインインしている必要があります。利用量は接続したアカウントに課金されます。開発起動は `cd app`、`pnpm install`、`pnpm start`。

## 最短手順

- README記載の手順は、対象PC向けインストーラーを入れてClaudeまたはGPTにサインインし、役割と利用するモデルを選んで従業員を追加、チャットまたは秘書に自然言語で依頼し、必要な承認を行って完了報告を受け取ることです。

## 変更履歴

- 2026-11-16: 初回登録
