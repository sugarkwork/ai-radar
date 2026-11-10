---
repo: "alirezarezvani/claude-skills"
name: "Claude Code Skills & Plugins"
genre: "other"
url: "https://github.com/alirezarezvani/claude-skills"
stars: 29573
forks: 4095
open_issues: 0
size_kb: 24392
language: "Python"
created: "2025-10-19"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v2.14.10"
last_release_at: "2026-11-10"
flags: ["unverified"]
risk_notes: "メンテナーの検証はClaude Codeでのスキル読み込みを対象とする。生成物の品質や作業時間への効果、CodexやCursorでの挙動、個別スクリプトの実行条件は独立に検証していない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2114967848775041508"]
fetched_at: "2026-11-10T11:47:50+00:00"
---

# Claude Code Skills & Plugins — コーディングエージェント向けの作業手順集

## 出来ること

- コードレビュー、テスト設計、プロダクト企画などの作業手順を、対応するエージェントで再利用できる。

## 目的・背景

- 各スキルはSKILL.mdに作業指示をまとめ、必要に応じてスクリプトや参照資料を添える。
- 公開テストでは、Claude Codeで389件中152件がすべての対象プロンプトで読み込まれ、無関係なプロンプトでは読み込まれなかったとメンテナーが報告している。

## 依存関係

- 利用には対応エージェントが必要。READMEによると、同梱Pythonツールは標準ライブラリで動作し、一部の文書抽出では外部パーサーを任意で利用できる。

## 実行条件

- スキルは利用するエージェントが読み込む場所に配置する。同梱Pythonスクリプトを使う場合はPython環境が必要。リポジトリはMITライセンスで、利用するエージェントの契約・料金は各提供元の条件に従う。
- コミット件数は30日・90日とも取得上限の100件に達しており、それぞれ100件以上を示す。

## 最短手順

- 使いたいスキルのSKILL.mdと同梱ファイルを確認し、フォルダ単位でCodexの ~/.codex/skills/ に配置する。
- Codexで、たとえば導入したコードレビュースキルの名前を指定し、対象の差分をレビューしてもらう。

## 変更履歴

- 2026-11-10: 初回登録
