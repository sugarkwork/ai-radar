---
repo: SwotAtmk/infinite-creation
name: Infinite Creation（Agent无限创作）
genre: video-gen
url: https://github.com/SwotAtmk/infinite-creation
license: MIT
stars: 193
language: JavaScript
created: 2026-09-09
updated: 2026-11-03
added: 2026-11-03
sources:
  - https://x.com/superfang119/status/2117543981446058211
forks: 46
open_issues: 6
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 123542
archived: false
fetched_at: "2026-11-03T15:43:28Z"
last_release: v1.0.5
last_release_at: 2026-11-02
---

# Infinite Creation（Agent无限创作）

## 出来ること

- 小説・脚本を入力すると、Agent がストーリー分解 → 人物設定 → シーン素材 → 絵コンテ（分镜）まで自動生成する。
- 生成した分镜を **ComfyUI + MiniMax H3** に渡して逐次ビデオ化し、長尺（時間制限なし）の動画に組み上げる。
- 人物バイブル／スタイルガイド／シーン配置表を自動で作り、人物・衣装・小道具・音声素材を管理してショット間のドリフトを抑える。
- Codex CLI / Claude Code / Gemini CLI / Qwen Code / Cursor Agent / Grok Build などを MCP 経由で接続し、パイプラインを引き継がせる。同梱スキル 35 個。
- 別系統として「无限·秩影」というコード映画ワークベンチを同梱。66 種のビジュアルスタイルを持ち、Three.js + FFmpeg でレンダリングコードを書かせてスタイル化動画を作る（ComfyUI 不要）。

## 目的・背景

中国語圏の開発者 SwotAtmk による、ローカル完結の「小説→長編動画」量産パイプライン。商用 API に依存せず、手元の ComfyUI と MiniMax H3 で回すことを前提にしている。作者自身がリプライで「最も崩れるのは分镜間の不一致」と認めており、人物一貫性が実用上の焦点。2026-09 作成、約 120MB のリポジトリ。

## 依存関係

- Node.js 22+ / pnpm 9+ / Bun / FFmpeg
- ComfyUI（導入済みであること）＋ MiniMax H3 のモデルとワークフロー
- MCP 対応のコーディングエージェント（任意だが推奨）
- 同梱の ComfyUI ワークフローを追加すると、対応するスキルが自動生成される

## 実行条件

- 作者記載の参考構成：**VRAM 12GB+ / RAM 32GB+ / ディスク 150GB+**
- 全ワークフローがその構成で快適に動く保証はない、と明記されている。
- 生成はショット単位の**直列**処理。本編の所要時間はショット数に比例する。
- Windows の場合は WSL 側に Node/FFmpeg/ComfyUI を揃える必要がある。

## 最短手順

```bash
git clone https://github.com/SwotAtmk/infinite-creation
cd infinite-creation
pnpm install          # Bun も併用
# ComfyUI の接続先・MiniMax H3 モデル・ワークフローを設定
# 小説/脚本を投入してパイプライン開始
```

## 変更履歴

- 2026-11-03: 初回登録（star 193 / pushed 2026-11-03）
