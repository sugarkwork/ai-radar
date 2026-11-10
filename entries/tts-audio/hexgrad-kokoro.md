---
type: "repo"
name: "Kokoro"
genre: "tts-audio"
url: "https://github.com/hexgrad/kokoro"
repo: "hexgrad/kokoro"
license: "Apache-2.0"
stars: 10016
language: "JavaScript"
created: "2025-01-10"
updated: "2025-08-06"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① このリポジトリは推論コードのみ。重みは HF の hexgrad/Kokoro-82M 側にあり、JS 実装は同リポジトリの kokoro.js/ サブディレクトリ（npm kokoro-js）。② 実質的にメンテ停止: 最終 push 2025-08-06、HF モデルカードの最終更新 2025-04-10、PyPI 0.9.4 は 2025-04-05、npm 1.2.1 は 2025-05-03、直近30日 commit 0、open issues 222。★9.9k は開発の活発さではなく配布実績（HF 月間約1,200万DL、npm 週約23万DL）の指標。③ kokoro-js の G2P は英語固定（phonemize.js が \"a\"→en-us、それ以外→en に落とす）。日本語・中国語などは Python + misaki が必須で、ブラウザ完結の多言語は不可。④ espeak-ng が OS 依存（Linux は apt、Windows は公式 msi）。無いと英語の辞書外フォールバックと一部言語が落ちる。⑤ Python 3.13 非対応（PyPI は >=3.10,<3.13、pyproject は <3.14 と表記が食い違う）。⑥ 声質のばらつきが大きい: VOICES.md が声ごとの学習時間を格付けしており、MM 分級（数十分）の声や F+ 評価の声もある。日本語は 5 声のみ。⑦ 重みは Apache-2.0 だが学習データに CC BY 3.0（Koniwa、1時間未満）と CC BY 4.0（SIWIS、11時間未満）が混在し、再配布時は帰属表示が必要。voices/*.pt 個別のライセンス条項は明示なし。⑧ 100〜500 トークンが最適で、10〜20 未満の短文と 400 超の長文で品質が落ちる。⑨ モデルカードが「kokoro を冠する類似ドメインは無関係の詐称サイト」と警告している。"
forks: 1121
open_issues: 223
commits_30d: 0
size_kb: 29122
archived: false
commits_90d: 0
commit_cadence: "stale"
fetched_at: "2026-11-09T21:43:06Z"
last_release: ""
last_release_at: ""
---

# Kokoro — 82M パラメータで 9 言語 54 ボイスを出すオープンウェイト TTS の推論ライブラリ

## 出来ること

- テキストから 24kHz モノラルの音声を生成する。`KPipeline(lang_code=...)` は (書記素, 音素, 音声) のタプルを順に返すジェネレータなので、長文は `split_pattern` で分割しながら逐次書き出せる
- 9 言語 54 ボイス: en-US 20 / en-GB 8 / zh 8 / ja 5 / hi 4 / es 3 / pt-BR 3 / it 2 / fr 1。声は `af_heart` のような「言語+性別+名前」で指定する
- `speed` で話速を変更でき、`voice=` に `.pt` のテンソルを直接渡せば自前の声も使える。HF 上には 71 のファインチューンと 119 の量子化版が登録されている
- CLI を同梱: `python3 -m kokoro -t "text" -l j --voice jf_alpha -o out.wav`。ファイル入力は `-i`、出力先を省けば標準出力に流れる
- `kokoro-js`（同リポジトリの `kokoro.js/`）は ONNX 版を Transformers.js 経由で動かす。ブラウザは wasm / WebGPU、Node は cpu を選ぶ。`TextSplitterStream` で LLM の出力を流し込みながら逐次音声化できる
- 音素化は別パッケージ `misaki` が担う。日本語は `misaki[ja]`（pyopenjtalk + unidic でアクセント記号と文節結合に対応）、中国語は `misaki[zh]`

## 目的・背景

