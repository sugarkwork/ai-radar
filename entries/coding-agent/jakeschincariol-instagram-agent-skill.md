---
name: "The Instagram agent skill"
genre: "coding-agent"
url: "https://github.com/Jakeschincariol/instagram-agent-skill"
repo: "Jakeschincariol/instagram-agent-skill"
stars: 6800
forks: 1329
open_issues: 61
size_kb: 75
language: "Python"
created: "2026-09-13"
updated: "2026-09-13"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 2
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Ryrenz/status/2121629259655520446"]
fetched_at: "2026-11-16T21:44:55Z"
last_release: ""
last_release_at: ""
---

# The Instagram agent skill

## 出来ること

- READMEによると、Instagram向けの13個のClaudeスキルが、Reels用フックや台本、キャプション、カルーセル、ストーリー、プロフィール、投稿計画、コメント・返信・DM案などを作成します。ローカルのPythonツールとして、フックの採点、台本の時間見積もり、キャプションのチェック、テキストの整形・検出も説明されています。投稿は利用者の承認後に行う設計とREADMEに記載されています。

## 目的・背景

- Instagram向けコンテンツの作成と確認を支援するClaudeスキル群です。READMEは「These skills write. You post.」と説明し、投稿自体は利用者が行うとしています。

## 依存関係

- READMEは、実行する5つのツールについて「No dependencies, no network, nothing uploaded.」と記載しています。

## 実行条件

- READMEに記載されたツールの例は `python3 hookscore.py hooks.txt`、`python3 beats.py script.txt --target 30`、`python3 caption.py caption.txt --keywords "client contracts,freelance pricing"`、`python3 humanize.py draft.txt --report`、`python3 detect.py draft.txt` です。READMEはローカルのテキストを対象に実行すると説明しています。

## 最短手順

- READMEの手順は、リポジトリのスキルをClaude Codeの `~/.claude/skills/` にコピーする方法、またはClaudeにリポジトリURLとインストール指示を貼る方法です。利用時には `templates/voice.md` を設定する手順も案内されています。

## 変更履歴

- 2026-11-15: 初回登録
