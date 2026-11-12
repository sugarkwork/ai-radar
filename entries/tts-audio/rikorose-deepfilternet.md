---
name: "DeepFilterNet"
genre: "tts-audio"
url: "https://github.com/Rikorose/DeepFilterNet"
repo: "Rikorose/DeepFilterNet"
license: "unknown"
stars: 5002
language: "Python"
created: "2021-10-10"
updated: "2026-11-06"
forks: 552
open_issues: 64
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 1
size_kb: 179186
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIのlicense値はunknown。READMEからライセンスを確認できない。CLIバイナリは48 kHzのWAVのみ対応と記載。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/RealMarvelX/status/2118525010088251781"]
fetched_at: "2026-11-12T11:19:25.090022+00:00"
---

# DeepFilterNet

## 出来ること

- DeepFilterNetは、48 kHzフルバンド音声向けの音声強調フレームワーク。READMEは、ノイズのあるWAVファイルを処理するCLI、Python API、学習・評価・可視化機能、およびリアルタイムのノイズ抑制に使うLADSPAプラグインを案内している。CLIで対応する入力はサンプリングレート48 kHzのWAV。出典: https://github.com/Rikorose/DeepFilterNet

## 目的・背景

- READMEでは、DeepFilterNetをフルバンド音声向けの低複雑度な音声強調フレームワークとして説明している。論文としてDeepFilterNet、DeepFilterNet2、実時間音声強調に関する資料を紹介している。READMEの説明と論文紹介は作者側の記載であり、ここでは独立した性能評価として扱わない。出典: https://github.com/Rikorose/DeepFilterNet

## 依存関係

- Python利用ではPyTorchおよびtorchaudioが案内され、README記載の最低要件は用途別にPyTorch 1.9以上または手動導入手順で1.8以上。手動構築ではRust/Cargo、maturin、poetryを使う。学習用追加機能にはHDF5関連の依存があり、READMEはLinux限定としている。導入方法により要件が異なるため、実際の環境に対応した手順を確認すること。出典: https://github.com/Rikorose/DeepFilterNet

## 実行条件

- READMEはフレームワークの対応OSをLinux、macOS、Windowsとし、学習はLinuxでのみテスト済みと記載。付属デモはLinuxのみ。CLIのdeep-filterは48 kHz WAVに対応し、Python利用ではPyTorchバックエンドを選べると説明している。出典: https://github.com/Rikorose/DeepFilterNet

## 最短手順

- READMEによると、CLIを使う場合はリリースページからコンパイル済みdeep-filterバイナリを入手し、`deep-filter audio-file.wav` の形式で入力WAVを指定する。Python wheelの場合はPyTorchとtorchaudioを導入した後、`pip install deepfilternet` を実行し、`deepFilter path/to/noisy_audio.wav` で処理する。入力は48 kHz WAV。出典: https://github.com/Rikorose/DeepFilterNet

## 変更履歴

- 2026-11-12: 初回登録
