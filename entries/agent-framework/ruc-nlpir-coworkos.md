---
repo: RUC-NLPIR/CoworkOS
name: CoworkOS
genre: agent-framework
url: https://github.com/RUC-NLPIR/CoworkOS
author: RUC-NLPIR（中国人民大学 NLP 研究室）
license: MIT
stars: 98
language: JavaScript
created: 2026-11-03
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/wildmindai/status/2117717765696241875
sources:
  - https://coworkos-ai.github.io/
  - https://arxiv.org/abs/2611.03178
forks: 10
open_issues: 2
commits_30d: 17
commits_90d: 17
commit_cadence: weekly
last_release: v0.1.3
size_kb: 10416
archived: false
fetched_at: "2026-11-04T04:59:35Z"
last_release_at: 2026-11-03
---

# CoworkOS

## 出来ること

- **長期・人手を挟む作業のための cowork ハーネス**。人が AI エージェントと一緒に、計画から検証済みの成果物まで持っていく。対象はコード・調査・文書・プレゼン・CAD・Blender・科学計算のワークフロー。
- **3層ランタイム**: Main Agent が計画を立てて委任し結果を評価、Coordinator Runtime がサブタスクを配車してライフサイクルを管理、任意の Subagents が割り当てられた作業を実行する。戦略はモデルが選び、調整・フィードバック・継続性はランタイムが持つ。
- **同じ成果物を人とエージェントが共有**: CLI・検索・ファイル・MCP が文書エディタ、プレゼン、CAD、Blender と繋がり、同じ文書・モデル・シーンを双方が編集できる。階層ワークスペース、セマンティックメモリ、統合前レビューのためのリビジョン管理された候補変更を持つ。
- **長時間ジョブ**: 状態とログを保持し、待機や中断のあとでも作業を再開できる。複雑な一回限りの納品と、数日単位の監視・判断・復旧の両方を想定。
- **RSI（再帰的自己改善）ループ**: 失敗を分析 → データ改善 → 学習 → 検証 → 反復、を状態と証跡を保ったまま回す。論文では5ラウンドで Qwen3.6-35B-A3B の8ベンチマーク平均が 33.19 → 42.95 に上がったと報告。
- デスクトップアプリ（macOS、Apple Silicon）と CLI（macOS / Linux）、npm パッケージ `coworkos-app`、デモとプロジェクトページを提供。

## 目的・背景

中国人民大学 NLP 研究室（RUC-NLPIR）による研究成果の公開実装。論文 *CoworkOS: Scaling Agent Coworkers for Real-world Automation*（arXiv:2611.03178）に対応する。単発のチャットではなく、人が途中で確認・指示変更できることを前提に、調整役をランタイム側へ寄せた設計。2026-11-03 公開、同日時点で 98 star、v0.1.3。

## 依存関係

- Node.js **22.19.0 以上**
- デスクトップ版: macOS 14+（Apple Silicon）
- CLI 版: macOS / Linux
- モデル: `coworkos init` でモデルサービスの URL・モデル ID・API キーを設定（OpenAI 互換の接続形式。`docs/en/configuration.md`）
- 文書・CAD・Blender 連携を使う場合は各アプリ側の環境が必要

## 実行条件

- モデルは自前の API キーで接続する。`coworkos doctor --test-connection` は実際にリクエストを送るためクォータを消費する。
- データと実行記録はローカルに置かれ、ワークスペース・メモリ・実行履歴を自分で管理する前提。
- 公開直後の v0.1.x。破壊的変更や未整備の導線があり得る。
- ライセンスは MIT（第三者コンポーネントに例外あり）。
- README のベンチマーク数値は論文側の報告で、独立再現は未確認。

## 最短手順

```bash
# デスクトップ（macOS / Apple Silicon）
npx coworkos-app@latest desktop install

# CLI のみ
npm install -g coworkos-app
cd /path/to/your/project
coworkos init
coworkos doctor --test-connection
coworkos
# 再開するとき
coworkos --continue
```

## 変更履歴

- 2026-11-04: 初回登録（v0.1.3）
