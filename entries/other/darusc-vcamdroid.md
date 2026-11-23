---
name: "VCamdroid"
genre: "other"
url: "https://github.com/darusc/VCamdroid"
repo: "darusc/VCamdroid"
license: "MIT"
stars: 521
language: "C++"
created: "2025-03-22"
updated: "2026-01-25"
forks: 63
open_issues: 16
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 48094
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/bkdgiffug/status/2119314977509282169"]
fetched_at: "2026-11-19T02:10:26.385437+00:00"
---

# VCamdroid

## 出来ること

- READMEによると、Android端末のカメラ映像をWindowsの仮想ウェブカメラとして利用する。USB（ADB）または同一Wi-Fi上で接続でき、前後カメラの切替、解像度変更、フラッシュ、映像の回転・反転・明るさ・コントラスト・彩度の調整を備えると説明されている。Zoom、OBS、Discord、Teamsなど標準ウェブカメラに対応するアプリで使えるとしている。

## 目的・背景

- スマートフォンのカメラ映像をPCのウェブカメラ入力として使うことを目的とする。READMEは、Android側のRTSP配信をWindowsクライアントで受け取り、SoftcamのDirectShowフィルターを通して仮想デバイスとして提供する構成を説明している。性能や遅延の独立測定は確認していない。

## 依存関係

- READMEでは、Android側のRTSP配信にRootEncoder、Windows側の受信・デコードにFFmpeg、仮想カメラにSoftcamを使用すると説明している。

## 実行条件

- README記載の利用条件は、Windows 10または11、Android 7.0以上。USB接続の自動インストールにはUSBデバッグが必要で、Wi-Fi接続ではPCとスマートフォンが同一ネットワークにあることが必要。仮想カメラの登録手順ではinstall.batを管理者として実行するよう記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの手順では、GitHub ReleasesからWindowsバイナリを取得して展開し、install.batを管理者として実行する。AndroidアプリはAPKを手動導入するか、USBデバッグを有効にしてinstall_apk.batで導入する。USB接続は両端でアプリを起動すると自動接続し、Wi-Fi接続は同一ネットワークでWindowsクライアントのQRコードをAndroidアプリから読み取って接続する。

## 変更履歴

- 2026-11-23: 初回登録
