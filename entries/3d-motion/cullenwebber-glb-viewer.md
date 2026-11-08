---
type: repo
repo: cullenwebber/glb-viewer
name: GLB Viewer
genre: 3d-motion
url: https://github.com/cullenwebber/glb-viewer
author: Cullen Webber（@SinzVII）
license: none
language: TypeScript
stars: 16
forks: 0
open_issues: 0
added: 2026-11-08
first_seen: 2026-11-07
source_post: https://x.com/SinzVII/status/2118904126923055436
sources: ["https://raw.githubusercontent.com/cullenwebber/glb-viewer/main/README.md"]
flags: ["unverified", "low-quality"]
risk_notes: "LICENSEファイルが404で、明示ライセンスなし（all rights reserved）。ソースは公開されているが、再配布・商用利用の許諾は不明。配布はmacOSのDMGのみ（arm64/x64、Apple公証なし→初回はOpen Anywayかxattr -cr）。Windows/Linuxのビルド手順はREADMEになく、Windows 11環境ではそのまま動かせない。16 starsの若いプロジェクトで、AI機能はない。DMG未ダウンロード・未起動（READMEとリポジトリ構成のみ確認）。"
fetched_at: "2026-11-08T06:40:00Z"
---

# GLB Viewer — Blender→three.js 向け GLB 最適化・KTX2 圧縮の macOS アプリ

## 出来ること

- GLB/glTF を読み込み、Three.js 向けに軽量化・検証・比較するローカル優先の macOS ワークスペース。
- テクスチャ: KTX2（ETC1S / UASTC、品質・effort・mipmap・解像度指定）、WebP / PNG / JPEG 変換。ETC1S は約12MPまでという制限の記載あり。
- ジオメトリ: Draco または Meshopt 圧縮、メッシュ簡略化と LOD、インスタンシング、シーン整理。
- 確認: glTF バリデーション、オリジナルとの同期比較ビュー、圧縮前後のサイズ実測レポート、WebGPU プレビュー。
- Blender アドオン（`blender/glb_viewer_bridge`）で監視エクスポートし、TSL ノードとして書き出せる。

## 目的・背景

- Blender で作ったアセットを three.js に持っていく際の「重い・テクスチャ形式が合わない・どこが重いか分からない」を、書き出し後に1画面で詰めるためのツール。作者自身が投稿で紹介しており、第三者の代理宣伝ではない。
- 2026-11-07 時点で 16 stars。若いプロジェクトで、README 以上の実績・利用報告は確認できていない。

## 依存関係

- macOS アプリ（DMG 配布）。ソースは TypeScript / Vite / three.js 系。
- Blender アドオンを使う場合は Blender 側のインストールが必要。
- Windows / Linux 向けのビルド手順・配布物は現時点で無い。

## 実行条件

- **macOS のみ**。Apple 公証がないため、初回起動は「Open Anyway」または `xattr -cr` が必要。
- **ライセンス未明示**（LICENSE 404）。業務利用・再配布は作者に確認するまで避ける。
- AI 機能は無い。純粋なアセット最適化ツール。

## 最短手順

1. GitHub Releases から macOS 用 DMG（arm64 / x64）を取得。
2. 初回は右クリック→Open、または `xattr -cr /Applications/GLB\ Viewer.app`。
3. GLB を開き、KTX2 / Draco / Meshopt の設定を選んで変換。
4. 比較ビューで元ファイルとの差分とサイズレポートを確認。
5. Blender から監視エクスポートする場合は `blender/glb_viewer_bridge` をアドオンとして読み込む。

## 変更履歴

- 2026-11-08: 初回登録（macOS専用・ライセンス未明示のため「保留」だったものを、注意付きで収録）
