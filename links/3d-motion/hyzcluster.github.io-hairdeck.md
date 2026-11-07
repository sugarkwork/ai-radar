---
type: "link"
name: "HairDeck"
genre: "3d-motion"
url: "https://hyzcluster.github.io/HairDeck/"
author: "hyz317 (Yuze He, Yixiang Wei, Wang Zhao, Chuhao Chen, Yanning Zhou, Yong-Jin Liu / Tsinghua University, CMU, CUHK)"
pricing: "free"
pricing_detail: "コードとチェックポイントは Apache-2.0 で無料公開。料金ページ (/pricing) は存在せず HTTP 404 で、有料プラン・従量課金はない。ホスト版デモ (Hugging Face Space, ZeroGPU) も無料。コストはローカル実行時の自前 GPU のみ。"
signup_required: true
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/Machinedelusion/status/2116624498933833758"]
flags: ["unverified"]
risk_notes: "ローカル実行には NVIDIA CUDA GPU (CUDA 12.8) または Apple silicon (MPS)、Python 3.12 / PyTorch 2.8 が必要。セットアップで重み・前処理モデル・Blender 4.2 LTS を取得する。SAM 3 と DINOv3 は Hugging Face 上で gated=manual のため、ライセンス同意と hf auth login が別途必要。必要 VRAM は未記載のため未確認。生成物はゲーム/アバター向けのアセットで、商用利用時はサードパーティモデルのライセンスを個別確認のこと。"
fetched_at: "2026-11-06T21:06:07Z"
---

# HairDeck — キャラ画像1枚からアニメーション可能なヘアカード (GLB/VRM) を生成

## 目的

- ゲームやアバターの髪を作る「ヘアカード」(アーティストが配置するリボン状メッシュ) を、キャラクター画像1枚から自動生成する研究プロジェクト。
- 髪を順序のないカードの集合として扱い、set diffusion transformer で全カードをまとめて denoise する。さらに揺れを駆動するスプリングボーンの鎖も生成し、そのまま動かせるアセットにする。

## 何ができるか

- CLI: python scripts/image_to_hair.py character.png --out results/my_character --n 4 で最大4バリエーションを生成し、python -m hairdeck.vrm.export results/my_character/character 0 で VRM アバターとして書き出す。エージェントはシェル実行だけでこのパイプラインを回せる。
- ローカル Web UI: python demo/app.py --port 7860 で Gradio を起動し、http://127.0.0.1:7860 に画像を投げて生成・バリエーション比較・VRM/アニメ書き出しができる (AI からはブラウザ操作またはローカル HTTP で叩ける)。
- 出力: カード単位の UV と色を持つ hair_seed0.glb / hair_seed0_nohead.glb、avatar_seed0.vrm、揺れ付きの turn_seed0.mp4、カード形状 cards_seed0.json とボーン鎖 chains_seed0.json。
- 条件付けは画像のほか点群にも対応。scripts/test.py で論文のベンチマーク (Chamfer 距離・カード向き誤差) を再現でき、scripts/train/ のランチャーで学習も回せる。
- ホスト版: Hugging Face Space (ZeroGPU, RUNNING) にアップロードするだけで試せる。コミュニティ製の ComfyUI-HairDeck ノード (GLB / rigged GLB / VRM 書き出し) も公開されている。
- MCP サーバや公開 REST API は提供されていない。AI が使う場合は CLI かローカル Gradio 経由になる。

## 料金

- 無料。コードとチェックポイントは Apache-2.0 で、有料ティアや従量課金はない。
- 料金ページは存在せず (https://hyzcluster.github.io/HairDeck/pricing は HTTP 404)。公式デモ (HF Space) も無料で、ローカル実行の実費は自前 GPU の電気代のみ。

## 登録の要否

- ページ閲覧・コード取得・ホスト版デモの試用にアカウント登録は不要。
- ただしローカル実行に必要な重みの取得で SAM 3 と DINOv3 が Hugging Face 上 gated=manual のため、各モデルのライセンス同意と hf auth login (HF アカウント) が要る。
- 同意後に python scripts/setup/download_weights.py を実行すると、チェックポイント・前処理モデル・Blender 4.2 LTS がまとめて入る。

## 変更履歴

- 2026-11-07: 初回登録
