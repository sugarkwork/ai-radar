---
name: "Jellyfin Server"
genre: "other"
url: "https://github.com/jellyfin/jellyfin"
repo: "jellyfin/jellyfin"
license: "GPL-2.0"
stars: 59334
language: "C#"
created: "2018-12-09"
updated: "2026-11-13"
forks: 5810
open_issues: 900
commits_30d: 60
commit_cadence: "daily"
commits_90d: 100
size_kb: 79350
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118778945424212086"]
fetched_at: "2026-11-14T05:15:48.430386+00:00"
---

# Jellyfin Server

## 出来ること

- メディアを管理し、専用サーバーから複数のアプリを使うエンドユーザー端末へストリーミングするFree Softwareのメディアシステムです。READMEでは、Jellyfin Serverリポジトリはバックエンドサーバーのコードを含むと説明しています。

## 目的・背景

- READMEによると、プロプライエタリなEmbyやPlexに代わる選択肢として、利用者がメディアの管理とストリーミングを制御できるようにするプロジェクトです。

## 依存関係

- .NET 10 SDKとffmpegが必要です。サーバーは既定でWebクライアントの静的ファイルも配信しますが、そのファイルはこのリポジトリに含まれないため、jellyfin-webからビルドするか、既存のサーバーインストールから取得する必要があります。

## 実行条件

- 開発手順では主要なOSをサポートするとし、FreeBSDは未対応と記載しています。コマンドライン実行の例では、Webクライアントのdistディレクトリを指定します。

## 最短手順

- README記載の開発実行手順は、依存関係を用意し、リポジトリを取得してWebクライアントのファイルを準備した後、`dotnet run --project Jellyfin.Server --webdir /absolute/path/to/jellyfin-web/dist`を実行する方法です。

## 変更履歴

- 2026-11-14: 初回登録
