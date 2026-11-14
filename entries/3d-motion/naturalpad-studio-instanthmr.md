---
name: "InstantHMR"
genre: "3d-motion"
url: "https://github.com/Naturalpad-studio/InstantHMR"
repo: "Naturalpad-studio/InstantHMR"
license: "Apache-2.0"
stars: 400
language: "Python"
created: "2026-04-29"
updated: "2026-11-10"
forks: 45
open_issues: 1
commits_30d: 18
commit_cadence: "weekly"
commits_90d: 61
size_kb: 102843
archived: false
flags: ["unverified"]
risk_notes: "モデルの利用条件は種類により異なります。READMEではnano/tiny/small/mediumはSAM License・非商用、medium-commercialはSAM Licenseとされていますが、ライセンスの詳細条件はREADMEに記載されていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/adjelmohamed/status/2118813115810803792"]
fetched_at: "2026-11-14T10:12:38.937726+00:00"
---

# InstantHMR

## 出来ること

- 画像内の人物ごとに、姿勢・体形・70点の2D/3Dキーポイントと、Momentum Human Rig（MHR）形式の全身メッシュを推定する。画像・動画・カメラ入力に対応するデモとPython APIがある。README記載のモデル単体レイテンシは、RTX 4070 TensorRTで0.70～0.98 ms、Galaxy S23 NPUで4.60～5.49 ms（人物1人あたり）。これらは論文で測定された値で、デモ全体の処理時間とは異なる。

## 目的・背景

- スマートフォンやデスクトップGPUで動作するリアルタイムの人体メッシュ復元を目的とする。READMEによると、モデルは公開アノテーション付きSAM 3D Bodyデータセットで学習されている。

## 依存関係

- Python 3.10～3.12。LinuxまたはWindowsではNVIDIAドライバー525以降が必要。READMEのインストール手順ではPyTorch、requirements.txt記載の依存パッケージを導入する。人物検出にはRF-DETRを使用する。TensorRT利用時はTensorRTの追加インストールが必要。

## 実行条件

- NVIDIA GPUがない場合やMacでは、READMEのCUDA用PyTorchインストール手順を省略する。デモは画像・動画・カメラ入力を受け付け、既定モデルはmedium、既定デバイスはcuda。モデルの利用条件はモデルごとに確認が必要で、READMEではnano/tiny/small/mediumは非商用と記載されている。

## 最短手順

- README記載の手順は、リポジトリをcloneしてディレクトリへ移動し、Python 3.10～3.12の仮想環境を作成、必要なPyTorchとrequirements.txtの依存関係をインストールすること。画像の実行例は `python demo.py --image photo.jpg`。初回利用時にモデル重みがHugging Faceから自動ダウンロードされる。

## 変更履歴

- 2026-11-14: 初回登録
