---
repo: "enoyola/jev-grand-prix"
name: "Jev Grand Prix"
genre: "other"
url: "https://github.com/enoyola/jev-grand-prix"
stars: 7
forks: 0
open_issues: 0
size_kb: 38
language: "JavaScript"
created: "2026-09-20"
updated: "2026-09-21"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 3
commit_cadence: "monthly"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "作者の試走結果は独立再現していない。TypeSafe APIの現在の料金、利用規約、キーの発行条件は未確認。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:33:58+00:00"
---

# Jev Grand Prix — AIの判断と高頻度の車両制御を分けたブラウザーレース

## 出来ること

- ブラウザー上のF1風レースでJevの走行を観察し、自分でも対戦できる。Jevは狙う走行ラインとペダル操作を選び、コースアウトの見込みを返す。

## 目的・背景

- サーバーが車両のテレメトリーを文章に変換し、3つの判断を1回のAPIリクエストにまとめる。ブラウザー側のコードは選ばれたラインへ毎秒120回操舵する。
- コードがコーナーごとの所要時間とコースアウトを記録し、Jevが周回間に次の目標速度を段階的に選ぶ。モデルの更新は不要。
- READMEの作者試走では8周で初周59.2秒、最終周50.9秒、コースアウト3回、API費用0.06米ドル。初周は静止スタートで、周回差にはスタート条件の差も含まれる。

## 依存関係

- uv、Python 3.12以上、typesafe-sdk 0.7.0以上、TypeSafe APIキー、ブラウザー。

## 実行条件

- Pythonサーバーをローカルで起動する。READMEではJevは早期アクセスで、キー取得に待機リストへの登録が必要な場合がある。リポジトリはMITで、外部APIには別途利用条件がある。

## 最短手順

- リポジトリをクローンし、プロジェクト直下の .env に TYPESAFE_API_KEY を設定する。
- uv run server.py を起動し、ブラウザーで http://localhost:8765 を開いて Start race を押す。
- AIから呼ぶ手順を流用する場合は、server.py のテレメトリー整形とTypeSafe API呼び出しを参照する。走行ラインとペダルを Choice、コースアウトの見込みを Noul として1リクエストにまとめる。

## 変更履歴

- 2026-11-11: 初回登録
