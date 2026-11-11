---
name: "GitReverse"
genre: "prompt-design"
url: "https://github.com/filiksyos/gitreverse"
repo: "filiksyos/gitreverse"
stars: 2081
forks: 337
open_issues: 18
size_kb: 10788
language: "TypeScript"
created: "2026-03-31"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 8
commits_90d: 31
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/RealMarvelX/status/2118349624763207790"]
fetched_at: "2026-11-11T22:14:14.260367+00:00"
---

# GitReverse

## 出来ること

- 公開GitHubリポジトリのメタデータ、ルートのファイルツリー（深さ1）、READMEを使い、Cursor、Claude Code、Codexなどに入力する想定の短い会話調プロンプトを1つ生成する。READMEでは、GitHub URLまたはowner/repo形式をホーム画面に入力する方法と、/owner/repo形式の共有リンクが説明されている。出典: https://github.com/filiksyos/gitreverse

## 目的・背景

- READMEの説明では、既存プロジェクトを一から作る際に使える合成ユーザープロンプトを生成する。サブフォルダーに限定したコンテキスト取得は今後の変更予定で、現状はリポジトリ全体を使う。出典: https://github.com/filiksyos/gitreverse

## 依存関係

- README記載の構成はNext.js 16（App Router）、React 19、TypeScript、Tailwind CSS 4、GitHub API。SupabaseとStripeは任意。クイック生成には対応するLLMプロバイダーのAPIキーが少なくとも1つ必要。出典: https://github.com/filiksyos/gitreverse

## 実行条件

- READMEの設定手順では、.env.exampleを.env.localにコピーし、少なくとも1つのLLM APIキーを設定する。GITHUB_TOKENは任意で、GitHub APIのレート制限を引き上げる用途。Supabaseの設定は任意で、サーバー側キャッシュと/libraryを有効にする。出典: https://github.com/filiksyos/gitreverse

## 最短手順

- README記載の開発手順: pnpm install、pnpm devを実行し、ブラウザーでローカルの開発サーバーを開く。事前に.env.localへLLM APIキーを設定する。出典: https://github.com/filiksyos/gitreverse

## 変更履歴

- 2026-11-11: 初回登録
