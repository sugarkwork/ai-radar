---
name: "nihongo"
genre: "prompt-design"
url: "https://github.com/AnIT012/nihongo"
repo: "AnIT012/nihongo"
license: "MIT"
stars: 99
language: "Python"
created: "2026-11-16"
updated: "2026-11-18"
forks: 1
open_issues: 0
commits_30d: 31
commit_cadence: "daily"
commits_90d: 31
size_kb: 1251
archived: false
flags: ["unverified"]
risk_notes: "評価は作者1人または同じ会社のAIによる判定とREADMEに記載されている。ChatGPTとCodexのモデルでは同じ検証をしていない。評価結果は作者の報告であり、独立した実測ではない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/sincostansinhk/status/2122823344739451040"]
fetched_at: "2026-11-18T02:13:20.387585+00:00"
---

# nihongo

## 出来ること

- AIが書く日本語の生成や推敲を支援するエージェントスキル。読み手・目的・掲載場所・書き手に合わせた書き方を判断する手順をまとめている。普段の応答向けのLiteと、メールや資料など向けの詳しいFullがあり、数値・日付・条件・行為者を変えないことや、自然な文を無理に直さないことを方針としている。READMEにはSlack投稿の修正例がある。

## 目的・背景

- 定型句を避けるだけでなく、相手との距離に合った敬語、前置きの過不足、文のつながりなどを扱い、場面に合う自然な日本語を支援することを目指している。

## 依存関係

- スキル本体はMarkdownで、READMEはNode.jsがあればnpx経由で導入できると説明している。Pythonは推敲後の意味の崩れの確認に使う任意の要素で、標準ライブラリだけで動くとREADMEに記載されている。

## 実行条件

- Claude Code、Codexなどではスキルを所定の場所に導入する。Claude Codeで毎回Liteを読み込む設定例として、`~/.claude/CLAUDE.md` に参照行を追加する手順がある。ClaudeやChatGPTのアプリでは、`nihongo/` フォルダをzipにしてスキル画面からアップロードする手順が記載されている。生成内容の正しさは保証されないため、数字・日付・固有名詞は送信前に確認するようREADMEは案内している。

## 最短手順

- Node.js環境で `npx skills add AnIT012/nihongo -g` を実行して導入する。Claude Code向けに指定する場合は `npx skills add AnIT012/nihongo -g -a claude-code`。Liteを毎回使うには、READMEの案内に従って `ALWAYS.md` の内容または参照行を設定に加える。

## 変更履歴

- 2026-11-23: 初回登録
