---
repo: VAST-AI-Research/UniRig
name: UniRig
genre: 3d-motion
url: https://github.com/VAST-AI-Research/UniRig
author: VAST-AI-Research（清華大学 + Tripo）
license: MIT
stars: 2081
language: Python
created: 2025-04-08
updated: "2026-06-04"
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/dextune/status/2117854353126236641
sources:
  - https://zjp-shadow.github.io/works/UniRig/
  - https://arxiv.org/abs/2504.12451
  - https://github.com/VAST-AI-Research/SkinTokens
forks: 206
open_issues: 28
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 22338
archived: false
fetched_at: "2026-11-09T21:31:53Z"
last_release: ""
last_release_at: ""
---

# UniRig

## 出来ること

- **任意の3Dメッシュに骨格とスキニングウェイトを自動で付ける**（SIGGRAPH 2025 / TOG）。人型・動物・手足の無い奇妙な形状も、1つのモデルで扱う。
- 工程は2段階: **骨格予測**（複数シードでバリエーションを試せる）→ **スキニングウェイト予測** → 予測結果を元ファイルに**マージ**。
- CLI で単体ファイルもディレクトリ一括も処理できる。骨格だけ・スキンだけを個別に生成し、後から結合する使い方も可能。
- 任意で Blender アドオン（VRM アドオンの改変版）を入れれば `.vrm` の入出力ができる。
- RigXL データセットと可視化スクリプトを同梱。

## 目的・背景

清華大学と Tripo による自動リギングの研究実装。従来は人体向けが中心だった自動リギングを、動物や人工物まで含む多様な形状に広げた。**現在は後継の [SkinTokens（TokenRig）](https://github.com/VAST-AI-Research/SkinTokens) が公開されており、README 冒頭でも「強力な後継」として案内されている**。UniRig は骨格とスキニングを別ステージで処理するが、SkinTokens は1本の自己回帰系列に統合し、スキニング精度 98〜133%・ボーン予測 17〜22% の改善を報告している。新規に組むなら SkinTokens、既存ワークフローや再現目的なら UniRig。2025-04-08 作成、2026-06-04 が最終 push、2,028 star。

## 依存関係

- Python 3.11、PyTorch 2.3.1 以上（検証済み）
- `spconv`（CUDA バージョンに合うホイール）、`torch_scatter` / `torch_cluster`（PyG のホイール指定）、`numpy==1.26.4`
- `flash_attn`（インストールで詰まりやすい。公式リポジトリの手順に従う）
- 学習済みチェックポイントは Hugging Face から取得（スクリプトが自動ダウンロード）
- 任意: Blender アドオン（`.vrm` 入出力用）

## 実行条件

- NVIDIA GPU 前提（CUDA 対応の PyTorch / spconv / flash-attn を揃える必要がある）
- 骨格予測は乱数シードを変えると別の骨格候補が出る。正解が1つではないため、複数試して選ぶ運用
- 予測結果はそのままでは完結せず、**マージ工程**が必要（骨格とスキンを別々に生成した場合は特に）
- ライセンスは MIT。ただし学習データ・チェックポイントの利用条件は別途確認

## 最短手順

```bash
git clone https://github.com/VAST-AI-Research/UniRig
cd UniRig
conda create -n UniRig python=3.11 && conda activate UniRig
python -m pip install torch torchvision
python -m pip install -r requirements.txt
python -m pip install spconv-{cuda版}
python -m pip install torch_scatter torch_cluster -f https://data.pyg.org/whl/torch-{torch版}+{cuda版}.html --no-cache-dir
python -m pip install numpy==1.26.4

# 骨格予測（入力は .obj / .fbx / .glb / .vrm）
bash launch/inference/generate_skeleton.sh --input examples/giraffe.glb --output results/giraffe_skeleton.fbx
bash launch/inference/generate_skeleton.sh --input examples/giraffe.glb --output results/giraffe_skeleton.fbx --seed 42

# スキニング（骨格を修正したファイルを渡す。骨格が不正確だと結果が大きく劣化する）
bash launch/inference/generate_skin.sh --input examples/skeleton/giraffe.fbx --output results/giraffe_skin.fbx
```

## 変更履歴

- 2026-11-04: 初回登録（後継 SkinTokens への案内つき）
