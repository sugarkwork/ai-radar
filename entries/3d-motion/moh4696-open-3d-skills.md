---
repo: Moh4696/open-3d-skills
name: open-3d-skills
genre: 3d-motion
url: https://github.com/Moh4696/open-3d-skills
license: MIT
language: JavaScript
created: 2026-10-31
updated: 2026-10-31
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/dextune/status/2117522164140347849
flags: []
risk_notes: ""
stars: 220
forks: 31
open_issues: 0
commits_30d: 3
commits_90d: 3
commit_cadence: monthly
size_kb: 1714
archived: false
fetched_at: "2026-11-04T01:23:46Z"
---

# open-3d-skills

## 出来ること

- 3D・アニメーション付きの**Webサイトを作るためのエージェントスキル8種**。それぞれ実サイトで検証済みとしている。
- 収録スキル: コードからの three.js リアルタイムシーン／スクロールに連動する映像／Safari でも再生できる透過動画／カーソルを追うキャラクター／製品の分解図（exploded view）／AI によるモーション素材生成／ブラウザ上での見た目チェック／60fps 録画。
- Claude Code・Codex・Cursor・Gemini CLI に対応。

## 目的・背景

2026-10-31 公開、★220。3D 表現は「動くものを作れる人」に偏りがちなので、定番の演出をスキルとして固定し、エージェントが同じ品質で再現できるようにする狙い。

## 依存関係

- Node.js（three.js を含むフロントエンド）
- 各エージェント（Claude Code / Codex / Cursor / Gemini CLI）
- 録画・チェック系スキルはヘッドレスブラウザ（Playwright 等）

## 実行条件

- 生成物はブラウザで動くWebサイト。サーバ側のGPUは不要。
- 対応ブラウザの差（透過動画は Safari 向けの工夫が入っている）に注意。

## 最短手順

```text
スキルディレクトリを各エージェントの skills に配置（README 参照）
```

## 変更履歴

- 2026-11-04: 初回登録（★220 / MIT / 2026-10-31 公開）
