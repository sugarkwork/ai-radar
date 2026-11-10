---
repo: "blender/blender"
name: "Blender"
genre: "3d-motion"
url: "https://github.com/blender/blender"
license: "unknown"
stars: 21829
language: "C++"
created: "2019-10-09"
updated: "2026-11-10"
forks: 3550
open_issues: 0
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 1448787
archived: false
flags: ["unverified"]
risk_notes: "GitHubミラーの最新リリース、発見投稿のClaudeによる全工程自動化、外部MCPとの接続、総費用、制作結果は未確認。レンダリング速度や画質の独立実測は行っていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117030430507401326"]
fetched_at: "2026-11-10T08:16:10+00:00"
---

# Blender｜2.5Dアニメーションのシーン制作とレンダリング

## 出来ること

- モデリング、リギング、アニメーション、レンダリング、合成、動画編集に対応する。Eeveeはリアルタイムのラスタライズ方式を採用しており、照明やカメラを調整しながらプレビューできる。

## 目的・背景

- 2.5D制作では、背景や小物を3Dシーンに置き、カメラと照明を設定してショットを出力する工程に使える。発見投稿の自動化と費用の主張は未検証。

## 依存関係

- 対応OSとGPUを備えた環境にBlenderを導入する。公式要件ではWindowsとLinuxの最小GPU要件にVRAM 2 GBとOpenGL 4.3またはVulkan 1.3が示されている。

## 実行条件

- 保存済みの.blendファイルはCLIからGUIなしでレンダリングできる。本体は無料で、READMEはBlender全体をGNU GPL v3と明記している。個別ファイルには互換ライセンスが適用される場合がある。frontmatterのlicenseはGitHub APIの観測値を記録している。

## 最短手順

- Blenderでシーンにカメラと照明を配置し、レンダーエンジンをEeveeに設定してscene.blendを保存する。
- AIから呼ぶ場合は、ローカルのコマンド実行権限を持つエージェントから `blender -b scene.blend -o //preview_ -F PNG -f 1` を呼び、まず1フレームの構図と照明を確認する。
- フレーム範囲を設定して保存したら、`blender -b scene.blend -o //frame_ -F PNG -a` で連番画像を書き出す。

## 変更履歴

- 2026-11-10: 初回登録
