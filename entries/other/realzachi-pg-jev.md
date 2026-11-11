---
repo: "realZachi/pg-jev"
name: "pg-jev"
genre: "other"
url: "https://github.com/realZachi/pg-jev"
stars: 1303
forks: 109
open_issues: 3
size_kb: 214
language: "Shell"
created: "2026-09-17"
updated: "2026-10-06"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 13
commit_cadence: "monthly"
last_release: "v0.2.1"
flags: ["unverified"]
risk_notes: "速度・精度・費用はREADMEの著者測定で、独立再現、別データでの精度、現行料金、ローカル互換サーバーの動作は未確認。最新リリースの公開ページでタグを確認したが、タイムゾーン付きの公開日時は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:34:37+00:00"
---

# pg-jev — PostgreSQLの行を自然言語で絞り込み・分類

## 出来ること

- `jev()`をWHERE句に置いて自然言語条件で行を絞り込む。`jev_prob()`で確率順に並べ、`jev_choice()`で指定した選択肢に分類できる。

## 目的・背景

- SQLの結合や構造化条件に、文章の意味に基づく行判定を組み合わせる。テーブルやビューの行を先読みし、既定で20行ずつJevへ送り、判定結果をDBセッション内にキャッシュする。
- READMEの著者測定では、欧州からAPIまで約190 msの環境で2,000行の初回処理が約3.5秒、費用は約0.012米ドル、キャッシュが効いた2回目は約50 ms。構造化データを正解とした3条件・各400行の試験では、1〜20行のバッチで正答率100%、80行で77〜94%と報告されている。

## 依存関係

- READMEの対応範囲はPostgreSQL 14〜17。`plpython3u`と拡張の作成に必要なスーパーユーザー権限を用意する。既定の接続先にはTypeSafe APIキーが必要。

## 実行条件

- 既定構成では評価対象の行データを外部APIへ送るため、共有可能な列だけをビューで渡せる。`jev.api_url`でローカル互換サーバーを指定できる。セッション内の判定キャッシュは行と質問の組み合わせに応じて増える。
- READMEは配布コードをPostgreSQL Licenseと記載。GitHub APIのライセンス値はunknown。ホスト型APIの費用はREADMEの測定例を参照。

## 最短手順

- PGXNから`pgxn install jev`で導入し、管理者が`CREATE EXTENSION jev CASCADE;`を実行する。`TYPESAFE_API_KEY`をPostgreSQLサーバープロセスに設定し、共有可能なテストデータで`SELECT * FROM tickets WHERE jev(tickets, 'the customer is angry');`を試す。
- **AIから呼ぶ手順**は、スキル対応エージェントのプロジェクトで`npx skills add realZachi/pg-jev`を使い、エージェントに導入条件の確認とセットアップを依頼する。導入後はエージェントが`jev()`を含むSQLを作成し、利用可能なPostgreSQL接続から呼び出す。

## 変更履歴

- 2026-11-11: 初回登録
