---
name: "FlashProve"
genre: "other"
url: "https://github.com/anthropics/FlashProve"
repo: "anthropics/FlashProve"
stars: 1017
forks: 109
open_issues: 4
size_kb: 174468
language: "Lean"
created: "2026-10-30"
updated: "2026-10-30"
archived: false
license: "Apache-2.0"
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Ryrenz/status/2118253498458317171"]
fetched_at: "2026-11-11T08:23:25.156827+00:00"
---

# FlashProve

## 出来ること

- モデルの重みを公開せず、応答が特定の重みに対応するモデルの出力であることを証明する。READMEによると、プロバイダーが重みに結び付いた commitment ID を公開し、GPUで応答ごとの証明を生成する。第三者は重みなしで、通常のCPUから `cp_verify` で検証できる。READMEにある保存済み例は合成重みの小型モデルであり、実際に提供されたモデルについての証明ではない。出典: https://github.com/anthropics/FlashProve

## 目的・背景

- READMEは、モデルの重みを明かさずに、応答したモデルを証明する仕組みと説明している。また、プロトコルの健全性をLean 4で証明したとしている。これはREADMEの記述であり、独立した実測結果としては扱っていない。出典: https://github.com/anthropics/FlashProve

## 依存関係

- 保存済み証明の検証にはLinux、bash、g++ 13以降、2 GB未満のRAMが必要。CPU上のtoy proofには加えてmakeとPython 3が必要。証明生成を行うGPU経路は、x86-64 Linux 4.14以降、SHA拡張対応CPU、他用途で使用していないNVIDIA H100 80 GB、CUDA 13.2 Update 2（nvcc 13.2.86）、gcc/g++ 13、binutils、flock、Python 3が必要。README記載の要件。出典: https://github.com/anthropics/FlashProve

## 実行条件

- 検証器のビルドと保存済み証明の確認はREADME記載で1〜2分、確認は2秒未満、RAMは2 GB未満。GPUの小型モデル経路は10 GB RAM、ビルド約29分、実行23〜30秒。全サイズの合成モデル経路は280 GB RAM、ビルド約42分。実際のLlama 4 Maverickを使う経路は、公開4-bit変換のダウンロード（232 GB）、330 GB RAM、245 GBのディスク容量、事前に用意するキャリブレーションセットが必要で、所要時間は数時間とされる。これらはREADME記載の条件・時間。出典: https://github.com/anthropics/FlashProve

## 最短手順

- リポジトリのルートから `verifier/build.sh` を実行して検証器をビルドし、README記載の `bin/cp_verify` コマンドで保存済み証明を検証する。成功時は終了コード0、最終行 `YES` が期待値。保存済み例は合成重みの小型モデルを使う。READMEは通常ユーザーで作業し、rootやsudoで実行しないよう指定している。出典: https://github.com/anthropics/FlashProve

## 変更履歴

- 2026-11-11: 初回登録
