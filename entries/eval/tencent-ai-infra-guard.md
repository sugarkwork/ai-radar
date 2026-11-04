---
repo: "Tencent/AI-Infra-Guard"
name: "AI-Infra-Guard (A.I.G)"
genre: eval
url: "https://github.com/Tencent/AI-Infra-Guard"
license: "Apache-2.0"
stars: 7379
language: "Python"
created: "2024-12-25"
updated: 2026-11-03
added: "2026-11-04"
first_seen: "2026-11-04"
sources: []
flags: []
risk_notes: ""
forks: 735
open_issues: 24
size_kb: 165597
archived: false
commits_30d: 67
commits_90d: 100
commit_cadence: daily
last_release: v4.6.8
fetched_at: "2026-11-04T22:51:39Z"
last_release_at: 2026-10-29
---

# AI-Infra-Guard (A.I.G)

## 出来ること

- AI 構成物のセキュリティ検査を1つの Web UI にまとめたプラットフォーム（Tencent Zhuque Lab）。個別のスキャナを単体 CLI としても配布している。
- **AI Infra Scan**: 公開されている AI サービス・推論基盤の構成を外部から検査する（`pip install aig-infra-scan`）。
- **Model Scan**: モデルエンドポイントの安全性評価（`pip install aig-model-scan`、OpenAI 互換 API を指定）。
- **MCP Scan**: MCP サーバーの実装を静的に検査し SARIF で出力（`pip install aig-mcp-scan`）。ツール定義の危険な記述や権限の広さを見る。
- **Agent Scan / Skills Scan**: エージェントとスキルの構成検査。
- **LLM jailbreak evaluation**: モデルのジェイルブレイク耐性を評価するテスト群（防御側の評価用途）。

## 目的・背景

「AI を組み込んだシステム」の攻撃面（プロンプト、ツール定義、MCP、推論基盤）を検査するためのレッドチーミング基盤。2024-12 公開、Tencent のセキュリティ研究チームが継続更新している。単体のスキャナを pip で入れて CI に組み込む使い方と、Docker で一式立ち上げて画面から使う使い方の両方を用意している。

## 依存関係

- Docker（一式起動の場合）。単体スキャナは Python パッケージ。
- Model / MCP スキャンは対象モデルの API キー、またはスキャン対象リポジトリのパスを渡す。
- Docker 版の推奨要件は README に RAM・ディスクの表がある（構成により変動）。

## 実行条件

- ライセンスは Apache-2.0。★7,372、30日で67コミットと活発。
- ジェイルブレイク評価のテスト群を含むため、**攻撃プロンプトの集まりでもある**。自組織のモデル／エージェントの耐性評価という用途に限って使い、第三者への攻撃には使わない。
- ワンクリック導入スクリプトは `curl … | bash` 形式（Docker を自動導入して起動する）。内容を確認してから実行する。

## 最短手順

```bash
# 一式（Web UI）
curl https://raw.githubusercontent.com/Tencent/AI-Infra-Guard/refs/heads/main/docker.sh | bash

# 単体: MCP サーバーの静的検査
pip install aig-mcp-scan
aig-mcp-scan --repo /path/to/mcp-server -o result.sarif.json
```

## 変更履歴

- 2026-11-04: 初回登録（★7,372 / Apache-2.0 / 最終push 2026-11-03 / v4.6.8）
