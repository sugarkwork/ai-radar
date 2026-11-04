---
repo: ahujasid/mcp-for-blender
name: MCP for Blender
genre: 3d-motion
url: https://github.com/ahujasid/mcp-for-blender
license: MIT
stars: 33316
language: Python
created: 2025-03-07
updated: 2026-11-04
added: 2026-11-03
sources:
  - https://x.com/y0urdumble/status/2117396633889427646
forks: 3020
open_issues: 55
commits_30d: 23
commits_90d: 97
commit_cadence: daily
size_kb: 2106
archived: false
fetched_at: "2026-11-04T22:51:58Z"
---

# MCP for Blender

## 出来ること

- LLM（Claude Desktop / Claude Code / Cursor など MCP 対応クライアント）から Blender を操作する。
- プロンプトによる 3D モデリング、シーン構築、オブジェクト操作、マテリアル設定。
- Blender 側はアドオン、外側は MCP サーバー（Python）の二層構成。
- 3D 生成は Meshy / Tripo / Hyper3D Rodin / Hunyuan3D の4系統。Tripo は自前 API キーでも使えるようになった（従来は Premium 専用）。モデルは `v3.1-20260211`（H3.1）と `P2-20260801`（P2.0）から選択、プロンプト1024字・画像20MB（jpg/png）まで。
- Meshy は `pose_mode`（`a-pose` / `t-pose`）に対応。キャラクターをリグ前提の姿勢で生成できるが、自前 Meshy キーのみ（Premium 経由では不可）。
- Hyper3D Rodin は複数画像をフォルダで渡し、1つのオブジェクトの各ビューとして生成できる。自前キーでは `Gen-2.5-Medium` ティアが既定で、トライアルキーはメインサイト経由のみ、fal.ai 経由は自前の fal.ai キーが要る。
- Tripo はアドオンの **Tripo Domain** で `.com`（中国版アカウント）を選べる。
- 旧名 `blender-mcp`。PyPI パッケージ名は `mcp-for-blender` に変更されたが、既存設定はそのまま動く。

## 目的・背景

Ahuja Sid によるサードパーティ製の Blender × LLM 連携。Blender Foundation 公式ではなく、README にもその旨の免責が明記されている。2025-03 作成で 3.3 万 star・3,000 fork。Blender を「コードで書く」のではなく「対話で触る」方向のツールで、レンダリング結果をスクリーンショットで返す仕組みを持つ。

## 依存関係

- Blender（3.x 以降）＋ 同梱の Blender アドオン
- Python 3.10+、`uv`（`uvx` でサーバー起動）
- MCP 対応クライアント（Claude Desktop / Claude Code / Cursor 等）
- 一部機能はビューポートのスクリーンショット取得に依存
- 自前キーで 3D 生成する場合: Meshy（有料プラン）/ Tripo / Hunyuan3D / Hyper3D の各 API キー。Tripo は `BLENDERMCP_TRIPO_API_KEY` でも注入可。キー未設定でも Premium 経由なら不要

## 実行条件

- Blender が GUI で起動していること（ヘッドレス専用ではない）。
- OS 不問。GPU は Blender 側の要件に従う（重いシーンは VRAM 依存）。
- Tripo の自前キー利用と Meshy の `pose_mode` はアドオンプロトコル15以降が必須。旧アドオンだと「not in this addon version」で落ちるので `uvx mcp-for-blender install-addon` → Blender 再起動。
- `quality=high` は Tripo 自前キーでは不可（Premium 側の機能）。
- Windows ホストの Blender と WSL / Docker / 別 PC の MCP サーバーを繋ぐ場合は、アドオンの環境設定で **Bind Address** を Blender 側の LAN IPv4（全インターフェースなら `0.0.0.0`）にし、**Allow Remote Connections** を有効にして接続し直す。クライアント側は `BLENDER_HOST` / `BLENDER_PORT` をそのアドレスとポートに合わせる。待受は認証も暗号化もなく、接続したクライアントは Blender 内で Python を実行できるため、信頼できるネットワーク内に限る（SSH トンネル経由の方が安全）。

## 最短手順

```bash
# Blender 側: addon.py をインストールして「Connect to MCP server」を開始
uvx mcp-for-blender install-addon   # 旧アドオンなら更新（Tripo 自前キー / pose_mode に必要）
# クライアント側:
uvx mcp-for-blender
```

## 変更履歴

- 2026-11-03: 初回登録（star 33,168 / pushed 2026-10-29）
- 2026-11-03: Tripo が自前 API キーで利用可能に（モデル H3.1 / P2.0、1024字・画像20MB、`BLENDERMCP_TRIPO_API_KEY`）、Meshy に `pose_mode`（a-pose / t-pose、自前キーのみ）、アドオンプロトコル 15・パッケージ 2.2.6 へ（992233b、8コミット/13ファイル +1365/-82）
- 2026-11-04: リモート接続（Bind Address / Allow Remote Connections）と、Tripo のドメイン選択・Hyper3D の複数画像入力と既定ティアを追記（2e4b0bc）
