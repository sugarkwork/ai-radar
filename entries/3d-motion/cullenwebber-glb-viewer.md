---
type: repo
repo: cullenwebber/glb-viewer
name: GLB Viewer
genre: 3d-motion
url: https://github.com/cullenwebber/glb-viewer
author: Cullen Webber（@SinzVII）
license: none
language: TypeScript
stars: 18
forks: 2
open_issues: 1
added: 2026-11-08
first_seen: 2026-11-07
source_post: https://x.com/SinzVII/status/2118904126923055436
sources: ["https://raw.githubusercontent.com/cullenwebber/glb-viewer/main/README.md", "https://x.com/sinzvii/status/2118904126923055436?a=WRpZZMJntrGprECzsA8&s=46", "https://x.com/SinzVII/status/2118904126923055436", "https://github.com/cullenwebber/glb-viewer"]
flags: ["unverified"]
risk_notes: "LICENSEファイルが404で、明示ライセンスなし（all rights reserved）。ソースは公開されているが、再配布・商用利用の許諾は不明。配布はmacOSのDMGのみ（arm64/x64、Apple公証なし→初回はOpen Anywayかxattr -cr）。Windows/Linuxのビルド手順はREADMEになく、Windows 11環境ではそのまま動かせない。16 starsの若いプロジェクトで、AI機能はない。DMG未ダウンロード・未起動（READMEとリポジトリ構成のみ確認）。"
fetched_at: "2026-11-09T21:30:37Z"
created: "2026-11-03"
updated: "2026-11-04"
commits_30d: 22
commits_90d: 22
commit_cadence: "daily"
size_kb: 9545
archived: false
amplifiers: []
last_release: "v1.5.0"
last_release_at: "2026-11-04"
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

- 2026-11-08: 初回登録（注意点を明記して収録）

## 追加出典・確認範囲（2026-11-09）

GLB/glTFをThree.js向けに比較・検査・最適化するmacOSアプリ。

KTX2/WebP/PNG/JPEG変換、Draco/Meshopt、LOD、同期比較、BlenderブリッジとWebGPUプレビューを案内。

原チェック時はLICENSEなし、DMGは未公証でWindows/Linux手順なし。再利用許諾・実機動作は未確認。

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:51.037793+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | cullenwebber/glb-viewer |
| url | https://github.com/cullenwebber/glb-viewer |
| license | unknown |
| language | TypeScript |
| created | 2026-11-03 |
| updated | 2026-11-04 |
| stars | 17 |
| forks | 1 |
| open_issues | 1 |
| commits_30d | 22 |
| commits_90d | 22 |
| commit_cadence | daily |
| size_kb | 9545 |
| archived | False |
| fetched_at | 2026-11-09T00:30:51.037793+00:00 |


- @SinzVII (Cullen Webber): https://x.com/SinzVII (Cullen Webber)/status/2118904126923055436
- 対象資料: https://github.com/cullenwebber/glb-viewer
- 参照: https://raw.githubusercontent.com/cullenwebber/glb-viewer/main/README.md

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
