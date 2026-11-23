---
name: "Pi Agent Computer Use"
genre: "agent-framework"
url: "https://github.com/alexshpunt/pi-agent-computer-use"
repo: "alexshpunt/pi-agent-computer-use"
license: "MIT"
language: "TypeScript"
updated: "2026-11-17"
open_issues: 0
size_kb: 23625
archived: false
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "README excerpt does not include installation or setup instructions, so the exact runtime requirements and shortest setup path remain unconfirmed. Safe mode is described as an extension ownership policy, not an OS security boundary."
stars: 94
forks: 5
created: "2026-10-02"
commits_30d: 100
commits_90d: 100
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119250061229986214"]
fetched_at: "2026-11-18T02:22:14.833429+00:00"
---

# Pi Agent Computer Use

## 出来ること

- Pi coding agentからWindowsアプリやブラウザーのウィンドウを読み取り、クリック、入力、ドラッグなどを行い、操作後の状態を再確認するための拡張です。UI Automationのツリーとスクリーンショット、変更箇所の表示、PlaywrightによるWebページ操作をREADMEが説明しています。

## 目的・背景

- エージェントが画面上の対象を観察してから操作し、結果を再確認できるようにすることを目的としています。READMEは、各操作の結果に実行された内容と未確認の内容が示されると説明しています。

## 依存関係

- READMEによると、ネイティブの画面取得と入力にはCua Driverの作者によるフォークを使い、Webページ操作にはPlaywrightを使います。Pi Agent IDEとの連携も説明されています。

## 実行条件

- 対象プラットフォームはWindowsおよびWSLとREADMEに記載されています。YOLOモードでは任意のウィンドウやディスプレイの読み取り、入力、任意パスからのプログラム起動が可能と説明されています。Safe modeは拡張内の所有権ポリシーで、OSのセキュリティ境界ではありません。

## 最短手順

- README抜粋にはインストールや起動の手順が含まれていないため、確認できません。

## 変更履歴

- 2026-11-23: 初回登録
