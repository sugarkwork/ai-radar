---
repo: "Tencent/WeVisOne-VL"
name: "WeVisOne-VL"
genre: other
url: "https://github.com/Tencent/WeVisOne-VL"
license: "Apache-2.0（Tencent 著作部分）"
stars: 1111
language: "Jupyter Notebook"
created: "2026-10-22"
updated: "2026-10-25"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 95
open_issues: 7
commits_30d: 3
commit_cadence: "monthly"
size_kb: 31126
archived: false
commits_90d: 3
fetched_at: "2026-11-09T21:41:29Z"
last_release: ""
last_release_at: ""
---

# WeVisOne-VL

## 出来ること

- 物体レベルの知覚（物体検出、指示対象の位置特定、カウント、ポイント指示、OCR）と、画素レベルの知覚（指示セグメンテーション、プロンプタブルなアルファマット）を1つの視覚言語モデルで扱う。
- マスクとアルファマットを出すピクセルデコーダは 9.6M パラメータで、SAM を別途走らせずに済む構成。
- 対象が存在しない場合は `None` を返す（存在しないものを幻覚的に出力しない）設計を明示。
- 重みは Hugging Face で 2B / 4B の2サイズ、Gradio デモも公開。推論パッケージ・Cookbook・評価パイプラインを同梱。
- マット作成用のアノテータ `Mask2Alpha` を別ブランチで公開。

## 目的・背景

微信（WeChat）Vision チームによる研究リリース。物体検出系の出力（点・ボックス）とセグメンテーション／マット系の出力（マスク・アルファ）を別モデルで繋ぐのではなく、構造化された次トークン予測で統一することを狙う。arXiv に技術報告（2610.31329）。

## 依存関係

- Python 3.10、`requirements.txt`、`pip install -e .`。
- 推論バックエンドは `transformers` または `vllm` を選択。
- モデル重みは Hugging Face から取得（`tencent/WeVisOne-VL-2B` / `-4B`）。

## 実行条件

- ファインチューニング用コードは未公開（README の TODO に残っている）。現状は推論と評価が中心。
- ライセンスは Tencent 著作のコードが Apache-2.0、第三者コンポーネントは元のライセンスのまま。混在しているため、商用利用時は各ファイルの表示を確認する。
- 学習データの詳細や再現手順は技術報告側にあり、このリポジトリだけでは学習を再現できない。

## 最短手順

```bash
git clone https://github.com/Tencent/WeVisOne-VL.git && cd WeVisOne-VL
conda create -n wevisone-vl python=3.10 -y && conda activate wevisone-vl
pip install -r requirements.txt && pip install -v -e .
```

```python
from PIL import Image
from wevisone_vl import WeVisOneVL
model = WeVisOneVL("tencent/WeVisOne-VL-4B", backend="transformers")
```

## 変更履歴

- 2026-11-03: 初回登録（★676 / created 2026-10-22 / pushed 2026-10-25）
