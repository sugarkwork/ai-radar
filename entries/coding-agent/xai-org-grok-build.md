---
name: "Grok Build"
genre: "coding-agent"
url: "https://github.com/xai-org/grok-build"
repo: "xai-org/grok-build"
stars: 27802
forks: 5248
open_issues: 0
size_kb: 62238
language: "Rust"
created: "2026-07-14"
updated: "2026-09-29"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 16
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:29:58.292576+00:00"
---

# Grok Build

## 出来ること

- コードベースを理解し、ファイル編集、シェルコマンド実行、ウェブ検索、長時間タスク管理を行うターミナル型AIコーディングエージェント。フルスクリーンTUIでの対話利用、スクリプトやCI向けのヘッドレス利用、Agent Client Protocol（ACP）経由のエディタ組み込みに対応するとREADMEは説明している。

## 目的・背景

- READMEによると、このリポジトリにはGrok BuildのRustソースコードとエージェント実行環境が含まれ、SpaceXAIのモノレポから定期的に同期される。

## 依存関係

- ソースビルドにはRustが必要。READMEは、 hermetic toolsの実行にDotSlashが必要で、protoコード生成にはDotSlash経由のprotoc、またはPATH上もしくはPROTOCで指定したprotocを使うと説明している。

## 実行条件

- READMEではmacOS、Linux、Windows向けのリリース済みバイナリを案内している。ソースビルドのホストはmacOSとLinuxをサポートし、Windowsはベストエフォートで、このツリーからのビルドは現時点でテストされていないと記載。初回起動時にはブラウザーでの認証が始まる。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載のmacOS/Linux/Git Bash向け手順は `curl -fsSL https://x.ai/cli/install.sh | bash`、Windows PowerShell向け手順は `irm https://x.ai/cli/install.ps1 | iex`。インストール後は `grok --version` でバージョンを確認する。

## 変更履歴

- 2026-11-23: 初回登録
