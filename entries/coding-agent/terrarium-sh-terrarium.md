---
name: "Terrarium"
genre: "coding-agent"
url: "https://github.com/terrarium-sh/terrarium"
repo: "terrarium-sh/terrarium"
license: "Apache-2.0"
stars: 57
language: "Rust"
created: "2026-08-16"
updated: "2026-11-17"
forks: 2
open_issues: 9
commits_30d: 62
commit_cadence: "daily"
commits_90d: 100
size_kb: 8019
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119294348093276479"]
fetched_at: "2026-11-18T20:07:45.081429+00:00"
---

# Terrarium

## 出来ること

- エージェントや開発ツールを、個別のカーネルとディスクを持つ仮想マシン「box」で実行する。ホスト側で共有するフォルダと接続を許可するネットワーク先を選べる。ストレージは再起動後も保持され、boxのサービスをホストのループバックで公開することもできる。

## 目的・背景

- コーディングエージェントや信頼できないインストーラー、ビルド、スクリプトをホストから分離したVM内で動かし、アクセス範囲をレシピで指定する用途。READMEは、VM内のrootもVM内にとどまることや、保護範囲と限界についてセキュリティモデルを参照するよう案内している。

## 依存関係

- READMEによると、ゲストカーネル、ベースシステム、VM関連部品はterraに組み込まれており、追加のデーモンやOCIイメージは不要。Linuxでは/dev/kvmへのアクセスが必要。

## 実行条件

- Linux（amd64、aarch64）、Apple Silicon搭載macOS、Windows（amd64、ARM64）に対応するとREADMEに記載。WindowsではWindows Hypervisor Platform機能を有効にする必要があり、詳細はプラットフォーム要件を参照。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- プロジェクトにdev.yamlを作成し、CPU・メモリ・ディスク、共有フォルダ、network.modeと許可先、作成時フックを設定する。READMEの例ではNode.js用にAlpineとnpmのレジストリへのHTTPSを許可し、nodejs・npm・gitを導入する。`terra ./dev.yaml setup`でboxを作成し、`terra`で中のシェルを開く。レシピは共有プロジェクトを編集でき、dev.yaml自体も編集可能なので、再度setupする前にレシピを確認するよう注意書きがある。

## 変更履歴

- 2026-11-23: 初回登録
