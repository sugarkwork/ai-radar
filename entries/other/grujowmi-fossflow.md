---
name: "FossFLOW"
genre: "other"
url: "https://github.com/Grujowmi/FossFlow"
repo: "Grujowmi/FossFlow"
stars: 15
forks: 3
open_issues: 0
size_kb: 750
language: "TypeScript"
created: "2026-05-22"
updated: "2026-05-22"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/awe0_io/status/2118740924612362518"]
fetched_at: "2026-11-14T00:12:59.120377+00:00"
---

# FossFLOW

## 出来ること

- React製のPWAでアイソメトリック図を作成できます。コンポーネントをキャンバスに配置し、ノード間を接続できます。ブラウザーセッションへのクイック保存、自動保存、JSON形式でのエクスポートとインポートに対応するとREADMEに記載されています。

## 目的・背景

- READMEでは、アイソメトリック図を作成するオープンソースのプログレッシブウェブアプリとして説明されています。Isoflowライブラリを利用し、FossFLOW用にフォークしてNPMで公開したと記載されています。

## 依存関係

- READMEに記載された構成は、ReactとIsoflowライブラリです。モノレポにはWebpackでビルドするReactコンポーネントライブラリと、RSBuildでビルドするPWAが含まれます。

## 実行条件

- オンライン版はブラウザーから利用できます。READMEではブラウザー内で動作し、オフライン対応と説明されています。Dockerでの起動方法と、ローカル開発向けのNode.js/npmコマンドが記載されています。Dockerの永続ストレージにはホスト側の diagrams ディレクトリを使います。

## 最短手順

- Docker Composeを使う場合は、リポジトリのREADMEに記載された手順で `docker compose up` を実行します。ローカル開発では、リポジトリを取得して `npm install`、`npm run build:lib`、`npm run dev` の順に実行します。図の作成は「+」から部品を追加してキャンバスに配置し、コネクターツールでノードを接続します。保存はセッションへのクイック保存、またはJSONのエクスポートを使います。

## 変更履歴

- 2026-11-14: 初回登録
