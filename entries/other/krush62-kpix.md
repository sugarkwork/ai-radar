---
name: "KPix"
genre: "other"
url: "https://github.com/krush62/KPix"
repo: "krush62/KPix"
license: "AGPL-3.0"
stars: 23
language: "Dart"
created: "2024-04-25"
updated: "2026-11-21"
forks: 2
open_issues: 8
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 11271
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/dextune/status/2119429745091686634"]
fetched_at: "2026-11-22T05:03:37.611458+00:00"
---

# KPix

## 出来ること

- READMEの説明によると、KPixは静止画とアニメーション向けのピクセルアートエディタです。インデックスカラーを使用し、パラメータからカラーパレットの色階調を生成します。描画ツール、色ランプに基づくシェーディング、参照・シェーディング・ディザリング・グリッド／遠近補助レイヤー、フレームごとの表示時間やオニオンスキンに対応します。PNG・WebPなどの画像、アニメーション形式、Aseprite・Gimp・Pixelorama・Photoshop形式への書き出し機能も説明されています。

## 目的・背景

- 作者によると、KPixは自身のピクセルアート制作手順に合わせた個人プロジェクトとして始まり、Flutterによるデスクトップ・タブレット開発の学習にも使われました。UIや作業手順には意図的な独自仕様があると説明されています。

## 依存関係

- README記載のLinux版では、libgtk-3-0、libblkid1、liblzma5が必要です。ファイル／ディレクトリ選択にはzenity、qarma、kdialogのいずれかが必要とされています。

## 実行条件

- READMEによると、Windows、Linux、Android、macOS、Webに対応します。Linuxでは記載の共有ライブラリが必要です。Android版はサイドロードで導入でき、作者はタブレットとスタイラスでの利用を想定しています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- WindowsはREADME記載のwingetコマンド `winget install --id krush62.kpix` で導入できます。Windowsのインストーラー／ポータブルZIP、LinuxのAppImage／Flatpak／tar.gz、AndroidのAPKも案内されています。LinuxのAppImageはデスクトップまたはターミナルから起動し、tar.gz版は展開後に `./kpix` を実行します。

## 変更履歴

- 2026-11-23: 初回登録
