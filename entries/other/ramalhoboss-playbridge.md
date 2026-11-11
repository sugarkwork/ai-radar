---
name: "PlayBridge"
genre: "other"
url: "https://github.com/ramalhoboss/PlayBridge"
repo: "ramalhoboss/PlayBridge"
stars: 15
forks: 1
open_issues: 1
size_kb: 10438
language: "Python"
created: "2026-10-29"
updated: "2026-11-06"
archived: false
license: "GPL-3.0"
commits_30d: 17
commits_90d: 17
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/nuno_leugim_10/status/2120302252569379293"]
fetched_at: "2026-11-11T01:33:26.777451+00:00"
---

# PlayBridge

## 出来ること

- READMEは、PS5のゲーム映像・音声をWindows PCへ配信し、PS5のゲーム一覧を表示して起動できると説明しています。録画、インスタントリプレイ、Go liveではゲーム音声にマイク音声を混ぜられます。可変リフレッシュレートにも対応すると記載されています。出典: https://github.com/ramalhoboss/PlayBridge

## 目的・背景

- READMEは、HDMIキャプチャーカードや公式Remote Playクライアント、PSN Remote Playのペアリングを使わずにPCでPS5のゲーム映像・音声を扱う用途として説明しています。利用には対応するPS5環境が必要です。出典: https://github.com/ramalhoboss/PlayBridge

## 依存関係

- READMEに記載された要件は、ファームウェア13.60のPS5と動作中のhomebrew/jailbreak環境、Payload ManagerのELF loader、64-bit Windows PC、ステレオ音声出力です。GPU映像出力にはDirect3D 11と動画デコード対応が必要とされ、利用時はPS5とPCを同じローカルネットワークに接続します。出典: https://github.com/ramalhoboss/PlayBridge

## 実行条件

- 自動ロードにはPayload ManagerのELF loaderがTCP 9021番ポートで待ち受けている必要があります。PlayBridgeはポート9076で接続するとREADMEに記載されています。ペイロードはファームウェア値0x13600007を確認し、他のファームウェアはこのビルドでサポートされません。Windows 11がテスト環境として記載され、他のWindows版は未検証です。出典: https://github.com/ramalhoboss/PlayBridge

## 最短手順

- 1. PS5でPayload Managerを起動し、ポート9021のELF loaderを利用可能にします。2. Windows PCでPlayBridge.exeを開きます。3. SettingsのConsoleでPS5を検出するかローカルIPを入力します。4. Pictureで画質プロファイルを選び、ELF already loaded in Payload Managerをオフにして設定を保存します。READMEによると、アプリが内蔵ELFを送信して接続します。出典: https://github.com/ramalhoboss/PlayBridge

## 変更履歴

- 2026-11-11: 初回登録
