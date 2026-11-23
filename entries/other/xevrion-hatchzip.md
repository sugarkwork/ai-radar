---
name: "HatchZip"
genre: "other"
url: "https://github.com/xevrion/hatchzip"
repo: "xevrion/hatchzip"
license: "Apache-2.0"
stars: 2968
language: "Rust"
created: "2026-10-21"
updated: "2026-11-16"
forks: 102
open_issues: 15
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 6765
archived: false
flags: ["unverified"]
risk_notes: "READMEによるとWindows版とmacOS版はコード署名されていない。Windowsでは保護警告を経て実行する手順が案内されている。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/awe0_io/status/2119255490920321262"]
fetched_at: "2026-11-18T05:12:30.540262+00:00"
---

# HatchZip

## 出来ること

- Windows・macOS・Linux向けのデスクトップアプリとCLI。ZIP、7z、RAR、tar、圧縮tar、分割アーカイブを展開中に縮小し、アーカイブが占めていた領域を出力に再利用する。READMEでは、展開前の空き容量確認、停止・クラッシュ後の再開、アーカイブを保持する通常展開も説明している。

## 目的・背景

- 大きなアーカイブを展開する際、アーカイブと展開後のファイルを同時に置く空き容量を確保しにくい状況を対象にしている。README記載の例では、出力が200 GBのゲームデータについて、従来方式はアーカイブと合わせて380 GB、HatchZipは200 GBを少し超える容量が必要としている。これはREADMEの説明であり、独立検証ではない。

## 依存関係

- READMEに記載された依存関係の説明は確認できなかった。

## 実行条件

- README記載の対応OSはWindows 10・11、macOS（Apple Silicon・Intel）、Linux。対応ファイルシステムは、ファイルを縮小できるものと説明されている。ZIPやtarでは最大の単一ファイル、7zではソリッドブロックが、一度に解放できる容量に関係する。

## 最短手順

- READMEの案内に従い、GitHub Releasesまたはhatchzip.devから対象OS用の配布物を入手し、インストールする。アーカイブを右クリックして「HatchZip」から「Extract here」を選ぶか、アプリでアーカイブを開いて「Extract」を選択する。実行前に空き容量の確認結果が表示される。

## 変更履歴

- 2026-11-23: 初回登録
