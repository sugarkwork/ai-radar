---
name: "HomeBox"
genre: "other"
url: "https://github.com/sysadminsmedia/homebox"
repo: "sysadminsmedia/homebox"
license: "AGPL-3.0"
stars: 7842
language: "Go"
created: "2024-06-17"
updated: "2026-11-07"
forks: 620
open_issues: 137
commits_30d: 22
commit_cadence: "daily"
commits_90d: 55
size_kb: 63666
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/ruyi3699/status/2118531565491818624"]
fetched_at: "2026-11-12T13:16:09.480330+00:00"
---

# HomeBox

## 出来ること

- 家庭内の品目をカテゴリ・場所・タグで整理し、カスタム項目を追加できる。検索、品目画像のアップロード、書類・保証の記録、購入日・価格・保守予定の管理に対応するとREADMEに記載されている。

## 目的・背景

- 家庭ユーザー向けの在庫・整理・管理システムとして紹介されている。READMEは、シンプルさと拡張性、SQLiteと組み込みWeb UIによるポータブルな運用を設計方針として挙げている。

## 依存関係

- READMEはSQLiteを使用すると説明している。掲載されたコンテナ起動例ではDocker、データ保存用ディレクトリ、認証用 pepper 値を使う。その他の依存関係はREADMEから確認できない。

## 実行条件

- READMEのQuick StartはDockerコンテナでの起動例を示す。ポート3100をコンテナの7745に割り当て、データ用ディレクトリを /data にマウントする。rootlessまたはhardenedイメージを使う場合のディレクトリ所有者設定例も記載されている。

## 最短手順

- READMEの例では、openssl rand -base64 48 で pepper を生成してファイルに保存し、必要に応じてデータ用ディレクトリを作成・権限設定した後、ghcr.io/sysadminsmedia/homebox:latest を指定した docker run コマンドで起動する。ここではコマンドの実行確認はしていない。

## 変更履歴

- 2026-11-12: 初回登録
