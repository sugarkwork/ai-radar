---
repo: paperclipai/paperclip
name: paperclip
genre: agent-framework
url: https://github.com/paperclipai/paperclip
license: MIT
stars: 111168
language: TypeScript
created: 2026-03-02
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-04
source_post: https://x.com/thegreatest_sv/status/2117687388214272339
sources: []
flags: []
risk_notes: "複数の自律エージェントに権限と予算を与えて走らせるため、権限範囲・承認フロー・支出上限を先に設計すること。既定の認証なし構成で外部公開しない。"
forks: 18414
open_issues: 6587
commits_30d: 100
size_kb: 475670
archived: false
commits_90d: 100
commit_cadence: daily
fetched_at: "2026-11-05T04:40:08Z"
last_release: v2026.1023.0
last_release_at: 2026-10-24
---

# Paperclip

## 出来ること

- チームのAIエージェント群を**組織として管理する**セルフホスト型アプリ（Node.js サーバー＋React UI）。README の比喩は「OpenClaw が従業員なら、Paperclip は会社」。
- 動かし方は「目標 → チーム編成 → 承認して実行」:
  1. 目標を定義する（例:「AIノートアプリで月商100万ドル」）。
  2. CEO・CTO・エンジニア・デザイナー・マーケターなどの役割にエージェントを割り当てる。プロバイダは問わない。
  3. 戦略を承認し、予算を設定して走らせる。進捗とコストは1つのダッシュボードで追う。
- 見た目はタスクマネージャーだが、内部に org chart（組織図）・予算・ガバナンス・目標整合・エージェント間調整を持つ。
- エージェントごとにモデルとハーネスを選べる。対応アダプタは OpenClaw、Claude Code、Codex、Cursor（+ Cloud）、Gemini CLI、OpenCode、Pi、Hermes + Gateway。
- タスク・スキル・権限・履歴をチーム単位で一元管理する。

## 目的・背景

個人が複数のエージェントCLIを並行で走らせると、誰が何をして何にいくら使ったかが追えなくなる。Paperclip はそこに組織のメタファー（役割・承認・予算）を持ち込み、PR単位ではなく事業目標単位でエージェントを運用する。クラウド版（Paperclip Cloud）はwaitlist受付中。

## 依存関係

- Node.js 24.11 以上（導入は `npx`）。ソースから動かす場合は pnpm 9.15 以上。
- ローカルでは単一のNodeプロセスが**組み込みPostgres**とローカルファイルストレージを管理する。本番は自前のPostgres／Dockerを指定できる。
- エージェント側のCLI（Claude Code、Codex、Gemini CLI など）はPaperclipホスト上に必要。Dockerイメージには同梱されている。

## 実行条件

- セルフホスト前提。アカウント登録は不要。
- 遠隔から使う場合は認証モード＋プライベートネットワーク（Tailscale等）にバインドするか、Dockerで常駐させる。
- **open issue が6,588件**と非常に多く、機能追加の速度に対して未整理・重複が蓄積している状態。導入時は対象バージョンのissueを確認する。
- リポジトリサイズは約475MB（`size_kb` 475,670）。

## 最短手順

```bash
# Node.js 24.11+
npx paperclipai@latest onboard --yes
```

以降はブラウザでダッシュボードを開き、目標・チーム・予算を設定する。

## 変更履歴

- 2026-11-05: 初回登録（★111,166 / pushed 2026-11-05 / MIT / v2026.1023.0）
