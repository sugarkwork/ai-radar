---
repo: pbakaus/impeccable
name: Impeccable
genre: agent-framework
url: https://github.com/pbakaus/impeccable
license: Apache-2.0
stars: 102748
language: Rust
created: 2025-11-16
updated: 2026-11-04
added: 2026-11-03
sources:
  - https://x.com/dragono64v/status/2117278757690253492
forks: 6075
open_issues: 65
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 897688
archived: false
fetched_at: "2026-11-04T22:53:44Z"
last_release: cli-v4.8.0
last_release_at: 2026-10-26
---

# Impeccable

## 出来ること

- コーディングエージェントに「デザインの語彙」を与えるスキル。`/impeccable <コマンド> <対象>` の形で、対象を1つに絞って指示する。
- 24 コマンドを4系統で提供する。**誘導**: bolder / quieter / distill / colorize / typeset / layout / animate / delight / overdrive。**レビュー**: critique（UX ヒューリスティックで採点）/ audit（アクセシビリティ・性能・テーマ・レスポンシブを P0〜P3 で報告）。**仕上げ**: polish / harden / clarify / adapt / optimize / onboard。**計画・設定**: shape / init / document / extract。ほかに live / generate。
- **スロップ検出器**: 62 条の決定論的ルールで「AI が作りがちな見た目」を検出する。LLM も API キーも使わない。
- 検出器は3経路で動く。(1) エージェントの編集フック（UI ファイルを編集するたびに指摘を返す）、(2) CLI `npx impeccable detect <path|URL>`（`--json` / `--github` で CI 連携）、(3) Chrome 拡張のオーバーレイ。
- `/impeccable live` で開発サーバー上にオーバーレイを出し、要素を選んでバリアントをその場で差し替え、ソースへ書き戻す（Vite / Next / SvelteKit / Astro / Nuxt / 素の HTML）。
- `/impeccable init` が `PRODUCT.md` を、`/impeccable document` が `DESIGN.md` を生成し、以降のコマンドがそれを読む。

## 目的・背景

pbakaus（Paul Bakaus）によるデザインスキル。README の主張は「Inter 一択・紫青グラデ・カードの入れ子・色背景にグレー文字といった既定解を、モデルが何であっても再生産してしまう」問題への対処。同じモデル・同じブリーフで比較したスクリーンショットを README に掲載している。2025-11-16 作成、Apache-2.0、エンジン本体は Rust 製の自己完結バイナリ。

## 依存関係

- `npx impeccable install`（npm）。ただし **Node が必要なのは npx の部分だけ**で、スキル本体は同梱または `~/.impeccable/bin/` に一度だけ取得される自己完結エンジンバイナリで動く。
- 対応ツール: Claude Code / Cursor / Codex CLI / GitHub Copilot / Devin / Replit Agent / Gemini CLI / Grok Build / OpenCode / Google Antigravity / Kiro / Trae / Rovo Dev / Qoder / Mistral Vibe / Pi / Hermes Agent / DeepSeek Harness / Veto。
- フックを使うには追加操作が要る場合がある: Codex は `/hooks` で承認、Grok Build は `/hooks-trust`、**Hermes Agent は `hermes plugins enable impeccable-design-hook`**。
- ライブモードの要素選択・バリアント切替はブラウザ（開発サーバー）を使う。URL スキャンはインストール済みの Chrome / Edge を使う。

## 実行条件

- 基本はコーディングエージェントとプロジェクトのチェックアウトがあること。ライブモードは Vite / Next / SvelteKit / Astro / Nuxt / plain HTML の開発サーバーが対象。
- ソース（JSX/TSX）に対するスキャンではパターン系ルールのみ。低コントラストや極小文字など**描画後のページが必要なルールは URL スキャン時のみ**実行される。
- `detect` の終了コードは 2 = 指摘あり、1 = 対象をスキャンできなかった。
- ライブモードの Apply は、1分以内にチャットエージェントがポーリングしていない場合 `codex`（無ければ `claude`）CLI を**承認・権限チェック・サンドボックスを無効にして**起動する。README 自身がこの挙動を明記し、`IMPECCABLE_LIVE_COPY_AGENT=chat|off` で切り替えられるとしている。未知のリポジトリで使う前に確認すること。

## 最短手順

```bash
# プロジェクトルートで
npx impeccable install          # ツール検出 → project/global 選択 → フック導入
# エージェントを再読み込みしてから
/impeccable init                # PRODUCT.md を生成
/impeccable critique the pricing cards

# エージェント無しで検出器だけ回す場合
npx impeccable detect src/
npx impeccable detect http://localhost:5173
```

## 変更履歴

- 2026-11-03: 初回登録（star 101,199 / pushed 2026-11-02）
