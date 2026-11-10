---
repo: "breferrari/obsidian-mind"
name: "Obsidian Mind"
genre: "coding-agent"
url: "https://github.com/breferrari/obsidian-mind"
license: "MIT"
stars: 5525
language: "TypeScript"
created: "2026-02-28"
updated: "2026-10-17"
forks: 610
open_issues: 16
commits_30d: 36
commit_cadence: "daily"
commits_90d: 100
size_kb: 7059
archived: false
last_release: "v10.0.0"
last_release_at: "2026-10-12"
flags: ["unverified"]
risk_notes: "READMEの例は作者による記載。振り分けの精度、検索品質、クライアント間の機能差、音声入力の動作は独立に検証していない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2115413335638470709"]
fetched_at: "2026-11-10T12:13:18Z"
---

# Obsidian Mindで会議メモを整理し、次のAIセッションに引き継ぐ

## 出来ること

- `/om-dump` に会議メモを渡す。READMEの例では、人物ノート、1on1の記録、決定記録、実績メモ、案件タスクに内容を振り分ける。
- `/om-standup` で進行中の案件、未完了タスク、最近のGit変更を読み込み、状況をまとめる。

## 目的・背景

- セッションをまたぐ情報をObsidianのVaultに保存する。フックが分類のヒントや文脈を渡し、エージェントがノートの記述とリンク付けを担う。

## 依存関係

- Obsidian 1.12以上、フック用のNode.js 22以上のLTS、Git、Claude Code・Codex CLI・Gemini CLIのいずれか。意味検索用のQMDは任意。

## 実行条件

- 公式READMEではClaude Codeをフルサポートとし、Codex CLIとGemini CLIも同じVaultを使えるとしている。Codexでフックを動かすにはフォルダーを信頼し、各フックを承認する。テンプレートはMITライセンス。

## 最短手順

- `git clone https://github.com/breferrari/obsidian-mind.git` で取得し、`obsidian-mind` をObsidianのVaultとして開く。設定の「一般」でObsidian CLIを有効にし、`brain/North Star.md` に目標を書く。
- Vaultのディレクトリで `claude` または `gemini` を起動し、会話欄で `/om-dump` にメモを渡す。次のセッションで `/om-standup` を呼ぶ。Codexでは `codex` を起動し、`om-dump` や `om-standup` と入力する。

## 変更履歴

- 2026-11-10: 初回登録
