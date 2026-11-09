---
type: "repo"
name: "HKUDS/AgentPilot"
genre: "agent-framework"
url: "https://github.com/HKUDS/AgentPilot"
author: "HKUDS"
source_post: "https://x.com/huang_chao4969/status/2118698314720006490"
sources: ["https://x.com/huang_chao4969/status/2118698314720006490?a=4nOkDTjr8JjvK5XRTds&s=46", "https://x.com/huang_chao4969/status/2118698314720006490", "https://api.github.com/repos/HKUDS/AgentPilot", "https://github.com/HKUDS/AgentPilot/blob/HEAD/README.md", "https://api.github.com/repos/HKUDS/AgentPilot/releases", "https://github.com/HKUDS/AgentPilot"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "Terminal-Bench 63.8%・AIME改善はREADMEの自己報告。9B戦略モデルの重みの取得方法は原チェックで確認できていない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "HKUDS/AgentPilot"
license: "MIT"
language: "Python"
created: "2026-03-24"
updated: "2026-11-06"
stars: 7961
forks: 938
open_issues: 55
commits_30d: 3
commits_90d: 7
commit_cadence: "monthly"
size_kb: 113883
archived: false
fetched_at: "2026-11-09T00:30:28.671426+00:00"
---

# HKUDS/AgentPilot

## 出来ること

小型の戦略モデルが計画を出し、Codex・Claude Code・Cursor・Hermes等の実行側アダプタにつなぐAgentPilot。

## 目的・背景

紹介対象は `HKUDS/AgentPilot`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:28.671426+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Python 3.12+、uv、対象エージェントと外部APIキー。評価にはTerminal-BenchやAIME等のデータが必要。

## 実行条件

Terminal-Bench 63.8%・AIME改善はREADMEの自己報告。9B戦略モデルの重みの取得方法は原チェックで確認できていない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/HKUDS/AgentPilot#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @huang_chao4969: https://x.com/huang_chao4969/status/2118698314720006490
- 対象資料: https://github.com/HKUDS/AgentPilot
- 参照: https://api.github.com/repos/HKUDS/AgentPilot
- 参照: https://github.com/HKUDS/AgentPilot/blob/HEAD/README.md
- 参照: https://api.github.com/repos/HKUDS/AgentPilot/releases

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
