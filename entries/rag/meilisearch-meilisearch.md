---
name: "Meilisearch"
genre: "rag"
url: "https://github.com/meilisearch/meilisearch"
repo: "meilisearch/meilisearch"
license: "unknown"
stars: 59927
language: "Rust"
created: "2018-04-23"
updated: "2026-11-19"
forks: 2808
open_issues: 320
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 93645
archived: false
flags: ["unverified"]
risk_notes: "READMEはMITライセンスと記載していますが、提供されたGitHub API測定値ではlicenseがunknownです。ライセンス欄はREADMEの記載とAPI値の不一致を示しています。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/rosemoni18/status/2119211334797840872"]
fetched_at: "2026-11-20T03:09:47.786988+00:00"
---

# Meilisearch

## 出来ること

- 全文検索、セマンティック検索、ハイブリッド検索を提供する検索エンジン。READMEは検索時のタイプミス許容やフィルタリングも機能として挙げています。検索速度に関する数値はREADMEの説明であり、ここでは独立に測定していません。

## 目的・背景

- アプリ、ウェブサイト、ワークフロー向けの検索エンジンとして紹介されています。READMEは、マネージドのMeilisearch Cloudと、自前インフラで動かすオープンソース版の両方を案内しています。

## 依存関係

- 添付READMEから、実行時の依存関係の詳細は確認できません。Dockerまたは提供バイナリを使う手順が掲載されています。

## 実行条件

- セルフホストではDockerイメージを起動する方法と、インストーラーを使ってバイナリを実行する方法がREADMEに掲載されています。Cloudを使う場合はプロジェクトを作成し、プロジェクトURLとAPIキーを使います。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- セルフホストの場合、READMEの例では `docker run -it --rm -p 7700:7700 -v $(pwd)/meili_data:/meili_data getmeili/meilisearch:latest` で起動します。次に `/indexes/movies/documents` へJSON文書をPOSTし、`/indexes/movies/search` へ検索語をPOSTします。READMEはインデックス処理が非同期のため、検索結果が空なら少し待って再試行するよう案内しています。

## 変更履歴

- 2026-11-23: 初回登録
