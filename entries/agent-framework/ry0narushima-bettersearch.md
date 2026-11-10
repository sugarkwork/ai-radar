---
repo: "ry0narushima/bettersearch"
name: "BetterSearch"
genre: agent-framework
url: "https://github.com/ry0narushima/bettersearch"
license: "MIT"
stars: 40
language: "Python"
created: "2026-10-18"
updated: "2026-10-18"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 4
open_issues: 0
commits_30d: 10
commits_90d: 10
commit_cadence: "weekly"
size_kb: 960
archived: false
fetched_at: "2026-11-09T21:34:48Z"
last_release: ""
last_release_at: ""
---

# BetterSearch

## 出来ること

- DeepSeek が公開した Search API を使い、エージェントに「調べて引用付きで答える」動作を足すスキル。Claude Code / Codex / Cursor / Gemini CLI / OpenCode / Hermes で動く。
- **Quick**（既定）: 2〜4本の鋭いクエリ（`lang:` `after:` `site:` を活用）→ 上位1〜3ページ取得 → `[1] [2]` の引用付きで回答。
- **Advanced**（「deep research」と言うか大きな問いのとき）: 8〜20クエリ・各最大50件 → 重複排除と権威順ランク → 上位25件取得 → サブ質問ごとに researcher を並列実行 → fact-checker（引用が原典に実在するか照合）→ reviewer（抜け・古い情報を指摘し追撃1回）→ レポート生成。
- レポートは単一の自己完結 HTML。CDN も JS 依存もなくオフラインで開け、ダークモード対応。主張ごとに **verified / single source / conflicting** のタグが付き、引用は出典カードへリンクする。
- サブエージェント機能のないエージェントでは、同じ役割を順番に実行して同じ出力形式にする。

## 目的・背景

検索 API そのものは安いが、雑な1クエリでは雑な答えしか返らない（英語で検索したのに上位5件のうち2件が中国語だった、と README にある）。API の「外側」—クエリ設計、並列調査、ファクトチェック、レポート整形—をスキルとして固めたもの。API キーはチャットを通さず、専用スクリプトが `~/.config/deepseek-research/`（chmod 600）に保存する。

## 依存関係

- Python 3。
- DeepSeek の API キー（`python3 ~/.claude/skills/bettersearch/scripts/dsr.py setup` で設定。`DEEPSEEK_API_KEY` でも可）。

## 実行条件

- README 記載の料金: DeepSeek Search $0.75 / 1,000コール、Fetch $0.75 / 1,000コール（比較として Brave $5、Exa $4〜）。
- インストールは `install.sh` を `curl` で流す方式。中身を確認してから実行したい場合は、リポジトリのスクリプトを直接読む。
- 高度モードは1回の質問で数十回の検索・取得を行うため、その分コストがかかる。

## 最短手順

```bash
curl -fsSL https://raw.githubusercontent.com/ry0narushima/bettersearch/main/install.sh | bash
python3 ~/.claude/skills/bettersearch/scripts/dsr.py setup
```

## 変更履歴

- 2026-11-03: 初回登録（star 40 / pushed 2026-10-18 / MIT）
