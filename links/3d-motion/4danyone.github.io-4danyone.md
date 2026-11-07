---
type: "link"
name: "4DAnyone"
genre: "3d-motion"
url: "https://4danyone.github.io/"
author: "4DAnyone authors（Zhejiang University / Ant Group、コードは ant-research 名義）"
pricing: "free"
pricing_detail: "料金ページは存在しない（/pricing は HTTP 404 を実測）。推論コードと公開重みは無料で取得できる。third_party サブモジュールのライセンスは別建てのため、商用利用時は個別確認が必要。"
signup_required: false
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/tokufxug/status/2118171681437175920"]
flags: ["unverified"]
risk_notes: "投稿は Faltwerk という4DGS圧縮・配信ツール（1.4GB→5〜7MB、Quest 3 で25〜40Mbps配信、AIアバターへの影付け）を名乗るが、対象ページに Faltwerk の記載は一切なく、実体は別プロジェクト 4DAnyone（SIGGRAPH Asia 2026）。投稿の圧縮率・配信帯域・実演は一次情報で確認できず本項目には採用していない。James C. Kane はページ内で 4DGS プレイヤー作者として謝辞に出るのみ。リポジトリは Apache-2.0 だが third_party（GVHMR 等）は別ライセンスで、パイプライン全体の商用利用は要確認。推論には 22GB 級 VRAM の GPU が必要。"
fetched_at: "2026-11-07T12:38:04Z"
---

# 4DAnyone — 単眼の手持ち動画から4Dヒトを再構成するモデルとCLI

## 目的

- スマートフォンなどで撮った1本の手持ち動画から、カメラ内部・外部パラメータや撮影リグなしで多視点動画を生成し、そのまま 4D Gaussian Splatting (4DGS) の再構成に渡せるようにする研究プロジェクト（SIGGRAPH Asia 2026、Zhejiang University / Ant Group）。

## 何ができるか

- CLI 推論: python inference.py --video_path <mp4> --output_dir <dir> --views_per_layer 6。視点数・ピッチ層・ヨー範囲を変えられ、--views_per_layer 24 --layer_pitches '[-10,15,35]' で3層48視点のような配置も指定できる（Python / Apache-2.0）。
- 生成した多視点動画を FreeTimeGS で 4DGS 化するパイプラインを同梱。入力は人物が写る単眼動画、出力は目標視点の動画群と 4DGS 再構成用データで、単体の圧縮・配信ツールではない。
- 4DAnyone-Base と蒸留版 4DAnyone-Turbo（4ステップ、既定で有効）の2モデル。README によれば RTX 4090 で121フレーム約27秒、ピーク 22GB VRAM。
- Gradio GUI（対話推論・可視化、Rerun ベース）と公開重み（Hugging Face、gated ではない）を提供。
- API サーバや MCP サーバは提供なし。エージェントから使う場合はシェル経由で CLI を叩く形になる（ブラウザ操作だけでは推論できない）。

## 料金

- 無料。料金ページ・有料プランは存在しない（https://4danyone.github.io/pricing は HTTP 404 を実測）。
- コードと公開重みは無料で取得可能（リポジトリのライセンスは Apache-2.0）。
- third_party/GVHMR などの同梱サブモジュールは別ライセンスのため、商用利用時は個別に確認が必要。
- 実コストは GPU（ピーク 22GB VRAM 級）の計算資源。

## 登録の要否

- 不要。アカウントなしで git clone、重みの自動／手動ダウンロード（scripts/download_model.py 等）、推論が可能（Hugging Face リポジトリは gated=false を API で確認）。
- 必要なのは conda/pip による環境構築（Python 3.11、git submodule update --init third_party/GVHMR、任意で FlashAttention-3 / SageAttention）と GPU。

## 変更履歴

- 2026-11-07: 初回登録
