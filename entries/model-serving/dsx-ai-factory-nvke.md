---
name: "NVIDIA Kubernetes Engine (NVKE)"
genre: "model-serving"
url: "https://github.com/dsx-ai-factory/nvke"
repo: "dsx-ai-factory/nvke"
flags: ["unverified"]
risk_notes: "Preview版で、本番ワークロードには推奨されていません。PreviewではAPI認証が初期状態で無効、インストール後のAPIは平文HTTPです。利用前に認証と保護されたアクセスを設定してください。管理クラスターのアップグレード・スケール・置換、および管理プレーンのアップグレード・バックアップ／復元手順はありません。"
stars: 1113
forks: 136
open_issues: 202
size_kb: 137628
language: "Go"
created: "2026-08-04"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Ryrenz/status/2120065434103812405"]
fetched_at: "2026-11-10T23:23:55.270745+00:00"
---

# NVIDIA Kubernetes Engine (NVKE)

## 出来ること

- NVKE管理プレーンを自前のNVIDIA GPU基盤に導入し、NICo経由で顧客向けの独立したKubernetesワークロードクラスターを作成・運用できます。ノードプールの作成・スケール・削除、Kubernetesのアップグレード、ノードの置換を扱います。ノードはTPMを使ってSPIFFE/SPIREでアテステーションし、etcdデータ暗号化はクラスターごとに利用できます。

## 目的・背景

- プラットフォームチームが管理プレーンを運用し、顧客がKubernetes APIやkubectlを通じて利用するクラスターを提供するための仕組みです。NVKEはKubernetesディストリビューションではなく、使い捨てのseedクラスターから管理クラスターを立ち上げ、その管理プレーンでワークロードクラスターを作成・管理する構成です。

## 依存関係

- 実インフラでのPreview時点の互換インフラプロバイダーはNVIDIA Infra Controller（NICo）のみです。実インストールではマシン、ネットワーク、ノードイメージ、レジストリを用意し、NICoへのアクセスを設定します。ローカルquickstartはLinuxホストまたはVM（amd64またはarm64）、Docker、仮想TPM対応を必要とします。

## 実行条件

- ローカルquickstartの最低要件は6 CPU、空きメモリ12 GiB、空きディスク100 GiBです。GPUハードウェアなしでシミュレーションマシン上の開発用管理プレーンとワークロードクラスターを評価できます。macOSではColima VM内で評価する手順があります。実インストールの対応バージョンと固定依存関係は公式のplatform and version referenceを確認してください。

## 最短手順

- 評価する場合はREADMEのLocal quickstartに従い、LinuxホストまたはVMで要件と必要ツールを用意してセットアップを進め、ワークロードクラスターを作成します。完了確認としてクラスターのノードがReadyと報告することを確認します。実インフラへの導入はPlan your installationの前提条件と手順に従います。

## 変更履歴

- 2026-11-11: 初回登録
