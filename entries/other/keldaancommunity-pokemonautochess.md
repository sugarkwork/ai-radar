---
name: "Pokemon Auto Chess"
genre: "other"
url: "https://github.com/keldaanCommunity/pokemonAutoChess"
repo: "keldaanCommunity/pokemonAutoChess"
license: "GPL-3.0"
stars: 1852
language: "TypeScript"
created: "2019-09-11"
updated: "2026-11-18"
forks: 581
open_issues: 16
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 1169355
archived: false
flags: ["unverified"]
risk_notes: "READMEはThe Pokémon Companyの権利を明記し、同社の要請で公開終了となる可能性を述べている。外部サービスの認証情報を自分で用意する必要があり、権利者の許諾や配布継続状況はREADMEから確認できない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119263387477749830"]
fetched_at: "2026-11-18T08:15:17.897075+00:00"
---

# Pokemon Auto Chess

## 出来ること

- READMEでは、ローカルでゲームを起動し、ボットと対戦できると案内している。開発サーバーで変更を試し、ビルドしたファイルを本番環境で起動する手順も記載されている。

## 目的・背景

- READMEは非営利のファン制作ゲームと説明し、ポケモン関連の権利はThe Pokémon Companyに属し、同社の要請により公開を終了する可能性があるとしている。

## 依存関係

- README記載の構成要素はNode LTS、MongoDB、Firebase。依存関係の網羅性や個々のバージョンはREADMEから確認できない。

## 実行条件

- MongoDBの`dev`データベースと空の`botv2`コレクションを用意し、接続URIを`.env`に設定する。Firebaseプロジェクトとメール/パスワード・匿名認証を設定し、Webアプリ設定値とAdmin SDK秘密鍵情報を`.env`に追加する。ボット対戦には`./db-commmands/botv2.json`のデータをインポートする。

## 最短手順

- Node LTSを用意し、リポジトリで`npm install`、`npm run download-music`、`npm run assetpack`を実行する。MongoDBとFirebaseを設定してから、開発起動は`npm run dev`、本番向けビルドは`npm run build`、ビルド後の起動は`npm run start`。

## 変更履歴

- 2026-11-23: 初回登録
