---
repo: "codewhale-hq/Codewhale"
name: "Codewhale"
genre: "coding-agent"
url: "https://github.com/codewhale-hq/Codewhale"
last_release: "v0.10.2"
flags: ["unverified"]
risk_notes: ["開発元のデモはスクリプト化したテストモデルを使用。実タスクでの成功率、モデル間の性能差、OS別の動作は未検証。", "既定の編集承認設定は公式文書間で記述が異なるため、利用する版とセッションの権限を確認する。リリースのタイムゾーン付き公開日時は未確認。"]
stars: 41173
forks: 3569
open_issues: 71
size_kb: 354208
language: "Rust"
created: "2026-01-19"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2114967848775041508"]
fetched_at: "2026-11-10T11:45:26+00:00"
---

# Codewhale｜モデルを選べるターミナル向けコーディングエージェント

## 出来ること

- プロジェクトを読み取り、指示に沿ってファイルを編集し、テストなどのコマンドを実行する。対話操作に加え、CLIで単発タスクを渡せる。

## 目的・背景

- Rust製のエージェントで、ホスト型APIとローカル推論を切り替えられる。開発元はテストモデルを用いたデモで編集とテストの実行を報告している。

## 依存関係

- ホスト型では選択したプロバイダーのAPIキーを設定する。ローカルではOllamaなどの推論環境と対応モデルを用意する。

## 実行条件

- 公式READMEはLinux・macOS・Windows向けのビルド済みバイナリを案内している。本体はMITライセンスで、ホスト型APIの料金と利用条件は選択したプロバイダーに従う。

## 最短手順

- 公式リリースから環境に合う版を導入する。作業用リポジトリのルートで `codewhale` を起動し、`/provider` で接続先とモデルを選ぶ。
- 別のAIエージェントからは、シェルツールで同じ作業ディレクトリを指定し、`codewhale exec 'プロジェクト構成とテストの入口を説明して'` を呼び出して結果を受け取る。

## 変更履歴

- 2026-11-10: 初回登録
