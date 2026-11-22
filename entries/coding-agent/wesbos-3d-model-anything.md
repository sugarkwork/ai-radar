---
name: "3D Model Anything"
genre: "coding-agent"
url: "https://github.com/wesbos/3d-model-anything"
flags: ["unverified"]
risk_notes: "GitHub APIのlicense値はunknown。READMEでは再利用可能なコードとスキルをMITライセンスとし、オフィス画像・テクスチャには別の利用条件があると説明しています。個別素材の条件はASSETS-LICENSE.mdで確認してください。 GitHub APIでライセンスを確認できていません。"
repo: "wesbos/3d-model-anything"
stars: 3035
forks: 455
open_issues: 24
size_kb: 36049
language: "Swift"
created: "2026-10-21"
updated: "2026-10-27"
archived: false
license: "unknown"
commits_30d: 5
commits_90d: 5
commit_cadence: "weekly"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/awe0_io/status/2119114909099380934"]
fetched_at: "2026-11-16T23:15:29.309826+00:00"
---

# 3D Model Anything

## 出来ること

- iPhoneで部屋を撮影し、形状と写真を使ってAIコーディングエージェントと編集可能なThree.jsシーンを作成します。リポジトリにはiPhoneアプリ、Three.jsビューアー、scan-to-threejsエージェントスキル、オフィスのデモが含まれます。READMEは、これは反復的な再構成ワークフローであり、ワンクリックで完全なモデルに変換するものではないと説明しています。現在の対象は部屋と室内です。

## 目的・背景

- 部屋の計測情報と写真をもとにモデルを作り、レンダリングと元写真を比較しながら調整する用途です。READMEには、オフィスのデモと、ドールハウス・歩行・俯瞰・ワイヤーフレーム・俯瞰配置の各ビューが記載されています。

## 依存関係

- ビューアーの実行にはNode.js 22.12以降が必要です。スキルのヘルパーにはPython 3、写真比較にはPillow、任意の深度再構成にはNumPy・Open3D・Pillowが必要です。撮影スクリプトはagent-browser CLIを使用します。

## 実行条件

- 自分の部屋をスキャンするにはLiDAR搭載のiPhoneまたはiPadが必要です。LiDAR非搭載端末ではスキャンのインポートと確認が可能です。スキャンデータは別途用意し、README記載の形式でdata/captures-in/<room>/に展開します。

## 最短手順

- ビューアーはNode.js 22.12以降でnpm ci、npm run devを実行します。スキルはローカルスキル対応エージェントでリポジトリを開き、scan-to-threejsを使って展開済みのキャプチャを処理します。READMEは最初にhouse-capture形式ガイドとプロジェクトレイアウトを参照するよう案内しています。

## 変更履歴

- 2026-11-22: 初回登録
