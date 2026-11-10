---
repo: "Vexa-ai/vexa"
name: "Vexa"
genre: "other"
url: "https://github.com/Vexa-ai/vexa"
license: "Apache-2.0"
stars: 2965
forks: 544
open_issues: 805
size_kb: 91894
language: "Python"
created: "2025-02-07"
updated: "2026-11-09"
archived: false
commits_30d: 4
commits_90d: 92
commit_cadence: "weekly"
last_release: "v0.12.28"
flags: ["unverified"]
risk_notes: "会議への参加、文字起こしの精度・遅延、話者割り当て、Macでの起動、MCP接続は独立実測なし。Jitsiのライブ検証はREADME上で保留。最新リリースの公開日時は年とタイムゾーンまで確認できなかった。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2115775716692533282"]
fetched_at: "2026-11-10T12:30:58+00:00"
---

# Vexa｜会議ボットと話者付き文字起こしを自前で運用

## 出来ること

- Google Meet・Microsoft Teams・Zoomにボットが参加し、話者付きの文字起こしをリアルタイムに取得できると開発元は説明している。発話が重なると話者欄が空になる場合がある。[公式README](https://github.com/Vexa-ai/vexa/blob/main/README.md)

## 目的・背景

- 会議内容をGit管理のMarkdownにまとめ、差分を追ったり、エージェントに過去の決定事項を尋ねたりできる。エージェント機能はセルフホスト構成で提供される。[公式README](https://github.com/Vexa-ai/vexa/blob/main/README.md)

## 依存関係

- Git、make、Docker Engine 26以上が必要。文字起こしには開発元が案内する試用向けの無料トークン、またはGPU上で自前運用するfaster-whisperサービスを使う。エージェントで会議内容を質問するにはLLM接続を別途設定する。[公式README](https://github.com/Vexa-ai/vexa/blob/main/README.md)

## 実行条件

- 本番の想定はLinux（Ubuntu 24.04）。MacではDocker Desktopで評価できるとされる。Compose本体はGPUなしで起動できる。既定では文字起こしサービスが未設定だとボット作成が503を返す。リポジトリはApache-2.0。[公式README](https://github.com/Vexa-ai/vexa/blob/main/README.md)
- GitHubの最新リリースページはv0.12.28を指し、Zoomでの文字起こしとローカル録音ストレージの変更を案内している。[公式リリース](https://github.com/Vexa-ai/vexa/releases/tag/v0.12.28)

## 最短手順

- 公式リポジトリをクローンして `make all` で公開済みイメージを起動し、`.env` で文字起こし先を設定する。`http://localhost:13000` のTerminalに会議URLを貼るとボットを参加させられる。[公式README](https://github.com/Vexa-ai/vexa/blob/main/README.md)
- AIから呼ぶ場合は、MCPクライアントに `http://localhost:18056/mcp` を登録し、起動時に発行されたAPIキーをBearer認証に設定する。`request_meeting_bot` に会議URLを渡し、`get_meeting_transcript` で話者・時刻・本文を取得する。[公式MCP文書](https://docs.vexa.ai/vexa-mcp)

## 変更履歴

- 2026-11-10: 初回登録
