---
repo: "arjun988/blender-skills"
name: "Blender Skills（94 specialist Blender skills）"
genre: "3d-motion"
url: "https://github.com/arjun988/blender-skills"
author: "arjun988"
license: "MIT"
stars: 2237
language: "TypeScript"
created: "2026-07-05"
updated: "2026-11-06"
forks: 193
open_issues: 3
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
size_kb: 729
archived: false
last_release: ""
last_release_at: ""
homepage: "https://blender-skills.vercel.app"
flags: ["unverified"]
risk_notes: "効果の定量評価・ベンチマークは無く、README の設計方針と投稿者のデモ動画だけが根拠。README は「Marketplace listing is currently under review by Anthropic」と記載しており、Claude Code プラグインマーケット未登録（GitHub から手動コピー）。30日コミットは1件で開発は低頻度（最終コミット 2026-11-06）。MCP 方式のため投稿が書く `blender -b -P script.py` の完全ヘッドレス実行とは前提が異なり、Blender を起動してアドオンから接続する必要がある。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2113374545302200732"]
fetched_at: "2026-11-08T20:07:36Z"
---

# Blender Skills — Blender を操作する 94 本のエージェントスキル集（MCP 経由）

## 出来ること

- Blender 作業のための 94 本の SKILL.md をまとめたパック。モデリング（hard-surface / prop / vehicle / environment / character / creature）、プロダクション（sculpting, retopology, uv-workflow, materials, texture-workflow, hair-groom, cloth-sim, lookdev）、テクニカル（geometry-nodes, lighting, camera-cinematography, rendering, compositing, animation, rigging, vfx-fx, physics-sim）、パイプライン（export-pipeline, unity/unreal/godot-export, lod-pipeline, qa-review）まで含む。
- アートスタイル系のスキルも同梱：voxel-style（投稿が使ったもの）、lowpoly-style、psx-horror-style、anime-style、pixel-art、retro-8bit/16bit など。voxel-style は「グリッドスナップ・斜めの有機ベベル禁止・小さなパレット・段差でシルエットを作る」というルールを明文化している。
- blender-director が入口になり、依頼文からスキル連鎖を自動で組む（例: blender-director → hard-surface → uv-workflow → materials → asset-optimization → export-pipeline）。
- 参照画像を渡すと reference-image-match が「参照解析 → カメラマッチ → ジオメトリ → マテリアル → ライティング → スクリーンショット比較ループ」を回す。投稿の「参照を1枚渡す」手順に対応する部分。
- 実行は BlenderMCP アドオン経由。エージェントは UI 操作を説明するのではなく MCP ツールを呼ぶ。

## 目的・背景

- 「チュートリアルbot」ではなく上級テクニカルアーティストの代わりとしてエージェントを使う、というのが README の掲げるコンセプト。各スキルは作業前にパイプラインを計画し、制作標準（命名規約・ポリゴン予算・ゲーム向け出力）に従い、書き出し前にチェックリストで検証する、としている。
- 作者 arjun988、MIT、2026-07-05 公開、version 1.3.0（CHANGELOG 上は 1.2.0 で 23 本、1.3.0 で 48 本を追加）。README は jeffallan/claude-skills に触発されたと明記。
- 投稿（@Y0urDumble）の /voxel-style はこのリポジトリの .claude/skills/voxel-style/SKILL.md に対応する。

## 依存関係

- Blender 本体（アドオンを入れて起動している必要あり／README のログでは 5.2.3 に接続）
- uv（Python パッケージランナー）
- ahujasid/blender-mcp（BlenderMCP アドオン）
- エージェント: Claude Code（.mcp.json + .claude/skills/）、Cursor（.cursor/mcp.json）、Kiro、Codex
- ライセンスは MIT。追加の課金・API キーは不要（モデル側の利用料のみ）

## 実行条件

- Blender を GUI で起動し、サイドバー N → BlenderMCP → Connect to Claude で接続を確立しておく。MCP 接続が前提なので、Blender が落ちている状態ではスキルは動かない。
- スキルは Markdown の指示書なので、モデル側がスキル（Agent Skills 形式）を読める必要がある。Claude Code / Cursor / Kiro / Codex のいずれか。
- 書き出し先（Unity / Unreal / Godot）を使う場合は各 export スキルが前提とするエンジン側の設定が要る。

## 最短手順

- 1. `git clone https://github.com/arjun988/blender-skills.git`
- 2. Claude Code なら `cp -r blender-skills/.claude/skills /path/to/your/project/.claude/skills/`（Cursor は .cursor/skills/ へコピー）
- 3. Blender に BlenderMCP アドオンを入れ、N パネル → BlenderMCP → Connect to Claude
- 4. エージェントを再起動して .mcp.json を読ませる（AI からは MCP の blender ツールとして見える）
- 5. チャットで「voxel toy style, white sticker outline, bright background でキャラを作り、リグを入れて 120bpm で踊らせて」のように発注すると、blender-director が voxel-style → rigging → animation の順にスキルを選ぶ
- 6. 最初は 4〜5 フレームだけレンダさせて確認 → 破綻を直す → 本番レンダ（Eevee）

## 変更履歴

- 2026-11-09: 初回登録
