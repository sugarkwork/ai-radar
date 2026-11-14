---
name: "Rakazo"
genre: "agent-framework"
url: "https://github.com/elie222/rakazo"
repo: "elie222/rakazo"
license: "Apache-2.0"
stars: 8321
language: "TypeScript"
created: "2026-08-13"
updated: "2026-11-14"
forks: 1505
open_issues: 274
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 177934
archived: false
flags: ["unverified"]
risk_notes: "本番運用でHTTPSを前段に置くこと、サンドボックスプロバイダーに応じた設定、開発時のNode.js・pnpm・Docker・Postgres等の条件がある。料金や未記載のプロバイダー条件はREADMEだけでは確認できない。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/NFT_Chen/status/2118825518024040589"]
fetched_at: "2026-11-14T11:15:16.322444+00:00"
---

# Rakazo

## 出来ること

- READMEでは、永続メモリやルーティンを持つAIチームメイトをセルフホストし、自分のモデルで動かせると説明している。ブラウザー・ターミナル・ファイルを使うコンピューター操作、グループチャット、委任・サブエージェント、共有可能なダッシュボードや文書の作成、音声チャット、アプリ連携とMCPを備える。Web、デスクトップ、iPhone、Androidから利用できる。

## 目的・背景

- READMEではGrok Botのオープンソースなセルフホスト代替として紹介されている。自分のマシンとモデルを使い、メモリやルーティンを持つAIチームメイトを運用することを目的としている。

## 依存関係

- 公開イメージによる起動にはDocker Engine、Composeプラグイン、curl、OpenSSLが必要。ソースからの開発にはNode.js 24.15.0以上の24.x系またはNode.js 26以上、pnpm 12、Dockerが必要で、Node.js 25.xは非対応。開発手順はPostgresの接続またはDockerによるローカルPostgres起動を利用する。

## 実行条件

- 公開イメージの標準タグはedgeで、READMEはlinux/amd64とlinux/arm64を記載している。初回起動後にアカウントを作成しモデルを接続する。ローカルDockerコンピューターは既定で有効。任意のリモートサンドボックスには対応プロバイダーとAPIキーが必要。開発環境ではデータベース、認証・暗号化用の秘密値などを設定する。公開サーバーではHTTPSをポート5173の前段に置く手順が案内されている。

## 最短手順

- 公開イメージを使う場合、README記載の手順で作業ディレクトリを作り、install-images.shを取得してbashで実行する。インストーラーはComposeファイルを取得し、ランダムな秘密値を含む.envを作成してRakazoを起動する。起動後にアカウントを作成し、モデルを接続する。

## 変更履歴

- 2026-11-14: 初回登録
