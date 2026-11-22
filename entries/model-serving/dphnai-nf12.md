---
name: "nf12"
genre: "model-serving"
url: "https://github.com/dphnAI/nf12"
repo: "dphnAI/nf12"
license: "Apache-2.0"
stars: 32
language: "Python"
created: "2026-11-06"
updated: "2026-11-14"
forks: 3
open_issues: 3
commits_30d: 12
commit_cadence: "weekly"
commits_90d: 12
size_kb: 539
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/NFT_Chen/status/2118977906474983767"]
fetched_at: "2026-11-16T21:56:00Z"
last_release: "v1.1.0"
last_release_at: "2026-11-11"
---

# nf12

## 出来ること

- BF16重み行列を固定長12-bit形式で符号化・復号し、PyTorch APIでlinear、embedding、MoE演算を利用できる。NVIDIA CUDA、AMD RDNA4 HIP、Apple Silicon Metalに対応し、Apple SiliconではMLX APIも提供する。README記載のベンチマークでは、機種・モデル・同時実行数によりBF16比の出力トークン速度は速い場合と遅い場合があり、H200の一部結果は不安定として集計されていない。これらは作者報告であり、独立実測ではない。

## 目的・背景

- BF16重み行列をlosslessに12-bitで表現し、GPUで扱うためのライブラリ。READMEによると、ビット配置とタイル化メモリ配置は参照論文の形式と互換ではない。

## 依存関係

- ソースビルドにはC++コンパイラ、CMake 3.26以上、Ninja、uvが必要。PythonパッケージにはPython 3.10以上と、CUDA・ROCm・MPS対応のPyTorch 2.10以上が必要で、MacではMLX 0.32以上を追加利用できる。GPU別のツールチェーン要件は「実行条件」を参照。

## 実行条件

- NVIDIAはSM80以降とCUDA Toolkit 13.0以上、AMDはRDNA4（gfx1200/gfx1201）とROCmおよびamdclang++、Apple SiliconはmacOS 14以上とXcode Metal Toolchainが必要。重み形状はN（out_features）が16の倍数、K（in_features）が64の倍数。Linux x86-64/ARM64にはNVIDIA向けwheelがあり、macOS wheelはなくMetal backendをソースからビルドする。

## 最短手順

- README記載の導入例は `uv pip install nf12`。利用例はBF16重みを `nf12.encode(w)` で符号化し、`nf12.decode(nw)` で復号、または `nf12.linear(x, nw)` で線形演算する。MacのMetal利用は `uv sync --locked --extra mlx`、MLX利用例では `nf12.mlx` をインポートする。

## 変更履歴

- 2026-11-15: 初回登録
