---
name: "LuxTTS"
genre: "tts-audio"
url: "https://github.com/ysharma3501/LuxTTS"
repo: "ysharma3501/LuxTTS"
license: "Apache-2.0"
stars: 5563
language: "Python"
created: "2026-01-23"
updated: "2026-06-05"
forks: 697
open_issues: 33
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 65
archived: false
flags: ["unverified"]
risk_notes: "READMEに記載された速度・音質・VRAM使用量は作者の説明であり、独立した実測結果ではありません。CPU/GPU/MPSでの利用例は示されていますが、実行環境や依存関係の詳細はREADMEだけでは確認できません。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/ruyi3699/status/2118954351532397028"]
fetched_at: "2026-11-15T09:18:34.217923+00:00"
---

# LuxTTS

## 出来ること

- LuxTTSはZipVoiceベースのテキスト音声合成モデルです。READMEは、参照音声を使った音声クローニング、48 kHz音声生成、GPUでリアルタイムの150倍超、CPUでリアルタイム超、1 GB以内のVRAMでの動作を特徴として挙げています。これらはREADMEに記載された作者の説明です。

## 目的・背景

- ZipVoiceと同じアーキテクチャを使い、4ステップに蒸留し、サンプリング手法を改良したとREADMEに説明があります。また、既定の24 kHz版の代わりに独自の48 kHzボコーダーを使用するとしています。

## 依存関係

- READMEの導入手順はリポジトリをcloneし、requirements.txtから依存パッケージをインストールします。モデル読み込み例はzipvoice.luxvoiceからLuxTTSをimportし、推論例はsoundfileとIPython.display.Audioを使用します。依存パッケージの詳細なバージョンはREADMEに記載されていません。

## 実行条件

- モデル読み込み例ではGPU（cuda）、CPU（threads=2）、MacのMPSを指定できます。推論例ではWAVを書き出す際にサンプルレート48000を指定します。音声クローニングには最低3秒の音声ファイルを使うようREADMEが案内しています。

## 最短手順

- README記載の手順: `git clone https://github.com/ysharma3501/LuxTTS.git`、`cd LuxTTS`、`pip install -r requirements.txt`。Pythonで`from zipvoice.luxvoice import LuxTTS`を読み込み、`LuxTTS('YatharthS/LuxTTS', device='cuda')`（CPUは`device='cpu', threads=2`、Macは`device='mps'`）でモデルを作成します。`encode_prompt('audio_file.wav', rms=0.01)`で参照音声を符号化し、`generate_speech(text, encoded_prompt, num_steps=4)`で生成します。生成音声はREADME例のようにsoundfileで48000 HzのWAVとして保存します。

## 変更履歴

- 2026-11-15: 初回登録
