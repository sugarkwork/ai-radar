---
name: "AI Second Brain"
genre: "coding-agent"
url: "https://github.com/charlie947/ai-second-brain"
flags: ["unverified"]
risk_notes: "README記載の機能・動作条件は独立検証していない。ChatGPTのエクスポートには1〜3日の待ち時間がかかる場合があると記載。"
repo: "charlie947/ai-second-brain"
stars: 229
forks: 45
open_issues: 0
size_kb: 523
language: "unknown"
created: "2026-04-17"
updated: "2026-10-24"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Bober_smart/status/2116978958121964030"]
fetched_at: "2026-11-10T14:14:46.869661+00:00"
---

# AI Second Brain

## 出来ること

- 3段階の手順を案内するClaude Code skill。ChatGPTとClaudeの履歴をタグ付きObsidian vaultに整理する「AI Brain」、raw/ と wiki/ を使って調査資料からwikiを構成する「Karpathy Wiki」、Gmail・NotebookLM・Granolaとの接続やiMessage Channels、/today・/ideas・/create のslash commandを用意する「Living Wiki」を扱う。段階を選んで進められる。

## 目的・背景

- READMEでは、Karpathyの個人wiki案、Alex FreedmanのAI履歴整理、Greg Isenbergのslash-command workflowをひとつのskillにまとめ、非技術者向けにセットアップを案内すると説明している。

## 依存関係

- Claude CodeとObsidianが必要。READMEではObsidianは無料と記載。Living Wikiのコネクター接続にはGmail、NotebookLM、Granolaが挙げられている。

## 実行条件

- READMEでは、macOSの権限付与やNotebookLMのブラウザログインなど、利用者の操作が必要な箇所では確認待ちになると説明している。Step 1と2はどのOSでも動作し、Step 3bのiMessage ChannelsはMacのみ。ChatGPTのエクスポート受領には1〜3日の待ち時間がかかる場合がある。

## 最短手順

- README記載の導入方法は、リポジトリを `~/.claude/skills/ai-second-brain` にcloneし、Claude Codeを開いて「Set up my AI second brain」と依頼すること。既存の同名フォルダーがあれば先にバックアップする。導入確認はClaude Codeで `/skills` を入力して一覧に `ai-second-brain` が表示されること。

## 変更履歴

- 2026-11-11: 初回登録
