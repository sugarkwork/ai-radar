---
repo: "Humpalumps/Ultra-Water"
name: "Ultra Water"
genre: 3d-motion
url: "https://github.com/Humpalumps/Ultra-Water"
license: "MIT"
stars: 653
language: "JavaScript"
created: "2026-10-28"
updated: "2026-11-02"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 97
open_issues: 0
commits_30d: 20
commits_90d: 20
commit_cadence: "daily"
size_kb: 163
archived: false
fetched_at: "2026-11-09T21:30:58Z"
last_release: ""
last_release_at: ""
---

# Ultra Water

## 出来ること

- three.js（WebGL2）向けのリアルタイム海レンダラ。FFT による波、岸の砕波、泡、スワッシュ、コースティクス、水中表現、浮力、島のデモシーンをまとめて実装。
- デモは `Lagoon` など複数のショット（カメラと太陽の位置がセット）を切り替えられる。左上のパネルに GPU・レンダ解像度・fps・ms/frame・20秒グラフを表示し、`Uncap FPS` / `Cap to display` / `Run benchmark`（300フレームをフェンス同期で計測）を備える。
- モバイル判定（`pointer: coarse`）で軽量プロファイルに自動で切り替える: 解像度0.6、MSAA 2x、反射0.35スケール、bloom なし。`?mobile` / `?desktop` で強制も可能。
- 作者の計測値（RTX 3060、Chrome/ANGLE D3D11、4x MSAA、1954×1692）は Open ocean 3.30ms（約303fps）〜 Surf rock 5.92ms（約169fps）。パス別の内訳（water / opaque / post / caustics / FFT）も README にある。

## 目的・背景

three.js で「実写寄りの海」を出そうとするとポストエフェクトとパス数で破綻しやすい。このリポジトリはパス構成とモバイル向けの段階的フォールバックを実測値つきで整理している点に価値がある。README は過去に掲載した数値が `readPixels`/`finish` 同期の誤りで2〜4倍低かったと自ら訂正しており、現在はフェンス同期のベンチマークを正としている。

## 依存関係

- Node.js（`npm install` / `npm run dev`）。
- 追加アセットの外部ダウンロードは不要。

## 実行条件

- デスクトップの Chrome/Edge 系を想定。モバイルは自動で軽量プロファイルになるが、端末によっては 30fps 固定に落ちる。
- 数値は作者の1環境での測定で、他 GPU での再現値ではない。

## 最短手順

```bash
git clone https://github.com/Humpalumps/Ultra-Water.git
cd Ultra-Water
npm install
npm run dev
```

## 変更履歴

- 2026-11-03: 初回登録（star 617 / pushed 2026-11-02 / MIT）
