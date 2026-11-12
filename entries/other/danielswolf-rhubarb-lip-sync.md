---
name: "Rhubarb Lip Sync"
genre: "other"
url: "https://github.com/DanielSWolf/rhubarb-lip-sync"
repo: "DanielSWolf/rhubarb-lip-sync"
license: "unknown"
stars: 2763
language: "C++"
created: "2015-10-19"
updated: "2026-06-16"
forks: 329
open_issues: 26
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 120528
archived: false
flags: ["unverified"]
risk_notes: "ライセンスは提供されたリポジトリ情報で確認できず、unknownです。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/RealMarvelX/status/2118525010088251781"]
fetched_at: "2026-11-12T11:19:46.293973+00:00"
---

# Rhubarb Lip Sync

## 出来ること

- 音声ファイルを解析して発話を認識し、2Dの口形アニメーション情報を生成する。CLIではTSV・XML・JSONなどの形式で出力でき、After Effects、Moho、OpenToonz、Spine、Vegas Pro向けの連携もREADMEに記載されている。

## 目的・背景

- ゲーム、アニメーション、その他の制作物で音声に合わせた口の動きを作る用途として説明されている。

## 依存関係

- READMEに外部依存関係の一覧は記載されていない。

## 実行条件

- Windows、macOS、Linux向けのコマンドラインツール。入力音声形式はWAVE（.wav）またはOgg Vorbis（.ogg）。

## 最短手順

- 対象OS向けのリリースを取得して展開し、コマンドラインで `rhubarb -o output.txt my-recording.wav` のように入力音声と出力先を指定する。

## 変更履歴

- 2026-11-12: 初回登録
