---
repo: "aa1143/NamiAgent"
name: "NamiAgent"
genre: "other"
url: "https://github.com/aa1143/NamiAgent"
stars: 483
forks: 53
open_issues: 1
size_kb: 2554
language: "Python"
created: "2026-10-30"
updated: "2026-10-30"
archived: false
license: "MIT"
commits_30d: 20
commits_90d: 20
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "最新リリース、テストの成功、デモと実モデルの動作、権限機構の実効性、モデルAPIの料金は未確認。著者は、権限機構で意図的な攻撃を防げないと明記している。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Ryrenz/status/2117921052726538618"]
fetched_at: "2026-11-10T10:58:16+00:00"
---

# NamiAgent｜最小ループから学ぶAIエージェントのPython教材

## 出来ること

- 第1〜11課のコードを比較し、ツール、権限、コンテキスト管理、Skills、MCP、子エージェント、計画、記憶を段階的に学べる。第12〜18課は既存エージェントの解説記事。
- READMEによると、ローカルWeb画面ではツール呼び出しと結果、モデルに送ったコンテキスト、概算トークン数を確認できる。

## 目的・背景

- モデルを呼び、ツールを実行し、結果をコンテキストに戻して再びモデルを呼ぶループを学ぶ。著者は本番向けフレームワークではなく、仕組みを理解するための教材と位置づけている。

## 依存関係

- Python 3.10以上。READMEが挙げる実行時の外部パッケージはopenaiのみ。テスト手順ではpytestを使用する。

## 実行条件

- デモと第11課の疑似モデルによるテストはAPIキー不要とREADMEに記載。実モデルを使う場合はAPI_KEYを設定する。既定はDeepSeekで、BASE_URLとMODELでOpenAI互換の接続先を変更できる。
- 専用の作業ディレクトリを使う。コードはMIT、docs/の記事はCC BY-NC 4.0。

## 最短手順

- リポジトリ直下で `pip install -r requirements.txt` を実行し、`python web/app.py --demo` を起動して `http://localhost:8765` を開く。
- AIからMCPツールを呼ぶ流れは第8課で学べる。第8課の形式に沿って `~/.nami-agent/mcp.json` にstdio MCPサーバーを設定し、実モデルに接続したNamiAgentにそのツールを使うタスクを入力する。

## 変更履歴

- 2026-11-10: 初回登録
