---
name: "OpenSpline"
genre: "tts-audio"
url: "https://github.com/openspline/openspline"
repo: "openspline/openspline"
license: "MIT"
stars: 433
language: "Python"
created: "2026-09-29"
updated: "2026-11-14"
forks: 54
open_issues: 7
commits_30d: 10
commit_cadence: "weekly"
commits_90d: 48
size_kb: 14391
archived: false
flags: ["unverified"]
risk_notes: "セルフホストではLinux/WSL2とNVIDIA GPUが必要とREADMEに記載。BlackwellおよびAmpere以前のGPUでは推論のハードウェア検証が必要とも記載されています。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119415527558840477"]
fetched_at: "2026-11-22T04:40:23.782720+00:00"
---

# OpenSpline

## 出来ること

- ポートレートと生成音声から、音声に同期したアバター動画を生成します。READMEではクラウドGPUまたは自前GPUでの利用、内蔵ビューアーやReact・Web Components、Python/Node対応を説明しています。

## 目的・背景

- 既存の音声AIエージェントにライブ顔アバターを追加する用途。プロンプト、ツール、マイク、音声プロバイダーは既存のものを利用する構成が示されています。

## 依存関係

- セルフホストのGPUサービスはNVIDIA GPUを使用。Python SDKはPython 3.10〜3.12、Node SDKはNode.js 20以上とREADMEに記載されています。

## 実行条件

- セルフホストではLinuxまたはWSL2とNVIDIA GPUが必要です。READMEによるとBlackwell向けにCUDA 12.8、旧世代NVIDIA GPU向けにCUDA 12.6を使用し、AMDとApple GPUは未対応です。クラウド利用はGPUやローカルインストールなしで試せるとREADMEに記載されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- セルフホストはREADME記載のインストーラーをLinux/WSL2のNVIDIA GPU環境で実行し、`sh ~/.local/share/openspline/run.sh`でデモを起動します。Python SDKは`pip install openspline`後、`Openspline().avatar("portrait.jpg", quality="low")`でアバターを作り、`avatar.stream(agent.audio_stream(), sample_rate=24000)`で生成PCM音声を渡します。

## 変更履歴

- 2026-11-23: 初回登録
