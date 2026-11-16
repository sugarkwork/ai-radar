---
name: "vLLM"
genre: "model-serving"
url: "https://github.com/vllm-project/vllm"
flags: ["unverified"]
risk_notes: "READMEには、必要なGPU・CPUの最低要件や対応するソフトウェアのバージョン条件が記載されていません。"
repo: "vllm-project/vllm"
stars: 96992
forks: 24870
open_issues: 10430
size_kb: 365543
language: "Python"
created: "2023-02-09"
updated: "2026-11-16"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/naka_1717/status/2119034856676159987"]
fetched_at: "2026-11-16T05:29:33.518506+00:00"
---

# vLLM

## 出来ること

- LLMの推論・サービング用ライブラリ。READMEはPagedAttentionによるKVメモリ管理、連続バッチ処理、量子化、分散推論、ストリーミング出力、構造化出力、ツール呼び出し、OpenAI互換APIサーバーなどを機能として挙げています。また、Hugging Face上の200超のモデルアーキテクチャをサポートすると説明しています。出典: https://github.com/vllm-project/vllm

## 目的・背景

- READMEはvLLMを「fast and easy-to-use library for LLM inference and serving」と説明し、元はUC BerkeleyのSky Computing Labで開発されたとしています。スループットやメモリ効率に関する記述はREADMEに記載された機能・効果の説明であり、独立した実測結果ではありません。出典: https://github.com/vllm-project/vllm

## 依存関係

- READMEは導入方法としてuvまたはpipを案内し、Hugging Faceモデルとの統合を説明しています。個別のパッケージ依存関係やバージョン制約はREADMEに記載されていません。出典: https://github.com/vllm-project/vllm

## 実行条件

- READMEはNVIDIA、AMD、IntelのGPUとx86、ARM、PowerPCのCPUに加え、複数のハードウェアプラグインをサポートすると記載しています。必要な最低ハードウェア要件やソフトウェアバージョンはREADMEに記載されていません。出典: https://github.com/vllm-project/vllm

## 最短手順

- README記載の導入例は `uv pip install vllm`、続けて起動高速化用のプリコンパイル済みカーネルを取得する場合は `vllm download-kernels` です。これはREADME掲載の手順であり、この環境での実行確認ではありません。詳細は https://docs.vllm.ai/en/latest/getting_started/quickstart.html を参照してください。

## 変更履歴

- 2026-11-16: 初回登録
