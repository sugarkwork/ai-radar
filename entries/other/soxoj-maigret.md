---
name: "Maigret"
genre: "other"
url: "https://github.com/soxoj/maigret"
repo: "soxoj/maigret"
stars: 40599
forks: 3269
open_issues: 62
size_kb: 31377
language: "Python"
created: "2020-06-27"
updated: "2026-11-13"
archived: false
license: "MIT"
commits_30d: 58
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118713263290741015"]
fetched_at: "2026-11-13T20:09:34.089321+00:00"
---

# Maigret

## 出来ること

- READMEによると、ユーザー名で5,900サイトに対応し、既定ではトラフィック順位上位500サイトを検索する。全サイト検索、タグによる絞り込み、プロフィールページやサイトAPIからの情報抽出、発見したユーザー名等を使った再帰検索、結果のグラフ表示と各形式のレポート出力に対応する。任意のAI分析モードも記載されている。

## 目的・背景

- ユーザー名だけを手掛かりに、複数サイト上のアカウントを確認し、公開ページから得られる情報をまとめるためのツール。READMEはAPIキー不要と説明している。

## 依存関係

- README記載の要件はPython 3.10以上。インストール手順ではpipを使用する。サイトデータベースはGitHubから自動更新され、オフライン時は組み込みデータベースにフォールバックすると説明されている。

## 実行条件

- Python 3.10以上の環境で実行する。READMEの基本例は `pip install maigret` の後に `maigret YOUR_USERNAME`。Windows向けには standalone実行ファイルの手順も記載されている。

## 最短手順

- READMEの例に従い、`pip install maigret` を実行し、その後 `maigret YOUR_USERNAME` を実行する。これはREADME記載の手順であり、この候補についての独立した実機検証ではない。

## 変更履歴

- 2026-11-14: 初回登録
