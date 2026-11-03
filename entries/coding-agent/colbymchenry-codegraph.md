---
repo: "colbymchenry/codegraph"
name: "CodeGraph"
genre: "coding-agent"
url: "https://github.com/colbymchenry/codegraph"
license: "MIT"
stars: 76377
language: "TypeScript"
created: "2026-01-18"
updated: 2026-11-01
added: "2026-11-03"
flags: []
risk_notes: ""
source_post: "https://x.com/goan999999/status/2117462867050144107"
sources:
  - "https://x.com/goan999999/status/2117462867050144107"
  - "https://colbymchenry.github.io/codegraph/"
forks: 5078
open_issues: 236
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 48358
archived: false
fetched_at: "2026-11-03T15:42:24Z"
last_release: v1.6.2
last_release_at: 2026-10-03
---

# CodeGraph

## 出来ること

- コードベースを「事前索引化した知識グラフ」にして、MCP サーバー経由でエージェントに渡す。シンボル・呼び出しエッジ・依存関係を1回の問い合わせで返すため、エージェントはファイルを総当たりで読まなくて済む。
- ファイル変更を監視してグラフを自動更新（`codegraph init` 後に再実行は不要と README が明記）。
- 20 以上の言語をネイティブ Rust カーネルで解析（TypeScript / JavaScript / Python / Go / Rust / Java / C# / PHP / Ruby / C / C++ / Swift / Kotlin / Scala / Dart / Lua / Solidity / Vue / Svelte など）。プリビルドの無い環境や構文エラーはファイル単位でフォールバック。
- CLI: `codegraph node <symbol>`（定義と参照元）、`codegraph affected`（変更の影響範囲をテストに引き当てる）、`codegraph upgrade` / `uninstall`。
- 対応エージェント: Claude Code、Cursor、Codex CLI、opencode、**Hermes Agent**、Gemini CLI、Antigravity、Kiro、GitHub Copilot、Windsurf、Qwen Code ほか（`codegraph install` が自動配線）。

## 目的・背景

2026-01 公開、7.6万 star。ポストの数値（トークン62%減・コスト44%減・ツール呼び出し88%減・時間53%短縮）は README のベンチマーク表と一致する（7リポジトリ、Claude Opus 4.8、各4回の中央値、CLI を両アームで封じた harness）。

**ただし README 自身が同時に「セッション終了時の残留コンテキストは約80%多い（VS Code で 67k vs 18k トークン）」と明記している**。処理トークンは減るが、コンテキスト窓は圧迫されるという両面がある。

## 依存関係

- スタンドアロンのインストーラは Node.js 不要（OS ごとのビルドを取得）。
- npm 経由なら `npm i -g @colbymchenry/codegraph`（任意の Node バージョンで可）。
- ライブラリとして API から使う場合のみ Node 22.5 以上（組み込み `node:sqlite` を使うため）。

## 実行条件

- 公式インストーラは `curl … | sh` 形式。中身を確認したい場合は npm 版を使う。
- プロジェクトごとに `.codegraph/` を作る（`codegraph init`）。索引はローカル保存で、外部送信はしないと README に記載。
- 小規模リポジトリでは建図のオーバーヘッドが勝つ場合がある（README も「探索に手間がかかる問いほど効く」と述べている）。
- 破壊的操作はしないが、`codegraph install` は各エージェントの MCP 設定を書き換える。既存設定のバックアップは取っておくこと。

## 最短手順

```bash
# macOS / Linux（Node 不要）
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
# もしくは npm
npm i -g @colbymchenry/codegraph

codegraph install     # 使っているエージェントに MCP を配線（新しい端末で実行）
cd your-project
codegraph init        # .codegraph/ を作り、グラフを構築
```

## 変更履歴

- 2026-11-03: 初回登録（star 76,373 / pushed 2026-11-01 / MIT / 20+言語）
