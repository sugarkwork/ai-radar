---
name: "AI Job Search"
genre: "coding-agent"
url: "https://github.com/ai-job-search-dev/ai-job-search"
repo: "ai-job-search-dev/ai-job-search"
license: "MIT"
stars: 72085
language: "Python"
created: "2026-03-18"
updated: "2026-11-16"
forks: 23191
open_issues: 71
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 5840
archived: false
flags: ["unverified"]
risk_notes: "求人ポータル検索スキルはデンマーク市場向け。個人情報を含むプロフィールファイルの保存先と、公開forkではそのファイルが追跡対象になる点に注意。効果の数値は作者の利用報告であり、独立検証ではない。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/bkdgiffug/status/2119015504304107839"]
fetched_at: "2026-11-16T21:42:26Z"
last_release: "v2.0.0"
last_release_at: "2026-11-16"
---

# AI Job Search

## 出来ること

- Claude Codeを使った求人応募ワークフロー。README記載の6コマンドで、プロフィール作成（/setup）、求人検索（/scrape）、候補の評価・絞り込み（/rank）、履歴書とカバーレターの作成（/apply）、面接準備（/interview）、応募結果の記録（/outcome）を行う。

## 目的・背景

- 作者は自身の求職活動でこの仕組みを使い、69件の応募、20件の初回面接、1件の採用を報告している。これは作者の経験談で、独立した効果検証ではない。

## 依存関係

- README記載の主な依存ツールはClaude Code、Python 3.10以上、Bun、lualatexとxelatexを含むLaTeX環境。応募書類のATS解析チェックにはpypdfが任意で必要。Claude Codeは有料サブスクリプションまたはAnthropic APIクレジットが必要と記載されている。

## 実行条件

- READMEはClaude Code CLIでの利用を案内。求人ポータル検索スキルはデンマーク市場向けだが、プロフィール評価などの中核ワークフローは言語・国を問わないと説明している。別のエージェントで使う場合は一部の検索スキルが利用でき、全体ワークフローはコミュニティforkで対応されている。

## 最短手順

- READMEのQuick startは、リポジトリを自分用に複製し、`python3 tools/install_portal_clis.py`（Windowsは`python tools\install_portal_clis.py`）でポータルCLIをセットアップ、Claude Codeを起動して`/setup`、続けて`/scrape`を実行する手順。インストーラーはbun installを`--ignore-scripts`で実行し、特定のライフサイクルスクリプト等を検出したCLIはスキップすると説明している。

## 変更履歴

- 2026-11-16: 初回登録
