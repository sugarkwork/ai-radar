---
repo: "Comfy-Org/ComfyUI"
name: "ComfyUI"
genre: "image-gen"
url: "https://github.com/Comfy-Org/ComfyUI"
last_release: "v0.44.0"
flags: ["unverified"]
risk_notes: "FP8とDynamic VRAMの速度改善幅、P-H3-Imageのモデル系譜と重みの利用条件、各機能の必要VRAMと出力品質、最新リリースの公開日時の年とタイムゾーンは未確認。導入と推論の実行検証は行っていない。"
stars: 146083
forks: 17401
open_issues: 5486
size_kb: 107607
language: "Python"
created: "2023-01-17"
updated: "2026-11-10"
archived: false
license: "GPL-3.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/sep_is_heim/status/2117816879461093847"]
fetched_at: "2026-11-10T10:41:51+00:00"
---

# ComfyUI v0.44.0で画像生成・編集ワークフローを組む

## 出来ること

- 画像生成・編集の処理をノードで接続し、ワークフローとして再利用できる。公式テンプレートにはP-H3-Imageで参照画像を編集する例がある。[公式編集テンプレート](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_p_h3_image_edit.json)
- v0.44.0では、複数の画像入力を扱うTextGenerateV2と、動画保存時のProResおよびクロマサブサンプリングの選択が追加された。[公式リリースノート](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.44.0)

## 目的・背景

- モデル、入力、処理、保存をグラフにまとめ、設定を差し替えて再実行できる。READMEによると、ComfyUIで生成したPNGをUIに読み込むと、シードを含むワークフローを復元できる。[公式README](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md)

## 依存関係

- 手動導入ではPython、ハードウェアに対応するPyTorch、requirements.txtのパッケージ、ワークフローが参照するモデルの重みを用意する。[公式README](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md)
- 本体のライセンスはGPL-3.0。モデルの重みの利用条件は配布元ごとに確認する。

## 実行条件

- 公式READMEはPython 3.13を案内している。PyTorchの導入方法はGPUとOSで異なる。導入後は `python main.py` でローカルサーバーを起動する。[公式README](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md)

## 最短手順

- 公式READMEの手動導入手順に沿ってPyTorchと依存パッケージを入れ、使用するモデルの重みを所定のディレクトリに置く。`python main.py` で起動し、ブラウザーでワークフローを読み込んでキューに送る。[公式README](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md)
- AIエージェントからは、API形式のワークフローを `prompt` に入れて自分のComfyUIサーバーの `POST /prompt` に送る。返却された `prompt_id` を使い、`GET /history/{prompt_id}` で結果を確認する。[公式サーバーAPI文書](https://docs.comfy.org/development/comfyui-server/comms_routes)

## 変更履歴

- 2026-11-10: 初回登録
