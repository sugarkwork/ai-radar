---
name: "P-H3-Image ComfyUI sample workflows"
genre: "image-gen"
url: "https://github.com/tori29umai0123/P-H3-Image_Workflows"
repo: "tori29umai0123/P-H3-Image_Workflows"
flags: ["unverified"]
risk_notes: "ライセンスは確認できていないため、利用・再配布条件は不明。 GitHub APIでライセンスを確認できていません。"
stars: 2
forks: 1
open_issues: 0
size_kb: 57691
language: "unknown"
created: "2026-11-06"
updated: "2026-11-06"
archived: false
license: "unknown"
commits_30d: 4
commits_90d: 4
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/SlipperyGem/status/2120080547779350641"]
fetched_at: "2026-11-10T23:10:18.321747+00:00"
---

# P-H3-Image ComfyUI sample workflows

## 出来ること

- キャラクター画像とポーズ参照画像を使い、参照画像2のポーズ・表情・構図をキャラクター画像1に適用するワークフローを提供する。手持ちオブジェクトの配置や手との接触を移す版、キャラクターのポーズと構図を保って衣装を適用する版もある。README記載の説明であり、出力はseed・モデル・参照画像によって変わる。

## 目的・背景

- P-H3-Image向けの編集可能なComfyUIサンプルワークフロー。v2のポーズ版は、先に参照画像の可視・切り抜き・隠れた領域を分析し、関連するキャラクターデザインだけを記述する2段階処理を行う。READMEは記述精度の改善可能性を説明しているが、推論時間は従来版より長く、隠れた詳細が生成結果に影響しない保証はない。

## 依存関係

- READMEによると、必要なのは`PH3ImageConditioning`と`MiniMaxH3SigmaShift`を含む最近のComfyUI、ワークフローが選択するP-H3-Imageモデル重み、ComfyUI-VLAnalyst、ComfyUI_text_Edit、ComfyUI-KJNodes。各拡張を`ComfyUI/custom_nodes/`に配置し、それぞれの説明に従って依存関係を導入してComfyUIを再起動する。リポジトリにはモデル重みとカスタムノードのソースコードは含まれない。出典: https://github.com/tori29umai0123/P-H3-Image_Workflows

## 実行条件

- ポーズ版は`Qwen/Qwen3.5-9B`、衣装版は`Qwen/Qwen3.5-4B`を選択し、対応するビジョン言語モデルを用意する。README記載のモデルファイルは`p-h3-image_w4a8.safetensors`、`p-h3-image_text_encoder_w4a8.safetensors`、`p-h3-image_vae_int8_convrot.safetensors`。参照画像を差し替える際は、ポーズ転送では画像2、衣装変更では画像1のアスペクト比が使われるため、生成前にキャンバスを確認する。出典: https://github.com/tori29umai0123/P-H3-Image_Workflows

## 最短手順

- 1. README記載の6枚の入力画像を`ComfyUI/input/`直下にコピーする。2. ワークフローJSONをComfyUIで開く。3. 2つの`LoadImage`ノードの画像を確認し、必要なら自分の参照画像に差し替える。4. P-H3モデルとVL Analystモデルの選択を確認してキューに追加する。生成画像は`SaveImage`で保存される。出典: https://github.com/tori29umai0123/P-H3-Image_Workflows

## 変更履歴

- 2026-11-11: 初回登録
