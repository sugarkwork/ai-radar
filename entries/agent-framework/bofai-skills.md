---
name: "BANK OF AI Skills"
genre: "agent-framework"
url: "https://github.com/BofAI/skills"
repo: "BofAI/skills"
license: "MIT"
stars: 164
language: "JavaScript"
created: "2026-03-02"
updated: "2026-11-18"
forks: 24
open_issues: 5
commits_30d: 12
commit_cadence: "weekly"
commits_90d: 54
size_kb: 4119
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/joejossy_12/status/2119196000963154122"]
fetched_at: "2026-11-18T08:13:22.004880+00:00"
---

# BANK OF AI Skills

## 出来ること

- AIエージェント向けの再利用可能なブロックチェーン作業スキルを提供する。README記載の例は、TRONウォレット操作、SunSwapの価格照会・スワップ・流動性操作、SunPerpの市場情報・注文・ポジション管理、TronScanのチェーンデータ照会、USDDの残高確認やスワップなど。

## 目的・背景

- BANK OF AIチームが作成した、プラットフォームに依存しないDeFi向け実用スキル集。各スキルにブロックチェーン作業の知識と手順をまとめ、エージェントによる特定のワークフロー実行を支援するとREADMEは説明している。

## 依存関係

- READMEによると、スキル定義のインストールでは外部CLI依存関係はインストールされない。wallet-cliは`@tron-walletcli/wallet-cli@4.14.0`、SunSwapとSunPumpは`sun-cli`を利用する。その他の外部依存関係は個別スキルの要件による。

## 実行条件

- READMEの案内は`npx skills add https://github.com/BofAI/skills/tree/main`で安定版mainからスキルと利用するエージェント基盤を選択して導入する方法。ウォレットやAPI認証の要否はスキルと操作によって異なり、公開市場照会や読み取り専用照会には認証不要の例がある。取引や非公開API操作にはウォレット、APIキーまたは署名鍵が必要な場合がある。

## 最短手順

- README記載のコマンド`npx skills add https://github.com/BofAI/skills/tree/main`を実行し、プロンプトに従ってスキルとエージェント基盤を選択する。導入後は対象のスキルファイルをエージェントに読ませるか、対応する作業を自然言語で依頼する。

## 変更履歴

- 2026-11-23: 初回登録
