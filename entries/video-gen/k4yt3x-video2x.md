---
name: "Video2X"
genre: "video-gen"
url: "https://github.com/k4yt3x/video2x"
repo: "k4yt3x/video2x"
license: "AGPL-3.0"
stars: 22687
language: "C++"
created: "2018-02-24"
updated: "2026-03-07"
forks: 1982
open_issues: 147
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 574222
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/AIExplorerTim/status/2118242415219982564"]
fetched_at: "2026-11-11T08:19:22.224059+00:00"
---

# Video2X

## 出来ること

- 動画のアップスケーリング（filtering）とフレーム補間に対応します。READMEによると、Anime4K v4およびMPV互換GLSLシェーダー、Real-ESRGAN、Real-CUGAN、RIFEを利用できます。モデルや画質に関する説明はREADMEに記載された作者の説明です。

## 目的・背景

- Video2Xは、機械学習ベースの動画超解像とフレーム補間を行うフレームワークとして紹介されています。

## 依存関係

- READMEには、Real-ESRGAN、Real-CUGAN、RIFEをncnnとVulkan経由で利用するとあります。追加依存関係の詳細は公式ドキュメントを参照してください: https://docs.video2x.org/

## 実行条件

- README記載のハードウェア要件は、プリコンパイル済みバイナリではAVX2対応CPU、GPUではVulkan対応です。対応OSはWindowsとLinuxです。コンテナイメージはLinuxとmacOS向けに案内されています。

## 最短手順

- WindowsではREADME記載のインストーラーまたはリリースページから導入し、基本的なGUI操作は https://docs.video2x.org/running/desktop.html を参照してください。Linuxでは対応ディストリビューションのパッケージまたはAppImageを利用できます。コンテナでの起動方法は https://docs.video2x.org/running/container.html を参照してください。

## 変更履歴

- 2026-11-11: 初回登録
