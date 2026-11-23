---
name: "FunClip"
genre: "other"
url: "https://github.com/modelscope/FunClip"
repo: "modelscope/FunClip"
license: "MIT"
stars: 6576
language: "Python"
created: "2023-05-17"
updated: "2026-11-01"
forks: 778
open_issues: 19
commits_30d: 6
commit_cadence: "weekly"
commits_90d: 24
size_kb: 45517
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:14:58.932641+00:00"
---

# FunClip

## 出来ること

- READMEによると、FunASRの音声認識結果からテキスト区間や話者を選んで動画を切り出せます。複数区間の切り出し、動画全体と対象区間のSRT字幕出力にも対応すると説明されています。Paraformer、SeACo-Paraformerのホットワード設定、CAM++による話者認識のほか、SenseVoiceやMOSSの利用方法も案内されています。これらはREADME記載の機能説明であり、独立した動作検証ではありません。

## 目的・背景

- READMEは、FunClipをローカル配置できるオープンソースの自動動画クリッピングツールと説明しています。Gradioで操作し、サーバー上に配置してブラウザーからアクセスする使い方も記載されています。

## 依存関係

- READMEはPython 3.12の仮想環境とrequirements.txtによる導入を案内しています。PyTorchとtorchaudioは利用環境に合う組み合わせを先に導入するよう記載されています。現行のモデル・字幕互換経路にはfunasr>=1.4.9が必要で、Gradio 4ランタイムを使用します。標準の字幕クリッピングにはImageMagickは不要で、内蔵字幕レンダラーはPillowを使用します。

## 実行条件

- README記載の導入手順は、リポジトリを取得し、Python 3.12の仮想環境を作成・有効化し、requirements.txtをインストールしてから起動するものです。モデル重みはソースアーカイブに含まれず、FunClip起動時に別途ダウンロードされると説明されています。MOSSを使う場合は、READMEに記載されたvLLM転写サービスが必要です。

## 最短手順

- READMEのPython環境向け手順：`git clone https://github.com/modelscope/FunClip.git`、`cd FunClip`、`python3.12 -m venv .venv`、仮想環境を有効化、`python -m pip install -r requirements.txt`、`python -m pip check`、`python funclip/launch.py --help`。起動例は `python funclip/launch.py` です。READMEは既存環境でrequirementsを更新してから再起動する手順も案内しています。

## 変更履歴

- 2026-11-23: 初回登録
