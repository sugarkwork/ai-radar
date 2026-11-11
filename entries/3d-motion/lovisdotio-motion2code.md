---
repo: "lovisdotio/motion2code"
name: "Motion2Code"
genre: "3d-motion"
url: "https://github.com/lovisdotio/motion2code"
license: "MIT"
stars: 349
forks: 31
open_issues: 2
size_kb: 7539
language: "HTML"
created: "2026-10-20"
updated: "2026-10-20"
archived: false
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "最新リリースの版と日時は未確認。掲載例の容量・再現精度、任意の動画への適用範囲、実行環境での動作は独立検証していない。外部ライブラリ・フォントの利用条件とエージェント利用料は未確認。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116241528737693741"]
fetched_at: "2026-11-10T13:03:43+00:00"
---

# Motion2Codeで動画を編集可能なSVGアニメーションに再構成する

## 出来ること

- モーション動画をインラインSVGと単一のGSAPタイムラインを使うループ付きHTMLとして再構成する。READMEには、画面録画をScrollTrigger付きの操作可能なページとして再構成する手順もある。

## 目的・背景

- 先に入力動画からフレーム、カット前後の画像、配色を抽出し、生成後は元動画と同時刻の描画を比較する。
- 作者のREADMEでは、文字アニメーションの一例を10秒・24 KBと記載している。容量と再現精度は独立実測していない。

## 依存関係

- 補助スクリプトにPython 3.9以上とffmpeg、ブラウザを開く処理にPlaywrightとChromiumを使う。生成ページはGSAP 3をCDNから読み込み、モーフ時はflubberも使う。READMEのページ仕様にはGoogle Fontsも記載されている。

## 実行条件

- 対応するコーディングエージェントと、利用権限のある入力動画を用意する。リポジトリのライセンスはMIT。ギャラリーの入力クリップは比較用として掲載されている。

## 最短手順

- Codex向けには、READMEの手順に従い `skills/motion2code` を `~/.agents/skills/` に配置する。
- Codexに『motion2codeスキルを使い、clip.mp4をループするSVG＋GSAPアニメーションに再構成して』と依頼する。
- エージェントが `study_video.py` で入力を分析してHTMLを作成したら、`frame_diff.py` で差分を確認し、`check_anim.py index.html --runtime` で再生とループの継ぎ目を確認する。

## 変更履歴

- 2026-11-11: 初回登録
