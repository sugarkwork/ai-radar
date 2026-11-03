---
repo: unicodef1wn/grokbot-field-notes
name: Grok Bot Field Notes
genre: agent-framework
url: https://github.com/unicodef1wn/grokbot-field-notes
license: MIT
stars: 662
language: Python
created: 2026-09-18
updated: 2026-09-20
added: 2026-11-03
sources:
  - https://x.com/thegreatest_sv/status/2117591176048005131
forks: 94
open_issues: 1
commits_30d: 0
commits_90d: 14
commit_cadence: monthly
size_kb: 11153
archived: false
fetched_at: "2026-11-03T15:42:21Z"
last_release: v1.0
last_release_at: 2026-09-20
---

# Grok Bot Field Notes

## 出来ること

- xAI の Grok Bot チームのエンジニア3名が、空のリポジトリから 72 時間のライブ配信で製品を作り切った際の運用知識を配布する。
- `AGENTS.md` を自分のリポジトリに置くだけで、ルール・プレイブックが効き始める。
- 69 個のボットロール、9 個のプレイブック、40 件の「壊れたこと」の失敗ログを収録。
- 24 ページのガイド PDF（リリースから取得可）と、多言語版（中国語訳）が存在。

## 目的・背景

マルチエージェント編成の実運用ノウハウを、きれいに整形された「成功事例」ではなく失敗込みで公開している点が特徴。cURL 一発で `AGENTS.md` を取得できる導線を用意している。2026-09 作成、662 star。同種の写しが複数存在するため、本家はこのリポジトリ。

## 依存関係

- なし（Markdown / PDF が中心）。
- 適用先のエージェント（Grok Bot / Claude Code / Cursor など AGENTS.md を読むもの）。
- 補助スクリプトに Python を使用。

## 実行条件

- OS 不問。GPU 不要。
- 適用先エージェントが `AGENTS.md` 規約に対応していること（非対応なら手動で指示に貼る）。

## 最短手順

```bash
curl -o AGENTS.md https://raw.githubusercontent.com/unicodef1wn/grokbot-field-notes/main/AGENTS.md
```

## 変更履歴

- 2026-11-03: 初回登録（star 662 / pushed 2026-09-20）
