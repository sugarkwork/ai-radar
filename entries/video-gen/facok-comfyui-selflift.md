---
name: "comfyui-SelfLift"
genre: "video-gen"
url: "https://github.com/facok/comfyui-SelfLift"
repo: "facok/comfyui-SelfLift"
license: "unknown"
stars: 418
language: "Python"
created: "2026-09-07"
updated: "2026-09-18"
forks: 26
open_issues: 12
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 44
size_kb: 170
archived: false
flags: ["unverified"]
risk_notes: "H3の画質に関する記述はREADME記載の単一シードでの結果で、独立した検証ではありません。H3向け機能は実験的とされています。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/superfang119/status/2118543853506769052"]
fetched_at: "2026-11-12T14:23:26.083605+00:00"
---

# comfyui-SelfLift

## 出来ること

- ComfyUI用のSelfLift Progressive Samplerは、画像モデルの初期デノイジングを低解像度で行い、その後にフル解像度へ移行する構成です。READMEは遷移でデノイザー評価回数を増やさず、rhoが0でなければVAEのデコード・拡大・再エンコードが1回加わると説明しています。またMiniMax H3向けの実験的な音声・動画対応と、動画の時間的一貫性を補正するH3 Temporal State Transport (TST) ノードを含みます。出典: https://github.com/facok/comfyui-SelfLift

## 目的・背景

- SelfLift画像機能はSelfLift-zero論文に基づくとREADMEに記載されています。H3向け適応は論文で検証されていない実験的機能です。TSTもH3向けの実験的ポートとして説明されています。出典: https://github.com/facok/comfyui-SelfLift

## 依存関係

- ComfyUIで利用します。画像サンプラは対象モデルに属するVAEを使うようREADMEが指定しています。H3外部アップスケーラは任意で、導入する場合はHugging FaceのチェックポイントをComfyUI/models/latent_upscale_models/に置いて再起動します。出典: https://github.com/facok/comfyui-SelfLift

## 実行条件

- サンプラは標準Eulerとs_churn=0のみ対応し、samplerとsigmasにはKSamplerSelectの標準eulerとモデル標準のスケジューラを接続します。TSTはMiniMax H3のみを対象とし、highres_tilingとは互換性がありません。READMEはH3をlowres_scale=0.5で使うと768ピクセルの短辺が384ピクセルになり、モデルの学習分布外となる可能性があるためモデルごとの確認を求めています。出典: https://github.com/facok/comfyui-SelfLift

## 最短手順

- ComfyUIでプラグインのノードを使い、画像サンプラには4次元画像latentとモデルのVAEを接続します。標準eulerとモデル標準スケジューラを指定してください。基本設定はtransition_step=6、lowres_scale=0.5、rho=0.3です。H3で外部アップスケーラを使う場合は任意のチェックポイントを所定のモデルディレクトリに置き、ComfyUIを再起動します。設定値はREADME記載の例であり、モデルにより確認が必要です。出典: https://github.com/facok/comfyui-SelfLift

## 変更履歴

- 2026-11-12: 初回登録
