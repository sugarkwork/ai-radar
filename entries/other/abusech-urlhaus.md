---
name: "URLhaus"
genre: "other"
url: "https://github.com/abusech/URLhaus"
repo: "abusech/URLhaus"
license: "unknown"
stars: 79
language: "Python"
created: "2018-07-10"
updated: "2024-11-09"
forks: 12
open_issues: 8
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 31
archived: false
flags: ["unverified"]
risk_notes: "READMEに記載された無料のAuth-Key取得には登録が必要です。リポジトリのライセンスは取得済みメタデータでunknownです。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/RoundtableSpace/status/2119071100307169630"]
fetched_at: "2026-11-16T17:10:50.592396+00:00"
---

# URLhaus

## 出来ること

- URLhausバルクAPIを使ったURLの照会、ファイルハッシュ（MD5またはSHA256）の照会、悪性URLの報告を行うPythonサンプルを提供します。ClamAVシグネチャファイルも提供し、READMEではcronで毎分更新する方法を案内しています。

## 目的・背景

- URLhausはマルウェア配布サイトを共有するオープンプラットフォームです。READMEは、APIとのやりとりに使うサンプルスクリプトをこのリポジトリの目的として説明しています。

## 依存関係

- READMEには依存パッケージの記載がありません。

## 実行条件

- READMEの例はPython 3を使用し、URLhaus APIの照会にはAuth-Keyが必要です。Auth-Keyはauth.abuse.chで無料取得できるとREADMEに記載されています。ClamAVシグネチャの定期更新にはcronを使う例があります。

## 最短手順

- READMEの例に従い、Auth-Keyを取得してからPython 3で各スクリプトを実行します。URL照会はlookup_url.py、複数URLの照会はlookup_url_bulk.py、ハッシュ照会はlookup_filehash.pyまたはlookup_filehash_bulk.pyを使います。

## 変更履歴

- 2026-11-16: 初回登録
