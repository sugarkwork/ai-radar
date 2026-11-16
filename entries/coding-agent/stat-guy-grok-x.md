---
name: "grok-x"
genre: "coding-agent"
url: "https://github.com/stat-guy/grok-x"
flags: ["unverified"]
risk_notes: "READMEはGrok-nativeとClaude Codeの両方を記載していますが、利用できる機能は実行環境や指定ツールに依存します。 GitHub APIでライセンスを確認できていません。"
repo: "stat-guy/grok-x"
stars: 0
forks: 0
open_issues: 0
size_kb: 150
language: "Python"
created: "2026-03-04"
updated: "2026-03-19"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/RoundtableSpace/status/2122166518041767999"]
fetched_at: "2026-11-16T04:18:22.271486+00:00"
---

# grok-x

## 出来ること

- READMEによると、Grokのx_searchでX投稿を検索し、アカウントや期間で絞り込み、投稿内の画像・動画を分析できます。web_searchとの併用、code_interpreterによる投稿頻度や反応の分析、6種類のスキーマによる構造化抽出にも対応すると説明されています。これらはREADME記載の機能説明であり、独立した実測結果ではありません。

## 目的・背景

- X上の情報を検索・監視・分析し、構造化して取り出すためのGrok skillです。Grok-nativeのprompt-based skillと、Claude Codeから使うPython helper scriptの2種類の利用方法が記載されています。

## 依存関係

- Claude CodeでPython helper scriptを使う場合、READMEにはPython 3.9以降、xAI API key、Claude Code、openaiパッケージが必要と記載されています。Grok-nativeではGrokの組み込みx_search、web_search、code_interpreterを利用すると説明されています。

## 実行条件

- Claude Code用の設定ではXAI_API_KEYを指定します。GROK_X_DEFAULT_MODELは任意で、省略時はgrok-4-1-fast-reasoningを使うとREADMEに記載されています。Grok-nativeはGrokのskillディレクトリにSKILL.mdを置いて利用する手順です。

## 最短手順

- README記載のGrok-native手順は、SKILL.mdをGrokのskillsディレクトリに配置し、Grok sessionで /grok-x <query or analysis request> を呼び出す方法です。Claude Codeではskillを配置し、xAI API keyを設定してから /grok-x <query or analysis request> を呼び出します。

## 変更履歴

- 2026-11-16: 初回登録
