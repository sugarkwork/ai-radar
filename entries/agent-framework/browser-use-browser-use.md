---
name: "Browser Use"
genre: "agent-framework"
url: "https://github.com/browser-use/browser-use"
repo: "browser-use/browser-use"
license: "MIT"
stars: 120559
language: "Python"
created: "2024-10-31"
updated: "2026-11-10"
forks: 13471
open_issues: 618
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 40312
archived: false
flags: ["unverified"]
risk_notes: "README記載の実行条件と手順は未実行。クラウド利用時の料金や各機能の効果・利用条件は、この資料からは検証していない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118043980420030914"]
fetched_at: "2026-11-10T16:21:31.320250+00:00"
---

# Browser Use

## 出来ること

- タスクを受け取り、モデルがPythonコードを書いて実ブラウザーを操作するエージェント。READMEでは、永続REPL、browser-harnessのヘルパー、Chrome DevTools Protocol（CDP）を使う構成と説明されている。

## 目的・背景

- 人が操作するようにウェブをナビゲートするオープンソースのブラウザーエージェントとして紹介されている。例として、運転試験の空き枠を探し、日時を選び、CAPTCHAに対応して予約するデモが記載されている。

## 依存関係

- README記載のPythonライブラリ利用ではPython 3.11以降が必要。構成要素としてPydantic AI、Chrome DevTools Protocol、browser-harnessのヘルパーが挙げられている。READMEにはuvまたは仮想環境でのpip導入例がある。

## 実行条件

- PythonライブラリのREADME例ではBrowser Use APIキーを設定する。既定ではBrowser Use gatewayのbu-fastモデルとBrowser Use Cloudブラウザーを使用する。ローカルブラウザーを使う例ではChrome/Chromium等を指定し、ChatOpenAIとOpenAI APIキーを使う。記載内容は実測していない。

## 最短手順

- READMEの例は、Python 3.12環境を作成し、`uv add 'browser-use==1.0.1'`でバージョンを固定して導入、`BROWSER_USE_API_KEY`を設定した後、`from browser_use import Agent`でAgentを作成して`run_sync()`を実行する手順。これは資料記載の手順で、実行確認はしていない。

## 変更履歴

- 2026-11-11: 初回登録
