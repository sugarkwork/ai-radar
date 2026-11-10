---
repo: "obsproject/obs-studio"
name: "OBS Studio"
genre: "other"
url: "https://github.com/obsproject/obs-studio"
stars: 79247
forks: 11149
open_issues: 1206
size_kb: 87955
language: "C"
created: "2013-10-01"
updated: "2026-11-10"
archived: false
license: "GPL-2.0"
commits_30d: 41
commits_90d: 100
commit_cadence: "daily"
last_release: "33.0.1"
flags: ["unverified"]
risk_notes: "最新リリースの年とタイムゾーンを含む公開日時は未確認。収録品質・負荷、エージェント経由の接続と録画、発見投稿で言及されたOpus 5.5との連携は未検証。90日コミット数は100件以上を表す。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:58:52Z"
---

# OBS Studioで制作画面と音声を収録する

## 出来ること

- 画面やウィンドウ、カメラなどをシーンに配置し、音声と合わせて録画・配信できる。[公式クイックスタート](https://obsproject.com/kb/quick-start-guide)

## 目的・背景

- AIで作った映像や操作デモを、画面とナレーションを組み合わせて収録する工程に使える。公式READMEは映像のキャプチャ、合成、エンコード、録画、配信を用途としている。[公式README](https://raw.githubusercontent.com/obsproject/obs-studio/master/README.rst)
- 無償のオープンソースソフトウェア。公式READMEはGNU GPL v2以降で配布すると説明している。[公式README](https://raw.githubusercontent.com/obsproject/obs-studio/master/README.rst)

## 依存関係

- AIエージェントから操作する場合は、起動中のOBS Studioとobs-websocket対応クライアントが必要。OBS Studio 28.0.0以降はobs-websocketを標準同梱する。[obs-websocket公式README](https://github.com/obsproject/obs-websocket)

## 実行条件

- 公式の基本要件はWindows、macOS、Linux/Unixに分かれる。Linux/UnixではOpenGL 3.3対応GPUとX Window SystemまたはWaylandが必要。必要なCPU性能はエンコーダー、解像度、FPS、シーン構成で変わる。33.0のリリースノートではUbuntu 24.04のサポート終了も明記されている。[公式システム要件](https://obsproject.com/kb/system-requirements) [公式リリースノート](https://github.com/obsproject/obs-studio/releases/tag/33.0.1)

## 最短手順

- OBS Studioで自動構成ウィザードを実行し、シーンに画面またはウィンドウのキャプチャを追加する。音声ミキサーと保存先を確認して短く録画し、保存ファイルを再生して映像と音声を確認する。[公式クイックスタート](https://obsproject.com/kb/quick-start-guide)
- AIから呼ぶ場合は、OBSのツールメニューからWebSocketサーバーを有効にし、パスワード認証を設定する。エージェントから呼べる対応クライアントを同じ端末上のOBSに接続し、シーンを設定した状態でStartRecordとStopRecordを順に呼ぶ。[obs-websocket公式README](https://github.com/obsproject/obs-websocket) [公式プロトコル仕様](https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md?plain=1)

## 変更履歴

- 2026-11-10: 初回登録
