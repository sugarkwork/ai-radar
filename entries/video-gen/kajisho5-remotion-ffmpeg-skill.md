---
name: "remotion-ffmpeg-skill"
genre: "video-gen"
url: "https://github.com/kajisho5/remotion-ffmpeg-skill"
repo: "kajisho5/remotion-ffmpeg-skill"
license: "MIT"
stars: 8
language: "Python"
created: "2026-10-24"
updated: "2026-11-14"
forks: 0
open_issues: 1
commits_30d: 77
commit_cadence: "daily"
commits_90d: 77
size_kb: 9223
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/Manojkumar2257/status/2119092488258674771"]
fetched_at: "2026-11-17T01:12:21.940383+00:00"
---

# remotion-ffmpeg-skill

## 出来ること

- READMEによると、実映像の長さ・fps・サイズ、無音区間、シーン切り替わり、音声ピークなどをffmpeg-skillで測定し、Remotionの既成Compositionで字幕、ジャンプカット、音声ピーク連動グラフィック、章カード、ハイライト、ビートモンタージュ、カラオケ字幕などを作成できます。レンダー後はフレーム数・fps・サイズ・音声の検証とコンタクトシートの確認を行うと説明されています。

## 目的・背景

- Remotion公式Agent SkillsがRemotionコードの作成を支援するのに対し、このSkillは実映像の測定情報を使った合成からレンダー検証、配信用チェックまでを扱うものとして紹介されています。ffmpeg-skillと併用する設計です。

## 依存関係

- READMEではffmpeg-skillを必須としています。RequirementsとしてPython 3.10以上、Node.js 18以上、FFmpegを挙げ、Remotionのヘッドレスブラウザーは初回レンダー時にダウンロードされると説明しています。

## 実行条件

- Claude Code、Cursor、Codex向けのAgent Skillです。`npx ffmpeg-skill`で必須のffmpeg-skillを、`npx remotion-ffmpeg-skill`で本Skillをインストールする手順が記載されています。README記載のRemotionライセンス条件では、従業員3人以下の個人・営利組織は無料で、より大きな企業にはRemotionの企業ライセンスが必要です。

## 最短手順

- 1. `npx ffmpeg-skill`を実行し、続けて`npx remotion-ffmpeg-skill`を実行します。2. `analyze.py`で入力動画と字幕などを解析し、タイムラインJSONを作成します。3. `render.py`でCompositionをレンダーし、必要に応じて`deliver.py`で配信用チェックを行います。全工程を進める例として`pipeline.py`の実行コマンドもREADMEにあります。

## 変更履歴

- 2026-11-22: 初回登録
