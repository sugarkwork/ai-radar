---
name: "Henge"
genre: "other"
url: "https://github.com/Leviidev/Henge"
repo: "Leviidev/Henge"
license: "GPL-2.0"
stars: 2368
language: "C"
created: "2026-11-02"
updated: "2026-11-15"
forks: 208
open_issues: 130
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 8152
archived: false
flags: ["unverified"]
risk_notes: "iPadでの実機動作は未確認。iOS 17–26での外部ディスプレイ出力も実機未確認。Apple Accountへのサインインは失敗すると記載。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/Ryrenz/status/2119092525004657074"]
fetched_at: "2026-11-16T21:10:30.032027+00:00"
---

# Henge

## 出来ること

- iPhone/iPad上でmacOSを独自エミュレーターにより実行する。READMEによると、Macのarm64コードを独自JIT、MMU、デバイスで動かし、QEMUやVirtualization.frameworkは使用しない。Appleの復元イメージをダウンロードして端末上にインストールし、仮想GPUの描画命令をMetalで再生する。タッチパッド操作、キーボード・マウス、コピー＆ペースト、共有フォルダーに対応する。外部ディスプレイ出力にも対応すると説明されている。

## 目的・背景

- iOSはアプリにハイパーバイザーを提供しないため、Hengeは独自のJIT、MMU、デバイスを用いてMacのarm64コードをエミュレートするとREADMEに記載されている。

## 依存関係

- 利用時に必要なJITの手段として、StikDebug、TrollStore、TrollStore Lite、脱獄、またはiOS 26以降のHenge内蔵StikJIT helperが挙げられている。

## 実行条件

- iOS/iPadOS 17以降、A14またはM1以降のチップが必要。macOS Sequoia 15.6.1の場合、空き容量は約43 GB（ダウンロード17 GB、Mac領域26 GB）が必要。iPad対応は新しく、実機では未確認とREADMEに記載されている。

## 最短手順

- ReleasesからHenge.ipaを取得してSideStoreまたはAltStoreでサイドロードするか、Henge.tipaをTrollStoreまたはTrollStore Liteでインストールする。JITを有効にし、アプリのInstallタブでmacOS Sequoia 15.6.1を選択する。インストール中はHengeを開いたまま端末を電源に接続する。

## 変更履歴

- 2026-11-22: 初回登録
