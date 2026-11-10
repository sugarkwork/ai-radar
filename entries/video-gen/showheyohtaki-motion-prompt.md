---
repo: "showheyohtaki/motion-prompt"
name: "Motion Prompt"
genre: "video-gen"
url: "https://github.com/showheyohtaki/motion-prompt"
license: "MIT"
stars: 1568
language: "JavaScript"
created: "2026-10-14"
updated: "2026-10-29"
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: []
risk_notes: ""
forks: 167
open_issues: 0
commits_30d: 15
commits_90d: 15
commit_cadence: "weekly"
size_kb: 32948
archived: false
fetched_at: "2026-11-09T21:46:32Z"
last_release: ""
last_release_at: ""
---

# Motion Prompt

## 出来ること

- 「AI に頼むときの名前」を集めた辞書。モーショングラフィックスの動き、カメラワーク、UI 部品、ランディングページの効果、写真のルック／ライティングの名前を、動くサンプル＋一言の意味＋依頼文の例付きで引ける。
- 収録は 8セット × 24名 = 192。名前リストは英語・日本語・スペイン語・簡体字・繁体字の5言語版がある。
- ギャラリーは全サンプルが動く（https://showheyohtaki.github.io/motion-prompt/）。スキルを入れると「これ何て言う動き？」でギャラリーを開いてくれる。
- 自分の分野・言語で同じ形式の辞書を作るためのプロンプトも同梱。

## 目的・背景

「アイデアが無いのではなく、動きの名前を知らないだけ」という気づきから作られた 2026-10 のプロジェクト。動画生成モデルやコーディングエージェントへの指示語彙を揃える用途。

## 依存関係

- Node.js 18 以上（ギャラリーとルックアップスクリプト `scripts/motion-prompt.mjs` が標準ライブラリのみで動く）。
- `npx skills add showheyohtaki/motion-prompt` または `/plugin install motion-prompt@motion-prompt`。

## 実行条件

- 名称辞書なので、使うだけならインストール不要（README に明記）。
- 生成は行わない。実際の映像化は別のツール（動画生成モデル、コーディングエージェント、Remotion 等）側の仕事。
- ポストは約2,900 star としているが、2026-11-03 時点の GitHub API 実測は 1,174。

## 最短手順

```bash
npx skills add showheyohtaki/motion-prompt
node <skill-dir>/scripts/motion-prompt.mjs info   # データソースと件数を確認
```

## 変更履歴

- 2026-11-03: 初回登録（star 1,174 / pushed 2026-10-29 / MIT / ポスト記載の star 数と相違）
