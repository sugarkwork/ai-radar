---
name: "DeepSearch"
genre: "other"
url: "https://github.com/techenthusiast167/DeepSearch-"
repo: "techenthusiast167/DeepSearch-"
license: "unknown"
stars: 156
language: "unknown"
created: "2025-10-14"
updated: "2025-12-24"
forks: 24
open_issues: 1
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 26
archived: false
flags: ["unverified"]
risk_notes: "READMEから確認できるのは検索URLの生成・保存とブラウザー起動機能です。広範な情報収集やリスク発見などの効果は独立に確認されていません。スクリプトの配布先はREADME記載のGistで、今回その内容は確認していません。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/bkdgiffug/status/2119377892358672721"]
fetched_at: "2026-11-19T21:10:40.323521+00:00"
---

# DeepSearch

## 出来ること

- READMEによると、25以上のGoogle検索演算子を使って、入力したユーザー名に関する検索URLを生成します。演算子を選択でき、生成したURLをテキストファイルに保存したり、任意でブラウザーのタブに開いたりできます。実際の検索結果や情報収集の網羅性は確認していません。

## 目的・背景

- READMEは、公開情報を使ったデジタルフットプリント調査や、許可を得たセキュリティ調査などのOSINT用途を掲げています。記載された用途や効果は作者による説明です。

## 依存関係

- README記載の依存パッケージはcoloramaです。Python 3.6以上とpipが前提として記載されています。

## 実行条件

- READMEにはWindows 10/11、macOS 10.14以上、Linuxでの対応が記載されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の手順では、指定されたGistからスクリプトを取得してdeepsearch.pyとして保存し、`pip install colorama`を実行後、`python deepsearch.py`で起動します。起動後、対象のユーザー名、ブラウザー自動起動の希望、使用する検索演算子を入力します。Gist内の配布スクリプト自体は未確認です。

## 変更履歴

- 2026-11-23: 初回登録
