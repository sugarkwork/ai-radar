---
name: "Nakama"
genre: "agent-framework"
url: "https://github.com/ahmadrosid/nakama"
repo: "ahmadrosid/nakama"
flags: ["unverified"]
risk_notes: "READMEによると、Dockerのリセット手順はデータを破棄し、ポート4310を公開する無関係なコンテナも削除する。実行前に影響範囲を確認すること。"
stars: 802
forks: 137
open_issues: 60
size_kb: 48795
language: "TypeScript"
created: "2026-05-23"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Ryrenz/status/2118192835266519269"]
fetched_at: "2026-11-11T02:11:02.748871+00:00"
---

# Nakama

## 出来ること

- チーム向けのAIエージェント基盤。ダッシュボードでエージェントとチャットでき、各エージェントは個別のプロンプトファイル、ツール、スキル、メモリを持つ。Telegram、WhatsApp、Discord、Slack、Composioとの連携をREADMEが案内している。出典: https://github.com/ahmadrosid/nakama

## 目的・背景

- READMEでは、複数組織、招待とロール、エージェント間の分離を備えた、チーム向けの運用基盤として紹介されている。マネージドクラウドまたはDockerコンテナでのセットアップを案内している。出典: https://github.com/ahmadrosid/nakama

## 依存関係

- ローカル実行にはBunが必要。PM2を使う方法ではBunとNode.js 22.12以降が必要とREADMEに記載されている。Dockerでの実行方法も案内されている。出典: https://github.com/ahmadrosid/nakama

## 実行条件

- ローカルでは依存関係をインストールしてWebまたはサーバーを起動する手順がある。サーバー公開時はHTTPSプロキシの使用をREADMEが案内している。初回起動時、プロバイダーとAPIキーが未設定なら入力を求められ、設定は `~/.nakama/config.ini` に保存される。出典: https://github.com/ahmadrosid/nakama

## 最短手順

- README記載のDockerで試す手順は、イメージを取得し、`NAKAMA_SECRETS_KEY` を用意してコンテナを起動する方法。サーバー運用ではComposeを使い、バージョンを固定してHTTPSプロキシを設定するよう案内されている。ここではコマンドを実行していない。出典: https://github.com/ahmadrosid/nakama

## 変更履歴

- 2026-11-11: 初回登録
