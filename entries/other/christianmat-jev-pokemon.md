---
repo: "christianmat/jev-pokemon"
name: "Jev Plays Pokémon Red"
genre: "other"
url: "https://github.com/christianmat/jev-pokemon"
license: "GPL-2.0"
stars: 133
language: "TypeScript"
created: "2026-09-25"
updated: "2026-09-28"
forks: 10
open_issues: 2
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 100
size_kb: 9041
archived: false
flags: ["unverified"]
risk_notes: "クリア結果、所要時間、費用は作者の報告。独立再現、現行の Gateway 料金、別環境での動作は未確認。GitHub の公開 Releases ページにリリースは掲載されていなかった。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:31:32+00:00"
---

# Jev Plays Pokémon Red — ゲーム状態から行動候補を組み立てる AI 実行基盤の実例

## 出来ること

- Game Boy エミュレーターの RAM からマップ、手持ち、戦闘、表示テキストを取得する。行動候補にタイプ相性やダメージ見積もりを添えて Jev に渡し、選ばれた行動をボタン入力に変換する。
- 作者は37時間40分、16,150回の判断、Jev 利用料約1.65米ドルでクリアしたと報告している。全滅は16回で、四天王への挑戦は15回だった。

## 目的・背景

- モデルが行動を選び、実行側が A* 経路探索、メニュー操作、ストーリー進行の判定を担う。行動候補の設計や、判断と操作を分離する構成を参照できる。
- 同じ失敗が続く場合は実行側が代替行動を選び、それでも進まなければチェックポイントを再読み込みする。クリア結果にはこれらの補助が含まれる。

## 依存関係

- macOS または Linux、Node.js 20 以上、Git。セットアップでは RGBDS と pret/pokered を使ってシンボルデータを生成する。
- エミュレーターは serverboy / GameBoy-Online 系。実モデルは Vercel AI Gateway 経由で呼び出す。

## 実行条件

- 正規に入手した Pokémon Red の米国・欧州版 ROM が必要。ROM は同梱されず、RAM アドレスは対象の版に依存する。README はコードのライセンスを GPL-2.0-or-later と記載している。
- 既定の mock は無料の代替動作。実モデルには Gateway の認証情報が必要で、README 記載の単価は入力100万トークン当たり0.042米ドル。

## 最短手順

- リポジトリを取得し、README に沿って `npm install` と `npm run setup` を実行する。対象 ROM を `roms/red.gb` に置き、`.env.example` を `.env` にコピーする。
- ローカルでは `npm start -- --speed 1` で起動し、`http://localhost:8787` で観戦できる。自動実行から CLI を呼ぶ場合は `npm run headless -- --steps 3000` でログを取得できる。
- Jev に判断を委ねる場合は、実行前に `JEV_MODE=gateway` と `AI_GATEWAY_API_KEY` を設定する。判断候補、確率、応答時間は `logs/jev-calls.jsonl` に記録される。

## 変更履歴

- 2026-11-10: 初回登録
