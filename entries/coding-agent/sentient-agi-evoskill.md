---
name: "EvoSkill"
genre: "coding-agent"
url: "https://github.com/sentient-agi/EvoSkill"
repo: "sentient-agi/EvoSkill"
stars: 1298
forks: 134
open_issues: 21
size_kb: 8819
language: "Python"
created: "2026-03-04"
updated: "2026-10-26"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/slatro_eth/status/2120861866712838495"]
fetched_at: "2026-11-12T14:18:16.262396+00:00"
---

# EvoSkill

## 出来ること

- ベンチマーク上で複数のスキルやプロンプトの変更案を評価し、新しいエージェントプログラムを作成する。READMEではClaude Code、OpenCode、OpenHands、Goose、Codex CLI、Harborへの対応を挙げている。README: https://github.com/sentient-agi/EvoSkill

## 目的・背景

- 単一プロンプトをその場で改訂する方式から、スキルとプロンプトを複数まとめて変更し、保留データで評価しながらエージェントを進化させることを目指す。これはREADMEに記載された設計説明であり、独立した実測結果を示すものではない。README: https://github.com/sentient-agi/EvoSkill

## 依存関係

- Python 3.12以上とuv（推奨）またはpipが必要。利用するエージェントのCLIは別途導入する。HarborはPythonパッケージに含まれる。README: https://github.com/sentient-agi/EvoSkill

## 実行条件

- CSVデータセットまたはHarborデータセットを用意し、利用するエージェント実行環境と認証情報を設定する。実行モードはLocal、Docker、Daytonaから選択できる。OpenCodeはCLI v1.4.0以上、GooseはCLI v1.25.0以上が必要とREADMEに記載されている。README: https://github.com/sentient-agi/EvoSkill

## 最短手順

- Python 3.12以上とuvを用意し、リポジトリで `uv sync` を実行する。対象のエージェントCLIと認証情報を設定した後、対象のGitリポジトリ内で `evoskill init` を実行し、生成された `.evoskill/config.toml` と `.evoskill/task.md` を設定して `evoskill run` を実行する。README: https://github.com/sentient-agi/EvoSkill

## 変更履歴

- 2026-11-12: 初回登録
