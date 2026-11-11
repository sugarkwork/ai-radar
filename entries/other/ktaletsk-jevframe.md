---
repo: "ktaletsk/jevframe"
name: "jevframe"
genre: "other"
url: "https://github.com/ktaletsk/jevframe"
license: "MIT"
stars: 21
language: "Python"
created: "2026-09-18"
updated: "2026-09-24"
forks: 3
open_issues: 2
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 12
size_kb: 405
archived: false
flags: ["unverified"]
risk_notes: "READMEと公開パッケージ情報を確認した。実行による精度、処理速度、費用削減の検証は行っていない。TypeSafe APIの現行単価とデータ保持条件、およびGitHubの最新リリースは未確認。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116142322543198271"]
fetched_at: "2026-11-10T12:55:53+00:00"
---

# jevframe — pandas・Polarsで行ごとに分類・採点し、確率を列に返す

## 出来ること

- レビューの感情判定、問い合わせの分類、ルーブリックに沿った採点を、DataFrameの行ごとに実行できる。二択判定は肯定の確率をSeriesで返し、分類や採点では各選択肢の確率も列として取得できる。
- READMEによると、結果は入力の行順とpandasのインデックスを保持する。公開デモではレビューの参照ラベルと推論結果を比較できる。

## 目的・背景

- TypeSafe Jevに選択した行データと型付きの質問を渡し、結果を表形式の処理に組み込む。複数の質問は同じ行のリクエストにまとめられ、非同期の並行数を制限できる。キャッシュは任意。

## 依存関係

- Python 3.10以上、typesafe-sdk>=0.7,<0.8、利用するDataFrameに応じてpandasまたはPolars。ライブラリのライセンスはMIT。

## 実行条件

- 通常利用にはTypeSafeの認証情報、または明示的に渡すクライアントが必要。推論時には質問の対象として選んだ行データがサービスへ送られる。APIの現行単価とデータ保持条件は未確認。

## 最短手順

- pandasで試す場合は、Pythonプロジェクトに `uv add 'jevframe[pandas]==0.1.0'` で追加し、環境変数 `TYPESAFE_API_KEY` を設定する。PyPIで公開されている版を使用する。
- ノートブックで `import jevframe.pandas` を実行して `.jev` を登録する。`review` 列のあるDataFrameに対し `df['urgent'] = await df.jev.noul('Does this customer need urgent help?', state='review')` と呼ぶと、肯定の確率を列に格納できる。

## 変更履歴

- 2026-11-11: 初回登録
