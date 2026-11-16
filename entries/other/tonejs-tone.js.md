---
name: "Tone.js"
genre: "other"
url: "https://github.com/Tonejs/Tone.js"
repo: "Tonejs/Tone.js"
stars: 14918
forks: 1094
open_issues: 52
size_kb: 26161
language: "TypeScript"
created: "2014-03-11"
updated: "2026-11-15"
archived: false
license: "MIT"
commits_30d: 38
commits_90d: 80
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/xoom777/status/2122155858499109073"]
fetched_at: "2026-11-16T06:25:08.839455+00:00"
---

# Tone.js

## 出来ること

- ブラウザー上の音楽アプリ向けに、シンセサイザーやエフェクト、サンプル再生、AudioContext時間に沿ったイベントのスケジューリングを提供する。Transportを使ってイベントやパートを同期できる。

## 目的・背景

- READMEによると、ミュージシャンとオーディオプログラマー双方に親しみやすいWeb Audioフレームワークを目指し、DAWにあるような共通機能と、独自のシンセサイザー・エフェクト・制御信号を作るための構成要素を提供する。

## 依存関係

- READMEに記載された依存関係の情報は確認できない。

## 実行条件

- READMEはブラウザーでの利用を説明している。ブラウザーの音声再生はユーザー操作前には開始されず、クリックやキー操作などのイベントからTone.start()を呼び、そのPromiseの解決後に再生・スケジューリングするよう記載されている。

## 最短手順

- README記載の手順: npm install toneで導入し、JavaScriptでimport * as Tone from "tone";と読み込む。ユーザー操作イベント内でawait Tone.start()を実行した後、const synth = new Tone.Synth().toDestination();と作成し、synth.triggerAttackRelease("C4", "8n");で音を鳴らす。

## 変更履歴

- 2026-11-16: 初回登録
