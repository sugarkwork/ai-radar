---
name: "cinetic"
genre: "video-gen"
url: "https://github.com/Leonxlnx/cinetic"
repo: "Leonxlnx/cinetic"
license: "MIT"
stars: 1303
language: "TypeScript"
created: "2026-09-28"
updated: "2026-11-09"
forks: 78
open_issues: 4
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 60899
archived: false
flags: ["unverified"]
risk_notes: "READMEでは作例動画はmediaブランチに置かれ、このブランチにはメディアを含めないと説明されています。機能や品質に関する記述はREADME上の作者の説明で、独立した動作確認ではありません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/flxrnc/status/2123392905934999811"]
fetched_at: "2026-11-20T03:14:40.933872+00:00"
---

# cinetic

## 出来ること

- コーディングエージェントに、製品のローンチ動画やアップデート動画をコードで制作させるスキルです。Remotion（React）またはHyperFrames（HTML、GSAP）を使い、台本、画面、動き、音楽、書き出しと品質チェックを組み立てるとREADMEは説明しています。

## 目的・背景

- 製品チームがよく作るローンチ動画とアップデート動画を、短いブリーフから制作することを想定しています。READMEは、画面を並べるだけでなく、台本の明瞭さ、各行のアニメーション、カメラの動き、ブランド表現を重視すると述べています。

## 依存関係

- READMEに記載された要件はNode.js 22以降、ffmpeg 6以降、Python 3.11以降、ヘッドレスChromium、および音響用のearshot 0.4です。標準のビルド先はRemotion（React）で、HyperFrames（HTML、GSAP）も選べます。

## 実行条件

- 初回制作の前にセットアップ手順にあるテストレンダーを行うようREADMEは案内しています。エージェントはClaude Code、Codex、Cursorなどskills CLIが対応するエージェントでの利用を想定しています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- `npx skills add Leonxlnx/cinetic` で追加し、エージェントに動画制作を依頼します。例としてREADMEは、データベースのブランチ機能を紹介する25秒のローンチ動画を挙げています。プロジェクトのひな型は `bash <skill>/scripts/new-film.sh films/acme --fps 60 --size 1920x1080` で作成できます。

## 変更履歴

- 2026-11-23: 初回登録
