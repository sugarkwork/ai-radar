---
name: "Git Plugin for Obsidian"
genre: "other"
url: "https://github.com/Vinzent03/obsidian-git"
repo: "Vinzent03/obsidian-git"
license: "MIT"
stars: 12302
language: "TypeScript"
created: "2020-10-27"
updated: "2026-11-19"
forks: 678
open_issues: 100
commits_30d: 16
commit_cadence: "weekly"
commits_90d: 81
size_kb: 6383
archived: false
flags: ["unverified"]
risk_notes: "READMEはモバイル版を「very unstable」とし、クラッシュ、バッファーオーバーフロー、処理が終わらない場合があると説明している。モバイルではSSH認証、rebase、submoduleに制限があり、リポジトリサイズにも制約がある。LinuxのSnapは非対応、Flatpakは非推奨。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/rosemoni18/status/2119211334797840872"]
fetched_at: "2026-11-20T03:09:45.829480+00:00"
---

# Git Plugin for Obsidian

## 出来ること

- Obsidian内でGitの自動コミット・pull・push、起動時の自動pull、変更のステージングとコミット、履歴・差分の確認、競合解決ができる。デスクトップではエディター上の変更箇所表示とsubmodule管理にも対応する。

## 目的・背景

- ObsidianのvaultにGit連携を追加し、変更の確認やリモートとの同期をObsidian内で扱うためのコミュニティプラグイン。

## 依存関係

- デスクトップ版はインストール済みのGitを実行し、リポジトリメタデータやGit設定にアクセスする。モバイル版はisomorphic-gitを利用する。

## 実行条件

- Obsidianのコミュニティプラグインとして利用する。HTTPSまたはSSH認証にはGitサービスに応じた追加設定が必要な場合がある。LinuxのSnap環境は非対応。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- Obsidianにプラグインを導入し、既存リポジトリをcloneするかvaultで新規リポジトリを初期化する。必要に応じてremoteと認証を設定し、Source Control Viewを開いて変更をステージ・コミットする。既定設定ではCommit-and-syncでコミット、pull、pushを行う。

## 変更履歴

- 2026-11-23: 初回登録
