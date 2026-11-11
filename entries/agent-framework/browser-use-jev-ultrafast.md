---
repo: "browser-use/jev-ultrafast"
name: "Jev Ultrafast"
genre: "agent-framework"
url: "https://github.com/browser-use/jev-ultrafast"
stars: 24346
forks: 1874
open_issues: 210
size_kb: 4519
language: "Python"
created: "2026-09-16"
updated: "2026-11-03"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 4
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: ["最新リリースのタグと公開日時、外部APIの現行料金・利用条件は未確認。", "性能値は開発元の報告。独立した再実行は行っておらず、別サイトや別環境での性能は未確認。"]
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:32:47+00:00"
---

# Jev Ultrafast — 操作の選択と入力文の生成を分けるブラウザエージェント

## 出来ること

- 自然言語の目標を受け取り、Chrome上のクリック、入力、選択などを実行する。ローカル画面では操作・対象の確率と実行履歴を確認できる。
- Google Flightsの例はチューリッヒ発ロンドン行きの片道便を検索し、経路・日付・候補表示を検証するところまで。便の選択や予約は行わない。

## 目的・背景

- 可視DOM要素を観測のたびに採番する。TypeSafe Jevが操作と対応する対象の候補を1リクエストで評価し、文字入力を選んだ場合だけ小型LLMを呼ぶ。通常のループではスクリーンショットを使わない。
- 開発元による便検索の1回の計測は、初回ページ観測後から7.073秒。モデル呼び出し、文字生成、ブラウザ操作、読み込み待ちを含む。同じ設定で各3回を比較した中央値は9.450秒から7.092秒に短縮した。比較は1タスク・1ブラウザプロファイルに限られる。

## 依存関係

- Python 3.12以上。READMEのセットアップではuvとChromeを使い、Python依存はbrowser-harness 0.1.13とHTTP/2対応のhttpx。
- TypeSafeとテキスト生成用サービスのAPIキーが必要。READMEの例はOpenRouter経由でinception/mercury-2.5を使う。

## 実行条件

- Chromeへの接続時にリモートデバッグの許可を求められることがある。エージェントが開くタブは既存のChromeプロファイルを共有する。
- 一般的なHTML・ARIAコントロールに対応する。Shadow DOM、フレーム、canvas、アップロード、ポップアップタブなどは対象外。DONEが返った後も目的を達成したか別途検証する。
- リポジトリはMIT。ライブ例は有料APIを呼び出す。外部APIの現行料金・利用条件は未確認。

## 最短手順

- リポジトリを取得して `uv sync` を実行し、`.env.example` を `.env` にコピーして `TYPESAFE_API_KEY` と `TEXT_MODEL_API_KEY` を設定する。
- `uv run jev` で起動し、ローカルの `http://127.0.0.1:8766` で Start demo を開く。Choose next で次の操作を実行前に確認できる。
- AIから呼ぶ場合は、呼び出し側のPythonツールで `jev_ultrafast.Agent(URL, goal)` を作り、`agent.run()` が返す状態を読み取る。READMEの例は `uv run --env-file .env python your_script.py` で起動する。

## 変更履歴

- 2026-11-11: 初回登録
