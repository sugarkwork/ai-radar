---
name: "BreakoutAnalysis"
genre: "finance-quant"
url: "https://github.com/calesthio/BreakoutAnalysis"
repo: "calesthio/BreakoutAnalysis"
license: "MIT"
stars: 286
language: "Python"
created: "2025-07-12"
updated: "2026-02-23"
forks: 70
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 1513
archived: false
flags: ["unverified"]
risk_notes: "スクリーニングやAI分析が投資成果につながるかはREADMEから確認できない。Alpacaの無料IEXデータと有料SIPデータではカバレッジが異なると記載されている。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/bkdgiffug/status/2119409853064200347"]
fetched_at: "2026-11-22T04:27:28.399795+00:00"
---

# BreakoutAnalysis

## 出来ること

- TradingViewのスクリーナーで市場時間中に15分ごとに米国株を走査し、Alpacaの過去データで候補を絞り込む。Gemini、GPT、またはOllamaを使った分析、ニュース、チャート画像を添えてDiscordやメールに通知する機能がREADMEに記載されている。

## 目的・背景

- 価格変動や出来高の増加などからブレイクアウト候補を検出し、通知にまとめる株式アラートシステム。候補の検出や分析が投資成果を保証するものではない。

## 依存関係

- README記載の構成要素はTradingViewスクリーナー、AlpacaのAPI、AI分析用のGemini・GPTまたはOllama、Discord webhook。メール通知には任意でGmail OAuth、チャート画像には任意でTradingViewアカウントを利用する。

## 実行条件

- READMEの最短手順ではPython依存関係のインストールとPlaywright Chromiumの導入が必要。Alpaca APIキー、AI APIキー、Discord webhook URLを設定する。メール通知、TradingViewのチャート画像、Alpaca SIPデータは任意の追加要素として記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の手順: リポジトリをcloneし、requirements.txtから依存関係をインストール、`playwright install chromium`を実行する。`config/config.example.json`を`config/config.json`へコピーして認証情報を設定し、`python src/tradealerts.py`を実行する。スクリーナーフィルターは`config/config.json`の`screeners.filters`で調整できる。

## 変更履歴

- 2026-11-23: 初回登録
