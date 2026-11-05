---
repo: VAST-AI-Research/SkinTokens
name: SkinTokens（TokenRig）
genre: 3d-motion
url: https://github.com/VAST-AI-Research/SkinTokens
author: VAST-AI-Research（清華大学 + Tripo）
license: MIT
stars: 597
language: Python
created: 2026-02-08
updated: 2026-05-12
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/dextune/status/2117854353126236641
sources:
  - https://zjp-shadow.github.io/works/SkinTokens/
  - https://arxiv.org/abs/2602.04805
  - https://huggingface.co/spaces/VAST-AI/SkinTokens
forks: 82
open_issues: 11
commits_30d: 0
commits_90d: 0
commit_cadence: stale
size_kb: 13374
archived: false
fetched_at: "2026-11-05T01:23:27Z"
---

# SkinTokens（TokenRig）

## 出来ること

- **1つのメッシュから、スケルトン階層とスキニングウェイトを一度に生成する自動リギング**。出力は標準的な3Dパイプラインにそのまま取り込める（キャラクターアニメーション・シミュレーション用）。
- **SkinTokens** はスキニングウェイトの学習済み・離散・コンパクト表現。FSQ-CVAE が疎なウェイトを小さな語彙に圧縮する。
- **TokenRig** は、骨格と SkinTokens を**1本のインターリーブされたトークン列**として自己回帰生成する枠組み。バックボーンは Qwen3-0.6B ベースの Transformer。
- 仕上げに **GRPO による強化学習**（関節の体積被覆、ボーンとメッシュの包含、スキニングの疎性、変形の滑らかさを報酬化）で調整する。
- 既存スケルトンがあるモデルは `--use_skeleton` で**スキニングだけ**を生成できる。テクスチャとスケールを保ったまま出力する `--use_transfer`、ボクセルベースの後処理 `--use_postprocess`、ディレクトリ一括処理にも対応。
- HF Space のブラウザデモ、ローカル Gradio デモ（`python demo.py`）、CLI の3通りで試せる。

## 目的・背景

UniRig（SIGGRAPH'25）の後継。UniRig が「骨格予測」と「スキニング」を別ステージに分けていたのに対し、SkinTokens は両方を1つの自己回帰系列に統合した。作者の報告では、スキニング精度が既存手法比 **98〜133% 改善**、ボーン予測が **17〜22% 改善**。清華大学と Tripo の研究（arXiv:2602.04805）。2026-02-08 作成、05-12 時点で 597 star。

## 依存関係

- **NVIDIA GPU（推論に14GB以上のVRAM）**
- Python 3.11 以上、CUDA Toolkit 12.1 以上、`uv` 推奨
- PyTorch 2.7.0 / torchvision 0.22.0 / torchaudio 2.7.0（CUDA 12.8 ビルドの例）、`flash-attn`
- 学習済みモデルは Hugging Face（`VAST-AI/SkinTokens`）から取得

## 実行条件

- 入力は単一の3Dメッシュ（GLB など。例は `examples/giraffe.glb`）。出力も GLB。
- Blender に取り込む際、`glTF_not_exported` ノードが残っていると書き出しに失敗する（README に対処あり）。
- 生成パラメータ: `--top_k 5`、`--top_p 0.95`、`--temperature 1.0`、`--repetition_penalty 2.0`、`--num_beams 10` が既定。
- 精度改善の数値は論文側の報告で、独立再現は未確認。
- 軽量な派生実装もある: `localai-org/skin-tokens.cpp`（C++/GGML 移植、234★・Apache-2.0）、`Aero-Ex/ComfyUI-SkinTokens`（ComfyUI ノード、84★・MIT）。どちらも本家とは別管理。

## 最短手順

```bash
git clone https://github.com/VAST-AI-Research/SkinTokens.git
cd SkinTokens
uv venv --python 3.11 && source .venv/bin/activate
uv pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu128
uv pip install -r requirements.txt
# flash-attn は別途（README 参照）

python demo.py --input examples/giraffe.glb --output results/giraffe.glb --use_transfer
```

## 変更履歴

- 2026-11-04: 初回登録（UniRig の後継として）
