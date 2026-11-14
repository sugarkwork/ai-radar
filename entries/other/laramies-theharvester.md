---
name: "theHarvester"
genre: "other"
url: "https://github.com/laramies/theHarvester"
repo: "laramies/theHarvester"
license: "GPL-2.0"
stars: 18318
language: "Python"
created: "2011-01-01"
updated: "2026-11-13"
forks: 2736
open_issues: 12
commits_30d: 63
commit_cadence: "daily"
commits_90d: 100
size_kb: 12998
archived: false
flags: ["unverified"]
risk_notes: "対象の所有または明示的なテスト許可が必要。選択した提供元には対象文字列が送られる。P1のDNS照会とP2の対象への直接接続は、選択した場合に実行される。Python 3.14とuvが必要。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118713263290741015"]
fetched_at: "2026-11-13T20:10:31.173378+00:00"
---

# theHarvester

## 出来ること

- 検索エンジン、証明書透明性ログ、DNSデータセット、コードリポジトリ、脅威インテリジェンス基盤などの公開情報源から、ホスト名、メールアドレス、IPアドレス、URL、ASN、人名、侵害名などを収集・正規化する。CLI、ローカルのHarvestView、REST APIから利用できる。

## 目的・背景

- 許可されたセキュリティ評価の初期偵察段階で使うツール。対象は自身が所有するか、明示的なテスト許可を得たものに限る。

## 依存関係

- README記載のクイックスタートではPython 3.14とuvが必要。uvがリポジトリの`.python-version`を使って必要なPythonを選択する。

## 実行条件

- 初回の例ではAPIキー不要のP0パッシブ情報源を使用する。パッシブでも選択した提供元には対象文字列が送られる。P1はDNS照会、P2は対象エンドポイントへの接続などを行い、選択した場合に実行される。許可された正確な対象と活動範囲を確認して使う。

## 最短手順

- `git clone https://github.com/laramies/theHarvester.git`、`cd theHarvester`、`uv sync`の後、`uv run theHarvester -d example.com -b crtsh,certspotter`を実行する。これはREADME記載の例であり、実際には許可された対象に置き換える。

## 変更履歴

- 2026-11-14: 初回登録
