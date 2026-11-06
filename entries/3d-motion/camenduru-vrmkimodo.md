---
type: "repo"
name: "VRMkimodo"
genre: "3d-motion"
url: "https://github.com/camenduru/VRMkimodo"
author: "camenduru (upstream: NVIDIA / nv-tlabs)"
repo: "camenduru/VRMkimodo"
license: "Apache-2.0"
stars: 15
language: "Python"
created: "2026-11-02"
updated: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/Machinedelusion/status/2116624498933833758"]
flags: ["unverified"]
risk_notes: "上流 nv-tlabs/kimodo のフォークで、独自追加は kimodo/exports/vrma.py のみ（README/CHANGELOG は上流と同一、CLI・デモからは未接続）。.vrma 書き出しはコード読解のみで実行検証していない。コードは Apache-2.0 だがモデル重みは NVIDIA Open Model License。ローカル生成には約17GB VRAM が必要。"
forks: 1
open_issues: 0
commits_30d: 21
commit_cadence: "daily"
size_kb: 44583
archived: false
fetched_at: "2026-11-06T14:52:30Z"
last_release: ""
last_release_at: ""
---

# VRMkimodo — テキストから3Dモーションを生成し VRM アニメーションで書き出す Kimodo フォーク

## 出来ること

- テキスト1文、または「文＋秒数」を並べた複数プロンプトから3Dの人間/ヒューマノイドモーションを生成する（CLI: kimodo_gen）
- 全身キーフレーム、手先/足先の位置・回転、2D経路・waypoint の制約 JSON を併用して動きを指定できる
- Web デモ kimodo_demo（http://127.0.0.1:7860）でタイムライン上に制約を置き、複数サンプルを比較できる
- 出力は Kimodo NPZ、Unitree G1 は MuJoCo qpos CSV、SMPL-X は AMASS NPZ、--bvh で BVH（SOMA のみ）
- このフォークは save_motion_vrma で SOMA モーションを VRM Animation（.vrma、VRMC_vrm_animation 拡張の GLB）へ書き出せる（README 未記載）

## 目的・背景

- 上流 nv-tlabs/kimodo は NVIDIA の kinematic motion diffusion モデル（700時間のモーションキャプチャで学習）の公式実装
- フォークは上流コードをそのまま取り込み、.vrma 書き出しモジュールだけを足したもの（README・CHANGELOG は上流と同一）
- 発見元の投稿は別プロダクト（HairDeck）の宣伝文で、このリポジトリの説明ではない

## 依存関係

- Python 3.8+ / PyTorch / transformers==5.1.0 ほか（pyproject.toml の dependencies）
- モデル重みは初回実行時に Hugging Face から自動取得（NVIDIA Open Model License、コードの Apache-2.0 とは別ライセンス）
- デモは viser、SOMA 系は py-soma-x を extras（[demo] / [soma]）で導入する

## 実行条件

- GPU ローカル推論は約17GB VRAM。TEXT_ENCODER_DEVICE=cpu で 3GB 未満に抑えられる
- Linux 前提（Windows は Docker 推奨）。Dockerfile / docker-compose.yaml 同梱
- .vrma 書き出しは SOMA モデル限定（30 または 77 joint）。G1・SMPL-X の出力は対象外
- .vrma 用の CLI オプションやデモ UI は無く、Python から呼ぶ必要がある

## 最短手順

- git clone https://github.com/camenduru/VRMkimodo && cd VRMkimodo && pip install -e ".[soma]"（エージェントはこのシェル実行だけで生成まで到達できる）
- kimodo_gen "A person waves and walks forward." --duration 4.0 --output out（--model 省略時は Kimodo-SOMA-RP-v1.2）
- 生成された out.npz から local_rot_mats (T,J,3,3) と root_positions (T,3) を torch テンソルで用意する（読み込みは kimodo.exports.load_kimodo_npz）
- from kimodo.exports import save_motion_vrma; save_motion_vrma("out.vrma", local_rot_mats, root_positions, skeleton=None, fps=30) で VRM Animation を書き出す（30 joint のときは SOMA スケルトンを渡す）
- 制約を使う場合はデモで保存した constraints.json を kimodo_gen --constraints に渡す

## 変更履歴

- 2026-11-06: 初回登録
