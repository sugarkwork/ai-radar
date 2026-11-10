---
repo: "github/spec-kit"
name: "Spec Kit"
genre: "coding-agent"
url: "https://github.com/github/spec-kit"
last_release: "v1.3.3"
flags: ["unverified"]
risk_notes: "公式資料で手順と対応環境を確認した。実行時の挙動、実装品質や手戻りへの効果、各エージェントの利用料金は未検証。最新リリースの表示は確認したが、公開日時の年とタイムゾーンを含む完全な値は未確認。"
stars: 149097
forks: 13388
open_issues: 227
size_kb: 22347
language: "Python"
created: "2025-08-21"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/AIExplorerTim/status/2117517393186689063"]
fetched_at: "2026-11-10T09:20:46+00:00"
---

# Spec Kit — AIコーディングエージェントで仕様から実装まで進めるツールキット

## 出来ること

- Specify CLIでプロジェクトを初期化し、エージェントのチャットから仕様、実装計画、作業タスクを順に作成して実装に進める。仕様の曖昧さの洗い出しや成果物間の整合性確認も公式手順に含まれる。

## 目的・背景

- 何を作るかとその理由を仕様として先に記述し、実装計画とタスクに落とし込む仕様駆動開発のためのツールキット。公式の手順では、各工程の成果物を確認してから次へ進む。品質向上や手戻り削減の効果は実測していない。

## 依存関係

- 公式の導入例では Python 3.11以上、uv、対応するAIコーディングエージェントが必要。以下の手順では GitHub Copilot を使用する。

## 実行条件

- Linux、macOS、Windowsに対応。CLIによる導入と初期化はターミナルで行い、初期化後のスキルはプロジェクトを開いたエージェントのチャットで呼び出す。リポジトリのライセンスはMIT。エージェント側の料金は未確認。

## 最短手順

- ターミナルで `uv tool install specify-cli`、`specify init my-project --integration copilot`、`cd my-project` を順に実行する。
- プロジェクトを開いたCopilotのチャットで、プロジェクトの原則を `/speckit-constitution` で一度定義する。機能ごとに `/speckit-specify` に要件を渡し、`/speckit-plan`、`/speckit-tasks`、`/speckit-implement` の順に呼び出す。各工程の出力を確認し、最後に `/speckit-converge` で仕様・計画・タスクに対する実装の残作業を確認する。

## 変更履歴

- 2026-11-10: 初回登録
