---
name: "Hermes Gadget"
genre: "agent-framework"
url: "https://github.com/Adolanium/hermes-gadget-sdk"
repo: "Adolanium/hermes-gadget-sdk"
license: "MIT"
stars: 548
language: "C++"
created: "2026-10-03"
updated: "2026-11-16"
forks: 97
open_issues: 6
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 8091
archived: false
flags: ["unverified"]
risk_notes: "実機ポートは、対象リビジョンの完全な物理検証レポートが記録されるまで実験的とREADMEに記載。ボード選定時は検証表の確認が必要。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/dextune/status/2119052257438179494"]
fetched_at: "2026-11-16T21:35:49Z"
last_release: "v0.5.0"
last_release_at: "2026-11-05"
---

# Hermes Gadget

## 出来ること

- Hermes Agentとの音声対話、返信や確認質問の画面表示、エージェントからのカード受信ができる。LED、センサー、その他の操作部品をエージェント用ツールとして公開できる。対応先はESP32-S3ボード、Raspberry Pi 4/5、デスクトップシミュレーター。音声利用には音声認識と音声合成の設定が必要。出典: https://github.com/Adolanium/hermes-gadget-sdk

## 目的・背景

- READMEでは、利用者自身のHermes Agentとそのツール、メモリー、スキルを使う小型デバイス向けプロジェクトと説明している。Hermes GadgetはNous Researchとは無関係のコミュニティプロジェクト。出典: https://github.com/Adolanium/hermes-gadget-sdk

## 依存関係

- README記載のデスクトップシミュレーターの開始要件はPython 3.10以上、CMake 3.16以上、C++17コンパイラー。Hermesとの実会話にはHermes AgentとGadgetプラグインが必要。音声には音声認識と音声合成の設定が必要。出典: https://github.com/Adolanium/hermes-gadget-sdk

## 実行条件

- ボードを使うセットアップにはChromeまたはEdge、USBデータケーブル、2.4 GHz Wi-Fi、Hermesが必要。デスクトップシミュレーターはハードウェアなしで試せる。READMEにはPython環境でのインストール、シミュレーターのビルドと起動、ペアリング付きデモサーバーの手順が記載されている。出典: https://github.com/Adolanium/hermes-gadget-sdk

## 最短手順

- READMEの手順は、Python環境でリポジトリルートから `python -m pip install -e ".[dev]"`、`hermes-gadget build-sim --test`、`hermes-gadget devserver --pairing` を実行し、別ターミナルで `hermes-gadget sim --url ws://127.0.0.1:8765/gadget --board sim-466x466-round` を実行する。最初のターミナルでシミュレーターに表示されたコードを使って `approve <CODE>` を入力する。これはREADME記載手順の要約であり、ここで実行確認はしていない。出典: https://github.com/Adolanium/hermes-gadget-sdk

## 変更履歴

- 2026-11-16: 初回登録
