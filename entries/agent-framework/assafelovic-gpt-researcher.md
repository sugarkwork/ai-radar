---
name: "GPT Researcher"
genre: "agent-framework"
url: "https://github.com/assafelovic/gpt-researcher"
repo: "assafelovic/gpt-researcher"
stars: 30630
forks: 4211
open_issues: 19
size_kb: 54578
language: "Python"
created: "2023-05-12"
updated: "2026-11-09"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118325722850697573"]
fetched_at: "2026-11-11T19:06:16.549783+00:00"
---

# GPT Researcher

## 出来ること

- Webとローカル文書を使った調査レポートの作成、情報源の要約と記録、調査結果の集約を行うとREADMEに記載されています。画像の取得・選別、JavaScript対応スクレイピング、PDFやWordなどへの出力、MCP連携も記載されています。

## 目的・背景

- READMEは、時間やリソースを要する調査、モデル知識の古さ、長文生成時のトークン制限、情報源の偏りや不足を課題として挙げています。これらの課題に対し、複数の調査エージェントで情報を集め、出典付きのレポートを作成する構成を説明しています。

## 依存関係

- READMEの基本手順ではPython 3.12以降、依存パッケージ、OpenAI APIキーとTavily APIキーを使用します。OpenAI互換API向けにOPENAI_BASE_URLを設定できると記載されています。追加機能や構成による依存関係の詳細はREADMEの範囲では確定できません。

## 実行条件

- README記載の基本手順では、APIキーを環境変数または.envファイルに設定し、依存パッケージをインストールして、uvicornでサーバーを起動します。PIPパッケージとしての利用例も記載されています。

## 最短手順

- READMEの手順は、Python 3.12以降を用意し、リポジトリを取得してディレクトリへ移動し、OPENAI_API_KEYとTAVILY_API_KEYを設定、requirements.txtの依存関係をインストールして、python -m uvicorn main:app --reloadで起動する流れです。コードの実行はこの審査では行っていません。

## 変更履歴

- 2026-11-11: 初回登録
