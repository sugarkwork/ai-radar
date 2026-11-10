---
repo: veda-sparse/Veda-on-ComfyUI
name: Veda Sparse Attention for ComfyUI (MiniMax-H3)
genre: video-gen
url: https://github.com/veda-sparse/Veda-on-ComfyUI
license: MIT
stars: 224
language: Python
created: 2026-10-02
updated: "2026-10-11"
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/KOF97AI/status/2118214947494646170
sources:
  - https://arxiv.org/abs/2605.30325
  - https://veda-sparse.github.io/
  - https://registry.comfy.org/publishers/veda-sparse/nodes/veda-sparse-attention
flags: []
risk_notes: ""
forks: 20
open_issues: 13
commits_30d: 4
commits_90d: 100
commit_cadence: "weekly"
size_kb: 2476
archived: false
fetched_at: "2026-11-09T21:46:52Z"
last_release: ""
last_release_at: ""
---

# Veda Sparse Attention for ComfyUI (MiniMax-H3)

## 出来ること

- ComfyUI の MiniMax-H3（**T2VA / FL2VA / R2VA**）に差し込む学習型スパースアテンションのノード。MODEL を受けて MODEL を返す1ノードで、モデルとLoRAの後、guider/sampler の直前に置く。
- 蒸留された小さな predictor が、アテンションマップのタイルのうち結果に効く上位**約10%**を事前に選び、残りをスキップする。
- README の計測（RTX 5070）: エンドツーエンド **2.9倍**、アテンション単体 **7.1倍**。クリップが長いほど差が広がる。
- 重みのパッチではなくアテンションの差し替えなので、Turbo・スタイルLoRA、量子化済みH3、先頭/末尾フレームや参照条件付けと併用できる。
- 起動時にカーネルのセルフテストを行い、使えないときは理由を出して停止する（黙って加速なしで描画しない）。実行後はノード上に「計算したアテンションの割合（例: 10.9%）」、解像度、尺が出る。
- `Ctrl+B` でノードをバイパスし、同じシードの full attention と比較できる。

## 目的・背景

Veda は「スパース率そのものより、スパースマスクが full attention のタイル幾何にどれだけ合っているかが品質を決める」という主張の手法（arXiv 2605.30325）。タイル選択を full attention からの再構成問題として定式化し、統計を考慮したタイルスコアとヘッド認識タイル化で推定誤差を下げる。本リポジトリはそれを ComfyUI のノードとして配布するもの。

## 依存関係

- ComfyUI **0.38.0 以上**。
- Triton（NVIDIA SM80 以降、Linux / Windows）または MLX（Apple Silicon）。Comfy Registry から入れると依存として自動で入る。
- predictor（**275MB**）を `ComfyUI/models/veda/` に置く。T2VA/FL2VA 用と R2VA 用でファイルが別。テンプレートから開くと missing-models ダイアログで取得できる。

## 実行条件

- 対応タスクは **T2VA / FL2VA / R2VA**。マスクを指定する「局部インペイント」専用ノードは README に記載がない。投稿の「局部換人・重绘が3倍」は、参照条件付け（R2VA）によるキャラクター置換と、生成全体の高速化を指すと読むのが正確。
- 速度の数値は RTX 5070 での計測。SM80 以降が必須で、世代によって差が出る。
- ComfyUI 標準の「Model Sparse Attention」とは**併用不可**（H3 のアテンションを丸ごと置き換えるため Veda が呼ばれない）。KJNodes の「MiniMax H3 Low VRAM Attention」とは併用可。
- リポジトリは 2026-10-02 作成・最終push 2026-10-11。配布の主軸は Comfy Registry の **v0.3.1**（2026-10-09 公開、8,327 DL、2026-11 時点）。
- ★218 と GitHub 上では小さいが、Registry 経由の導入が前提の構成。

## 最短手順

```bash
# ComfyUI Manager で "Veda" を検索、または
comfy node install veda-sparse-attention

# テンプレート: Workflow -> Browse Templates -> Veda-on-ComfyUI
#   「Veda MiniMax H3 T2VA」または「Veda MiniMax H3 R2VA」

# 既存ワークフローへ追加する場合:
#   MODEL 線上の LoRA の後・guider/sampler の直前に
#   「Veda Sparse Attention (MiniMax H3)」を挿入 → predictor を選択
```

## 変更履歴

- 2026-11-05: 初回登録（★218 / pushed 2026-10-11 / MIT / Registry v0.3.1）
