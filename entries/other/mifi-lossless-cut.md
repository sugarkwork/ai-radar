---
repo: "mifi/lossless-cut"
name: "LosslessCut"
genre: "other"
url: "https://github.com/mifi/lossless-cut"
last_release: "v3.70.2"
flags: ["unverified"]
risk_notes: "実ファイルでの処理速度、カット位置、CLIとHTTP APIの動作は未実測。公開リリースページで最新タグは確認したが、公開日時の年とタイムゾーンは未確認。"
stars: 45884
forks: 2317
open_issues: 164
size_kb: 31407
language: "TypeScript"
created: "2016-10-30"
updated: "2026-11-09"
archived: false
license: "GPL-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:59:03.611Z"
---

# LosslessCutで動画・音声を再エンコードせずに切り出す

## 出来ること

- 動画・音声の区間抽出、トラックの取り出し、同一コーデックの素材の結合、MKVからMP4などへのコンテナ変換に対応する。

## 目的・背景

- 生成・収録済みの素材から使う部分だけを残す粗編集に使える。既定のキーフレームカットでは、書き出しの開始位置が指定点より前のキーフレームになることがある。

## 依存関係

- メディア処理にFFmpegとFFprobeを使用する。公式CLI文書には両者の実行ファイルがあるフォルダーを指定する設定もある。

## 実行条件

- Windows、macOS、Linux向けのデスクトップアプリ。GitHubの公式配布は無償で、Mac App StoreとMicrosoft Storeの版は有料。実験的なHTTP APIはループバックで待ち受け、認証なしで同じ端末のプログラムから操作できる。

## 最短手順

- 公式GitHub配布版を展開して起動し、素材を開く。タイムラインで開始点をI、終了点をOで指定し、Exportで書き出す。出力を再生して開始位置を確認する。
- AIエージェントにローカルのシェル実行権限がある場合は、実行ファイルのパスを設定した上で `LosslessCut file1.mp4` を呼び出して素材を開ける。区間指定と書き出しは上記のGUI手順で行う。

## 変更履歴

- 2026-11-10: 初回登録
