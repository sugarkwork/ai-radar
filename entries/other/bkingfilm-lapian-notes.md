---
name: "拉片笔记（Lapian Notes）"
genre: "other"
url: "https://github.com/bkingfilm/lapian-notes"
flags: ["unverified"]
risk_notes: "AI分析の品質は利用するAIに依存し、READMEは無料AIが大量の画像を処理できず分析を省略する場合があると説明している。"
repo: "bkingfilm/lapian-notes"
stars: 798
forks: 74
open_issues: 1
size_kb: 852
language: "TypeScript"
created: "2026-07-08"
updated: "2026-10-26"
archived: false
license: "MIT"
commits_30d: 7
commits_90d: 9
commit_cadence: "weekly"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/fhwofjow51260/status/2119043539309113474"]
fetched_at: "2026-11-16T21:58:58Z"
last_release: "v0.5.3"
last_release_at: "2026-10-26"
---

# 拉片笔记（Lapian Notes）

## 出来ること

- 映画から1秒間隔でフレームを抽出し、字幕とともにAI分析用のZIPを作成できる。AIの分析結果を読み込むと、剧情泳道时间轴・構造ツリー・観客の感情曲線を生成し、段落ノートを編集してMarkdownなどに出力できる。作者のREADMEによる機能説明。出典: https://github.com/bkingfilm/lapian-notes

## 目的・背景

- 映画の叙事を体系的に学ぶクリエイター向けに、映画を編集可能なショット単位の学習ノートにするツール。READMEでは、映画とノートのデータはサーバーへアップロードされず、ローカルで動作すると説明している。出典: https://github.com/bkingfilm/lapian-notes

## 依存関係

- 開発者向け手動実行ではNode.js 20.19+または22.12+とChrome系ブラウザーが必要。ffmpegは任意で、導入時にRMVB/AVI/HEVCなどの自動変換が利用できる。出典: https://github.com/bkingfilm/lapian-notes

## 実行条件

- Windowsは展開後にrun.bat、Macはrun.commandを起動する。開発者向け手動実行はnpm install、npm run dev。自動変換と字幕検索にはdev serverまたは起動スクリプトが必要。静的ビルドではこの2機能が手動操作に縮退する。出典: https://github.com/bkingfilm/lapian-notes

## 最短手順

- 最新版リリースのZIPをダウンロードして展開し、Windowsではrun.bat、Macではrun.commandを起動する。映画ファイルを読み込み、生成した分析パッケージを任意のAIへ渡し、返されたJSONをツールへ取り込む。AI直連機能では利用者自身のAPI keyを設定し、token料金は利用者のアカウントに請求される。出典: https://github.com/bkingfilm/lapian-notes

## 変更履歴

- 2026-11-16: 初回登録
