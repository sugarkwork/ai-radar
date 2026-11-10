---
repo: Win-Hao/music-mv
name: music-mv
genre: video-gen
url: https://github.com/Win-Hao/music-mv
author: Win-Hao
license: MIT
stars: 116
language: Python
created: 2026-10-20
updated: "2026-10-20"
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/dextune/status/2117678193822085189
sources: []
forks: 5
open_issues: 0
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
size_kb: 29746
archived: false
fetched_at: "2026-11-09T21:47:02Z"
last_release: ""
last_release_at: ""
---

# music-mv

## 出来ること

- 曲（`song.mp3`）を渡すと、**全フレームをコードで描いた**ミュージックビデオを作るエージェントスキル。動画生成モデルは使わない。
- 六段階で進み、各段階で止まって人の OK を待つ: 曲を聴く → 画風を決める → キャラクターを描く → 脚本・絵コンテ → まず下書き → 本編。
- 曲の解析: 歌詞をタイムライン付き字幕にし、BPM・拍点・区間・急に静かになる箇所・低音が抜ける箇所を測り、曲の解釈も調べる。
- 画風は4種（**ピクセルゲーム風** 320×180 を1ピクセルずつ、24色パレット、ディザ、フレームごとに描き替え、歌詞はゲームのダイアログ枠／**紙のコラージュ絵本**／**クレヨン・水彩絵本**（p5.brush）／**紙の立体絵本**（浅い被写界深度・暖色光））。`reference.mp4` を置けば、その動画から配色・描法・リズム・トランジションを抽出して真似る。
- キャラクターの一貫性は、主人公を**1つのコードファイル**に書いて全ショットがそこから取ることで担保する。
- 自己検証: コンタクトシートで画面を確認し、フレーム差分でリズムを測り（スライドっぽい区間・意図しないハードカット・黒フレームを検出）、歌詞を1行ずつ照合し、音量を原曲に合わせる。
- スクリプト単体でも使える: `analyze_song.py`（BPM・拍点・区間・変化点）、`contact_sheet.py`（コンタクトシート／歌詞照合）、`video_rhythm.py`（切れ目・ショット長・静止区間・黒フレーム）、`finalize_audio.py`（原曲を元の音量で戻す）。

## 目的・背景

AI で MV を作る手段が動画生成に偏る中で、**コードで描く**方針を取るスキル。1〜1.5分の MV で7〜10時間、改版4〜9回が普通と明記されており、生成の一発性ではなく反復編集のワークフローとして設計されている。ドキュメントは中国語。2026-10-20 作成、同日最終 push、77 star。

## 依存関係

- Python 3.9+、`numpy` / `librosa` / `Pillow`（`pip install -r requirements.txt`）
- `ffmpeg`
- Node.js 18+（HyperFrames レンダラ用。初回にレンダラとヘッドレス Chrome を自動取得）
- 任意: Whisper（歌詞の自動書き起こし）
- エージェント: Claude Code / Codex / Cursor / Gemini CLI など SKILL.md を読めるホスト。`npx skills add` でも可

## 実行条件

- レンダリングは Canvas 系が速く、p5.brush の水彩は約0.3秒/フレーム（1分の映像で約20分）。
- 曲の著作権は原曲作者に帰属する。同梱の作例も音声なしの GIF のみで、歌入り動画は配布していない。
- 画風の学習に使う参照動画は自分で用意する前提。出力の商業利用条件は README に記載なし（未確認）。

## 最短手順

```bash
npx skills add Win-Hao/music-mv -g
# または
git clone https://github.com/Win-Hao/music-mv ~/.claude/skills/music-mv

mkdir my-mv && cd my-mv && cp /path/song.mp3 .
# エージェントに:
#   「给 song.mp3 做一支 MV，横屏，画风想要纸艺拼贴」
```

## 変更履歴

- 2026-11-04: 初回登録
