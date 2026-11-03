---
type: "prompt"
name: "CodeGraph を Codex に接続する導入プロンプト"
genre: "prompt-design"
url: ""
author: "@goan999999"
source_post: "https://x.com/goan999999/status/2117462867050144107"
sources:
  - "https://github.com/colbymchenry/codegraph"
added: "2026-11-03"
flags: []
risk_notes: ""
target: "Codex"
transcribed_from: "text"
prompt_sha1: "dcfee5432f15899e0c1f5fc0ec8b0ef0c98dfabb"
---

# CodeGraph を Codex に接続する導入プロンプト

## 目的

CodeGraph（コード知識グラフの MCP サーバー）を既存の Codex 環境に組み込み、インストール・MCP 設定・索引構築・動作検証までをエージェントに一括でやらせる。手順の暗記を省き、既存設定を壊さないことを明示している点が要点。

## 前提

- Codex CLI が動く環境。
- リポジトリ `colbymchenry/codegraph` の存在（MIT、TypeScript、2026-11-03 時点 76,373 star）。
- 索引を作る対象プロジェクトがローカルにあること。
- MCP 設定ファイルを書き換えるため、事前にバックアップを取る（プロンプト内でも「既存設定を上書きするな」と指示している）。

## プロンプト本文

```text
帮我将 colbymchenry/codegraph 接入当前 Codex 环境。检查运行依赖和兼容性，完成安装、MCP 配置与代码索引初始化。随后验证代码搜索、函数调用追踪和依赖关系查询是否可用，确保 Codex 能正常调用。不要覆盖现有配置，完成后给出测试结果和日常使用说明
```

（原文ママ。中国語。意味: 「colbymchenry/codegraph を現在の Codex 環境に接続してほしい。実行依存と互換性を確認し、インストール・MCP 設定・コード索引の初期化まで完了させる。その後、コード検索・関数呼び出しの追跡・依存関係の問い合わせが使えるかを検証し、Codex から正常に呼べることを確認する。既存の設定は上書きしないこと。完了後にテスト結果と日常の使い方を出してほしい」）

## 使い方

1. 対象プロジェクトのディレクトリで Codex を起動する。
2. 上記プロンプトをそのまま貼る。
3. 返ってきたテスト結果（検索・呼び出し追跡・依存問い合わせの3種）を確認する。
4. 失敗した場合は「インストール済みか」「MCP が配線されているか」「`codegraph init` 済みか」を切り分ける（この3つは別工程で、README も別手順として扱っている）。

## 注意点

- プロンプト自体は無害（設定の上書き禁止と検証を指示している）。ただしエージェントに設定ファイルを触らせる以上、実行前に `~/.codex/` 等のバックアップを取る。
- CodeGraph の README は「MCP 配線（`codegraph install`）と索引構築（`codegraph init`）は別」と明記している。プロンプトでは両方を1回で頼んでいるため、片方だけ実行されて終わる可能性がある。結果の自己申告を鵜呑みにせず `codegraph` の状態を確認する。
- 残留コンテキストが増える方向のトレードオフがある（README 記載）。

## 変更履歴

- 2026-11-03: 初回登録（@goan999999 の投稿本文末尾より転記）
