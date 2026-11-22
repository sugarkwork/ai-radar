---
name: "Hill Climb"
genre: "coding-agent"
url: "https://github.com/Bil0000/Hill-Climb"
repo: "Bil0000/Hill-Climb"
license: "MIT"
stars: 140
language: "Python"
created: "2026-11-02"
updated: "2026-11-12"
forks: 5
open_issues: 3
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 8
size_kb: 82
archived: false
flags: ["unverified"]
risk_notes: "READMEの機能説明と試行例は配布者の記述であり、独立した実機検証ではありません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/GitTrend0x/status/2122653626900332544"]
fetched_at: "2026-11-17T23:27:49.107122+00:00"
---

# Hill Climb

## 出来ること

- READMEによると、エージェントが小さな変更を行うたびに指定コマンドでスコアを測定し、テスト・型検査・lintなどのガードも実行します。スコアが改善し、ガードがすべて通れば変更を個別コミットし、それ以外は作業ツリーをリセットします。チェック対象ファイルをロックして変更を拒否する機能、進捗ログ、複数リポジトリへの対応も説明されています。

## 目的・背景

- READMEは、エージェントの自己申告だけに頼ると、テストの期待値変更、既存機能の破損、同じ案の再試行、変更内容の追跡困難が生じうるという課題を挙げています。指定したチェック結果をスコアとして扱い、改善の確認と不採用変更の取り消しを自動化する目的です。

## 依存関係

- READMEには外部パッケージ依存なしと記載されています。

## 実行条件

- READMEにはPython 3.9以上とgitが必要と記載されています。サーバーやアカウントは不要との説明です。

## 最短手順

- READMEのCodex向け手順は、リポジトリをcloneし、`skills/hill-climb`を`~/.codex/skills/`へコピーして、プロンプトでスキル名を指定する方法です。小さな目標は直ちに開始し、大きな目標では1画面の計画を提示して開始指示を待つと説明されています。

## 変更履歴

- 2026-11-22: 初回登録
