---
repo: "wquguru/shisei"
name: "Shisei"
genre: "link-asset"
url: "https://github.com/wquguru/shisei"
stars: 478
forks: 102
open_issues: 0
size_kb: 255884
language: "Python"
created: "2026-10-29"
updated: "2026-11-02"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v0.4.1"
flags: ["unverified"]
risk_notes: "線画と各マップの画素整合、生成結果の一貫性、ControlNetのモデル別互換性、ZIPの中身とチェックサムは独立検証していない。リリースタグは確認済みで、公開日時は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/dextune/status/2117483057343353195"]
fetched_at: "2026-11-10T09:05:26+00:00"
---

# Shisei — 画像生成向けのマネキン姿勢素材集

## 出来ること

- 4シリーズの計280ポーズから参照画像を選べる。正面・斜め・側面・上・下の5方向を扱い、品質審査で除外されたビューなどには欠番がある。名称とカテゴリは日・中・英・韓の4言語。
- READMEによると、944の線画ビューに同じ画素位置に対応するクレイ・深度・法線マップを収録。v0.4.1では各マップの個別ZIPと全形式入り69.0 MBのZIPを配布する。 [README](https://github.com/wquguru/shisei#readme)

## 目的・背景

- 顔のないマネキンを参照画像にし、姿勢や構図と、顔・服・背景の指定を分ける。作者は同じ姿勢の別アングルを使うとショット間の一貫性を保ちやすいと説明している。審査で除外した理由は `data/qc.json` に記録する。 [README](https://github.com/wquguru/shisei#readme)

## 依存関係

- 公開ギャラリーは静的サイトで、READMEは追加の実行時依存がないと説明している。ローカルでギャラリーをビルドする手順にはPython 3を使う。深度・法線マップによる条件付けには、対応するControlNetワークフローを用意する。 [README](https://github.com/wquguru/shisei#readme)

## 実行条件

- 素材は無料。画像とプロジェクト独自のデータはCC0 1.0、コードと文書はApache-2.0。外部カタログ由来のポーズの選定・番号・名称・カテゴリは両ライセンスの対象外とREADMEに記載されている。 [READMEのライセンス欄](https://github.com/wquguru/shisei#license)

## 最短手順

- 公開ギャラリーでポーズと角度を選び、参照画像を受け付ける画像生成ツールに線画を姿勢・構図の参照として渡す。 [公開ギャラリー](https://shisei.indaloop.app/en/)
- ControlNetを使う場合は、リリースから深度または法線のZIPを選び、対象ビューの画像を対応する条件入力に渡す。 [v0.4.1](https://github.com/wquguru/shisei/releases/tag/v0.4.1)

## 変更履歴

- 2026-11-10: 初回登録
