---
name: "bolt.diy"
genre: "coding-agent"
url: "https://github.com/stackblitz-labs/bolt.diy"
repo: "stackblitz-labs/bolt.diy"
license: "MIT"
stars: 20087
language: "TypeScript"
created: "2024-10-13"
updated: "2026-10-14"
forks: 10614
open_issues: 14
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 100
size_kb: 14941
archived: false
flags: ["unverified"]
risk_notes: "WebContainers APIにはエンタープライズ展開向けの個別の商用ライセンス条件があるとREADMEに記載。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/thegreatest_sv/status/2118770137646162218"]
fetched_at: "2026-11-14T04:12:34.300392+00:00"
---

# bolt.diy

## 出来ること

- ブラウザー上でフルスタックWebアプリを開発できるAI開発環境。READMEでは22以上のクラウド・ローカルLLMプロバイダー、コードエディター、ターミナル、差分表示、ライブプレビュー、Git操作、スナップショット復元、ZIP書き出し、Netlify・Vercel・GitHub Pagesへのデプロイ、Supabase、チャート、MCPツールを紹介している。

## 目的・背景

- 好みのLLMをプロンプトごとに選べるオープンソースのAI開発環境として説明されている。READMEでは、プロジェクトがCole Medinにより開始され、コミュニティ主導で拡大したとしている。

## 依存関係

- 開発の前提条件としてNode.js 22.12.0以上とpnpm 9.15.9以上をREADMEに記載。WebContainers APIを利用する。各プロバイダー、デプロイ、統合機能の追加依存関係はREADMEに網羅されていない。

## 実行条件

- APIキーまたはローカルプロバイダーのエンドポイントをUIのSettings → Providersで設定するか、環境変数で設定する。READMEによるとOpenRouter、Anthropic、OpenAI、Googleは初期状態で有効で、他のプロバイダーはSettingsで有効化・設定する。

## 最短手順

- README記載の手順は、リポジトリをcloneし、ディレクトリに移動してpnpm installを実行後、pnpm run devで開発サーバーを起動する。Dockerでは.env.exampleを.env.localへコピーし、開発用にdocker compose --profile development upを実行する。

## 変更履歴

- 2026-11-14: 初回登録
