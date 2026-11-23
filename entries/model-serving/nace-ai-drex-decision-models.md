---
name: "Drex decision models"
genre: "model-serving"
url: "https://github.com/nace-ai/drex-decision-models"
repo: "nace-ai/drex-decision-models"
license: "Apache-2.0"
stars: 153
language: "Python"
created: "2026-10-09"
updated: "2026-11-16"
forks: 22
open_issues: 4
commits_30d: 33
commit_cadence: "daily"
commits_90d: 61
size_kb: 2871
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/ai_hakase_/status/2119327568226636054"]
fetched_at: "2026-11-19T07:14:17.165120+00:00"
---

# Drex decision models

## 出来ること

- 状態と名前付きの型付き質問（はい／いいえ、複数選択、評価尺度）を渡すと、各選択肢の確率を返す意思決定モデル。READMEによると、Drex v2.0、v1.5、DLMはPythonで実行でき、Drex Maxは `python -m drex_max` で実行できる。llama.cppとOllamaにも対応し、モデルによりKapitsaやMLXも利用できる。

## 目的・背景

- 生成文ではなく、入力した状態と質問に対する選択肢ごとの確率を返すオープンな意思決定モデル群。READMEにはモデルとランナーの対応表、重みの配布先、実行手順が掲載されている。

## 依存関係

- READMEのPython手順では、仮想環境を作成し `pip install -r requirements.txt` を実行して、Hugging Faceからモデル重みを取得する。モデル別の重みとランナーの条件はREADMEの表を参照。

## 実行条件

- Pythonの標準例はDrex v1.5を使用し、NVIDIA GPUが対象。READMEではDrex DLMのApple silicon対応も記載されている。KapitsaはApple silicon向けで、Drex MaxのQ8_0には48 GB、affine Q4には24 GB以上のメモリが必要とされる。各モデルページに詳細な手順とハードウェア条件がある。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載のPython例：`git clone https://github.com/nace-ai/drex-decision-models.git`、`cd drex-decision-models`、仮想環境を作成・有効化し、`pip install -r requirements.txt`。続けて `hf download nace-ai/drex-v1.5 --local-dir weights/drex-v1.5` を実行し、`python inference.py --model weights/drex-v1.5 --request examples/request.json` で推論する。

## 変更履歴

- 2026-11-23: 初回登録
