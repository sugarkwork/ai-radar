---
repo: islandmed/SculptForge
name: SculptForge
genre: 3d-motion
url: https://github.com/islandmed/SculptForge
license: GPL-3.0
language: C++
created: 2026-10-21
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/Ryrenz/status/2117558671286616452
flags: []
risk_notes: ""
stars: 504
forks: 61
open_issues: 18
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 136699
archived: false
fetched_at: "2026-11-04T01:11:10Z"
last_release: v0.10.10
last_release_at: 2026-11-03
---

# SculptForge

## 出来ること

- ZBrush のオープンソース代替を名乗るデジタル彫刻ツール。Linux / macOS / Windows で動作し、アカウント不要・テレメトリなし・アプリ内課金なし。
- 動的トポロジ、マスク、ボクセルリメッシュ、四角形リトポロジといった彫刻の主要機能を備える。
- 書き出しは FBX / glTF / OpenUSD。**Unreal Engine への送信**と Blender ブリッジに対応。
- ゲーム向けの LOD 生成、Gaussian Splatting、画像/テキストからの3D生成（ビルトインAI）を含む。
- MCP 対応（トピックに `mcp`）。エージェントから操作できる構成。

## 目的・背景

2026-10-21 作成、半月で ★504・30日100+コミット。彫刻ツールのライセンス費用を避けたい個人・インディー開発者向けに、モデリングからゲームエンジンへの受け渡しまでを1つにまとめる狙い。C++ と Dear ImGui で書かれたネイティブアプリ。

## 依存関係

- デスクトップアプリ（ビルド済みバイナリあり）
- GPU（彫刻・3D生成に必要。具体的なVRAM要件は未確認）
- Unreal Engine / Blender（連携を使う場合）
- MCP クライアント（エージェント連携を使う場合）

## 実行条件

- OS: Linux / macOS / Windows。
- ディスク: リポジトリは約137MB。
- GPL-3.0。改変して配布する場合は GPL の条件に従う。

## 最短手順

```text
Releases から各OSのビルドを取得（またはソースからビルド）
```

## 変更履歴

- 2026-11-04: 初回登録（★504 / v0.10.10 / GPL-3.0 / 30日100+コミット）
