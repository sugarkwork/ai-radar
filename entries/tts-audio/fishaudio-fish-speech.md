---
name: "Fish Speech"
genre: "tts-audio"
url: "https://github.com/fishaudio/fish-speech"
repo: "fishaudio/fish-speech"
license: "unknown"
stars: 33764
language: "Python"
created: "2023-10-10"
updated: "2026-11-14"
forks: 2946
open_issues: 28
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 15
size_kb: 33277
archived: false
flags: ["unverified"]
risk_notes: "READMEによるとコードベースと関連モデル重みはFish Audio Community Licenseだが、S2-Proの重みはFish Audio Research License。利用前にLICENSEで条件を確認すること。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/DivyanshT91162/status/2119134534134600107"]
fetched_at: "2026-11-17T07:14:07.133619+00:00"
---

# Fish Speech

## 出来ること

- Fish Speechはテキストからの音声生成、音声クローニング、複数話者生成、自然言語による感情・韻律制御に対応する。READMEはDrama 3について複数キャラクターのシーン生成、長文音声、音声の部分編集、複数ターンの修正を記載している。S2-Proでは話者IDによる複数話者生成と、参照音声10〜30秒を使った音声クローニングを説明している。これらはREADME記載の機能説明であり、独立した実機評価ではない。

## 目的・背景

- Drama 3はS2-Proの後継モデルとして紹介され、長尺音声、対話的な修正、編集機能を拡張したとREADMEに記載されている。READMEは公開ベンチマーク結果を示し、詳細な評価結果は技術レポートを参照するよう案内している。

## 依存関係

- 提示されたREADME部分では、実行時依存ライブラリやバージョンの一覧を確認できない。

## 実行条件

- READMEはInstallationとInferenceの案内先として https://speech.fish.audio/install/ および https://speech.fish.audio/inference/ を示し、環境構築、重みの取得、Dockerデプロイ、CLI・APIサーバー・WebUIの説明があるとしている。詳細な条件は提示されたREADME本文だけでは確認できない。

## 最短手順

- READMEは人向けに https://speech.fish.audio/install/ での導入と https://speech.fish.audio/inference/ での推論手順を案内している。LLMエージェント向けには、同じインストール案内に従ってFish Audio Drama 3またはS2-Proを導入・設定する手順を記載している。

## 変更履歴

- 2026-11-22: 初回登録
