---
name: "股票智能分析系统（daily_stock_analysis）"
genre: "finance-quant"
url: "https://github.com/ZhuLinsen/daily_stock_analysis"
repo: "ZhuLinsen/daily_stock_analysis"
license: "MIT"
stars: 69545
language: "Python"
created: "2026-01-10"
updated: "2026-11-10"
forks: 56670
open_issues: 43
commits_30d: 34
commit_cadence: "daily"
commits_90d: 100
size_kb: 120431
archived: false
flags: ["unverified"]
risk_notes: "READMEの説明や掲載例は独立検証された性能・投資効果を示すものではありません。実際の分析精度や各データソースの利用条件・料金はREADMEだけでは確認できません。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2119950747898974362"]
fetched_at: "2026-11-10T23:13:53.629808+00:00"
---

# 股票智能分析系统（daily_stock_analysis）

## 出来ること

- READMEによると、A株・香港株・米国株・日本株・韓国株・台湾株とETFを対象に、行情・K線・テクニカル指標・ニュース・公告・ファンダメンタルズ情報を集約し、AI決策レポートを生成します。Web／デスクトップの作業画面、複数ターンのAgent問答、画像・CSV・Excel・クリップボードからの銘柄インポート、GitHub Actions・Docker・ローカル定時実行、複数チャネルへの通知を備えると説明されています。

## 目的・背景

- READMEでは、自選銘柄を毎日分析し、決策ダッシュボードを企業微信・飛書・Telegram・Discord・Slack・メールへ自動配信するシステムとして紹介されています。

## 依存関係

- README記載の行情データ源はAkShare、Tushare、Pytdx、Baostock、YFinance、Longbridgeです。モデル接続先としてModelflare、AIHubMix、Gemini、OpenAI互換サービス、DeepSeek、通義千問、Claude、Ollamaなど、ニュース検索源としてSerpAPI、Anspire、Tavily、Bocha、Brave、MiniMax、SearXNGなどが挙げられています。バージョンや全依存パッケージは添付READMEからは確認できません。

## 実行条件

- READMEのローカル実行手順ではPython 3.10以上を掲げ、依存関係のインストール、環境変数設定、自選銘柄リストの指定を案内しています。GitHub Actions手順ではAIモデルの認証情報を少なくとも1つ、通知チャネルを少なくとも1つ、自選銘柄リストを設定し、Actionsを有効化する必要があると記載されています。無料行情源は上流の制限・インターフェース変更・ネットワーク変動の影響を受け、安定性は保証されないとの説明があります。

## 最短手順

- READMEのローカル手順：`git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis`、`pip install -r requirements.txt`、`.env.example`を`.env`へコピーして設定し、`python main.py`を実行します。Actionsを使う場合はリポジトリをForkし、必要なSecretsと`STOCK_LIST`を設定してActionsを有効化し、「每日股票分析」ワークフローを手動実行します。

## 変更履歴

- 2026-11-11: 初回登録
