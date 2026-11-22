---
name: "exo"
genre: "model-serving"
url: "https://github.com/exo-explore/exo"
repo: "exo-explore/exo"
license: "Apache-2.0"
stars: 48467
language: "Python"
created: "2024-06-24"
updated: "2026-11-06"
forks: 3625
open_issues: 472
commits_30d: 81
commit_cadence: "daily"
commits_90d: 100
size_kb: 43669
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/naka_1717/status/2119034856676159987"]
fetched_at: "2026-11-16T21:56:07Z"
last_release: "v1.0.71"
last_release_at: "2026-04-23"
---

# exo

## 出来ること

- exoはデバイスをAIクラスターとして接続し、単一デバイスには収まらない大きさのモデルを実行できるとREADMEで説明されています。デバイスの自動検出、デバイス構成やネットワークを考慮したモデル分割、Tensor Parallelism、MLXを使った推論、OpenAI Chat Completions・Claude Messages・OpenAI Responses・Ollama各APIとの互換性、Hugging Face Hubからのカスタムモデル読み込みに対応するとしています。出典: https://github.com/exo-explore/exo

## 目的・背景

- 複数デバイスの計算資源をまとめて、単一デバイスより大きなモデルを実行することを目的としています。READMEはThunderbolt 5上のRDMAによる低遅延化や、複数デバイスでの速度向上を説明しています。数値はREADME記載の作者側の説明であり、独立した実測としては扱っていません。出典: https://github.com/exo-explore/exo

## 依存関係

- READMEでは推論バックエンドとしてMLX、分散通信にMLX distributedを使用すると記載されています。出典: https://github.com/exo-explore/exo

## 実行条件

- macOSアプリはApple silicon搭載MacとmacOS Sequoia 15.1以降が必要です。Thunderbolt上のRDMAにはmacOS Tahoe 26.2以降が必要です。ソースからはmacOSまたはLinuxで実行可能とREADMEに記載されています。複数デバイスを自動検出させるには、同じネットワーク上で同じexoバージョンを実行します。出典: https://github.com/exo-explore/exo

## 最短手順

- macOSアプリを使う場合は、README記載の配布物を開いてEXOをApplicationsフォルダへ移し、起動します。Homebrewでは `brew install --cask exo` を実行します。別のMacを加える場合は、両方にEXOをインストールして起動し、同じローカルネットワークに接続するかThunderboltケーブルでつなぎ、同じバージョンを使います。出典: https://github.com/exo-explore/exo

## 変更履歴

- 2026-11-16: 初回登録
