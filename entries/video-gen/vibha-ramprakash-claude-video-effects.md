---
repo: "Vibha-Ramprakash/claude-video-effects"
name: "claude-video-effects"
genre: "video-gen"
url: "https://github.com/Vibha-Ramprakash/claude-video-effects"
license: "unknown"
stars: 839
language: "Python"
created: "2026-10-22"
updated: "2026-11-09"
forks: 202
open_issues: 1
commits_30d: 9
commit_cadence: "weekly"
commits_90d: 9
size_kb: 2977
archived: false
flags: ["unverified"]
risk_notes: "公式 README は公開 raw URL で確認。最新リリース、顔追従・遮蔽処理・発話位置の精度、初回セットアップの所要時間、Codex 互換性は未確認。ライセンス欄は親の GitHub API 実測値 unknown を保持。MIT と同梱素材の個別ライセンスは README の記載に基づき、各ライセンス本文は未照合。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/ganfanren_ai/status/2117590608487325707"]
fetched_at: "2026-11-10T09:44:20Z"
---

# Claude Video Effects — Claude Code でトーク動画に顔追従エフェクトを追加

## 出来ること

- README は51種類のエフェクトを掲載。素材を頭の周りに回す orbit や、人物を残して周囲を暗くする spotlight などを時間指定で重ねられる。元の音声を維持し、MP4を別ファイルに出力する。

## 目的・背景

- 既存の短尺トーク動画に演出を加えるスキル。作者は顔追従と、顔を覆う要素の背面配置を説明している。出力は確認用の下書きで、効果音や字幕の追加は含まれない。

## 依存関係

- Claude Code、Python、ffmpeg を使用。README は顔追跡に OpenCV YuNet、人物切り抜きに MediaPipe Selfie Segmenter を挙げる。

## 実行条件

- 作者は人物が画面内にいる縦長動画を推奨。README の記載では標準出力は1080pで、不足する Python と ffmpeg は初回に導入する。
- README はスキルを無料と案内し、モデル・フォントの個別ライセンスとして MIT、Apache 2.0、SIL OFL を記載。その他は MIT と案内している。Claude Code 側の利用料金は未確認。

## 最短手順

- 正規リポジトリを ~/.claude/skills/effects にクローンし、Claude Code を再起動する。Windows PowerShell では $HOME\.claude\skills\effects を使う。
- Claude Code のチャットに動画を追加し、`/effects orbit from 3 to 6 seconds` と入力する。README によれば、出力は元動画と同じ場所の `yourvideo_effects.mp4`。

## 変更履歴

- 2026-11-10: 初回登録
