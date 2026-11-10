---
repo: "justinhe16/trade-jev"
name: "trade-jev"
genre: "finance-quant"
url: "https://github.com/justinhe16/trade-jev"
stars: 13
forks: 3
open_issues: 1
size_kb: 994
language: "Python"
created: "2026-09-17"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 16
commits_90d: 21
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "コードの実行と損益の独立再計算は未実施。別期間での成績、実約定での損益、現行のAPI・市場データ料金、最新リリースは未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115461838607659474"]
fetched_at: "2026-11-10T12:19:21Z"
---

# trade-jev｜Jevの売買シグナルを板データでバックテスト・再評価

## 出来ること

- Nasdaq-100先物（NQ）の板データを使い、JevのBUY／SELL／HOLDを、保有継続・ランダム・板の偏りを用いる比較ルールと並べて検証できる。保存した応答はAPIを再呼び出しせず再評価できる。

## 目的・背景

- Jevには15秒ごとに板の上位10段、直近価格、注文フロー、保有ポジションを渡す。著者によると、2026年6月8〜26日の15取引日で22,401回のモデル呼び出しに0.91米ドルかかった。全シグナルに従う設定の模擬損益は−128,590米ドル（6,941取引）。信頼度0.70以上、同方向4回連続、200ティックの損切りと100ティックの利確を使う再評価では＋20,795米ドル（178取引、12勝日）。
- 著者は同じ15日間で試した1,920設定からフィルタを選んだ。保存応答には収録時点の保有ポジションが反映されるため、別条件でモデルを再呼び出した場合と再評価の結果は異なりうる。

## 依存関係

- Python 3.12以上とuv。主要依存はTypeSafe SDK、Databento、NumPy、pandas、PyArrow。コードはMIT。Databentoの板・価格データはライセンスの都合で公開結果から除外されている。

## 実行条件

- 合成データの比較ルールはAPIキー不要。Jevを使う場合はTYPESAFE_API_KEYと対象の板データが必要。履歴データの場所はTRADE_JEV_DATAで指定できる。保存応答の再評価にはJevの追加呼び出し費用がかからない。

## 最短手順

- 公開済みの結果を読むにはリポジトリの results/FINDINGS.md を開く。ローカルで比較ルールを試すには uv sync 後、TRADE_JEV_DATA を data/sample に設定し、uv run python -m trade_jev.run --days 2026-06-23 --policies hold,random,imbalance を実行する。
- AIエージェントからJevを使うバックテストを呼ぶには、APIキーと履歴データを設定した環境で、シェルツールから uv run python -m trade_jev.run --days 2026-06-23 を起動する。応答と模擬取引の出力先は runs/<id>/。

## 変更履歴

- 2026-11-10: 初回登録
