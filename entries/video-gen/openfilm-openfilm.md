---
name: "OpenFilm"
genre: "video-gen"
url: "https://github.com/openfilm/openfilm"
repo: "openfilm/openfilm"
flags: ["unverified"]
risk_notes: "生成音声・音楽・画像・動画の利用には、接続サービスの利用またはOpenFilmへのサインインが必要と記載されています。各サービスの料金や利用条件はREADMEでは確認できません。"
stars: 6950
forks: 669
open_issues: 27
size_kb: 55842
language: "TypeScript"
created: "2026-10-04"
updated: "2026-11-13"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/Yarad_ai/status/2121225629177663872"]
fetched_at: "2026-11-14T15:07:50.363346+00:00"
---

# OpenFilm

## 出来ること

- コーディングエージェントがHTMLページを組み合わせて動画を作成し、ローカルのブラウザー上で動くStudioで編集できます。READMEには、タイムライン編集やMP4、GIF、音声、字幕、静止画などの書き出し機能が記載されています。

## 目的・背景

- READMEは、エージェントが作った動画を人がStudioで確認・編集できる仕組みとして説明しています。動画の各ページは `frame(t)` で時刻に応じた画面を描画します。

## 依存関係

- README記載のインストール要件はNode.js 22.2以上とffmpegです。Studioの保存バージョンにはgitも必要で、初回実行時にヘッドレスChromium（約100 MB）をダウンロードします。ソースから実行する場合はNode.js 22.18以上、pnpm 9、ffmpeg、gitが必要です。

## 実行条件

- READMEではmacOS、Windows、Linuxに対応するとしています。StudioはChromiumベースのブラウザー（ChromeまたはEdge）で使用します。生成音声・音楽・画像・動画には、対応サービスのキーをStudioのSettings → Servicesで設定するか、StudioでOpenFilmにサインインする方法が記載されています。

## 最短手順

- README記載の手順は `npx skills add openfilm/openfilm` を実行し、エージェントに動画制作を依頼する方法です。スキル非対応のエージェント向けには `npx -y openfilm@latest` を実行して表示される手順に従うよう案内しています。

## 変更履歴

- 2026-11-14: 初回登録
