---
name: "whisper.cpp"
genre: "other"
url: "https://github.com/ggml-org/whisper.cpp"
repo: "ggml-org/whisper.cpp"
stars: 55259
forks: 6315
open_issues: 371
size_kb: 48721
language: "C++"
created: "2022-09-25"
updated: "2026-11-16"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/DivyanshT91162/status/2119134534134600107"]
fetched_at: "2026-11-17T07:12:12.164333+00:00"
---

# whisper.cpp

## 出来ること

- Whisper音声認識モデルの推論をC/C++で実行する実装です。READMEはCPUのみでの推論、NVIDIA・AMDなどのGPU対応、Apple Silicon向け最適化、量子化、VAD、C-style APIを挙げています。出典: https://github.com/ggml-org/whisper.cpp

## 目的・背景

- READMEは軽量な実装により、さまざまなプラットフォームやアプリケーションへ統合しやすいと説明しています。iPhone上でのオフライン実行例も紹介されていますが、これはREADMEに記載された作者側の例で、独立した実測ではありません。出典: https://github.com/ggml-org/whisper.cpp

## 依存関係

- READMEは「Plain C/C++ implementation without dependencies」と説明しています。Core MLモデルの生成を使う場合は、ane_transformers、openai-whisper、coremltoolsが必要と記載されています。出典: https://github.com/ggml-org/whisper.cpp

## 実行条件

- READMEのQuick startでは、CMakeでビルドし、変換済みのggml形式モデルと音声ファイルを使います。whisper-cliの例は16-bit WAVのみ対応と記載され、他形式は事前変換が必要です。対応環境としてmacOS、iOS、Android、Linux、FreeBSD、WebAssembly、Windowsなどが挙げられています。出典: https://github.com/ggml-org/whisper.cpp

## 最短手順

- README記載の手順は、リポジトリを取得し、モデルをダウンロードして、CMakeでビルド後に音声を文字起こしします。例: `cmake -B build`、`cmake --build build -j --config Release`、`./build/bin/whisper-cli -f samples/jfk.wav`。モデルの取得例は`sh ./models/download-ggml-model.sh base.en`です。出典: https://github.com/ggml-org/whisper.cpp

## 変更履歴

- 2026-11-22: 初回登録
