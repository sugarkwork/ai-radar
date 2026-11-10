---
repo: "georgmartius/vid.stab"
name: "VidStab"
genre: "other"
url: "https://github.com/georgmartius/vid.stab"
license: "unknown"
stars: 991
language: "C"
created: "2011-11-24"
updated: "2026-08-14"
forks: 126
open_issues: 10
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 23
size_kb: 1748
archived: false
last_release: "v1.1.2"
flags: ["unverified"]
risk_notes: "補正量・画質・処理速度は実測していない。READMEはmasterの仕様を含むため、最新公開リリースv1.1.2や各FFmpeg配布ビルドでの機能差は未確認。公開日の年は取得した表示から確定できなかった。ライセンス欄は親工程のAPI値を保持し、利用条件は対象バージョンのライセンス文書で確認する。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/RealMarvelX/status/2117612832019689696"]
fetched_at: "2026-11-10T09:50:37Z"
---

# VidStabで手持ち動画の揺れを補正する

## 出来ること

- FFmpegのvidstabdetectでフレーム間の動きを解析し、vidstabtransformで解析結果を使って手ぶれを補正する。

## 目的・背景

- 手持ち撮影や車載撮影で生じる揺れを抑える。READMEではフレーム間の平行移動と回転を検出し、カメラの動きを平滑化する仕組みを説明している。
- 補正効果は開発元の説明に基づく。素材ごとの改善幅や処理速度は未測定。

## 依存関係

- この手順には、libvidstab対応でvidstabdetectとvidstabtransformの両フィルターを備えたFFmpegが必要。
- masterのREADMEはLGPL 2.1以降、v1.1.2までのリリースはGPLと記載している。

## 実行条件

- 両パスに同じフレーム列を同じ順序で渡す。インターレース素材は、両パスで同じ設定のデインターレース処理を先に行う。
- 解析結果の一時ファイルと出力動画を書き込める作業ディレクトリを使う。

## 最短手順

- AIエージェントから呼ぶ場合は、ローカルのコマンド実行機能で `ffmpeg -filters` を実行し、両フィルターが利用可能か確認する。
- 1パス目で `ffmpeg -i input.mp4 -vf vidstabdetect=result=motion.trf -f null -` を実行する。
- 1パス目が成功したら、同じ作業ディレクトリと入力で `ffmpeg -i input.mp4 -vf vidstabtransform=input=motion.trf stabilized.mp4` を実行する。

## 変更履歴

- 2026-11-10: 初回登録
