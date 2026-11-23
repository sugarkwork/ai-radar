---
name: "SoMarkDown Viewer"
genre: "other"
url: "https://github.com/SoMarkAI/SoMarkDownViewer"
repo: "SoMarkAI/SoMarkDownViewer"
license: "MIT"
stars: 2
language: "JavaScript"
created: "2026-03-14"
updated: "2026-09-09"
forks: 0
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 1
size_kb: 1874
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119370852126908922"]
fetched_at: "2026-11-19T19:14:37.701695+00:00"
---

# SoMarkDown Viewer

## 出来ること

- SoMarkDown文書をリアルタイム編集・描画する。READMEによると、数式、化学構造（SMILES）、コードのシンタックスハイライトなどを描画でき、双方向の同期スクロールと、クリック位置の双方向ジャンプにも対応する。SoMarkDownはmarkdown-itを基盤とするMarkdown拡張形式と説明されている。

## 目的・背景

- SoMarkDown文書のプレビューと描画を行うWebアプリ。SoMarkの文書解析製品で解析結果を受け渡す形式としてもSoMarkDownが使われるとREADMEに記載されている。

## 依存関係

- READMEはネイティブHTML・JavaScript・CSSで実装されていると説明し、描画機能にはSoMarkDownのJavaScriptおよびCSSファイルを取得する手順を示している。

## 実行条件

- README記載の手順では、SoMarkDownのJavaScript・CSSファイルを配置し、HTTPサーバー経由で配信する。例としてPython 3.xのhttp.serverを使用する。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の手順: リポジトリをcloneし、`./get_latest_smd.sh`を実行してSoMarkDownのJavaScript・CSSを取得する。次に`python3 -m http.server 8000`でHTTPサーバーを起動し、ブラウザーからサーバー上のアプリを開く。ファイルはURLで相対パスを指定するか、画面のOpen Fileボタンからローカルファイルを選んで読み込める。

## 変更履歴

- 2026-11-23: 初回登録
