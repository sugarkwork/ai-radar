---
repo: "Dzy-HW-XD/a-share-quant-selector"
name: "A-Share Quant Selector"
genre: other
url: "https://github.com/Dzy-HW-XD/a-share-quant-selector"
license: "MIT"
stars: 506
language: "Python"
created: "2026-02-10"
updated: 2026-09-08
added: "2026-11-05"
first_seen: "2026-11-04"
source_post: "https://x.com/bkdgiffug/status/2118124886585454934"
sources: []
flags: []
risk_notes: ""
forks: 107
open_issues: 3
size_kb: 95
archived: false
commits_30d: 0
commits_90d: 1
commit_cadence: stale
fetched_at: "2026-11-05T00:04:33Z"
---

# A-Share Quant Selector

## 出来ること

- A株の「碗口反発（茶碗の縁からの反発）」型の押し目を機械的に拾う選股ツール。Python + akshare でデータを取り、KDJ・トレンドライン・出来高の条件でふるいにかける。
- 条件は4つ。①短期トレンドラインが中長期の多空ラインより上（上昇トレンド）②直近 M 日以内に出来高急増の陽線がある ③その期間の最大出来高が陰線の日なら除外 ④KDJ の J 値が閾値以下（売られすぎ）。
- さらに10件の過去成功例と「三维類似度（2本のライン＋出来高比＋形状）」で照合して順位付けする。結果は「碗の中へ回落」「多空ラインに接近」「短期トレンドラインに接近」に自動分類。
- 選ばれた銘柄ごとにトレンドラインと出来高入りの K 線チャートを生成し、DingTalk（钉钉）へ自動通知。ST/*ST・上場廃止・異常銘柄は自動で除外する。
- Web 管理画面付き（銘柄データ・K 線・KDJ を可視化）。データ更新は 15 時前なら前日分を使うなど、当日データの有無を見て判断する。DingTalk API のレート制限には自動バックオフで対応。

## 目的・背景

個人が板を見ながら目視でやっている「押し目のかたち探し」を、パラメータを変えながら検証できる形に落とすためのもの。README 自身が「完全なクオンツフレームワークではなく、個人の復盤とパラメータ調整向け」と位置づけている。

## 依存関係

- Python 3 と `requirements.txt`。データ取得は akshare（East Money など公開データ源に依存）。
- DingTalk 通知は任意。`config/config.yaml` に webhook と secret を書く（未設定でも選股自体は動く）。

## 実行条件

- ライセンスは MIT。
- **投資助言ではない**。README／投稿とも「形態が似ていても、その後の上昇を保証しない」と明記している。
- A株専用。米国株にはそのままでは使えない。
- 直近の更新は 2026-09-08 で、約2か月動いていない。akshare 側の仕様変更でデータ取得が壊れる可能性がある。

## 最短手順

```bash
git clone https://github.com/Dzy-HW-XD/a-share-quant-selector.git
cd a-share-quant-selector
pip3 install -r requirements.txt
python3 main.py init                 # 初回の全量データ取得
python3 main.py run --max-stocks 500 # まず500銘柄で試す
python3 main.py web                  # Web 画面
```

## 変更履歴

- 2026-11-05: 初回登録（★506 / MIT / Python / 最終push 2026-09-08）
