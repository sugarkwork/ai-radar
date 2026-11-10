---
repo: camenduru/VRMExMR
name: VRMExMR
genre: 3d-motion
url: https://github.com/camenduru/VRMExMR
license: 未確認（API は NOASSERTION。ExMR 側の条件を確認）
stars: 15
language: Python
created: 2026-11-04
updated: "2026-11-05"
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/camenduru/status/2118211316384976963
sources:
  - https://github.com/twehrbein/ExMR
  - https://arxiv.org/abs/2610.26213
flags: [unverified]
risk_notes: "ライセンス表記がなく、ExMR 側の利用条件（研究用か商用可か）を一次情報で確認できていない。商用利用の前に必ず確認する。"
forks: 0
open_issues: 0
commits_30d: 39
commits_90d: 39
commit_cadence: "daily"
size_kb: 28180
archived: false
fetched_at: "2026-11-09T21:30:32Z"
last_release: ""
last_release_at: ""
---

# VRMExMR

## 出来ること

- **単眼動画から SMPL-X の身体・手・足のモーションを復元**し、VRM / Blender / Unity / Unreal / ヒューマノイドロボット向けに書き出す Docker イメージ。
- 中身は ExMR（Extremity Motion Refinement for Monocular Human Motion Capture、arXiv 2610.26213）のデモコード。足元の接地（foot contact）と手足の細部を補正するのが特徴で、**world-grounded**（世界座標で接地した）モーションを出力する。
- 出力形式: 3D/2D ジョイント、BVH、Blender 経由の FBX（Unity / Unreal 向け）、GMR を使ったヒューマノイドロボットへのリターゲット。
- VRM への書き出しを想定した構成（リポジトリ名の由来）。camenduru による Docker 化で、環境構築なしで起動できる。

## 目的・背景

動画1本から3Dキャラクターのモーションを作る際、足の滑り・接地のズレ・手の細部が崩れるのが実用上の障害になる。ExMR はそこを補正する手法で、FootMR（3DV 2026）のジャーナル拡張。VRMExMR はそれを Docker で扱えるようにした配布形態。

## 依存関係

- Docker（GPU パススルー: `--gpus all`）と NVIDIA ドライバ。
- イメージ: `camenduru/vrmexmr`。`--shm-size=8g`、出力はボリューム `vrmexmr-data`。
- ポート 8010 で UI/API を公開。

## 実行条件

- **ライセンス未確認**。ExMR 側のリポジトリに明示的なライセンス表記が見当たらず、商用利用の可否が判断できない。業務利用は保留。
- ExMR は**デモコードのみ**（評価・学習コードは今後公開）。研究用途の再現が前提。
- 入力は単眼動画。人物が画面内に収まり、全身（足元まで）が写っている必要がある。縦向きスマホ動画の修正は ExMR v0.1.5 で入っている。
- ★13・2026-11-04 公開。Docker イメージのタグ・GPU 要件は README を確認する。

## 最短手順

```bash
docker run -d --name vrmexmr --restart unless-stopped \
  --gpus all --shm-size=8g -p 8010:8010 \
  -v vrmexmr-data:/app/outputs \
  camenduru/vrmexmr

# ブラウザで http://localhost:8010 を開き、動画をアップロード
```

## 変更履歴

- 2026-11-05: 初回登録（★13 / pushed 2026-11-05 / ライセンス未確認 / ExMR デモ）
