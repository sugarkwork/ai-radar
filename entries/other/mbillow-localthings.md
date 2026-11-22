---
name: "LocalThings"
genre: "other"
url: "https://github.com/mbillow/localthings"
repo: "mbillow/localthings"
license: "MIT"
stars: 1383
language: "Python"
created: "2026-06-30"
updated: "2026-11-15"
forks: 141
open_issues: 92
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 6485
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/Ryrenz/status/2119137828927910070"]
fetched_at: "2026-11-17T03:14:10.066449+00:00"
---

# LocalThings

## 出来ること

- Home Assistantから、SmartThingsアプリに対応するSamsung家電を家庭内ネットワーク経由で操作・監視する。READMEでは洗濯機、乾燥機、冷蔵庫、エアコン、オーブンなどを挙げ、電源、運転モード、開始・一時停止・停止、温度、残り時間、ドア状態、エネルギー使用量など、家電が報告する情報に応じた操作項目やセンサーを作成すると説明している。プッシュ対応機器は状態変化を受信し、それ以外は30秒ごとに確認する。

## 目的・背景

- Samsung家電とHome Assistantを、クラウドアカウントに依存せず家庭内ネットワークで接続する。READMEによると、初回の家電追加時には公開識別子の取得のためSamsungサーバーへ一度接続するが、その後はサーバーへ接続せずに動作する。

## 依存関係

- Home Assistantが必要。家電との通信にはOCF、CoAP over DTLSを使用し、プロトコル層はsmartthings-localライブラリが実装する。

## 実行条件

- 家電のIPアドレスを指定してセットアップする。初回の家電追加では公開識別子取得のためインターネット接続が必要。以降の家電追加はIPアドレスのみで、インターネット接続不要とREADMEに記載。自動証明書を拒否する一部機器では事前共有鍵が必要になる場合がある。

## 最短手順

- HACSのIntegrationsからLocalThingsをダウンロードするか、HACSを使わず`custom_components/localthings/`をHome Assistant設定内の`custom_components/`へコピーしてHome Assistantを再起動する。次にSettings > Devices & Services > Add Integration > LocalThingsを開き、家電のIPアドレスを入力する。

## 変更履歴

- 2026-11-22: 初回登録
