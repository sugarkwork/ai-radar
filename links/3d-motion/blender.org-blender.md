---
name: "Blender"
genre: "3d-motion"
url: "https://www.blender.org/"
author: "Blender Foundation"
pricing: "free"
pricing_detail: "完全無料。GPL-2.0-or-later。寄付（Development Fund）は任意。サインアップ不要、インターネット接続なしでも動作。商用利用可で、制作物（画像/動画/.blend）は自分のもの。"
signup_required: false
flags: ["unverified"]
risk_notes: "Blender 自体は GPL の無料ソフトで、モデリング/レンダー/Python API は公式で確認済み。ただし投稿の『瓶・液体・金キャップ・ロゴを全部コードから』は投稿の主張で、.blend も生成スクリプトも配布されていないため再現性は未検証。動画は 1440x1800 の1フォーマットで、16:9/9:16/1:1 の3形式は UI 上は終盤 6/6 で完了表示になるが、実ファイルは確認できない。『GPU from 2016』は画面内の GTX 1050 Ti 表記で、実測ではない。投稿の $1,500–5,000 も未検証。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2114084322227503206"]
fetched_at: "2026-11-09T13:18:50Z"
---

# Blender — 無料・GPL の3D制作スイート、投稿ではビルドとレンダーを担当

## 目的

- 投稿の BUILD / LIGHT / RENDER 工程。ガラス瓶、液体、金キャップ、ロゴのモデリング、マテリアル、ライティング、EEVEE/Cycles レンダーを担う実行ツール。
- AI が生成したコードや MCP ツールを受け取って実際に 3D シーンを構築する側で、Claude Code や Blender MCP がなくても手作業で使える。

## 何ができるか

- モデリング/スカルプト/UV、アニメーション/リギング、VFX トラッキング、Cycles（パストレーサー）と EEVEE、Python API（bpy）、コマンドラインのバックグラウンド実行、動画シーケンサー、glTF/FBX/OBJ などの入出力。
- AI からは Python スクリプトを書かせて `blender --background --python script.py` で実行するか、MCP for Blender などの外部 MCP サーバー経由で操作する。Blender 本体の標準機能として MCP は確認できない（Blender MCP は別アドオン）。
- 投稿の『all from code』は bpy で実現できるが、投稿の .blend や生成スクリプトは配布されていない。
- EEVEE はリアルタイム寄り、Cycles は物理ベースのパストレース。ガラス/液体/金属の反射を作る場合は Cycles のほうが扱いやすいが、レンダー時間は長くなる。

## 料金

- 無料。GPL-2.0-or-later。公式サイトに料金ページはなく、寄付は任意。
- 商用利用可。Blender で作った画像・動画・.blend は自分のものとして扱える。
- アドオン/スクリプトを配布する場合は GPL 互換ライセンスが必要になることがある（公式ライセンスページに記載）。

## 登録の要否

- 不要。ダウンロードしてインストールするだけ。アカウントもネット接続も不要（一部の任意アドオンは接続する）。
- 2026-11-09 時点の安定版は 5.2.3 LTS（2026-10-22 リリース）。5.3 は 2026-11-10 公開予定。
- Windows インストーラは 349 MB、macOS Apple Silicon は 330 MB、Linux は 367 MB（公式ダウンロードページの表示）。

## 変更履歴

- 2026-11-09: 初回登録
