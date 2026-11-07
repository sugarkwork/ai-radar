---
type: "link"
name: "Sand3D (sand3d)"
genre: "3d-motion"
url: "https://sandflow.ai/sand3d/"
author: "Sandflow (Sandflow-ai)"
pricing: "free"
pricing_detail: "Python パッケージは Apache-2.0、データセットは CC BY 4.0 でいずれも無料。料金ページ https://sandflow.ai/pricing は 404 で有料プランは存在せず、未公開の基盤モデルのみウェイトリスト。"
signup_required: false
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/HuggingPapers/status/2118290438805135578"]
flags: []
risk_notes: "公開直後の若いプロジェクト（GitHub リポジトリ作成 2026-11-03、PyPI 初公開も同週、星 910）。bpy（Blender モジュール）依存で Python 3.11 か 3.13 が必要（3.12 非対応）、導入環境は重い。MCP サーバ・REST API・専用 CLI は提供されず、Python 実行環境が前提。元ポスト（Tencent の TailorRig データセット）は本件と無関係な宣伝で、根拠にしていない。"
fetched_at: "2026-11-07T10:59:19Z"
---

# Sand3D — 3D オブジェクトを短い Python コードで書く、LLM 向けモデリングライブラリ

## 目的

- 3D 形状を「部品ごとの短い Python プログラム」として記述するためのライブラリ。座標を手計算せず、名前付きの部品・辺・面を操作するので、LLM が数百トークンで物体を書き、人間がそのまま読める。
- エージェントに「関節付きの椅子を作って GLB で出して」と頼む使い方を想定しており、生成物はそのまま three.js／ゲームエンジン／ROS・Isaac などのパイプラインに渡せる。

## 何ができるか

- pip install sand3d → import sand3d as s3d。Blender の bpy 上で動き、bpy は依存パッケージとして自動で入る（別途 Blender のインストールは不要）。
- プロファイル（rect/circle/poly/spline など）、ソリッド（extrude/revolve/loft/sweep/wire/torus など）、編集（hole/pocket/fillet/chamfer/shell など）、配置（at/on=/transform/grid/ring）、関節（joint/pose）を s3d.<verb> のフラットな約 70 動詞で扱う。寸法は既定でミリメートル。
- 書き出しは拡張子で指定する 1 呼び出し: GLB（Web・ゲームエンジン向け、関節はノードの extras）、URDF（ROS・PyBullet・MuJoCo・Isaac 向け）、USDA（OpenUSD・Omniverse・Isaac Sim 向け）、OBJ、STL。
- AI からの使い方は Python ライブラリ（コード生成＋実行）のみ。API 全体が約 3,600 トークンの docs/api.md に収まり、llms.txt と AGENTS.md/CLAUDE.md も用意されているため、システムプロンプトに API を丸ごと入れて使う設計。MCP サーバ、REST API、専用 CLI はリポジトリ内に存在しない。
- 学習・参照用として 100,000 件の Sand3D プログラム（Objaverse 67K、CAD 24K、Articraft 9.2K、NVIDIA SimReady 2.3K、AutoMate 3.1K 由来）が Hugging Face で CC BY 4.0 公開され、Spaces のエクスプローラで閲覧できる。

## 料金

- すべて無料。Python パッケージは Apache-2.0、データセットは CC BY 4.0。
- 有料プランや料金ページは存在しない（https://sandflow.ai/pricing は 404）。未公開の基盤モデルのみ「Release soon」でウェイトリスト登録制。

## 登録の要否

- 不要。pip で導入でき、アカウント作成やログインなしで利用できる。
- Hugging Face のデータセットも gated ではない（API で gated=false、private=false を確認）。

## 変更履歴

- 2026-11-07: 初回登録