- StyleTTS 2 + ISTFTNet のデコーダのみ（拡散なし、エンコーダ非公開）を 82M パラメータまで縮めたモデル。学習は A100 80GB で計 1,000 時間・約 1,000 ドル、音声はパブリックドメイン・許諾済みライセンス・合成音声だけを使ったと明記されている
- 狙いは「小型でも上位モデルに近い品質を、CPU でも動く速度で」。API 提供時の相場は 100 万文字あたり 1 ドル未満という試算がモデルカードに載っている
- ただしこのリポジトリは推論コードのみで、重みは HF 側。2025-08-06 の最終 push 以降 commit はなく、HF モデルカードも 2025-04-10 で止まっている。活発に開発中というより「完成したものが配布され続けている」状態と見るのが正確

## 依存関係

- Python 3.10 以上 3.13 未満（PyPI のメタデータ。pyproject は 3.14 未満と書いており食い違う）
- `torch` / `transformers` / `huggingface_hub` / `numpy` / `loguru` / `misaki[en]>=0.9.4`（pip が自動で導入）
- espeak-ng（OS パッケージ）: 英語の辞書外フォールバックと一部の非英語で使う。Linux は `apt-get install espeak-ng`、Windows は公式 msi
- 日本語は `misaki[ja]` を追加（fugashi / unidic / pyopenjtalk。pyopenjtalk は環境によってビルドツールが要る）。中国語は `misaki[zh]`
- JS は Node またはブラウザ + `kokoro-js`（依存は `@huggingface/transformers` と `phonemizer`）。重みは `onnx-community/Kokoro-82M-v1.0-ONNX`

## 実行条件

- 出力は 24kHz モノラル WAV。GPU は必須ではなく、`device` 引数で明示もできる
- 品質の当たり外れが大きい。100〜500 トークンが最適で、10〜20 未満の短文と 400 超の長文で崩れる。声ごとの学習量は VOICES.md に格付け付きで公開されており、数十分しか学習していない声や F+ 評価の声も混ざる
- 日本語の声は女性 4・男性 1 の 5 つだけ。モデルカード自身が「非英語は G2P が弱い、声が 1 つしかない言語（フランス語）もある」と断っている
- ライセンス: 重みは Apache-2.0。ただし学習データに CC BY 3.0（Koniwa、1 時間未満）と CC BY 4.0（SIWIS、11 時間未満）が含まれ、再配布時は帰属表示が要る。`voices/*.pt` 個別の条項は明示されていない
- JS 側の G2P は英語固定（`"a"`→en-us、それ以外→en）。日本語などをブラウザ内だけで完結させる口は用意されていない

## 最短手順

Python:

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -U "kokoro>=0.9.4" soundfile
sudo apt-get install -y espeak-ng        # Windows は公式 msi を導入
pip install "misaki[ja]"                 # 日本語を使う場合のみ
```

```python
from kokoro import KPipeline
import soundfile as sf

pipe = KPipeline(lang_code="j")          # a/b/e/f/h/i/j/p/z
for i, (gs, ps, audio) in enumerate(pipe("こんにちは。今日はいい天気ですね。", voice="jf_alpha", speed=1)):
    sf.write(f"{i}.wav", audio, 24000)
```

CLI だけなら: `python3 -m kokoro -t "こんにちは。" -l j --voice jf_alpha -o out.wav`

JS（英語のみ）:

```bash
npm i kokoro-js
```

```js
import { KokoroTTS } from "kokoro-js";

const tts = await KokoroTTS.from_pretrained("onnx-community/Kokoro-82M-v1.0-ONNX", {
  dtype: "q8",        // fp32 / fp16 / q8 / q4 / q4f16
  device: "cpu",      // web は wasm / webgpu
});
const audio = await tts.generate("Hello from Kokoro.", { voice: "af_heart" });
audio.save("out.wav");
```

## 変更履歴

- 2026-11-07: 初回登録
