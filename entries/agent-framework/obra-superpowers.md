---
repo: obra/superpowers
name: Superpowers
genre: agent-framework
url: https://github.com/obra/superpowers
license: MIT
stars: 311667
language: Shell
created: 2025-10-09
updated: 2026-11-03
added: 2026-11-03
sources:
  - https://x.com/thegreatest_sv/status/2117591176048005131
forks: 27728
open_issues: 351
commits_30d: 3
commits_90d: 6
commit_cadence: monthly
size_kb: 8070
archived: false
fetched_at: "2026-11-03T15:42:15Z"
last_release: v7.0.1
last_release_at: 2026-10-21
---

# Superpowers

## 出来ること

- コーディングエージェント向けの「開発方法論」を、合成可能なスキル群として配布する。
- スキルは brainstorming / 計画 / 実装 / デバッグ / レビュー / サブエージェント駆動開発などをカバー。
- エージェントに「まずスキルを読んでから作業する」よう指示する初期プロンプトを同梱。
- Claude Code、Codex CLI、Cursor、Gemini CLI、Copilot CLI、Grok Build CLI、Qwen Code、OpenCode、Hermes Agent など多数のホストに対応（README に導入手順が並ぶ）。
- プラグインマーケットプレイス（`obra/superpowers-marketplace`）とスキル集（`obra/superpowers-skills`）が別リポジトリで存在。

## 目的・背景

Jesse Vincent（obra）による、エージェントの「行き当たりばったりな実装」を抑えるための方法論パッケージ。単発のプロンプト集ではなく、計画→実装→検証のループをスキルとして強制する点が特徴。2025-10 作成、現在 31 万 star・27,000 fork と、このジャンルでは最大規模。ライセンスは MIT だが、README に商用サービス（サポート等）への導線がある。

## 依存関係

- ホスト側のコーディングエージェント（Claude Code / Codex CLI / Cursor / Gemini CLI ほか）。
- インストーラはシェルスクリプト。Git があれば動く。
- 追加のランタイム依存は無し（スキルは Markdown）。

## 実行条件

- OS 不問（WSL 可）。GPU 不要。
- ネット接続（クローン／マーケットプレイス取得）。
- エージェント側のスキル／プラグイン機構が有効になっていること。

## 最短手順

```bash
git clone https://github.com/obra/superpowers.git
cd superpowers
./install.sh          # ホストエージェントを対話で選択
# Claude Code なら: /plugin marketplace add obra/superpowers-marketplace
```

## 変更履歴

- 2026-11-03: 初回登録（star 311,640 / pushed 2026-11-03）
