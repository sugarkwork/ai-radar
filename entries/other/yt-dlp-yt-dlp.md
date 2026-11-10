---
repo: "yt-dlp/yt-dlp"
name: "yt-dlp"
genre: "other"
url: "https://github.com/yt-dlp/yt-dlp"
stars: 206601
forks: 18169
open_issues: 2777
size_kb: 65029
language: "Python"
created: "2020-10-26"
updated: "2026-11-04"
archived: false
license: "Unlicense"
commits_30d: 26
commits_90d: 89
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "最新リリース、個別動画での字幕取得の成否と字幕品質は未確認。発見投稿が述べる制作本数や収益性も未検証。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2114798387249717600"]
fetched_at: "2026-11-10T11:39:07+00:00"
---

# yt-dlpで動画を保存せずに字幕を取得する

## 出来ること

- 対応サイトの動画から、配信元が提供する字幕や自動生成字幕をファイルに保存できる。`--skip-download` で動画本体の保存を省ける。

## 目的・背景

- 既知の動画URLから字幕を取得し、AIによる要約や構成分析の入力にする。字幕の有無と言語は動画ごとに確認する。発見投稿の制作本数や収益性は、この用途の技術的根拠に含めていない。

## 依存関係

- 公式READMEは ffmpeg、ffprobe、yt-dlp-ejs、対応するJavaScriptランタイムを強く推奨している。

## 実行条件

- Pythonで実行する場合、公式READMEの対応範囲はCPythonまたはPyPyの3.11以上。リポジトリのライセンスはUnlicense。取得した字幕の再利用条件はコンテンツごとに確認する。

## 最短手順

- インストール済みの環境で、利用権限のある単一動画URLを `yt-dlp --list-subs "URL"` に渡し、字幕の言語タグを確認する。
- 日本語字幕がある場合は `yt-dlp --skip-download --write-subs --sub-langs ja "URL"` で保存する。自動生成字幕を使う場合は `--write-subs` を `--write-auto-subs` に替える。
- AIから呼ぶ場合は、ローカルCLIを実行できるエージェントのツールに固定した引数と許可済みURLを渡す。保存された字幕ファイルの本文を読み込み、要約や分析の入力にする。

## 変更履歴

- 2026-11-10: 初回登録
