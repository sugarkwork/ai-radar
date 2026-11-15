---
name: "BAMA: Build Any Mac App"
genre: "coding-agent"
url: "https://github.com/daveebbelaar/bama"
repo: "daveebbelaar/bama"
stars: 1819
forks: 223
open_issues: 3
size_kb: 1253
language: "Swift"
created: "2026-10-24"
updated: "2026-11-05"
archived: false
license: "MIT"
commits_30d: 27
commits_90d: 27
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/AIExplorerTim/status/2118910064606233060"]
fetched_at: "2026-11-15T00:18:08.409699+00:00"
---

# BAMA: Build Any Mac App

## 出来ること

- エージェント向けの21個のスキルで、アプリの画面調査、ユーザーストーリー作成、Swift/SwiftUIでの実装、デザイン、ビルドと検証を支援します。READMEの説明では、実装をストーリー単位で進め、コミット前にライト/ダークモードの画面スナップショットとテストを実行します。出典: https://github.com/daveebbelaar/bama

## 目的・背景

- 気に入ったアプリを参考に、SwiftとSwiftUIによるネイティブMacアプリを作るための手順・スキルをまとめています。READMEは、既存アプリの画面を調べて画面一覧を作り、受け入れ条件付きのユーザーストーリーとマイルストーンに落とし込む流れを示しています。出典: https://github.com/daveebbelaar/bama

## 依存関係

- README記載の要件はmacOS 26以降、Swift 6.2ツールチェーン用のXcode 26以降、スキルに対応するエージェントです。ネイティブアプリの画面調査（cloneスキル）にはコンピュータ操作機能が必要と記載されています。出典: https://github.com/daveebbelaar/bama

## 実行条件

- Claude Code、Codex、Cursor、Gemini CLIなどのスキル対応エージェント向けです。READMEは、Claude Codeプラグイン、Codexプラグイン、skills.sh経由、または手動の導入方法を記載しています。macOS 26以降とXcode 26以降が要件です。出典: https://github.com/daveebbelaar/bama

## 最短手順

- README記載の導入例は `npx skills@latest add daveebbelaar/bama` です。導入後、作りたいアプリを説明してエージェントに依頼します。プロジェクト内で次のスキル選択に迷う場合は `/bama` を使う手順も記載されています。出典: https://github.com/daveebbelaar/bama

## 変更履歴

- 2026-11-15: 初回登録
