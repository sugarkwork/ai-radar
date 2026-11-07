---
repo: "earthtojake/text-to-cad"
name: "text-to-cad"
genre: "3d-motion"
url: "https://github.com/earthtojake/text-to-cad"
author: "earthtojake (Thompson Labs LLC)"
license: "MIT"
stars: 25757
language: "Python"
created: "2026-04-22"
updated: "2026-11-07"
forks: 2446
open_issues: 46
size_kb: 436278
archived: false
commits_30d: 51
commits_90d: 100
commit_cadence: "daily"
last_release: "v0.10.4"
last_release_at: "2026-11-06"
flags: ["unverified"]
risk_notes: "有効性は配布元の設計説明と自己申告のみで、生成された CAD の寸法精度・製造可能性を第三者が測定した結果は確認していない。DFM/DfAM の検査は mesh 計測と規則の引用だが、規則の妥当性・合否閾値は未検証。PyPI の分類は Development Status :: 4 - Beta。Python 3.14 固定で 3.13 以前では動かない。Windows 11 の Smart App Control 有効環境では OCP のネイティブモジュールが遮断される。既定でテレメトリ有効。リポジトリサイズは API 表記 436,278 KB。"
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/opensourcelab9/status/2118601779063701949"]
fetched_at: "2026-11-07T15:52:19Z"
---

# text-to-cad — エージェントが build123d で書く3D CAD 生成プラグイン（STEP/STL/3MF + MCP）

## 出来ること

- 自然言語や画像の指示から、エージェントが build123d の Python スクリプトとして3Dモデルを書き、STEP・GLB・STL・3MF に書き出す
- 製造向けの検査: DFM（板金・CNC・射出成形。draft・アンダーカット・投影面積を mesh から測り、指摘ごとに規則を引用）、DfAM（壁厚・オーバーハング・サポート体積・造形方向）
- 寸法・隠れ線・穴注記・表題欄つきの工学図面 PDF、2D DXF、ロボット記述の URDF / SRDF / SDF（ROS・MoveIt・Gazebo 用）
- G-code スライス（OrcaSlicer と自分のプリンタプリセット）、Bambu Lab への送信、SendCutSend 入稿前チェック、既製 STEP 部品（ねじ・ベアリング・モータ・コネクタ）の検索
- ローカルの CAD ビューアが、エージェントアプリ内またはブラウザでモデルを表示し、再ビルドのたびに追従する
- MCP サーバ（cad-mcp）と12のスキルを同梱し、Claude Code・Codex・Cursor・Gemini・Grok から呼び出せる

## 目的・背景

- 「Design physical products with AI」を掲げ、テキスト指示から物理製品の3Dモデルを作る作業を、エージェントのローカルワークフローとして回すプラグイン。MIT、著作権者は Thompson Labs LLC、PyPI に cad / cad-server / cad-mcp の 0.10.4 を公開
- モデルをコードで表すため寸法を後から編集でき、.xbf ドキュメントに部品名・色・材質・ジョイントを保持する。サーバが作業状態をメモリに持ち、変更分だけ再ビルドする設計
- 2026-04-22 作成、2026-11-07 時点で 25,757 stars / 2,446 forks / 46 open issues。30日で51コミット、90日は API の100件上限で打ち止め（実際は100件以上）。直近リリースは v0.10.4（2026-11-06）で開発は継続中
- CAD カーネルに Open CASCADE（cadquery-ocp-novtk）を使い、Python 側は build123d、JS 側は npm workspaces でビューアと MCP を構成する

## 依存関係

- Python 3.14 以上（uv 管理の Python 3.14 を使う）
- cad（ライブラリ）: numpy>=2,<3。CAD カーネルは extra の build123d（build123d>=0.13,<0.14、cadquery-ocp-novtk>=8.0,<8.1、bd_materials、threejs-materials、matplotlib、shapely、ezdxf、pillow）
- cad-server: cad==0.10.4、uv>=0.7、ezdxf、pillow。cad コマンドとビューアのサーバを提供する
- cad-mcp: 標準ライブラリのみ。stdio で起動し、ローカルの CAD サーバへ HTTP で中継する薄いトランスポート
- リポジトリ側の JS: npm workspaces（packages/core、packages/ui、apps/web、apps/mcp、apps/docs）と package-lock.json（約494 KB）
- 外部ツール: OrcaSlicer（G-code スライス）、Bambu Connect または Bambu Studio（印刷送信）、SendCutSend（板金・レーザー入稿の事前チェック）

## 実行条件

- macOS / Linux は texttocad.dev の install.sh を sh で実行、Windows は PowerShell で install.ps1 を実行する
- uv が無ければ導入し、初回起動でランタイムと Python 3.14 をダウンロードするためネットワーク接続が必要。初回は Claude Code の MCP_TIMEOUT 既定 30 秒を超えることがあり、再起動すると続きから再開する
- GPU 不要（CAD カーネルは CPU で動く）。リポジトリサイズは API 表記 436,278 KB
- Windows 11 で Smart App Control が有効だと ImportError: DLL load failed while importing OCP で失敗する。無効化（戻すには Windows 再インストールが必要）か WSL で回避する
- 既定で利用統計とクラッシュレポートを送信する。インストーラの --no-telemetry で無効化できる
- ライセンスは MIT（無償）。GitHub API の spdx_id と LICENSE 本文（MIT License, Copyright (c) 2026 Thompson Labs LLC）が一致する

## 最短手順

- Claude Code: claude plugin marketplace add earthtojake/text-to-cad#latest の後に claude plugin install text-to-cad@earthtojake。プラグインがスキルと MCP サーバをまとめて入れる
- MCP クライアントへ直接登録する場合（リポジトリの mcp.json のとおり）: 転送は stdio、command は uvx、args は --no-config / --managed-python / --python 3.14 / --from cad-mcp==0.10.4 / cad-mcp の順、env に CAD_INSTALL_CHANNEL=agent-plugins
- エージェントに部品やアセンブリを頼むと、モデルを Python スクリプトとして書き、cad run src/bracket.py でビルドしてビューアに表示する
- エージェントが使う MCP ツール: cad_show（モデル ID か絶対パスで表示）、cad_view と cad_screenshot（カードやタブを描くホストのみ）、cad_inspect・cad_snapshot・cad_export（全ホスト）
- CLI で直接叩く場合: cad doctor（インストール診断）、cad viewer --json FILE（既存ファイルを表示しページ URL を返す）、cad run --with pandas model.py（追加依存をその1回だけ入れる）
- 自前の Python 環境で回すなら pip install 'cad[build123d]==0.10.4' の後に python model.py（extra を外すと import build123d が失敗する）

## 変更履歴

- 2026-11-07: 初回登録
