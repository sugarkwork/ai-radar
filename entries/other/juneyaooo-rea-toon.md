---
name: "rea-toon"
genre: "other"
url: "https://github.com/JuneYaooo/rea-toon"
repo: "JuneYaooo/rea-toon"
license: "unknown"
stars: 253
language: "Python"
created: "2026-11-14"
updated: "2026-11-17"
forks: 45
open_issues: 0
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 8
size_kb: 15062
archived: false
flags: ["unverified"]
risk_notes: "READMEはライセンスを「Noncommercial」と表示していますが、API計測値はlicense unknownです。具体的なライセンス条件は未確認です。長編シリーズではトークン消費が多く、APIモデルは呼び出しごとに課金されるとREADMEにありますが、実際の費用は未確認です。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/shenxiankk/status/2122508772186738901"]
fetched_at: "2026-11-17T23:25:29.941429+00:00"
---

# rea-toon

## 出来ること

- 手元にある短編ドラマ動画を分析し、作品の構成や視聴者を引きつける要素をまとめたStudy、シーンや台詞を整理したScript、各ショットの画面・動き・台詞・音などを記したShot scriptを生成します。出力には閲覧用HTMLページと、エージェントが読めるVIDEO.md形式のデータが含まれます。READMEでは、ライブアクション、AI生成ドラマ、2D/3Dアニメ、モーションコミック、解説動画を対象として説明しています。

## 目的・背景

- 短編ドラマがなぜ機能するのか、脚本がどう書かれているか、各ショットがどう撮られているかを学ぶための分析ツールとして説明されています。各分析結果にはショット番号、時刻、台詞、フレームなどの根拠を付け、誤りを修正してページを再構築できるとREADMEにあります。

## 依存関係

- READMEでは、ショット分割や音声分離にrea-videoを利用すると説明しています。字幕トラックのOCRはローカルで行うと記載されています。

## 実行条件

- Python 3.10以上とffmpegが必要です。画像を扱えるエージェント、またはrea-toon用に設定したOpenAI互換のビジョンモデルが必要です。エージェント自身が画像を確認する方式ではAPIキー不要とREADMEにあります。動画はローカルにあるファイルまたはエピソードごとのファイルを含むフォルダーから入力し、リンクからのダウンロードには対応しません。

## 最短手順

- Claude Code、Codex、またはコマンドを実行できるエージェントに、READMEの例にならって「Install https://github.com/JuneYaooo/rea-toon, then break down this short drama: <動画ファイルまたはエピソード動画のフォルダー>」と指示します。長いシリーズは、READMEが勧めるようにまず5話で結果と費用を確認してから続けます。

## 変更履歴

- 2026-11-22: 初回登録
