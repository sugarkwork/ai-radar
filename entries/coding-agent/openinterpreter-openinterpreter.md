---
name: "Open Interpreter"
genre: "coding-agent"
url: "https://github.com/openinterpreter/openinterpreter"
repo: "openinterpreter/openinterpreter"
stars: 68864
forks: 5943
open_issues: 39
size_kb: 285189
language: "Rust"
created: "2023-07-14"
updated: "2026-11-11"
archived: false
license: "Apache-2.0"
commits_30d: 11
commits_90d: 100
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118325722850697573"]
fetched_at: "2026-11-11T19:07:28.427910+00:00"
---

# Open Interpreter

## 出来ること

- 低コストモデル向けのコーディングエージェント。READMEでは、複数のエージェントハーネスの切り替え、ACPクライアントからの起動、Codex exec protocolとの互換性、MCP・skills・hooks・permissions・AGENTS.mdのサポートを説明している。コマンドはmacOS・Linux・Windowsのネイティブサンドボックス内で実行すると記載されている。出典: https://github.com/openinterpreter/openinterpreter

## 目的・背景

- READMEは、低コストモデルで良好な性能を得るエージェントハーネスのエミュレーションを目的として説明している。また、共有規格やディレクトリを優先し、ユーザー作成データを読みやすい形式で保つポータビリティ方針を示している。出典: https://github.com/openinterpreter/openinterpreter

## 依存関係

- READMEは、Rustで再実装したバージョンであると説明している。選択したプロバイダーやモデルの利用には、プロバイダー設定が関係する。詳細は公式プロバイダーガイドを参照。出典: https://github.com/openinterpreter/openinterpreter

## 実行条件

- README記載のインストール対象OSはmacOS、Linux、Windows。プロバイダーやモデルの利用条件は選択内容により異なり、READMEはプロバイダーガイドを案内している。

## 最短手順

- README記載の手順: macOS・Linuxでは `curl -fsSL https://www.openinterpreter.com/install | sh`、Windowsでは `irm https://www.openinterpreter.com/install.ps1 | iex` を実行し、その後ターミナルで `i` または `interpreter` を入力する。出典: https://github.com/openinterpreter/openinterpreter

## 変更履歴

- 2026-11-11: 初回登録
