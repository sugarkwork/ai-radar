---
name: "RedDownloader"
genre: "other"
url: "https://github.com/Jackhammer9/RedDownloader"
repo: "Jackhammer9/RedDownloader"
license: "GPL-3.0"
stars: 177
language: "Python"
created: "2021-10-09"
updated: "2025-12-08"
forks: 23
open_issues: 7
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 743
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/bkdgiffug/status/2119227400688930870"]
fetched_at: "2026-11-17T18:08:57.204053+00:00"
---

# RedDownloader

## 出来ること

- READMEによると、Reddit投稿URLから画像・動画・ギャラリーを取得できます。サブレディットから投稿を取得する機能のほか、投稿者やユーザー情報の取得、取得済み投稿の重複を避けるキャッシュ機能も説明されています。

## 目的・背景

- Redditメディアを簡単にダウンロードするためのPythonライブラリとして紹介されています。READMEでは、利用者自身のPRAW botを用意せずに使えるとしています。

## 依存関係

- READMEには依存パッケージの一覧や実行時の依存関係は記載されていません。

## 実行条件

- README記載の導入方法は `pip install RedDownloader` です。例では `from RedDownloader import RedDownloader` で読み込み、`RedDownloader.Download(url)` を呼び出します。認証なしで利用できるとREADMEに記載されています。

## 最短手順

- README記載の手順: `pip install RedDownloader` の後、`from RedDownloader import RedDownloader` を実行し、`RedDownloader.Download("https://www.reddit.com/r/videos/comments/xi89wf/this_guy_made_a_1hz_cpu_in_minecraft_to_run/")` のように投稿URLを渡します。出力先は既定で現在の作業ディレクトリです。

## 変更履歴

- 2026-11-22: 初回登録
