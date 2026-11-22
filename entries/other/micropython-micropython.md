---
name: "MicroPython"
genre: "other"
url: "https://github.com/micropython/micropython"
repo: "micropython/micropython"
license: "unknown"
stars: 22205
language: "C"
created: "2013-12-20"
updated: "2026-11-17"
forks: 9062
open_issues: 1605
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 77501
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/dextune/status/2119157945149923762"]
fetched_at: "2026-11-17T05:33:49.647675+00:00"
---

# MicroPython

## 出来ること

- 制約のあるプラットフォーム向けにPython 3.xの実装を提供する。READMEによると、Python 3.4構文の全体と一部の後続機能を実装し、基本的なデータ型と組み込みモジュールを備える。また、GPIO、Timers、ADC、DAC、PWM、SPI、I2C、CAN、Bluetooth、USBなど、ハードウェアや周辺機器へアクセスするMicroPython固有モジュールを提供する。データ型とモジュールの機能はPythonの一部に限られる。

## 目的・背景

- READMEでは、資源制約のあるシステムでPythonを動かすことを中心に据え、最小性、効率、整合性を設計上の価値としている。

## 依存関係

- リポジトリのビルドにはmake（BSD系ではgmake）、bash、gcc、Python 3.3以降が必要。rp2およびesp32ポートでは追加でCMakeを使用する。外部依存関係はlib/にサブモジュールとして置かれる。

## 実行条件

- マイクロコントローラ、Unix系（Linux、BSD、macOS、WSL）、Windows向けのポートがある。スクリプトは.pyソースまたは.mpyプリコンパイル済みバイトコードとして、デバイス上のファイルシステムから、または実行ファイルにfreezeして実行できる。

## 最短手順

- READMEの案内に従い、APIリファレンスと利用方法は公式オンラインドキュメントを参照する。リポジトリのビルドにはmake（BSD系ではgmake）を使用する。READMEには個別ポートのビルド・導入手順までは記載されていない。

## 変更履歴

- 2026-11-22: 初回登録
