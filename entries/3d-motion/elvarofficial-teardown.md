---
repo: "elvarofficial/teardown"
name: "teardown"
genre: "3d-motion"
url: "https://github.com/elvarofficial/teardown"
license: "MIT"
stars: 2781
language: "JavaScript"
created: "2026-10-30"
updated: "2026-10-31"
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: []
risk_notes: ""
forks: 429
open_issues: 9
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
size_kb: 18266
archived: false
fetched_at: "2026-11-09T21:30:51Z"
last_release: ""
last_release_at: ""
---

# teardown

## 出来ること

- 「これはどう動くのか」と聞くと、機械を3Dシミュレータにしたオフライン HTML を1枚作る Claude Code スキル。中央で機械が動き、周囲のパネルが実数値を読み、ボタンで実際に働いている部品が開き、放置すると自動でツアーが回る。
- 例: ロボット蜂 Mellis HB-7、ロボットサソリ Telson SC-8、ロボットタコ Pelagos OC-8、V8 エンジン、セスナ、ストランドビースト。
- 最終成果物は単体 HTML（オフラインで開ける）。加えて ffmpeg で 60fps の動画に録れる。

## 目的・背景

2026-10-30 作成、翌日までに1,500 star。機械原理・構造分解・工学の解説向け。ポストでは「3D で回転・分解できる」と紹介されているが、実体は「1枚の HTML シミュレータ＋録画」であり、動画生成モデルではない。

## 依存関係

- Node.js 20 以上。
- インストール後に一度 `npm install` と `npx playwright install chromium` を実行する。
- 動画化に ffmpeg、効果音に Python 3。

## 実行条件

- 生成はローカルのブラウザ描画。GPU・API キー不要。
- 出力は HTML（オフライン可）。録画は Playwright 経由なのでヘッドレス Chromium が必須。
- モデル形状はコードで記述するため、実在機の正確な図面再現ではない（README の作例も「動く仕組みの説明」用）。

## 最短手順

```bash
npx skills add elvarofficial/teardown -g -a claude-code
cd <skill-dir> && npm install && npx playwright install chromium
node sims/build.mjs v8-live      # teardown-out/dist/v8-live.html
```

## 変更履歴

- 2026-11-03: 初回登録（star 1,524 / pushed 2026-10-31 / MIT / Node 20+）
