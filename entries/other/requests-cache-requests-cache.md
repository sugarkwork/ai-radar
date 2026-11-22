---
name: "requests-cache"
genre: "other"
url: "https://github.com/requests-cache/requests-cache"
repo: "requests-cache/requests-cache"
stars: 1508
forks: 174
open_issues: 23
size_kb: 5551
language: "Python"
created: "2012-04-12"
updated: "2026-11-17"
archived: false
license: "BSD-2-Clause"
commits_30d: 5
commits_90d: 39
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:19:26.106033+00:00"
---

# requests-cache

## 出来ること

- requestsのSessionに近い使い方でHTTP応答をキャッシュし、SQLite、Redis、MongoDB、DynamoDBなどの保存先に対応するとREADMEは説明しています。Cache-Controlヘッダーや独自の有効期限を設定できます。キャッシュ済み応答の速度はREADMEで「sub-millisecond」と説明されていますが、ここでは独立した実測をしていません。

## 目的・背景

- requestsを使うPythonプログラムで、応答を永続化して再利用し、同じリクエストの待ち時間を減らすためのライブラリです。READMEは、期限切れ時にも条件付きリクエストで時間を節約できると説明しています。

## 依存関係

- READMEはPythonのrequestsライブラリとの併用を案内しています。追加のバックエンドを使う場合の依存関係は、提示されたREADMEだけでは確認できません。

## 実行条件

- READMEにはpipでの導入例があります。キャッシュ期限は既定で無期限と説明されているため、応答の鮮度が必要な場合はexpire_afterやCache-Control対応などを設定してください。

## 最短手順

- `pip install requests-cache`で導入し、`import requests_cache`の後に`requests_cache.CachedSession('demo_cache')`を作成して`session.get(URL)`を呼び出します。READMEの例ではキャッシュファイル名として`demo_cache.sqlite`が示されています。

## 変更履歴

- 2026-11-22: 初回登録
