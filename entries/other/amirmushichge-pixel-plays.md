---
repo: "amirmushichge/pixel-plays"
name: "Pixel Plays"
genre: "other"
url: "https://github.com/amirmushichge/pixel-plays"
license: "MIT"
stars: 448
forks: 43
open_issues: 2
size_kb: 12025
language: "HTML"
created: "2026-10-31"
updated: "2026-10-31"
archived: false
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: ["候補投稿が言及するClaude Opus 5.5の使用は、作者投稿を取得できなかったため未確認。最新リリース、ブラウザでの動作・性能、別題材への改変結果も未確認。"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/AiAircle34052/status/2117088054892785671"]
fetched_at: "2026-11-10T08:19:51+00:00"
---

# Pixel Plays｜画像素材なしで描画するブラウザゲーム5本

## 出来ること

- ボッチャ、橋からの飛び込み、洗濯物入れ、テニス、スケートボードの5本を収録。READMEには公開プレイ先が掲載されている。

## 目的・背景

- 各ゲームは素のJavaScriptで書かれた1ページ。ソフトウェアラスタライザが、固定の正投影カメラで捉えた場面を低解像度Canvasに描画し、最近傍補間で拡大する。
- 共通のengine.jsがカメラや深度バッファ、影などを担当し、各ゲームが場面の準備、更新、描画を定義する。コーディングエージェントに別題材のゲームを実装させる際も、この分担を仕様として参照できる。

## 依存関係

- READMEによると、ビルド工程と外部パッケージは不要。付属のローカルサーバーを使う場合はNode.jsが必要。
- コードはMIT。MUSIC.mdによると、付属のSuno生成MP3はMITの適用外で、プロジェクト外での再利用は許諾されていない。改変版では自前の曲に差し替えるか、曲を省ける。

## 実行条件

- 公開版はブラウザから開ける。ローカルでは静的ファイルサーバーで配信でき、付属サーバーの案内先は http://127.0.0.1:5300/ 。

## 最短手順

- READMEに記載された公開プレイ先 https://pixel-plays-ruby.vercel.app/ をブラウザで開き、ゲームを選ぶ。
- 別題材で作る場合は、READMEのゲーム追加手順と既存の1本を参照し、新しいHTMLページに場面とルールを定義して、shell.jsのゲーム一覧へ登録する。

## 変更履歴

- 2026-11-10: 初回登録
