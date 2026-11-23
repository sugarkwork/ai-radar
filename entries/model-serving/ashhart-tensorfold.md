---
name: "TensorFold"
genre: "model-serving"
url: "https://github.com/ashhart/TensorFold"
repo: "ashhart/TensorFold"
stars: 2317
forks: 542
open_issues: 723
size_kb: 79982
language: "Zig"
created: "2026-06-19"
updated: "2026-11-18"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119259662357033209"]
fetched_at: "2026-11-18T07:15:45.071184+00:00"
---

# TensorFold

## 出来ること

- READMEによると、Zigバイナリで言語モデルを配信し、MetalまたはCUDAカーネルを実行する。Completions、Responses、Anthropic Messages APIを提供し、`/v1/models`で配信中のモデル名を確認できる。

## 目的・背景

- Apple SiliconまたはNVIDIA GPU上で言語モデルを動かすサーバーとして紹介されている。READMEはPythonやMLXのインストールなしで配信できると説明している。

## 依存関係

- READMEはPythonとMLXのインストールは不要と説明している。モデル重みには個別のライセンスがあるため、利用するチェックポイントの条件を確認する必要がある。

## 実行条件

- READMEの例はApple Silicon搭載Mac、またはLinux上のNVIDIA GPU向け。Linuxの例ではglibc 2.28以上、NVIDIAドライバーR580以上（CUDA 13.0）が必要とされている。Windows向けには別ガイドが案内されている。

## 最短手順

- Apple SiliconではHomebrewでTensorFoldを導入し、README記載の固定リビジョンを`tensorfold pull`で取得してから、`tensorfold serve`で起動する。Linux NVIDIA向けにはリリースアーカイブとSHA-256確認の手順が記載されている。起動後、別の端末からAPIへリクエストを送る。

## 変更履歴

- 2026-11-23: 初回登録
