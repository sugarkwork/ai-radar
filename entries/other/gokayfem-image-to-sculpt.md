---
name: "Image 2 Sculpt"
genre: "other"
url: "https://github.com/gokayfem/image-to-sculpt"
repo: "gokayfem/image-to-sculpt"
license: "MIT"
stars: 289
language: "Python"
created: "2026-11-08"
updated: "2026-11-08"
forks: 21
open_issues: 0
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 2
size_kb: 187
archived: false
flags: ["unverified"]
risk_notes: "README gives a typical case cost of about $2; actual cost may vary with calls and the per-case budget. A fal API key is required for masks, depth, normals, and generated views; the README also describes a front-only path using a cut-out PNG and user-provided views."
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/Vlixsi/status/2121631327036318061"]
fetched_at: "2026-11-14T16:11:56.248394+00:00"
---

# Image 2 Sculpt

## 出来ること

- Coding-agent向けのskillとPythonツールキット。入力画像のマスク・深度・法線を使い、画像のシルエットや表面に合わせて3Dスカルプトを段階的に作成する。複数視点を登録・スクリーニングし、各視点のシルエットIoU、輪郭距離、法線角度、粗さ、入力画像の深度を個別に確認する。ビルド手順を記録し、Blenderで再生して.blend、GLB、OBJ、STLを出力する。

## 目的・背景

- READMEは、通常の画像から3Dへの生成では背面や視点のずれ、形状の不整合、作成過程の不透明さが問題になると説明している。本ツールは入力画像が見ている部分を基準にし、生成視点を登録・検査し、各作業段階を記録する方法を提供する。これはREADMEに記載された設計と機能の説明であり、独立した実測結果ではない。

## 依存関係

- Python 3.10以上、numpy、scipy、scikit-image、Pillow。requirements.txtのインストールでfal-clientとmatplotlibも追加される。Blender 5.2以上。再生や動画にはffmpegが必要。マスク、深度、法線、生成視点にはFAL_KEYの設定が必要。

## 実行条件

- README記載の対象はキャラクター、クリーチャー、フィギュア、製品など。シーンや部屋、非常に細い構造、透明または鏡面の素材は対象外。複数写真のインポートや、APIキーなしで切り抜きPNGと独自視点を使う方法も記載されている。READMEによると典型的なケースは約2ドルで、API呼び出しはケースごとの予算設定に従う。

## 最短手順

- インストール後、READMEの例では `python3 skills/image-to-sculpt/scripts/i2s.py new cases/owl --input owl.jpg --subject "carved wooden owl figurine"` でケースを作り、`python3 skills/image-to-sculpt/scripts/i2s.py run cases/owl` で処理を実行する。各段階は個別にも実行でき、`doctor` で依存関係を確認できる。これらはREADME記載の手順であり、この環境では実行していない。

## 変更履歴

- 2026-11-14: 初回登録
