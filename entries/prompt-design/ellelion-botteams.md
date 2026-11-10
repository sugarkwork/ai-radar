---
repo: "ellelion/botteams"
name: "Grok Bot Teams"
genre: "prompt-design"
url: "https://github.com/ellelion/botteams"
flags: ["unverified"]
risk_notes: ["Grok Bot上での導入成功率、生成結果、実行時の料金、最新リリースは未確認。コネクタごとの動作も実機では確認していない。"]
stars: 26
forks: 6
open_issues: 1
size_kb: 3696
language: "TypeScript"
created: "2026-08-20"
updated: "2026-09-08"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 100
commit_cadence: "monthly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117591176048005131"]
fetched_at: "2026-11-10T09:46:03+00:00"
---

# Grok Bot Teams — 役割分担と定期処理を再利用できるチームレシピ

## 出来ること

- チームのBot構成、グループチャット、定期処理をまとめたレシピから導入用プロンプトを生成できる。
- 公開APIからチームと単体Botの一覧を取得できる。

## 目的・背景

- チームごとにMarkdownを1ファイル用意し、YAMLフロントマターで役割や接続先を管理する。公開JSON Schemaとリポジトリの意味検査で定義を確認する。
- 運営元のVerifiedは人数や名簿などの構成条件を示す。導入の成功率や業務成果は実測していない。

## 依存関係

- 導入先はGrok Bot。外部サービスを利用する場合はレシピに記載されたコネクタをGrok Bot側で接続する。ディレクトリのローカル開発にはREADME記載のNode 22.12.0とnpmを使う。

## 実行条件

- 公開ディレクトリはアカウント不要で、リポジトリはMIT。Grok Bot側の利用料金は未確認。
- READMEによるとコネクタはアカウント単位で共有され、プロンプトで指定する利用モードはアクセス権限を変更しない。

## 最短手順

- ディレクトリで導入可能なチームを開き、Botの役割とコネクタを確認して導入用プロンプトをコピーする。
- Grok Botにプロンプトを貼り付け、提案された定期処理を確認する。スキルの追加とサイドバーのセクション作成は必要に応じて別途行う。
- APIを使う場合は、HTTP取得機能のあるAIに https://botteams.io/api/teams?limit=5 をGETし、返ったチーム候補を要約するよう依頼する。READMEでは認証キー不要としている。

## 変更履歴

- 2026-11-10: 初回登録
