---
repo: "carson-katri/geometry-script"
name: "Geometry Script"
genre: "3d-motion"
url: "https://github.com/carson-katri/geometry-script"
license: "GPL-3.0"
language: "Python"
flags: ["unverified"]
stars: 379
forks: 33
open_issues: 33
size_kb: 22244
created: "2022-11-13"
updated: "2026-11-09"
archived: false
commits_30d: 6
commits_90d: 6
commit_cadence: "weekly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
risk_notes: ""
sources: ["https://x.com/Y0urDumble/status/2115534594854551771"]
fetched_at: "2026-11-10T12:23:04+00:00"
---

# Geometry Script — BlenderのノードツリーをPythonで組む

## 出来ること

- Geometry Nodes、シェーダー、コンポジターのノード構成をPythonで記述する。公式のRepeat Grid例では、格子の点に入力ジオメトリをインスタンス配置する。

## 目的・背景

- 複雑なノードツリーの編集や再構成をコードで行い、生成したツリーはBlenderのノードエディターで調整できる。リポジトリのライセンスはGPL-3.0。

## 依存関係

- 公式インストール文書ではBlender 5.2以降が必要。ノード関数はBlenderのバージョンに合わせて生成されるため、使用するバージョンに対応した拡張ビルドを選ぶ。

## 実行条件

- Claude Codeスキルは、BlenderのMCPサーバーに接続済みならMCP経由で実行し、それ以外ではバックグラウンドのBlenderで実行する仕様。

## 最短手順

- 公式インストールページから使用中のBlenderに対応する拡張を導入する。
- Claude Codeで `/plugin install geometry-script --marketplace carson-katri/geometry-script` を使ってスキルを追加し、入力ジオメトリを格子状に並べるGeometry Nodesグループの作成を依頼する。Claude Code 2.1.275より前のバージョンはREADMEのマーケットプレイス追加手順に従う。
- Blenderで生成されたノードグループを開き、格子の幅と高さを変えて配置を確認する。

## 変更履歴

- 2026-11-10: 初回登録
