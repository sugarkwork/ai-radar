---
name: "SpiderFoot"
genre: "other"
url: "https://github.com/smicallef/spiderfoot"
repo: "smicallef/spiderfoot"
license: "MIT"
stars: 24564
language: "Python"
created: "2012-04-28"
updated: "2026-04-13"
forks: 4081
open_issues: 406
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 16517
archived: false
flags: ["unverified"]
risk_notes: "モジュールごとのAPIキー要件や料金の詳細はREADMEだけでは特定できない。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118713263290741015"]
fetched_at: "2026-11-13T20:09:38.798685+00:00"
---

# SpiderFoot

## 出来ること

- Web UIまたはCLIからOSINT調査を行い、200超のモジュールで情報源の照会・データ分析を行う。CSV、JSON、GEXFへのエクスポート、SQLiteバックエンド、可視化、YAML設定可能な相関エンジンを備えるとREADMEに記載。

## 目的・背景

- READMEでは、レッドチーム演習やペネトレーションテストでの偵察、および自組織がインターネット上に公開している情報の把握を用途としている。対象はIPアドレス、ドメイン、ホスト名、CIDR、ASN、メールアドレス、電話番号、ユーザー名、人名、Bitcoinアドレスなど。

## 依存関係

- Python 3.7以上とPythonライブラリが必要。READMEはライブラリの導入にpipを案内し、具体的な依存一覧はrequirements.txtを参照する手順を示している。

## 実行条件

- READMEの手順では、Python 3.7以上の環境を用意し、配布リリースまたはGit masterを取得してrequirements.txtから依存ライブラリを導入する。外部サービス連携にはAPIキーが必要なモジュールがあり、READMEによると多くは不要だが、一部には無料枠がある。

## 最短手順

- README記載の安定版手順: v4.0のアーカイブを取得して展開し、展開先で `pip3 install -r requirements.txt` を実行後、`python3 ./sf.py -l 127.0.0.1:5001` を実行する。

## 変更履歴

- 2026-11-14: 初回登録
