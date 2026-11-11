---
name: "karpathy-llm-wiki"
genre: "agent-framework"
url: "https://github.com/Astro-Han/karpathy-llm-wiki"
repo: "Astro-Han/karpathy-llm-wiki"
flags: ["unverified"]
risk_notes: "READMEに記載された利用統計や運用実績はREADME上の説明であり、独立検証していない。インストール方法としてnpx add-skillが記載されているが、実行条件や追加依存関係はREADMEだけでは確認できない。"
stars: 2718
forks: 314
open_issues: 11
size_kb: 372
language: "Python"
created: "2026-04-05"
updated: "2026-07-23"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Bober_smart/status/2116978958121964030"]
fetched_at: "2026-11-10T14:14:31.536519+00:00"
---

# karpathy-llm-wiki

## 出来ること

- LLMエージェントがソースをraw/に取り込み、持続的な知識ページをwiki/に作成・更新する。wiki内を検索してページへの引用付きで回答し、索引・リンク・wikiの状態をlintする。

## 目的・背景

- 質問のたびに元資料を再検索する代わりに、取り込んだ資料を構造化されたMarkdownページへまとめ、知識や相互参照を蓄積するワークフローを提供する。READMEではRAGとの違いを、検索時に合成する方式と取り込み・保守時に合成する方式として説明している。

## 依存関係

- Agent Skills標準に対応するツール向けのskillとして説明されている。READMEにはClaude Code、Cursor、Codex CLI、OpenCodeなどの利用方法が記載されている。追加依存関係はREADMEから確認できない。

## 実行条件

- READMEには、npx add-skill Astro-Han/karpathy-llm-wikiでの導入方法と、Codex CLIではskillファイルを.agents/skills/karpathy-llm-wiki/にコピーする方法が記載されている。具体的な実行環境や必要バージョンはREADMEに記載がない。

## 最短手順

- README記載の導入方法でskillを配置し、最初のソースとしてURL・ファイル・貼り付けテキストを指定して取り込む。続けてwikiについて質問し、必要に応じてlintを依頼する。

## 変更履歴

- 2026-11-11: 初回登録
