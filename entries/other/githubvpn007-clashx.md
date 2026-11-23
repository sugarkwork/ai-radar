---
name: "ClashX macOS 代理配置与使用教程"
genre: "other"
url: "https://github.com/githubvpn007/ClashX"
flags: ["low-quality", "unverified"]
risk_notes: "READMEは「未知の開発者」からのアプリを許可する手順を案内し、配布ファイルをこのリポジトリのReleaseから提供しています。配布物の安全性は確認できません。 READMEはmacOS 10.5以降と記載していますが、現行macOSでの動作は確認できていません。配布ファイルの安全性とライセンスもREADMEからは確認できません。 GitHub APIでライセンスを確認できていません。"
repo: "githubvpn007/ClashX"
stars: 936
forks: 112
open_issues: 16
size_kb: 2164
language: "unknown"
created: "2021-07-26"
updated: "2025-09-10"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/AIExplorerTim/status/2119354247716425944"]
fetched_at: "2026-11-19T16:15:53.505371+00:00"
---

# ClashX macOS 代理配置与使用教程

## 出来ること

- READMEでは、ClashXをmacOS上で動作するルールベースのプロキシツールとして紹介しています。対応プロトコルとしてVmess、Shadowsocks、Snell、SOCKS5を挙げ、プロキシモードやノードの切り替え、ノードの遅延テスト、托管リンクによる設定、ルール判定の分析、ログ出力を説明しています。

## 目的・背景

- ClashXの設定と利用を案内するリポジトリです。READMEは、ClashXがVPN接続を配布するものではないと明記しています。

## 依存関係

- READMEに記載された利用手順では、利用者自身のClashサブスクリプション設定が必要です。ClashX初回起動時には、システムプロキシ設定用のHelperをインストールする手順も案内されています。

## 実行条件

- READMEの記載ではmacOS 10.5以降が必要で、MacBook、iMac、Mac Proを対象としています。この動作条件はREADMEの記述であり、現行環境での動作確認を示すものではありません。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの手順は、ReleaseからmacOS用ファイルを取得して起動し、初回起動時に案内されるHelperをインストール、ClashXメニューの「配置」→「托管配置」→「管理」からサブスクリプションを追加します。設定が反映されたら出站モードを「规则判断」にし、ProxyまたはGlobalグループのノードを選び、「设置为系统代理」を有効にします。

## 変更履歴

- 2026-11-23: 初回登録
