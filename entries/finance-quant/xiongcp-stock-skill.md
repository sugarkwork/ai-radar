---
name: "kline-structure-chart"
genre: "finance-quant"
url: "https://github.com/xiongcp/stock-skill"
repo: "xiongcp/stock-skill"
stars: 121
forks: 2
open_issues: 0
size_kb: 36732
language: "Python"
created: "2026-10-16"
updated: "2026-11-18"
archived: false
license: "Apache-2.0"
commits_30d: 95
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Ryrenz/status/2119401807206031643"]
fetched_at: "2026-11-20T05:12:26.778461+00:00"
---

# kline-structure-chart

## 出来ること

- READMEの説明では、A株・香港株・米国株のOHLCVデータからK線構造を計算し、トリプルバリア風控計画、15日間の正常変動幅、無前視バックテストを生成する。JSON、PNG、オフラインHTML看板、Markdownレポートを出力し、Claude CodeやCodexなどのAgent Skills対応エージェントとCLIから利用できる。これらはREADMEに記載された機能で、独立した実績検証を示すものではない。

## 目的・背景

- READMEは、大規模言語モデルによるチャートの価格読み取りや、先読みを含む分析、根拠のない上昇確率表現などを避けるため、決定論的な構造分析と風控を行う研究用ツールとして説明している。投資助言ではなく、注文を実行しない旨も記載されている。

## 依存関係

- README記載の必要環境はPython 3.12以上とPillow。uvは推奨だが必須ではなく、uvを使わない場合はvenvとpipを利用できる。インストールにはGitHubとPyPIへのアクセス、分析のたびに新浪・Yahoo・腾讯の行情接口へのネットワークアクセスが必要。LinuxでPNGに中国語を描画する場合は中国語フォントも必要。

## 実行条件

- macOS、Linux、Windowsが対象とREADMEにあるが、Windowsのインストールスクリプトは未実測と記載。ネットワークから行情を取得できない場合は[DATA_UNAVAILABLE]で終了し、行情を推定・補完しない設計と説明されている。対象は研究・学習用途。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- macOS/LinuxではREADME記載の `curl -fsSL https://raw.githubusercontent.com/xiongcp/stock-skill/main/install.sh | bash` でインストールする。WindowsではPowerShell用の `irm https://raw.githubusercontent.com/xiongcp/stock-skill/main/install.ps1 | iex` が案内されている。導入後に新しいエージェントセッションを開き、例として銘柄コードを指定して分析を依頼する。CLIでの利用方法やuvを使わない手順もREADMEに案内されている。

## 変更履歴

- 2026-11-23: 初回登録
