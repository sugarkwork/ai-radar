---
repo: "wquguru/cicada"
name: "知了 Cicada"
genre: "tts-audio"
url: "https://github.com/wquguru/cicada"
last_release: "v1.8.0"
flags: ["unverified"]
risk_notes: "公開資料の確認のみ。認識・翻訳精度、遅延、話者識別、共有時の機密情報検出、実際の外部送信先は未検証。Lingの現行料金と無料枠の適用条件は提供元で未確認。"
pricing_detail: "アプリ本体はApache-2.0。開発元READMEはLingの月10元分の無料枠を会議約10〜50時間分と見積もる。利用時間は機能と使用量に依存する。"
stars: 2104
forks: 366
open_issues: 6
size_kb: 40282
language: "Swift"
created: "2026-11-01"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/wquguru/status/2117574970280923492"]
fetched_at: "2026-11-10T09:40:06+00:00"
---

# 知了 Cicada — 会議・配信の二言語字幕、通訳、AI議事録

## 出来ること

- 会議や配信の音声を二言語字幕にし、要約、議題、決定事項、タスクを整理する。決定事項やタスクから元の発言に戻れ、会議後はMarkdown、Word、SRTへ出力できる。

## 目的・背景

- 会議アプリにボットを参加させず、端末のシステム音声を取り込む構成。AppleシリコンMacでは標準設定で音声認識を端末内で行う。認識テキストの翻訳・議事録生成や、設定に応じた音声処理では外部サービスへの送信が発生する。

## 依存関係

- AppleシリコンMacではAppleの音声認識を使用。Ling構成では議事録にLing-3.1-flash、音声翻訳と音声合成にMing系モデルを使う。議事録には対応するAIサービスが必要で、音声クローニングはREADME上ではLing構成に限られる。Macで翻訳音声を会議アプリに渡すにはBlackHole 2chを使う。
- 本体はApache-2.0。外部AIサービスの料金や利用条件はサービスごとに適用される。

## 実行条件

- macOS 14.4以降（Appleシリコン／Intel）、Windows 10 2004以降、Ubuntu 22.04／24.04のデスクトップ、Android 10以降。AppleシリコンのmacOS 14.4〜15ではシステムの音声入力を有効にする。Intel MacはLingキー、Windows・Linux・Androidは対応するAIサービスのキーが必要。
- Macで字幕を使うにはシステム音声の収録権限が必要。READMEによるとMacアプリはAppleの公証を受けていない。

## 最短手順

- GitHub Releasesで対象OSとCPU向けの配布物を選び、掲載されているSHA-256を照合する。AppleシリコンMacではDMGからアプリケーションフォルダに移し、初回ガイドでシステム音声の収録を許可してサンプル会議の字幕を確認する。
- AI議事録を使う場合は、Cicadaの「設定 › AIサービス」で対応サービスとAPIキーを設定する。設定したAIサービスはCicadaから呼び出される。Macで会議相手に翻訳音声を届ける場合は、通訳設定でBlackHole 2chを導入する。

## 変更履歴

- 2026-11-10: 初回登録
