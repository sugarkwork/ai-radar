---
repo: "1jehuang/jcode"
name: "jcode"
genre: coding-agent
url: "https://github.com/1jehuang/jcode"
license: "MIT"
stars: 21447
language: "Rust"
created: "2026-01-05"
updated: 2026-11-04
added: "2026-11-04"
first_seen: "2026-11-04"
sources: []
flags: []
risk_notes: ""
forks: 2501
open_issues: 788
size_kb: 469116
archived: false
commits_30d: 100
commits_90d: 0
commit_cadence: daily
last_release: "v0.99.1"
---

# jcode

## 出来ること

- Rust 製のコーディングエージェント用ハーネス（CLI）。複数エージェントの並列実行を前提に、メモリ消費を抑える設計。
- セッションを複数同時に開いても軽いことを売りにしている（投稿者の計測では10セッションで 100MB 台、起動は十数ms と主張。数値は投稿者・ベンダー側のもので独立検証はしていない）。
- 会話のセマンティックメモリを内蔵し、過去のやり取りを自動で検索して文脈に戻す。
- サイドバーでファイルと差分のプレビュー、Mermaid のレンダリング。
- Claude / OpenAI / Gemini / Copilot / DeepSeek など複数プロバイダに対応（README の対応表記）。MCP サーバーとしても使える。
- 既存の Claude Code や Codex の設定・スキルをある程度引き継げることを想定した設計（`jcode` 独自の設定体系を持つ）。

## 目的・背景

「エージェントを何本も並列で走らせるとマシンが重くなる」問題に対する、Rust 実装の軽量ハーネスという位置づけ。2026-01 公開、Y Combinator S26 のプロジェクトとして README に記載がある。個人開発のツールではなく、リリースとコミットが現在も継続している。

## 依存関係

- バイナリ配布。`jcode.sh` のインストールスクリプト、または GitHub Releases から取得。
- 認証は各プロバイダの API キー、もしくは既存 CLI（Claude Code 等）のログインを利用。

## 実行条件

- ライセンスは MIT。
- 公式インストーラは `curl … | bash` 形式。中身を確認せずに実行したくない場合は Releases のバイナリを使う。
- ★21,000 台と大きいが、issue も788件と多い。破壊的変更が入りやすい（v0.x 系）点は留意。

## 最短手順

```bash
curl -fsSL https://jcode.sh/install | bash
jcode
```

## 変更履歴

- 2026-11-04: 初回登録（★21,447 / MIT / Rust / 最終push 2026-11-04 / v0.99.1）
