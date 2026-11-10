---
repo: DozenTwelve/Papermorph
name: Papermorph
genre: video-gen
url: https://github.com/DozenTwelve/Papermorph
license: MIT
language: JavaScript
created: 2026-10-03
updated: "2026-11-09"
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/DDJCXX/status/2117504549661577290
flags: []
risk_notes: "入力に書籍・教材を使う場合、その著作物の利用許諾が必要。生成物の権利は利用者側の責任。"
stars: 1476
forks: 190
open_issues: 2
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 831937
archived: false
fetched_at: "2026-11-09T21:44:39Z"
last_release: "engine-v2.11"
last_release_at: "2026-11-07"
---

# Papermorph

## 出来ること

- 本や教材を、**アニメーション付き・ナレーション付き・インタラクティブな Web 教材**に変換する Claude Code 向けスキル。
- 用途別の出力: 教材PDF → 章ごとのインタラクティブ授業（数式や図が解説に合わせて動く）／童話 → 紙人形アニメ（ナレーション・字幕・効果音付き）／1つのテーマ → 7分のドキュメンタリー＋縦型ショート6本。
- 絵本は、スキャンした原書の挿絵から図柄・舞台・文字を切り抜いて人形と背景にできる（`lift.py`）。絵を描き起こさず、原本の画風のまま動かす作り方。
- 各章を 1080p の動画と字幕として書き出せる。ナレーションは無料のTTSを使用。
- SCORM 対応（トピックに `scorm`）。eラーニング配信を想定した構成。
- **engine-v2.10**: 既定エンジンが v2.10 に上がり、`cam.onPlane`（パンで遠景を画面内の一点に置く）などのカメラ操作が加わった。教材・絵本側の不具合修正も続いている。

## 目的・背景

2026-10-03 公開、★1,145。知識系コンテンツを「読む」から「見る・触る」に変える需要に合わせたスキルで、Claude Code のスキル機構（`SKILL.md`）として配布される。v2.9 のエンジンでレンダリングする。

## 依存関係

- **uv / ffmpeg / Playwright** の3つを事前にインストールする必要がある（投稿でも明記）。Playwright は chromium と firefox の両方を入れる（`check.py` が両方で回して、Firefox の滑らかさも見る）。
- Claude Code（スキル実行）
- ナレーションは Edge TTS（ネットワーク接続が必要）または Kokoro（ローカル）。ElevenLabs を使う場合のみ有料。
- Node.js（レンダリング周り）。画像生成・動画化・ElevenLabs など有料ステップを使うときだけ OpenRouter か OpenAI のキーが要る。

## 実行条件

- レンダリングはローカル（Playwright のヘッドレスブラウザ＋ffmpeg）。
- ディスク: リポジトリは約733MB（サンプル・アセット込み）。生成物が別途積み上がる。
- 書籍・教材を入力にする場合、著作権者の許諾が必要。

## 最短手順

```bash
uv --version && ffmpeg -version && python -m playwright install
# Claude Code にスキルとして導入し、書籍PDFまたはテーマを渡す
```

## 変更履歴

- 2026-11-04: 初回登録（★1,145 / engine-v2.9 / MIT / 30日100+コミット）
- 2026-11-05: 絵本の原書スキャンから図柄・舞台・文字を切り抜く `lift.py` を追加。依存の実態を修正（Edge TTS はネットワーク必須、Playwright は chromium と firefox、有料ステップのみ OpenRouter/OpenAI キー）（342e272）
- 2026-11-06: 既定エンジンを engine-v2.10 に更新、`cam.onPlane` などのカメラ操作を追記（2952bed / b761eae）
