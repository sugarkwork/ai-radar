---
repo: "resemble-ai/chatterbox"
name: "Chatterbox"
genre: "tts-audio"
url: "https://github.com/resemble-ai/chatterbox"
last_release: "v0.1.2"
flags: ["unverified"]
risk_notes: "公開元が案内する聴取評価の詳細と結果、生成速度、必要VRAM、透かしの検出性能は未検証。GitHubリリースの公開日は未確認。音声参照素材の利用許諾は個別に確認が必要。"
stars: 27726
forks: 3730
open_issues: 381
size_kb: 1557
language: "Python"
created: "2025-04-23"
updated: "2026-11-04"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/nuannuan_share/status/2119640438135242817"]
fetched_at: "2026-11-10T09:29:46Z"
---

# Chatterboxで台本からナレーションを生成する

## 出来ること

- 台本を入力して音声を生成し、WAVに保存できる。英語向けのTurboは笑い声などを指定するタグにも対応する。

## 目的・背景

- Resemble AIが公開する音声合成・音声変換プロジェクト。公開元はTurboの自然さ、表現力、総合的な好みを比較する聴取評価をREADMEから案内している。

## 依存関係

- プロジェクト設定はPython 3.10以上を要求し、PyTorch、TorchAudio、Transformersなどを依存関係として宣言している。リポジトリのライセンスはMIT。

## 実行条件

- READMEによると開発・テスト環境はDebian 11とPython 3.11。Turboの掲載例はCUDAを指定する。ローカル実行にはモデル重みと実行環境が必要。

## 最短手順

- Python 3.11の仮想環境にREADMEの手順でchatterbox-ttsを導入する。
- CUDA環境でChatterboxTurboTTS.from_pretrained(device='cuda')を呼び、英語の台本をgenerateに渡す。モデルのサンプルレートを使ってtorchaudio.saveでWAVに保存する。
- AIエージェントから使う場合は、台本を受け取りWAVのパスを返すPython関数としてこの処理を公開し、エージェントのツールに登録する。

## 変更履歴

- 2026-11-10: 初回登録
