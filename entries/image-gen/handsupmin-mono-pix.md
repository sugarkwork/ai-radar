---
name: "MonoPix"
genre: "image-gen"
url: "https://github.com/handsupmin/mono-pix"
repo: "handsupmin/mono-pix"
license: "unknown"
stars: 160
language: "TypeScript"
created: "2026-03-13"
updated: "2026-10-12"
forks: 8
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 2
size_kb: 28149
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/dextune/status/2119218844560478676"]
fetched_at: "2026-11-17T14:21:50.123532+00:00"
---

# MonoPix

## 出来ること

- 画像をピクセルアートに変換するClean（セルごとの最多色）とDetail（セルごとの平均色）、画像内のピクセルグリッドを検出して整えるSnapを提供。切り抜き、結果比較、PNG出力、直近10件のローカル履歴にも対応するとREADMEに記載されています。

## 目的・背景

- READMEは、AI生成画像などのぼやけた輪郭や不揃いなグリッドをSnapで整え、透明度を保った出力を目指すと説明しています。元画像の格子が不規則な場合、完全な復元は保証できないとの注意もあります。

## 依存関係

- README記載の技術スタックはReact 19、TypeScript 5.9、Vite、Tailwind CSS v4、shadcn/ui、Zustand、fast-pixelizer、Dexie.js、react-easy-crop、react-i18nextです。

## 実行条件

- README記載の要件はNode.js 18以上です。処理はWeb Workerで実行し、データは端末外へ送信されないとREADMEは説明しています。

## 最短手順

- README記載の手順: `git clone https://github.com/handsupmin/mono-pix.git`、`cd mono-pix`、`npm install`、`npm run dev`。

## 変更履歴

- 2026-11-22: 初回登録
