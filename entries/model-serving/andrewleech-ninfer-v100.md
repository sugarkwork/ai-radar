---
name: "NInfer"
genre: "model-serving"
url: "https://github.com/andrewleech/ninfer-v100"
repo: "andrewleech/ninfer-v100"
license: "Apache-2.0"
stars: 1
language: "C++"
created: "2026-09-02"
updated: "2026-11-08"
forks: 0
open_issues: 0
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 100
size_kb: 19500
archived: false
flags: ["unverified"]
risk_notes: "READMEの実測・性能値は配布者の報告であり、独立に検証していない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119384955608351017"]
fetched_at: "2026-11-19T23:10:36.282712+00:00"
---

# NInfer

## 出来ること

- 単一のNVIDIA GeForce RTX 5090またはTesla V100上で、明示的に登録されたQwenチェックポイントを推論するC++/CUDAエンジン。テキスト・画像・動画を含むプロンプトに対応し、ローカルCLIまたはOpenAI/Anthropic互換HTTP APIから利用できる。ランタイムは単一GPU・常駐モデル1つで、起動時に1～8件の同時リクエスト容量を設定する。

## 目的・背景

- 選定されたQwenチェックポイント向けに推論性能を狙った、独自実装のエンジン。READMEでは、RTX 5090とTesla V100を対象とし、V100ではNVFP4をソフトウェアカーネルで実行すると説明している。README記載の性能値は配布者による測定報告で、他の構成との比較にはモデル量子化や設定の違いがある場合がある。

## 依存関係

- Linux 64-bit、対象GPUに応じたCUDA Toolkit（RTX 5090は13.1、Tesla V100は12.8）、CMake 3.28以上、C++20対応ホストコンパイラ、Ninja、pkg-config、FFmpeg開発ライブラリ（libavformat >= 60、libavcodec >= 60、libavutil >= 58、libswscale >= 7）、libcurl >= 7.85が必要。

## 実行条件

- ビルドはsm_120a（RTX 5090）またはsm_70（V100）のいずれか一方を対象にする。モデルは対応する`.ninfer`アーティファクトを別途取得し、ソースビルドしたツリーから実行する。READMEにはインストールターゲットおよびパッケージ済みバイナリ配布はないとある。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README例では、`git clone https://github.com/Neroued/ninfer.git`で取得し、`cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release`および`cmake --build build -j`でビルドする。V100ではCUDA 12.8のnvccと`-DCMAKE_CUDA_ARCHITECTURES=70`を指定する。次にHugging Face CLIで例示されたQwen3.8-27B NVFP4アーティファクトを取得し、`./build/apps/ninfer`または`./build/apps/ninfer-serve`から実行する。

## 変更履歴

- 2026-11-23: 初回登録
