---
repo: "JohnHeibel/ClaudeAnimationBase"
name: "Claude Animation Base"
genre: "video-gen"
url: "https://github.com/JohnHeibel/ClaudeAnimationBase"
stars: 2827
forks: 266
open_issues: 8
size_kb: 8183
language: "JavaScript"
created: "2026-09-23"
updated: "2026-09-24"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 15
commit_cadence: "monthly"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "公開資料の読み取りで確認。コードは実行しておらず、映像の仕上がり、端末ごとの描画速度、他のエージェントでの再現性、エージェントの利用料金は未確認。発見投稿の再生数・制作時間は本キットの評価根拠に含めていない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2115193601458151552"]
fetched_at: "2026-11-10T11:59:28+00:00"
---

# Claude Animation Baseで作る手描き風2Dアニメーション

## 出来ること

- Clawdの表情、向き、目や口、帽子、ダンスなどを組み合わせてシーンを作る。付属レンダラーは確認用のコマ一覧やMP4を書き出せる。

## 目的・背景

- 作者がミュージックビデオ制作に使ったコードとモデルの挙動の振り返りをもとに、キャラクター素材と制作ガイドをまとめた。READMEでは、絵コンテ、ショット実装、コマ一覧での確認、動画出力の順に進める。

## 依存関係

- 描画にp5.jsとp5.brush、ブラウザー制御にpuppeteer-coreを使う。ローカルレンダリングにはNode.js、Google Chrome、FFmpegが必要。

## 実行条件

- READMEによれば、専用GPUがない環境では水彩塗りの描画が遅くなる。LinuxではソフトウェアWebGL用に `--soft-gl` が用意されている。
- リポジトリはMITライセンス。複製や実質的な部分の再配布では著作権表示と許諾文を保持する。GitHubの公開Releases一覧は空だった。

## 最短手順

- リポジトリを取得し、ルートで `npm install` と `node render.mjs --clip --out=out/video.mp4` を順に実行すると、README記載の11秒デモを書き出せる。
- 新作はリポジトリをClaude Codeなどのコーディングエージェントで開き、`ANIMATION_GUIDE.md` を読ませたうえで、登場キャラクター、動作、尺を指定する。絵コンテを先に出し、ショットごとの実装とコマ一覧での確認を経て `out/video.mp4` に出力するよう依頼する。

## 変更履歴

- 2026-11-10: 初回登録
