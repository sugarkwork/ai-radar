---
name: "Tost AI - Sprite Sheet Studio"
genre: "image-gen"
url: "https://github.com/camenduru/TostAI-Sprite-Sheet-Studio"
repo: "camenduru/TostAI-Sprite-Sheet-Studio"
license: "unknown"
stars: 88
language: "Python"
created: "2026-09-26"
updated: "2026-10-02"
forks: 6
open_issues: 0
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 14
size_kb: 991
archived: false
flags: ["unverified"]
risk_notes: "APIでライセンスがunknown。VRMBG-3.0はゲート付きで、モデル取得にHF_TOKENが必要。Docker実行にはNVIDIA GPU（最低4GB VRAM）が必要とREADMEに記載されている。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/dextune/status/2119044699583635664"]
fetched_at: "2026-11-16T09:22:34.973247+00:00"
---

# Tost AI - Sprite Sheet Studio

## 出来ること

- 動画から背景を除去してスプライトシートを生成し、サイドカーJSON、プレビュー、GIFを作成する。既存のシートではピボット調整、マット修正、色抜き、再グリッド化、タイミング調整、再出力ができる。背景除去にはVRMBG-3.0、任意のマスク動画、または元動画のアルファを使う選択肢がある。出典: README（https://github.com/camenduru/TostAI-Sprite-Sheet-Studio）。

## 目的・背景

- ジェネレーターとエディターを1つのサーバーで提供する。生成時には結果を検査するinvariant gateがあるとREADMEに記載されている。出典: README（https://github.com/camenduru/TostAI-Sprite-Sheet-Studio）。

## 依存関係

- README記載のPython依存はtorch、cv2、transformers、PIL、numpy、fastapi、uvicorn。ffmpegは補助スクリプトでのみ使う任意依存。Dockerイメージはモデルと3つのpixel opsを含むと記載されている。

## 実行条件

- Python実行には上記MLスタックを含むPython環境が必要。Docker実行にはNVIDIA GPU（最低4GB VRAM）が必要とREADMEに記載。VRMBG-3.0はゲート付きで、モデル取得にはHF_TOKENが必要。Dockerのビルド手順ではHF_TOKENをsecret mountで渡し、build-argにしないよう説明されている。

## 最短手順

- README記載のPython手順: リポジトリの作業ディレクトリへ移動し、MLスタックを含むPythonでapp.pyを起動する。Docker手順: イメージを取得し、NVIDIA GPUを有効にして8765番ポートを公開してコンテナを起動する。コマンドと条件の出典: README（https://github.com/camenduru/TostAI-Sprite-Sheet-Studio）。

## 変更履歴

- 2026-11-16: 初回登録
