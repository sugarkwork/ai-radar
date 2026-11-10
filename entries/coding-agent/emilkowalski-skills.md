---
repo: "emilkowalski/skills"
name: "Skills for Designers and Engineers"
genre: "coding-agent"
url: "https://github.com/emilkowalski/skills"
stars: 55592
forks: 3238
open_issues: 1
size_kb: 230
language: "Markdown"
created: "2026-03-16"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 8
commits_90d: 16
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "公開文書を確認した。インストールと呼び出しの動作、対応バージョン、導入による品質・性能の改善、エージェント側の料金は未確認。発見投稿のダッシュボードは技術的根拠に含めていない。READMEは公開raw URLで確認した。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117998992126591399"]
fetched_at: "2026-11-10T11:22:38Z"
---

# Emil KowalskiのUIアニメーション設計・レビュー用Agent Skills

## 出来ること

- `animate` はUIモーションの要否、目的、イージング、時間、変更するプロパティを順に判断して実装する。`review-animations` は既存の動きを著者の基準でレビューする。

## 目的・背景

- 著者がUI設計で使う判断基準をエージェントに渡す。例えば、操作頻度の高いUIではアニメーションを省くか短くし、表示時と終了時で動きの役割を分けて考える。改善効果の独立実測はない。

## 依存関係

- READMEの導入手順は `npx` を使う。スキルの利用には対応するコーディングエージェントが必要。対象UIの実装依存は選ぶスキルと既存プロジェクトに応じて変わる。

## 実行条件

- 対象のUIプロジェクトで、導入したスキルがエージェントから利用できる状態にする。リポジトリのライセンスはMIT。GitHubのReleases欄には確認時点で公開リリースが表示されていなかった。

## 最短手順

- 対象プロジェクトでREADME記載の `npx skills@latest add emilkowalski/skills` を使って導入する。
- Claude Codeで `animate` が利用可能になったら、`/animate トーストの表示と終了に短いトランジションを追加し、視差効果を減らす設定にも対応して` のように対象と条件を指定して呼び出す。

## 変更履歴

- 2026-11-10: 初回登録
