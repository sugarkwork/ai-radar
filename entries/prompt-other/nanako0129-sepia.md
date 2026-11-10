---
repo: "Nanako0129/sepia"
name: "sepia"
genre: "prompt-other"
url: "https://github.com/Nanako0129/sepia"
stars: 3761
forks: 237
open_issues: 6
size_kb: 1021
language: "Python"
created: "2026-08-28"
updated: "2026-11-03"
archived: false
license: "MIT"
commits_30d: 67
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "StoryScopeの93.2%は論文の小説コーパスにおける人間とAIの二値分類のmacro-F1。sepiaによる改稿の品質改善、業務文書への有効性、ホスト別の動作、利用料金、最新リリースは未確認。今回の確認は公開資料の閲覧のみ。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Ryrenz/status/2117784513040257439"]
fetched_at: "2026-11-10T10:38:25Z"
---

# sepia — 小説の構成と業務文書の文体を見直すAgent Skill

## 出来ること

- 小説では物語構成から見直し、業務文書ではリリースノート、PRへの返信、障害の事後検証、技術記事などの用途別ルールを使う。
- 新規執筆のwrite、診断のみのreview、最小限の修正を行うrefactor、事実と意図を引き継いで全面改稿するrecreateを選べる。

## 目的・背景

- 小説の語句を直す前に物語構成を見直す設計。着想元のStoryScope論文では、物語特徴だけを使った人間とAIの二値分類でmacro-F1 93.2%を報告している。改稿品質の評価は未確認。[StoryScope](https://arxiv.org/abs/2604.03136)

## 依存関係

- Agent Skills対応ホストが必要。操作別のラッパーは中核スキルに依存するため、公式READMEではプラグイン一式の導入を案内している。[公式README](https://github.com/Nanako0129/sepia#operation-entries)

## 実行条件

- CodexとClaude Codeにはネイティブプラグインがある。READMEでの導入確認はインストール完了とスキル項目の表示が範囲。リポジトリのライセンスはMITで、ホストの利用料金は未確認。[公式README](https://github.com/Nanako0129/sepia#install)

## 最短手順

- CodexのCLIで `codex plugin marketplace add Nanako0129/sepia`、続けて `codex plugin add sepia@sepia` を実行する。[公式README](https://github.com/Nanako0129/sepia#codex)
- Codexセッションで `$sepia-review` を指定し、原稿と用途を渡して診断を依頼する。最小限の修正には `$sepia-refactor`、全面改稿には `$sepia-recreate` を使う。[操作一覧](https://github.com/Nanako0129/sepia#operation-entries)

## 変更履歴

- 2026-11-10: 初回登録
