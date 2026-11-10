---
name: "HyperGrok Trading Desk"
genre: "finance-quant"
url: "https://github.com/galleonlabs/hypergrok-trading-desk"
last_release: "v1.7.1"
flags: ["unverified"]
risk_notes: "独立した動作検証は未実施。各環境の導入・権限設定、注文承認の強制と迂回耐性、取引成績、ホスト環境と取引所の料金は未確認。v1.7.1のリリースノートによると、公開Grok Botテンプレートは当時v1.7.0を配布しており、v1.7.1への更新状況は未確認。"
repo: "galleonlabs/hypergrok-trading-desk"
stars: 472
forks: 110
open_issues: 1
size_kb: 1635
language: "Python"
created: "2026-08-16"
updated: "2026-11-04"
archived: false
license: "MIT"
commits_30d: 26
commits_90d: 80
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117591176048005131"]
fetched_at: "2026-11-10T09:44:37+00:00"
---

# HyperGrok Trading Desk — Hyperliquid市場調査のためのAIエージェント用スキル集

## 出来ること

- 7つの役割定義と17のSKILL.mdを収録。Opening BellはHyperliquidの公開/infoから価格、資金調達率、建玉、スプレッド、板の厚みを取得する。READMEに開発元の出力例がある。

## 目的・背景

- 市場調査、戦略検証、リスク審査、注文、事後レビューを分担し、注文内容をチケットで引き継ぐ設計。
- MITライセンス。複製や実質的な部分の再利用時は著作権表示と許諾文を保持する。

## 依存関係

- Opening Bellとdesk doctorはPython 3の標準ライブラリを使う。公開市場データの取得にはHyperliquidへのネットワーク接続が必要。署名処理には公式Python SDKまたは@nktkas/hyperliquidを使う構成がREADMEに記載されている。

## 実行条件

- Grok Botでは調査モードから始まり、公開市場データの参照にウォレットやAPIキーは不要。注文機能には取引用APIウォレット、検証済みの承認制御、個別チケットへの承認が必要と文書化されている。

## 最短手順

- Grok Botにv1.7.1固定のbootstrapスキル（https://github.com/galleonlabs/hypergrok-trading-desk/blob/v1.7.1/skills/hypergrok-bootstrap/SKILL.md）を指定して調査モードでセットアップし、Desk LeadにETHのOpening Bellを依頼する。返答で取得元とUTC時刻を確認する。

## 変更履歴

- 2026-11-10: 初回登録
