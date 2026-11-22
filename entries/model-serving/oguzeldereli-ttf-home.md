---
name: "ttf-home"
genre: "model-serving"
url: "https://github.com/oguzeldereli/ttf-home"
repo: "oguzeldereli/ttf-home"
license: "unknown"
stars: 18
language: "C++"
created: "2026-11-09"
updated: "2026-11-17"
forks: 4
open_issues: 2
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 4941
archived: false
flags: ["unverified"]
risk_notes: "README сообщает о скоростях, точности и качестве аудио, но это заявления автора; независимая проверка не проводилась. Лицензия репозитория не указана в измеренных данных. GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/swarogan/status/2122681494019649868"]
fetched_at: "2026-11-18T00:31:50.217277+00:00"
---

# ttf-home

## 出来ること

- ttf-home は独自の ggml ベース runtime で .ttf 形式のテキストモデルと VoxCPM2 音声モデルを実行します。テキストモデルの継続生成、チャット、OpenAI 形式の API サーバー、ベンチマークに対応すると README は説明しています。別経路として、TTF パッチ適用済み llama.cpp で Qwen3.8 GGUF と GGUF エクスポートを実行できます。CLI には学習、変換、ファインチューニング、エクスポートの機能もまとめられています。

## 目的・背景

- README は、三値重み {-1, 0, +1} を使う言語・音声モデルを家庭用コンピューターで実行することを目的として掲げています。学習は別リポジトリ ttf-ternary の方式を利用し、通常の master weights と Adam 状態の代わりに低ランク accumulator を使うと説明しています。

## 依存関係

- 独自 runtime のビルドには git、cmake、C++17 コンパイラーが必要です。NVIDIA GPU を使う場合は CUDA Toolkit と nvcc も必要です。README はモデル実行に Python や PyTorch は不要としています。Python CLI 経由の手順では pip install -e . を使います。llama.cpp 経路のビルドには Python 3.11 以降も必要と記載されています。

## 実行条件

- CUDA ビルド例は `cmake -S engine -B engine/build-cuda -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release`、続けて `cmake --build engine/build-cuda -j --target ttf-home` です。CPU のみの場合は `-DGGML_CUDA=OFF` を指定します。README は CUDA コンパイラー識別の段階で失敗し、gcc が CUDA Toolkit の対応より新しい場合、`-DCMAKE_CUDA_HOST_COMPILER=g++-13` など nvcc が受け入れる gcc を指定するか、CUDA Toolkit を更新する回避策を示しています。

## 最短手順

- `git clone https://github.com/oguzeldereli/ttf-home && cd ttf-home` の後、README 記載の CMake コマンドでビルドします。ビルドした実行ファイルは `engine/build-cuda/ttf-home model.ttf "Once upon a time" -n 128` のように呼び出せます。音声生成は `engine/build-cuda/ttf-home speech.ttf "Hello from a ternary model." -o hi.wav` の形式です。

## 変更履歴

- 2026-11-22: 初回登録
