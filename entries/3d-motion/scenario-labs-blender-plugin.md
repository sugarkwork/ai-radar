---
repo: "scenario-labs/blender-plugin"
name: "Scenario for Blender"
genre: "3d-motion"
url: "https://github.com/scenario-labs/blender-plugin"
stars: 968
forks: 97
open_issues: 55
size_kb: 96720
language: "Python"
created: "2026-08-30"
updated: "2026-11-10"
archived: false
license: "GPL-3.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "blender-plugin-v0.13.0"
last_release_at: "2026-11-04"
flags: ["unverified"]
risk_notes: "インストール、MCP接続、生成品質、処理時間、実消費CUは未実測。発見投稿の羊牧場デモにおける本拡張の寄与と所要時間、生成物の利用条件は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2115534594854551771"]
fetched_at: "2026-11-10T12:24:30+00:00"
---

# Scenario for Blender — PBR素材の生成・適用とローカルMCP連携

## 出来ること

- 公式READMEによると、MaterialsでPBRテクスチャセットを生成・保存し、選んだメッシュのマテリアルスロットに適用できる。画像、動画、3Dメッシュ、音声の生成機能もある。

## 目的・背景

- BlenderのビューポートからScenarioの生成モデルを使い、結果を編集中のシーンに取り込むための実験的なPython拡張。ローカルMCPを通じてエージェントから開いているシーンを参照できる。

## 依存関係

- Blender 5.0以降、APIアクセス可能なScenarioアカウント、インターネット接続、BlenderのAllow Online Accessが必要。READMEでは拡張コードをGPL-3.0-or-laterと説明している。

## 実行条件

- 生成やプロンプト補助はCreative Units（CU）を消費する。生成前に見積もりを確認でき、モデルや設定、参照素材によって費用が変わる。見積もり時にもプロンプトとパラメータがScenarioへ送信される。
- ローカルMCPは既定で同一マシンのループバックに待ち受け、接続時の認証を要求しない。接続したクライアントはシーンを読み取り、有料処理を要求できる。任意のPython実行は既定で無効。

## 最短手順

- BlenderでAllow Online Accessを有効にし、Get Extensionsに公式リポジトリ https://blender.scenario.com/repo/index.json を追加してScenarioをインストールする。拡張の設定でScenarioの接続を設定する。
- ビューポートのScenarioパネルでMaterialsとモデルを選び、プロンプトと必要な参照素材を指定する。見積もりを確認して生成し、保存されたテクスチャセットを対象スロットに適用する。
- AIから使う場合は、同じマシンでScenarioのAgents (MCP)を開き、ConnectでCodexまたはClaude Codeにscenario-blenderを登録してクライアントを再読み込みする。既定URLは http://127.0.0.1:9876/mcp 。エージェントにscene_summaryを呼ばせると、開いているシーンの概要を確認できる。

## 変更履歴

- 2026-11-10: 初回登録
