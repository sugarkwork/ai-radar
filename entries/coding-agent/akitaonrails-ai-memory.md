---
name: "ai-memory"
genre: "coding-agent"
url: "https://github.com/akitaonrails/ai-memory"
repo: "akitaonrails/ai-memory"
license: "MIT"
stars: 15992
language: "Rust"
created: "2026-05-21"
updated: "2026-11-15"
forks: 1199
open_issues: 55
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 54713
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/ruyi3699/status/2119061557858464140"]
fetched_at: "2026-11-16T14:11:28.066661+00:00"
---

# ai-memory

## 出来ること

- 複数のコーディングエージェント、プロジェクト、マシンで共有する長期メモリを提供する。READMEによると、ライフサイクルフックで観測内容を取り込み、セッション終了時にMarkdownページへまとめ、次のセッションに要約を渡す。検索は全文、エンティティ、リンクを使い、ベクトル検索は任意。引き継ぎには担当者を持つ型付きプロトコルを使う。

## 目的・背景

- READMEでは、エージェントごと・マシンごとに分かれたメモや、ツール切替時に引き継がれない作業状況を課題として挙げ、複数エージェントで共有可能なメモリを目的としている。情報源は通常のMarkdownファイルを置くGit管理のWikiで、データベースは再構築可能な派生インデックスとして説明されている。

## 依存関係

- READMEは既定の取り込み・検索・引き継ぎがAPIキーなしで動作し、LLM呼び出しを使わないと説明している。LLMを使う背景処理や任意のベクトル検索も記載されているが、このREADME抜粋ではそれらの具体的な依存パッケージやプロバイダー要件は確認できない。

## 実行条件

- READMEのバッジにはRust 1.95+とある。Linux、macOS、WSL2上のWindowsをサポートし、ネイティブWindowsはExperimentalと記載。任意の管理コンソールは`management-ui`機能でビルドし、HTTP transportと`--enable-management-ui`を指定して起動する。

## 最短手順

- READMEは`ai-memory run`によるエージェント起動例として、`ai-memory run codex`を示している。インストールやサーバー起動の完全な手順は添付README抜粋では確認できない。

## 変更履歴

- 2026-11-16: 初回登録
