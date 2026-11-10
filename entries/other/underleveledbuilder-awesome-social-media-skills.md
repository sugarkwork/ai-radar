---
repo: "UnderleveledBuilder/awesome-social-media-skills"
name: "Awesome Social Media Skills"
genre: "other"
url: "https://github.com/UnderleveledBuilder/awesome-social-media-skills"
flags: ["unverified"]
risk_notes: "最新リリース、検索スキルの導入と動作、掲載ツールの実効性・安全性・個別の料金や利用条件は未確認。READMEによると、投稿や返信を行う一部のツールはアカウント認証を要し、Cookieをローカルに保存する場合がある。"
stars: 252
forks: 40
open_issues: 6
size_kb: 3123
language: "Python"
created: "2026-10-19"
updated: "2026-11-08"
archived: false
license: "CC0-1.0"
commits_30d: 33
commits_90d: 33
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Ryrenz/status/2117620066875293733"]
fetched_at: "2026-11-10T10:04:19Z"
---

# Awesome Social Media Skills — SNS運用向けAIスキルの公開カタログ

## 出来ること

- 企画、原稿、カバー画像・短尺動画、公開、分析の工程別に、小紅書、抖音、WeChat、Bilibili、X、YouTube、TikTok、LinkedInなどの候補を探せる。確認したREADMEにはスキル189件とMCPツール・オープンソース基盤27件が記載されている（メタデータ更新日2026-11-05）。

## 目的・背景

- SNS運用で必要な作業とプラットフォームを起点に、用途に合う候補を絞り込むための資料。運営者による手作業の確認はリポジトリの説明・構成・分類が対象で、スクリプトによる検査も行ったと記載されている。

## 依存関係

- 一覧の閲覧には公開READMEを使う。エージェントから候補を探す場合は、スキル対応のエージェントと、READMEが案内するnpx経由のskills CLIを使う。掲載先のライセンス、料金、APIキー要件は個別に確認する。

## 実行条件

- social-media-skill-finderは一覧から導入候補を選ぶためのスキル。実際の投稿・返信は選んだ掲載ツールの機能で、必要なアカウント認証や利用条件はツールとプラットフォームに依存する。

## 最短手順

- READMEの工程別またはプラットフォーム別の索引で候補を探し、掲載先のREADMEとSKILL.mdで要件を確認する。
- AIから探す場合は、README記載の `npx skills add UnderleveledBuilder/awesome-social-media-skills` でsocial-media-skill-finderを導入し、Codexなどの対応エージェントに『YouTubeの短尺動画の台本作成に使えるスキルを一覧から選んで』と依頼する。

## 変更履歴

- 2026-11-10: 初回登録
