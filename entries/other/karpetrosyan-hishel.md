---
name: "Hishel"
genre: "other"
url: "https://github.com/karpetrosyan/hishel"
repo: "karpetrosyan/hishel"
license: "BSD-3-Clause"
stars: 422
language: "Python"
created: "2023-07-15"
updated: "2026-11-10"
forks: 57
open_issues: 7
commits_30d: 14
commit_cadence: "weekly"
commits_90d: 28
size_kb: 3622
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:18:17.509830+00:00"
---

# Hishel

## 出来ること

- PythonでHTTPキャッシュを追加するライブラリ。READMEによるとHTTPX、HTTPX2、Requests、ASGIアプリケーションに少ないコード変更で統合でき、FastAPIにも対応。RFC 9111に従うモード、SQLite・Redisまたは独自ストレージ、同期・非同期処理、TTL・TTI・サイズ制限、リクエスト単位の上書き、ストリーミングに対応すると説明されている。高性能・省メモリなどの効果はREADME上の説明で、独立測定値は確認していない。

## 目的・背景

- HTTP応答をキャッシュし、独自の制限を使うかRFC 9111の仕様に従うことを目的としたPythonライブラリ。

## 依存関係

- README抜粋では必須依存パッケージを確認できない。連携対象としてHTTPX、HTTPX2、Requests、ASGI、FastAPI、ストレージとしてSQLiteとRedisが記載されている。

## 実行条件

- Python向け。対応Pythonバージョンや詳細な実行要件は、提供されたREADME抜粋では確認できない。

## 最短手順

- README抜粋にはインストール・コード例が含まれていないため、具体的な導入手順は確認できない。

## 変更履歴

- 2026-11-22: 初回登録
