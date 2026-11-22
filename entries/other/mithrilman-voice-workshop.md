---
name: "Voice Workshop (Officina della voce)"
genre: "other"
url: "https://github.com/MithrilMan/voice-workshop"
repo: "MithrilMan/voice-workshop"
license: "Apache-2.0"
stars: 37
language: "TypeScript"
created: "2026-11-08"
updated: "2026-11-08"
forks: 9
open_issues: 1
commits_30d: 31
commit_cadence: "daily"
commits_90d: 31
size_kb: 15783
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/FabioAngela79/status/2119235589136408721"]
fetched_at: "2026-11-17T20:10:56.879267+00:00"
---

# Voice Workshop (Officina della voce)

## 出来ること

- 人声を声帯のバズ、乱流のヒス、声道のフィルターに分けて、音と可視化で試せる。学習用の章立て、理論なしで触れるPlay、音源・声道・ノイズ・出力を個別に扱うLabを備える。頭部の調音操作、音声・母音・音素・メロディの再生、スペクトルやスペクトログラムなどの表示がある。READMEによると計算はブラウザー内で行う。

## 目的・背景

- 人声がどのように作られるかを、声帯、喉、口、フォルマント、ノイズ、スペクトログラムなどに分けて学び、操作・試聴できる対話型シミュレーター。READMEは関連動画「The Buzz and the Filter」の概念に沿うと説明している。

## 依存関係

- README記載の実行環境はNode.js 20.19+または22.12+（Vite 8）。ブラウザーで音声を扱うにはAudioWorklet対応の新しいChrome、Edge、Firefox、Safariが必要。Docker Composeで実行する方法も記載されている。

## 実行条件

- ブラウザー利用はREADME記載の公開デモ https://mithrilman.github.io/voice-workshop/ を開く。ローカル実行はNode.jsと対応ブラウザーを用意し、npm install、npm run devを実行する。READMEによると音声再生はブラウザーのユーザー操作後に開始する。

## 最短手順

- 公開デモを開き、ヘッダーの「▶ Sound / Suono」を押して音声を開始する。声道のハンドルやスライダー、音素・声・文・実験を操作する。ローカルで試す場合はREADME記載の要件を満たし、npm installの後にnpm run devを実行する。

## 変更履歴

- 2026-11-22: 初回登録
