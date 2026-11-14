---
name: "Hermes Agent"
genre: "agent-framework"
url: "https://github.com/NousResearch/hermes-agent"
repo: "NousResearch/hermes-agent"
language: "Python"
commit_cadence: "daily"
stars: 263292
forks: 59333
open_issues: 53308
size_kb: 1458600
created: "2025-07-22"
updated: "2026-11-14"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/RoundtableSpace/status/2118837821079212188"]
fetched_at: "2026-11-14T13:06:35.597718+00:00"
---

# Hermes Agent

## 出来ること

- READMEでは、複数プロバイダーのモデル利用、CLI/TUIでの対話、Telegram・Discord・Slack・WhatsApp・Signal向けゲートウェイ、cronによる定期実行、サブエージェントによる並列作業、過去の会話検索やスキル作成・改善を説明している。これらはREADME記載の機能説明であり、独立した実機検証結果ではない。

## 目的・背景

- Nous Research製のエージェントとして紹介されている。モデルプロバイダーを選択でき、ローカル端末以外の環境やメッセージングサービスから利用する構成も説明されている。

## 依存関係

- READMEのWindows向け説明では、ソースインストーラーがPython 3.14、Node.js、npm、pnpm、ripgrep、FFmpegおよびPython依存関係をPMに委ねるとしている。その他の環境や機能ごとの依存条件は、添付READMEだけでは網羅的に確認できない。

## 実行条件

- READMEにはLinux、macOS、WSL2、Windowsネイティブの導入手順がある。また、Android/Termuxはaarch64向けAPTリポジトリを使い、デスクトップ/サーバー向けインストーラーを使わないよう案内している。モデル利用には任意の対応プロバイダーを選ぶ説明がある。

## 最短手順

- README記載のLinux/macOS/WSL2向け導入コマンドは `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`。Windowsネイティブ向けはPowerShellで `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`。導入後は `hermes setup` で設定し、`hermes` で対話を開始する手順が示されている。

## 変更履歴

- 2026-11-14: 初回登録
