---
name: "jevwire"
genre: "agent-framework"
url: "https://github.com/Brainwires/jevwire"
repo: "Brainwires/jevwire"
stars: 27
forks: 6
open_issues: 1
size_kb: 3243
language: "TypeScript"
created: "2026-09-17"
updated: "2026-11-06"
archived: false
license: "MIT"
commits_30d: 11
commits_90d: 43
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2120147118237114757"]
fetched_at: "2026-11-11T06:11:40.668057+00:00"
---

# jevwire

## 出来ること

- 状態と型付き質問を入力し、定義済みの回答候補に対する確率を返す分類モデルをハーネスに接続します。README記載では、7つのMCPツール、各ツールに対応する組み込み用のrun関数、Claude Codeのフックを提供します。生成、算術、数え上げ、日付比較、複数段階の推論には使わないと説明されています。出典: https://github.com/Brainwires/jevwire

## 目的・背景

- READMEでは、エージェントが任意に呼び出さない可能性のあるツールだけに依存せず、ハーネス側に必須チェックを組み込める構成として説明されています。Claude Codeプラグインはツール呼び出し前、取得結果の後、ターン終了前に判断を配置します。分類器によるノートはツール実行後に渡されるため、その実行を止めるものではないと記載されています。出典: https://github.com/Brainwires/jevwire

## 依存関係

- 全導入経路でNode.js 20以上が必要です。TypeSafe APIキーを使います。MCPサーバーとライブラリの例ではnpmパッケージ「@brainwires/jevwire」を利用します。出典: https://github.com/Brainwires/jevwire

## 実行条件

- APIキーがない場合、Claude Codeプラグインの判断フックは無効になり、決定的なパターンチェックのみ動作するとREADMEに記載されています。ライブラリではDecisionModelインターフェースを差し替えられ、テスト用のfakeも利用できると説明されています。出典: https://github.com/Brainwires/jevwire

## 最短手順

- Claude Codeプラグインの場合、Claude Codeで「/plugin marketplace add Brainwires/jevwire」、続けて「/plugin install jev@brainwires-jevwire」を実行し、プラグイン設定または起動シェルのTYPESAFE_API_KEYを設定して「/reload-plugins」を実行します。Bare MCP serverでは「claude mcp add jev -e TYPESAFE_API_KEY=sk-... -- npx -y @brainwires/jevwire」を使用します。出典: https://github.com/Brainwires/jevwire

## 変更履歴

- 2026-11-11: 初回登録
