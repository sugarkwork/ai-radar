---
repo: "Yeachan-Heo/oh-my-claudecode"
name: "oh-my-claudecode"
genre: "agent-framework"
url: "https://github.com/Yeachan-Heo/oh-my-claudecode"
stars: 40729
forks: 3637
open_issues: 16
size_kb: 163022
language: "TypeScript"
created: "2026-01-09"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v5.8.4"
last_release_at: ""
flags: ["unverified"]
risk_notes: "導入と実行は未検証。単一エージェントと比較した品質・所要時間・モデル利用料の実測は確認していない。最新リリースのタグは確認したが、公開日時のタイムゾーンは確認できなかった。30日・90日のコミット数はいずれも取得上限に達しており、100件以上を示す。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2114967848775041508"]
fetched_at: "2026-11-10T11:46:29Z"
---

# oh-my-claudecodeでClaude Codeの開発タスクをチームに分担する

## 出来ること

- Claude Codeのセッション内で複数のエージェントに開発タスクを分担させる。開発元は、計画、要件整理、実行、検証、修正を段階的に進める構成を説明している。

## 目的・背景

- 複数の作業者を使う開発タスクを、Claude Codeのセッション内からまとめて進めるためのプラグイン。処理の流れは公式READMEに記載されている。

## 依存関係

- Claude Code CLIと、Claude Pro・Maxの契約またはAnthropic APIキーが必要。リポジトリはMITライセンスで、Claudeの利用には契約またはAPIの利用条件が適用される。

## 実行条件

- セッション内のTeamモードではClaude Codeのネイティブチームを有効化する。端末から別プロセスのワーカーを起動する `omc team` にはtmuxが必要で、READMEはWindows向けにpsmuxを案内している。

## 最短手順

- Claude Code内で `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode` と `/plugin install oh-my-claudecode` を順に入力し、`/omc-setup` を実行する。
- `~/.claude/settings.json` の `env` で `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` を `1` に設定する。
- Claude Codeセッションで `/team 3:executor` に続けて、型エラーの修正などの依頼を入力し、AIのチームに作業を渡す。

## 変更履歴

- 2026-11-10: 初回登録
