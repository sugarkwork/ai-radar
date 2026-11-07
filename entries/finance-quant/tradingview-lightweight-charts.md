---
repo: tradingview/lightweight-charts
name: Lightweight Charts
genre: finance-quant
url: https://github.com/tradingview/lightweight-charts
license: Apache-2.0
stars: 17788
language: TypeScript
created: 2019-05-24
updated: 2026-11-06
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources:
  - https://tradingview.github.io/lightweight-charts/
flags: []
risk_notes: ""
forks: 2694
open_issues: 129
commits_30d: 63
commits_90d: 100
commit_cadence: daily
size_kb: 223577
archived: false
fetched_at: "2026-11-06T22:53:25Z"
last_release: v5.2.1
last_release_at: 2026-08-12
---

# Lightweight Charts

## 出来ること

- TradingView 製の**金融チャートライブラリ**。HTML5 canvas に描画し、軽量（約45KB）で高速。株価・為替・暗号資産のローソク足、ライン、エリア、ヒストグラム、バーチャートを描ける。
- リアルタイム更新に強い。`series.update({time, value})` で最新バーの値だけ差し替える設計なので、WebSocketで流れてくるティックをそのまま反映できる。
- パン／ズーム、クロスヘア、価格スケール、タイムスケール、マーカー、価格ライン、トレンドラインの描画ツールを標準で持つ。
- TypeScript で書かれ型定義を同梱。React/Vue/Svelte など任意のUIフレームワークに埋め込める。
- v5.2.1 でリポジトリに **Agent Skill**（`.github/skills/lightweight-charts/SKILL.md`）が同梱された。v5 API の規約・考え方・よくある落とし穴を AI コーディングアシスタントに教える内容。

## 目的・背景

TradingView のチャートを自前サービスに組み込みたい、という需要に対して、**フル機能の Charting Library（別ライセンス）ではなく、描画に絞った軽量版**を Apache-2.0 で公開したもの。バックテスト結果の可視化や、自作トレードダッシュボードのチャート部分に使う。

## 依存関係

- npm: `npm install lightweight-charts`。ブラウザ向けのESモジュール。
- ビルド環境（Vite / webpack など）がある前提。単体の `<script>` でもCDN版が使える。

## 実行条件

- v5 系では系列の追加が `chart.addSeries(LineSeries, options)` に変わった。v4 の `addLineSeries()` を使うサンプルは動かないので、バージョンを合わせる。
- データは `{ time, open, high, low, close }` の配列。時刻は UTC の UNIX 秒（または `YYYY-MM-DD`）。並びは昇順で、重複・逆行があると描画が崩れる。
- MA などの指標は自分で計算して別系列として追加する（ライブラリは指標を持たない）。
- ★17,775・直近30日で59コミット。v5.2.1。

## 最短手順

```bash
npm install lightweight-charts
```

```js
import { createChart, CandlestickSeries } from 'lightweight-charts';

const chart = createChart(document.getElementById('chart'), {
  layout: { background: { color: '#0b0e14' }, textColor: '#d1d4dc' },
  timeScale: { timeVisible: true },
});

const candles = chart.addSeries(CandlestickSeries, {
  upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,
});
candles.setData([
  { time: 1762300800, open: 100, high: 104, low: 99, close: 103 },
  { time: 1762387200, open: 103, high: 105, low: 101, close: 102 },
]);

// リアルタイム更新
// candles.update({ time: 1762473600, open: 102, high: 106, low: 102, close: 105 });
```

## 変更履歴

- 2026-11-05: 初回登録（★17,775 / pushed 2026-11-05 / Apache-2.0 / v5.2.1）
- 2026-11-06: v5.2.1 — リポジトリに Agent Skill を同梱（v5 API の規約と落とし穴）（2e1d5ce9）
