---
repo: "HeyChengC/vibe-knowledge-film"
name: "vibe-knowledge-film"
genre: "video-gen"
url: "https://github.com/HeyChengC/vibe-knowledge-film"
license: "未確認（GitHub API は NOASSERTION）"
stars: 1191
language: "JavaScript"
created: "2026-10-06"
updated: "2026-10-13"
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: [unverified]
risk_notes: "ライセンス未確認（API は NOASSERTION、標準ライセンスファイル無し）。参照サンプルの転用可否も不明。"
forks: 112
open_issues: 0
commits_30d: 2
commits_90d: 9
commit_cadence: "monthly"
size_kb: 47139
archived: false
fetched_at: "2026-11-09T21:44:57Z"
last_release: ""
last_release_at: ""
---

# vibe-knowledge-film

## 出来ること

- 知識系ショート動画（抖音で流行した「バイブ知識大賞」形式）を作るスキル。2モード: 「夜曲」＝抽象的で難解な知識を語る／「寓言」＝心理・行動のロジックを物語として見せる。
- 文案またはテーマを渡すと、画風選択 → 字幕稿 → 絵コンテ（分鏡表）→ コードプロジェクト生成まで進み、まず30秒のサンプルを出して確認後に全編を作る。
- 効果音を自動で付け、BGM は自分で差し替え可能。
- 仕組みは Canvas + JavaScript で毎フレーム描画し、ブラウザで1フレームずつ撮影して動画に圧縮、音を混ぜる（動画生成モデルは使わない）。

## 目的・背景

2026-10 公開。作者が市況のヒット作を分解して2つの画風にまとめたもの。サンプルとして「夜曲: タンパク質折り畳み（2024年ノーベル化学賞）」「寓言: 鳩の迷信」の頭33秒が入っている。

## 依存関係

- Python（`pip install -r requirements.txt`）、`python -m playwright install`。
- ローカルに Google Chrome と ffmpeg が必要（レンダリングはローカルの Chrome を開く）。
- フォントは SIL Open Font License のものを同梱せず、`get_fonts.py` を一度実行して取得する。

## 実行条件

- 中国語コンテンツ前提（字幕・フォント・音声）。日本語での運用は未確認。
- **ライセンス表記が不明確**（GitHub API 上 NOASSERTION、リポジトリに標準ライセンスファイルが見当たらない）。利用条件は作者への確認が必要。
- リポジトリ内の参照サンプルは学習用で、そのまま自分の作品として公開できない（ポスト記載。README に同等の明記は未確認）。

## 最短手順

```bash
git clone https://github.com/HeyChengC/vibe-knowledge-film.git
cd vibe-knowledge-film
pip install -r requirements.txt
python -m playwright install
python get_fonts.py
# 以降はエージェントに文案とともに依頼
```

## 変更履歴

- 2026-11-03: 初回登録（star 978 / pushed 2026-10-13 / ライセンス未確認）
