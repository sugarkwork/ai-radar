---
name: "DS Harness Remote"
genre: "coding-agent"
url: "https://github.com/liguobao/ds-harness-remote"
repo: "liguobao/ds-harness-remote"
flags: ["unverified"]
risk_notes: "アカウント登録には招待コードが必要とREADMEに記載。招待コードの入手条件、利用料金は資料から確認できない。"
stars: 2667
forks: 198
open_issues: 49
size_kb: 45202
language: "TypeScript"
created: "2026-08-14"
updated: "2026-11-12"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/Ryrenz/status/2118509316688748877"]
fetched_at: "2026-11-12T08:07:34.601984+00:00"
---

# DS Harness Remote

## 出来ること

- READMEによると、DeepSeek Harness DesktopなどのHostにWeb、PC、モバイル端末から接続し、ワークスペースの選択、会話モデルの切り替え、ファイルの読み取り専用プレビュー、リモートターミナル、許可された開発サービスのプレビューを利用できる。Codex、Cursor、Google Antigravityなどのワークスペース接続にも対応すると説明されている。

## 目的・背景

- Harnessを作業用コンピューター上で動かしたまま、別の端末から同じセッション、ワークスペース、ツール、プロジェクト設定を利用するためのリモート接続手段として説明されている。

## 依存関係

- DeepSeek Harness Desktopのプラグインとして使う場合は、npmパッケージ ds-harness-remote@0.6.4 を導入する。READMEにはACP連携、WebRTC接続、TURNリレー、セルフホスト用Serverの記載がある。詳細な依存パッケージは提示されたREADME範囲から確認できない。

## 実行条件

- DesktopプラグインはDeepSeek Harness DesktopのExtensions / Plugin managementから導入し、再起動する。利用にはサインインが必要で、アカウント登録には招待コードが必要とされる。セルフホストではTURN利用にcoturnの独自デプロイが必要。READMEによると、最小構成のServerは完全なホスト型Remote Web体験を提供しない。

## 最短手順

- DeepSeek Harness DesktopでExtensions / Plugin managementを開き、npmから ds-harness-remote@0.6.4 をインストールして再起動する。サイドバーのRemoteを開いてサインインし、別端末から同じアカウントで接続する。オンラインのHostを選び、既存のワークスペースを開くかリモートディレクトリを参照する。

## 変更履歴

- 2026-11-12: 初回登録
