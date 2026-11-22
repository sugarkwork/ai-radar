---
name: "gputaskman"
genre: "other"
url: "https://github.com/shanselman/gputaskman"
repo: "shanselman/gputaskman"
license: "MIT"
stars: 3436
language: "Python"
created: "2026-11-03"
updated: "2026-11-16"
forks: 170
open_issues: 13
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 2266
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/toyxyz3/status/2119155644427300969"]
fetched_at: "2026-11-17T05:29:44.473151+00:00"
---

# gputaskman

## 出来ること

- GPUのデバイス・プロセス別メモリとエンジン活動を表示し、読み込まれたランタイム、モデルファイル、LLMバッファ内訳を関連付けて確認できる。READMEは、プロセスのメモリとエンジン活動は計測値、モデルの識別やGGUF由来の内訳は推定を含むと説明している。出典: https://github.com/shanselman/gputaskman#readme

## 目的・背景

- GPUメモリ使用量について、モデル重み・KV cache・ブラウザー・デスクトップ合成など、何が使用しているかを調べるためのローカルGPU監視ツール。クラウド、CPUのみ、NPUのみのワークロードは対象外。出典: https://github.com/shanselman/gputaskman#readme

## 依存関係

- ソースから実行する場合、README記載のWindows手順ではGit for Windowsとuv、またはPython 3.11以降とpipを使う。uv手順はロック済み依存関係を使用する。監視にCUDA Toolkit、モデルのダウンロード、APIキーは不要と記載されている。出典: https://github.com/shanselman/gputaskman#clone-and-run

## 実行条件

- 対応環境はWindows、Linux/WSL、Apple Silicon搭載macOS。READMEはPython 3.11以降と対応GPU・ドライバー構成を条件としている。Windowsでは現行のWDDMドライバーが必要。ポータブル配布物はREADMEによるとWindowsではPython不要だが、対応GPUと現行WDDMドライバーが必要。出典: https://github.com/shanselman/gputaskman#install-from-pypi / https://github.com/shanselman/gputaskman#portable-windows-download

## 最短手順

- README記載のWindowsソース実行手順: Git for Windowsとuvを用意し、PowerShellで `git clone https://github.com/shanselman/gputaskman.git`、`cd gputaskman`、`uv run --locked gputaskman` を実行する。初回実行にはインターネット接続が必要と記載されている。出典: https://github.com/shanselman/gputaskman#clone-and-run

## 変更履歴

- 2026-11-22: 初回登録
