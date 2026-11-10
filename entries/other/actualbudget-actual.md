---
repo: "actualbudget/actual"
name: "Actual Budget"
genre: "other"
url: "https://github.com/actualbudget/actual"
stars: 30135
forks: 3272
open_issues: 205
size_kb: 675919
language: "TypeScript"
created: "2022-04-29"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v26.11.0"
flags: ["unverified"]
risk_notes: "定期支出の検出精度、発見投稿のiPhone向けGrok Botの構成と節約額、独自のAI連携手順の動作は未検証。GitHubのリリース表示と公式ノートの日付が異なるため、公開日時は記載していない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117960732184633699"]
fetched_at: "2026-11-10T11:12:04Z"
---

# Actual Budgetで定期支出を見つけ、取引データをAIから参照する

## 出来ること

- SchedulesのFind schedulesで既存取引から定期支払いの候補を出し、確認したものを予定に登録できる。公式文書によると、同じ支払いでも支払先名が一致しないと候補に出ない場合がある。[Schedules](https://actualbudget.org/docs/schedules/)

## 目的・背景

- 端末上のデータを中心に家計を管理し、必要に応じて同期サーバーで端末間の変更を同期する。アプリ本体はMITライセンスで無償。マネージドホスティングには別途費用がかかり得る。[公式README](https://raw.githubusercontent.com/actualbudget/actual/master/README.md)

## 依存関係

- プログラムからの取引取得にはNode.jsと公式npmパッケージ @actual-app/api を使う。クライアントは予算のローカルコピーを処理する。[Using the API](https://actualbudget.org/docs/api/)

## 実行条件

- Windows、macOS、Linux向けのローカルアプリがある。同期サーバーをセルフホストする場合は公式Dockerイメージを利用できる。定期支出の候補抽出には取引履歴が必要。[公式README](https://raw.githubusercontent.com/actualbudget/actual/master/README.md) [Docker](https://actualbudget.org/docs/install/docker/)

## 最短手順

- Actual Budgetに取引履歴を取り込み、Schedules → Find schedulesを開く。提案された支払先、金額、周期を確認し、必要な候補だけ予定に登録する。[Schedules](https://actualbudget.org/docs/schedules/)
- AIに参照させる場合は、公式APIの初期化と予算読み込みの手順に沿ってNode.js側を設定する。口座と期間を受け取り、getTransactionsで取得した取引を支払先・日付・金額に絞って返す関数を作り、利用するAIクライアントのツールとして登録する。これは公式APIを使った独自連携の構成例。[Using the API](https://actualbudget.org/docs/api/) [API Reference](https://actualbudget.org/docs/api/reference/#gettransactions)

## 変更履歴

- 2026-11-10: 初回登録
