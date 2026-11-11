---
name: "LivePortrait"
genre: "video-gen"
url: "https://github.com/KlingAIResearch/LivePortrait"
flags: ["unverified"]
risk_notes: "ライセンスは提示された測定値でunknown。READMEの記載に基づく機能・手順であり、未記載の実行環境や効果は確認できていない。 GitHub APIでライセンスを確認できていません。"
repo: "KlingAIResearch/LivePortrait"
stars: 19446
forks: 2026
open_issues: 292
size_kb: 39665
language: "Python"
created: "2024-07-03"
updated: "2026-06-01"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Y0urDumble/status/2118038616257515823"]
fetched_at: "2026-11-10T16:16:53.557781+00:00"
---

# LivePortrait

## 出来ること

- 公式PyTorch実装として、ポートレートアニメーションを提供する。READMEには人・猫・犬の対応、画像駆動モード、領域制御、ポートレート動画編集、Gradioインターフェースでのポーズ編集が記載されている。

## 目的・背景

- READMEによると、Stitching and Retargeting Controlを用いた効率的なポートレートアニメーションの論文に対応する公式実装。

## 依存関係

- READMEはgit、conda、FFmpegの事前導入を案内している。LinuxまたはWindowsでAnimals modeを使う場合はX-Poseが必要。

## 実行条件

- READMEの環境例はPython 3.10。LinuxまたはWindowsでCUDAのバージョンに応じてPyTorchを導入する手順が示されている。CUDA確認手順はHumans modeのみを使う場合は任意とされている。

## 最短手順

- README記載の手順は、リポジトリをcloneし、作業ディレクトリへ移動、conda環境をPython 3.10で作成・有効化すること。その後、利用するOS・モードに応じて依存関係を導入する。

## 変更履歴

- 2026-11-11: 初回登録
