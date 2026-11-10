---
repo: "wilwaldon/Claude-Code-Video-Toolkit"
name: "Claude Code Video Toolkit"
genre: "video-gen"
url: "https://github.com/wilwaldon/Claude-Code-Video-Toolkit"
license: "unknown"
stars: 110
language: "unknown"
created: "2026-02-26"
updated: "2026-02-26"
forks: 17
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 12
archived: false
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "外部ツールの導入・レンダリング、出力品質、現行バージョンでの互換性、料金は未検証。READMEにはMIT表記があるが、親のGitHub API測定ではライセンスはunknown。外部ツールや素材の利用条件は各提供元で確認する。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:06:59+00:00"
---

# Claude Code Video Toolkit — 動画制作のためのスキル・MCP導入ガイド

## 出来ること

- RemotionでのReactベースの動画制作、Manimでの数理アニメーション、Playwright MCPでの画面録画、YouTubeのクリップ・字幕処理、FFmpegでの変換・圧縮の手順を探せる。

## 目的・背景

- Claude Codeが動画の構成やコードを作り、用途別の外部ツールが描画・録画・後処理を担う。READMEに掲載される同名のdigitalsamba製プロジェクトは別リポジトリ。

## 依存関係

- 動画制作には選んだ外部ツールを導入する。READMEの例では、モーショングラフィックスにRemotion Agent Skills、画面録画にPlaywright MCP、YouTubeクリップと字幕処理にyt-dlp、libass対応のFFmpeg、pysrtを使う。

## 実行条件

- READMEはブラウザで参照できる。掲載手順を試すにはClaude Codeと用途別の実行環境が必要。公開GitHub Releasesにはリリースの掲載がない。

## 最短手順

- モーショングラフィックスを試す場合は、READMEに記載の `npx skills add remotion` で外部のRemotionスキルを導入する。Claude Codeに『ロゴと機能紹介を含む短い製品紹介動画を作って』と依頼し、生成されたReactコンポーネントをRemotionでMP4にレンダリングする。

## 変更履歴

- 2026-11-10: 初回登録
