---
repo: "jdnichollsc/seam"
name: "Seam"
genre: "video-gen"
url: "https://github.com/jdnichollsc/seam"
stars: 26
forks: 3
open_issues: 1
size_kb: 30028
language: "Python"
created: "2026-10-22"
updated: "2026-11-06"
archived: false
license: "MIT"
commits_30d: 25
commits_90d: 25
commit_cadence: "daily"
last_release: "v0.0.1"
flags: ["unverified"]
risk_notes: "GitHubの最新リリースリンクはv0.0.1へ転送された。公開日時と、現行READMEの機能が同タグに含まれる範囲は未確認。生成品質、所要時間、GLB入力、MCP連携は独立に再現していない。READMEでは24 GB GPU、Linux、macOSでの動作は未検証。クラウド経由の実レンダーも未検証と記載されている。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/jdnichollsc/status/2118227726288953484"]
fetched_at: "2026-11-10T11:49:19+00:00"
---

# Seam — ComfyUIで画像・動画・GLBをつなぐトランジション生成ツール

## 出来ること

- 2つのショットを指定し、煙やウィップパンなどのトランジションを生成する。GLBはブラウザで視点を決めて静止画にするか、カメラの周回を短いクリップとして記録できる。
- 使用したワークフローと入力静止画を書き出し、ComfyUIで開き直せる。

## 目的・背景

- 既定のLTX-2.5が開始・終了フレームを条件に中間映像を生成する。Seamはプリセットから生成プロンプトを組み立て、Comfy SDK経由でComfyUIに処理を送る。
- READMEにはRTX 5090での作者計測があり、5秒のSmokeプリセットは10回で中央値41秒。

## 依存関係

- ComfyUI 0.41.3以上、Comfy SDK、ローカル用のcomfy-api-proxy、Python 3.12とuv、Node 20以上、ffmpeg。既定構成はLTX-2.5とGemma系の重みを使う。

## 実行条件

- READMEの推奨構成はVRAM 32 GBのNVIDIA GPUとRAM 64 GB。作者の検証環境はWindows 11とRTX 5090。
- Seam本体はMIT。既定のLTX-2.5の重みはアクセス制限付きで、Gemmaも独自の利用条件が適用される。ローカル生成はクレジット不要。Comfy Cloudの一部モデルはクレジットを消費する。

## 最短手順

- 公式READMEの導入手順に沿ってモデルを用意し、ComfyUIとcomfy-api-proxyを起動する。`uv run seam doctor`で構成を確認し、`uv run seam serve`で起動する。
- ブラウザで `http://127.0.0.1:7860` を開き、サンプルのショットペアと効果を選んで生成する。
- AIから呼ぶにはClaude Codeで `claude plugin marketplace add jdnichollsc/seam`、続けて `claude plugin install seam` を実行し、2枚の画像を指定して煙のトランジション生成とプレビュー表示を依頼する。

## 変更履歴

- 2026-11-10: 初回登録
