---
name: "music-skill"
genre: "coding-agent"
url: "https://github.com/owoevan-dev/music-skill"
repo: "owoevan-dev/music-skill"
license: "MIT"
stars: 241
language: "Python"
created: "2026-11-02"
updated: "2026-11-17"
forks: 29
open_issues: 0
commits_30d: 45
commit_cadence: "daily"
commits_90d: 45
size_kb: 62764
archived: false
flags: ["unverified"]
risk_notes: "READMEで参照されるInstall節の内容は確認できていないため、レンダラーや音源バンクの詳細な依存関係・導入条件は未確認です。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/GitTrend0x/status/2122653626900332544"]
fetched_at: "2026-11-17T23:27:40.947791+00:00"
---

# music-skill

## 出来ること

- エージェントがオリジナルの器楽曲を作曲し、楽譜を確認してサンプル音源で演奏、ミックス、マスタリングするとREADMEは説明しています。MP3・WAVに加え、MIDI、パートごとのステム、編集して再レンダリングできるプロジェクトファイルを出力するとしています。

## 目的・背景

- READMEは、音楽生成モデルを使わずにエージェントが各音符を作成する方式を掲げています。映像やゲームの長さ、カット位置、ループ長などに合わせた作曲や、変更箇所に応じた小節単位の書き換えを用途として説明しています。これらはREADME記載の機能・用途の説明であり、独立した実機検証ではありません。

## 依存関係

- READMEのQuick startでは、レンダラーとサウンドバンクのセットアップが必要とされています。具体的なソフトウェア名や依存関係は確認できていません。

## 実行条件

- READMEはPython 3.10以降と記載しています。セットアップ時に約3.7 GBをダウンロードすると説明しています。

## 最短手順

- Claude Codeでは`/plugin marketplace add owoevan-dev/music-skill`、続けて`/plugin install music-skill@music-skill`を実行します。Codexなど他のエージェントでは`npx skills add owoevan-dev/music-skill`を使う手順が示されています。その後、エージェントにレンダラーとサウンドバンクをセットアップさせ、自然文で曲を依頼します。

## 変更履歴

- 2026-11-22: 初回登録
