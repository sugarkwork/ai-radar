---
name: "Telegram Media Downloader"
genre: "other"
url: "https://github.com/Neet-Nestor/Telegram-Media-Downloader"
repo: "Neet-Nestor/Telegram-Media-Downloader"
license: "GPL-3.0"
stars: 6450
language: "JavaScript"
created: "2022-06-11"
updated: "2026-10-19"
forks: 637
open_issues: 76
commits_30d: 19
commit_cadence: "weekly"
commits_90d: 19
size_kb: 1152
archived: false
flags: ["unverified"]
risk_notes: "ダウンロード制限のあるコンテンツへの適用可否や利用条件は、Telegram側の権限・規約との関係をREADMEだけでは確認できない。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/bkdgiffug/status/2118637513862783231"]
fetched_at: "2026-11-13T06:25:23.508893+00:00"
---

# Telegram Media Downloader

## 出来ること

- Telegram Web のチャット、ストーリー、プライベートチャンネルで画像・GIF・音声・動画のダウンロード操作を追加するユーザースクリプト。ダウンロード制限が有効な場合に、画像・GIF・動画のボタンを追加するとREADMEは説明している。音声メッセージのダウンロードなど一部機能は /k/ 版のみ。ダウンロードパネルでは進行状況の確認、キュー、キャンセル、再試行が可能。出典: https://github.com/Neet-Nestor/Telegram-Media-Downloader

## 目的・背景

- Telegram Web の標準操作で保存できない場合にも、メディアのダウンロード操作を利用できるようにする。保存を許可しているチャットでは、Telegram Web の標準ダウンロードボタンを使うようREADMEは案内している。出典: https://github.com/Neet-Nestor/Telegram-Media-Downloader

## 依存関係

- ブラウザーに対応するユーザースクリプト管理拡張が必要。READMEはTampermonkey、Violentmonkey、Greasemonkey、Userscriptsなどを例示している。

## 実行条件

- Telegram Webapp上で使用する。README記載の対応版は /k/ と /a/ で、一部機能は /k/ のみ。転送中はTelegramタブを開いたままにする。直接保存に対応しないブラウザーでは、ダウンロードマネージャーへ渡す前にデータを保持するため、大きなファイルがブラウザー資源を多く使う場合がある。出典: https://github.com/Neet-Nestor/Telegram-Media-Downloader

## 最短手順

- ユーザースクリプト管理拡張を導入し、README記載のGreasy Fork掲載ページからスクリプトをインストールする。手動導入の場合はTampermonkey Dashboardに src/tel_download.js を追加してインストールする。出典: https://github.com/Neet-Nestor/Telegram-Media-Downloader

## 変更履歴

- 2026-11-13: 初回登録
