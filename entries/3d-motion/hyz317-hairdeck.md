---
type: "repo"
name: "HairDeck（1枚の画像からアニメ調ヘアカードと揺れボーンを作る）"
genre: "3d-motion"
url: "https://github.com/hyz317/HairDeck"
repo: "hyz317/HairDeck"
license: "Apache-2.0"
stars: 1034
language: "Python"
created: "2026-10-29"
updated: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-10-31"
sources: ["https://x.com/Machinedelusion/status/2116624498933833758", "https://hyzcluster.github.io/HairDeck", "https://huggingface.co/hyz317/HairDeck"]
flags: []
risk_notes: "入力エンコーダにゲート付きモデルを使う：facebook/sam3 と facebook/dinov3-vitl16-pretrain-lvd1689m は HF 上で規約同意が必要で、`hf auth login` していないと停止する。Blender 4.2 LTS と VRM Add-on をダウンロードスクリプトが自動取得し、PATH の `ffmpeg` も必要。生成されるメッシュ・テクスチャの権利や、入力画像（既存キャラクター）の扱いはツール側では担保されないので利用者の責任。品質評価は論文側のテストセット評価で、手持ちの絵柄での再現は別途確認が要る。"
forks: 77
open_issues: 2
commits_30d: 7
commit_cadence: "weekly"
size_kb: 749
archived: false
fetched_at: "2026-11-09T21:31:01Z"
last_release: ""
last_release_at: ""
commits_90d: 7
---

# HairDeck — キャラクター画像1枚から、ゲームでそのまま使えるヘアカードと揺れボーンを生成する

## 出来ること

- 1枚の画像から**スタイライズドなヘアカード**を生成する。各カードを1トークンとして扱い、**セット拡散Transformer**で髪型全体をまとめて生成する（カードを1枚ずつ継ぎ足す方式ではないので、束の重なりや流れが破綻しにくい）
- **UV付きのジオメトリ**：個々のカードを保ったまま、カード単位のUV座標を出力する
- **色も画像から予測する**：カードに沿って色を推定するので、ツートーンカラーやアクセサリーも反映され、GLB/VRM の書き出しに色が乗る
- **スプリングボーンの生成**：カードを動かすボーン鎖を拡散モデルで生成し、スキニングまで行う。だから揺れものを手で仕込まなくても髪が動く
- 出力形式は **GLB メッシュ**、またはアバターに付けて **VRM** として書き出し（Blender 経由）
- 1枚から最大4バリエーションまで生成できる（`--n 1..4`、`--seed` で先頭シード指定）
- カードだけ／単色だけに絞るオプション（`--no-chains` / `--no-colors`）があり、自前のチェックポイントも指定できる（`--ckpt` と対応する `--chain_ckpt`）
- ローカルGradioデモ、HF Spaces のオンラインデモ、head-turn の確認動画書き出しも同梱

## 目的・背景

- アニメ調キャラクターの髪は、カード（板ポリ）を並べて束感を出す手法がゲーム現場の定番だが、カードの配置・UV・色・揺れボーンを手作業で作るのは重い。HairDeck はそこを画像1枚から一括生成する
- 研究色が強く、論文（arXiv 2610.40599）とプロジェクトページ、HF の重み・デモが同時に公開されている。著者は Tsinghua University / CMU / CUHK
- 2026-11-02 に Windows 対応、11-03 に Apple Silicon（MPS、CUDA/Triton 不要）、11-05 にカラー対応と、リリース後1週間で対応環境を広げている

## 依存関係

- Linux または Windows（ネイティブ）＋ NVIDIA CUDA GPU。Python 3.12、PyTorch 2.8、CUDA 12.8。Apple Silicon Mac は MPS で動作
- `requirements.txt` に加えて `pip install --no-deps pyrender==0.1.45`（古い PyOpenGL ピンを持ち込まないため）
- **Blender 4.2 LTS ＋ VRM Add-on**：`scripts/setup/download_weights.py` が OS に合う Blender を取得する。既存の Blender を使う場合は `HAIRDECK_BLENDER` で指定
- PATH に `ffmpeg`
- 重みは HF の `hyz317/HairDeck`。加えて **SAM 3**（`facebook/sam3`）、**DINOv3**（`facebook/dinov3-vitl16-pretrain-lvd1689m`）、**BiRefNet-matting** を取得する。前2つは**ゲート付き**なので、HF 上で規約に同意してから `hf auth login` が必要
- 作業領域は `HAIRDECK_ROOT` で指定（`ckpt/`、`data/`、`third_party/`、出力先）

## 実行条件

- CUDA GPU が実質必須（Apple Silicon は MPS 経路）。CPU 実行は案内されていない
- 初回セットアップで Blender と複数のモデル重みをダウンロードするため、相応のディスクと時間が要る
- Windows は自動モデルオフロード付きのローカルGradio手順（`docs/windows.md`）、macOS は `docs/macos.md` の手順に従う
- `--n` は 1〜4。それ以上のバリエーションはシードを変えて複数回実行する
- 生成結果は `OUT/<画像名>/` 配下に出る。VRM 書き出しは `python -m hairdeck.vrm.export <結果ディレクトリ> <バリエーション番号>`

## 最短手順

```bash
git clone https://github.com/hyz317/HairDeck.git
cd HairDeck

python -m pip install -r requirements.txt
python -m pip install --no-deps pyrender==0.1.45   # 古い PyOpenGL ピンを避ける

# ゲート付きモデルの規約に HF 上で同意してからログイン
hf auth login
export HAIRDECK_ROOT=/path/to/workspace
python scripts/setup/download_weights.py           # 重み + Blender 4.2 LTS + VRM Add-on

# 画像1枚から4バリエーション生成
python scripts/image_to_hair.py character.png --out results/my_character --n 4

# バリエーション0を VRM アバターとして書き出す
python -m hairdeck.vrm.export results/my_character/character 0
```

```bash
# カードだけ欲しい / 単色でよい場合
python scripts/image_to_hair.py character.png --out results/x --no-chains --no-colors
```

## 変更履歴

- 2026-11-06: 初回登録
