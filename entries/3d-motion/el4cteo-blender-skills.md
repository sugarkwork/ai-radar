---
repo: "EL4CTEO/blender-skills"
name: "Blender Agent Skills"
genre: "3d-motion"
url: "https://github.com/EL4CTEO/blender-skills"
last_release: "v1.2.0"
flags: ["unverified"]
risk_notes: "テスト通過は公開リリースでの作者報告。テストの再実行、生成物の品質差、投稿の羊牧場の制作・レンダリング時間、各エージェントやMCP構成での実動作は未検証。リリースの年とタイムゾーンを含む公開日時は未確認。"
stars: 933
forks: 89
open_issues: 1
size_kb: 6042
language: "Python"
created: "2026-10-14"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 9
commits_90d: 9
commit_cadence: "weekly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2115534594854551771"]
fetched_at: "2026-11-10T12:24:07+00:00"
---

# Blender Agent Skills — Blender制作工程をAIエージェントから使う

## 出来ること

- モデリング、UV展開、PBR素材、ベイク、リギング、アニメーション、書き出し、品質確認の手順をエージェントから使える。公開リリースv1.2.0では28スキルを案内している。

## 目的・背景

- blender-coreが依頼内容に応じて専門スキルへ振り分け、BlenderのPython APIを使う実行経路を案内する。作者はv1.2.0でBlender 5.2.3のヘッドレステスト67件が通過したと報告している。

## 依存関係

- Blender 5.2以降と、Claude CodeやCodexなどAgent Skills対応のエージェントが必要。起動中のBlenderを操作する場合はBlender MCPサーバーを別途用意する。リポジトリはMITライセンス。

## 実行条件

- MCP経由では起動中のBlenderを操作する。MCPを使わない場合はBlenderをバックグラウンドで起動して処理する。

## 最短手順

- Claude Codeで `/plugin marketplace add EL4CTEO/blender-skills` を実行し、続けて `/plugin install blender-agent-skills@blender-agent-skills` で導入する。
- Claude Codeに『blender-coreを使い、木箱を作ってglTFで書き出して』と依頼する。blender-coreからモデリングや書き出しの専門スキルを参照できる。

## 変更履歴

- 2026-11-10: 初回登録
