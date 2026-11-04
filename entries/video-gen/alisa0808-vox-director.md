---
repo: Alisa0808/vox-director
name: vox-director
genre: video-gen
url: https://github.com/Alisa0808/vox-director
license: MIT
language: Python
created: 2026-07-10
updated: 2026-10-05
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/dopamine_crypto/status/2117557411363860742
flags: []
risk_notes: ""
stars: 2608
forks: 365
open_issues: 6
commits_30d: 1
commits_90d: 2
commit_cadence: monthly
size_kb: 53626
archived: false
fetched_at: "2026-11-04T01:23:42Z"
---

# vox-director

## 出来ること

- 題材を一行渡すと、**Vox 風の紙コラージュ解説動画**を最後まで作るエージェントスキル。台本・画像・動き・ナレーション・音楽・字幕をまとめて mp4 にする。
- 見た目の作り込みが特徴。破れた紙の縁、テープ、新聞の切り抜き、網点、場面ごとの単色背景など、Vox の解説映像で使われるコラージュ表現を再現する。
- 実行基盤は Atlas Cloud（生成）＋ ffmpeg（合成）。Claude Code / Codex などのコーディングエージェントから呼び出す。
- DSH プラグインとしても動作する（トピックに `dsh-plugin`）。

## 目的・背景

2026-07 公開、★2,608。ショート動画の量産を狙ったものだが、単なるスライド＋読み上げではなく「紙コラージュ」という特定の様式に振り切っている点が他と違う。

## 依存関係

- Python、ffmpeg
- Atlas Cloud の API（画像・音声・動画の生成）
- 呼び出し元のエージェント（Claude Code / Codex / DSH）

## 実行条件

- 生成はクラウドAPI前提。API キーと従量課金。
- ディスク: リポジトリ約52MB（素材は生成時に増える）。
- 出力は解説・広告向けの様式で、任意の映像スタイルに合わせる用途には向かない。

## 最短手順

```text
エージェントにスキルとして導入し、題材を一行で渡す（README 参照）
```

## 変更履歴

- 2026-11-04: 初回登録（★2,608 / MIT / 最終push 2026-10-05）
