---
repo: islandmed/SculptForge
name: SculptForge
genre: 3d-motion
url: https://github.com/islandmed/SculptForge
license: GPL-3.0
language: C++
created: 2026-10-21
updated: 2026-11-04
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/Ryrenz/status/2117558671286616452
flags: []
risk_notes: ""
stars: 555
forks: 69
open_issues: 28
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 137447
archived: false
fetched_at: "2026-11-04T22:53:13Z"
last_release: v0.10.11
last_release_at: 2026-11-04
---

# SculptForge

## 出来ること

- 無料・オープンソースのデジタル彫刻ツール。Linux / macOS / Windows で動作し、アカウント不要・テレメトリなし・アプリ内課金なし。v0.10.11 で README とアプリ内の表記から他社製品名を外し、「Classic sculpting keys」「Classic layout」などの自社名に統一した。
- 動的トポロジ、マスク、ボクセルリメッシュ、四角形リトポロジといった彫刻の主要機能を備える。
- 書き出しは FBX / glTF / OpenUSD。**Unreal Engine への送信**と Blender ブリッジに対応。
- ゲーム向けの LOD 生成、Gaussian Splatting、画像/テキストからの3D生成（ビルトインAI）を含む。
- Preferences > Updates の**更新チャンネル**で Stable / Preview を選べる。Preview は GitHub のプレリリース（`vX.Y.Z-beta.N`）を配信し、安定版より古いビルドは配信しない。
- ベータ版（v0.11.0-beta.1）では6パック計60本のブラシパック、手続き的アルファ6種、スクリプト用の `mask_by_peaks` / `mask_by_color` / `mask_by_facing` と `brush_use` が加わった。大筆向けの Fast Big Brushes は実験扱いで既定はオフ。
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

- 2026-11-04: 初回登録（★504 / v0.10.10 / GPL-3.0 / 30日100+コミット）、Stable/Preview の更新チャンネルと自社名への表記統一（v0.10.11）、ブラシパック60種（v0.11.0-beta.1）
