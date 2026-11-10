---
name: "FreeMoCap"
genre: "3d-motion"
repo: "freemocap/freemocap"
url: "https://github.com/freemocap/freemocap"
stars: 10769
forks: 1026
open_issues: 193
size_kb: 299536
language: "TypeScript"
created: "2021-04-12"
updated: "2026-11-09"
archived: false
license: "AGPL-3.0"
commits_30d: 2
commits_90d: 20
commit_cadence: "monthly"
last_release: "v2.0.0-alpha.25"
flags: ["unverified"]
risk_notes: "公開資料による確認。インストール、撮影、追跡精度、処理速度、Blender出力の品質は実測していない。最新リリースのタグは公開ページの転送先で確認したが、公開日時は未確認。READMEのソースビルド手順には非公開Git依存があり、公開アクセスだけでの再現性は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117396633889427646"]
fetched_at: "2026-11-10T08:51:17Z"
---

# FreeMoCap｜Webカメラで始めるマーカーレス動作追跡

## 出来ること

- Webカメラ1台で身体の2Dキーポイントを追跡し、2Dアニメーションの動きの参照に使える。3Dモーションキャプチャは2台以上で行い、公式ガイドは3台を推奨する。
- 撮影データはファイルとして保存され、Pythonなどで分析できる。アニメーション付きの3Dシーンを作る場合はBlenderを追加する。

## 目的・背景

- 一般的なカメラで動作計測を始められるようにするオープンソースプロジェクト。SkellyTrackerが画像から2Dキーポイントを抽出し、複数台での3D再構成では各カメラの位置関係を校正する。

## 依存関係

- 追跡バックエンドはSkellyTracker。3D撮影には印刷したChArUcoボードが必要。Blenderは3Dシーン化に使うオプション。
- リポジトリのライセンスはAGPL-3.0。公式資料はソフトウェアを無償のオープンソースとして案内しており、3D撮影にはカメラと校正用の印刷物を用意する。

## 実行条件

- 公式要件はApple Silicon搭載Mac、x64のWindowsまたはLinux。CPUで追跡でき、Windows/Linuxの対応NVIDIA GPUではCUDA版を使える。
- 単眼撮影は校正不要。3D撮影ではカメラをPCに直接接続し、ChArUcoボードで校正する。

## 最短手順

- 公式のOS別デスクトップ版を導入し、FreeMoCapを開く。Connect CamerasでWebカメラ1台を接続し、短い動作を録画・処理して2D追跡を確認する。
- READMEのpip経由ではPython 3.9〜3.11の環境に `pip install 'freemocap[cpu]'` を入れる。Windows/Linuxで対応NVIDIA GPUを使う場合は `freemocap[cuda]` を選び、端末から `freemocap` でGUIを起動する。
- シェルを使えるAIエージェントからは、導入済み環境で `freemocap` を起動し、撮影はGUIで操作する。処理後は保存されたデータファイルをPythonで読み込んで分析できる。

## 変更履歴

- 2026-11-10: 初回登録
