---
repo: "facebookresearch/audiocraft"
name: "AudioCraft / MusicGen"
genre: "tts-audio"
url: "https://github.com/facebookresearch/audiocraft"
license: "MIT"
stars: 23835
language: "Jupyter Notebook"
created: "2023-06-08"
updated: "2026-03-03"
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 2713
open_issues: 401
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 25025
archived: false
fetched_at: "2026-11-09T21:43:02Z"
last_release: ""
last_release_at: ""
---

# AudioCraft / MusicGen

## 出来ること

- 音声生成・処理の研究用 PyTorch ライブラリ。EnCodec（ニューラル音声圧縮／トークナイザ）と MusicGen（テキスト／メロディ条件付き音楽生成 LM）を同梱する。
- MusicGen はテキスト1行から数十秒の音楽を生成。メロディ条件付け（既存曲の旋律に沿わせる）と継続生成に対応。
- 推論だけでなく学習コードも入る（学習はリポジトリのローカルクローンが前提）。

## 目的・背景

Meta（facebookresearch）の音声生成研究リポジトリ。2023-06 作成。ポストでは MusicGen を別項目として並べているが、MusicGen は本リポジトリ内のモデルで、ポストのリンクも同一 URL。そのため MusicGen 単独のファイルは作らず本エントリに統合した（引用ポストの10項目は実質9リポジトリ）。

## 依存関係

- Python 3.9、PyTorch 2.1.0（README の指定バージョン）。
- ffmpeg（音声の読み書きに必要）。
- モデル重みは初回実行時に取得される。オフライン実行には事前ダウンロードが要る。

## 実行条件

- README が固定しているのは Python 3.9 + torch 2.1.0。より新しい torch での動作は保証されない。
- 生成は CPU でも動くが、実用的な速度には GPU が必要（必要 VRAM はモデルサイズ依存で README に明記なし＝未確認）。
- 出力の商用利用条件はモデルカード側の記載に従う（リポジトリの MIT とは別）。

## 最短手順

```bash
python -m pip install 'torch==2.1.0'
python -m pip install -U audiocraft
```

```python
from audiocraft.models import MusicGen
model = MusicGen.get_pretrained('facebook/musicgen-small')
model.set_generation_params(duration=8)
wav = model.generate(['80s pop with a driving bassline'])
```

## 変更履歴

- 2026-11-03: 初回登録（star 23,812 / pushed 2026-03-03 / MIT）
