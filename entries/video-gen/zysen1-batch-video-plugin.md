---
repo: "zysen1/batch-video-plugin"
name: "batch-video-plugin"
genre: video-gen
url: "https://github.com/zysen1/batch-video-plugin"
license: "MIT"
stars: 100
language: ""
created: "2026-11-01"
updated: "2026-11-01"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 25
open_issues: 0
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
size_kb: 47
archived: false
fetched_at: "2026-11-09T21:47:09Z"
last_release: ""
last_release_at: ""
---

# batch-video-plugin

## 出来ること

- 一言の物語を N 個の10秒ショットに分割し、各ショット1〜6本の候補を抽选（生成）→ 自動選片 → 終審 → 二次剪輯 → 成片までを通す、縦型/横型ショートの制作パイプライン。
- 人物・場景・視覚の三段ロック（风格圣经）を毎ショットのプロンプト先頭に逐字で差し込み、2ショット目以降は前ショットの最終フレームから接力させることで、ショット間のキャラクター一貫性を保つ。
- 終審は各候補の首/中/尾フレームを抜き、15種類の「偽信号」（プラスチック肌、表情の硬さ、色温度のズレ、服飾・髪型の跳び、同一性ドリフト、継ぎ目のカメラ跳び、看板の文字化け、小道具の消失、口パクの不明瞭など）で pass / warn / fail を判定し、カット秒数まで含む修正案を出す。規格（長さ/解像度/音声）と実在感は別採点。
- 終審から ffmpeg 用の精剪方案（各ショットの裁剪点、継ぎ目のハードカット or 2〜3フレームのディゾルブ、色温度・露出・ラウドネスの統一、軽いグレイン）を自動生成し、実行して成片を書き出す。剪不了的ショットは再抽清单へ回す。
- Web UI（ビルド不要の素の JS）と JSON API、SQLite 保存、发布文案の自動生成（AI 生成である旨の表記入り）。

## 目的・背景

Muse 内プラグインの公開ワークフロー記述を元に、ゼロから独立実装したものと明記されている（本家のコードやユーザーデータは含まない）。**動画生成モデルは同梱しない**。既定の mock バックエンドは ffmpeg でプレースホルダのクリップを作るだけで、全工程がモデル無しでも通ることを確認するための構成。実用の映像を得るには `adapters.py` に自前の動画生成ベンダーを接続する必要がある。

## 依存関係

- Python 3.12 以上。
- `ffmpeg` / `ffprobe` が PATH 上に必要。
- pip 依存はゼロ（標準ライブラリ + SQLite + ffmpeg のみ）。フロントはビルド不要。

## 実行条件

- そのままでは mock バックエンドのみ。実生成には外部の動画生成 API への接続設定が必須。
- データは `./data/`（SQLite と生成物）に置かれ、gitignore 済み。
- 単体テストと end-to-end のデモテストが同梱（`python3 -m unittest discover -s tests -v` / `demo_test.py`）。

## 最短手順

```bash
git clone https://github.com/zysen1/batch-video-plugin.git
cd batch-video-plugin
python3 server.py --port 8000
# http://127.0.0.1:8000
```

## 変更履歴

- 2026-11-03: 初回登録（star 42 / pushed 2026-11-01 / MIT）
