---
name: "jev-code"
genre: "coding-agent"
url: "https://github.com/FrancoisChastel/jev-code"
repo: "FrancoisChastel/jev-code"
license: "MIT"
stars: 59
language: "TypeScript"
created: "2026-09-19"
updated: "2026-10-31"
forks: 9
open_issues: 6
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 42
size_kb: 931
archived: false
flags: ["unverified"]
risk_notes: "分類結果の品質・較正性能はこのREADMEでは独立検証されていない。利用にはNode.js 20以上と、選択したホストのAPIキーが必要。ホストごとの料金や費用はREADMEに記載なし。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2120147118237114757"]
fetched_at: "2026-11-11T06:11:26.887950+00:00"
---

# jev-code

## 出来ること

- Claude Code、Codex、Pi、OpenCode、およびシェルから利用できるJev用ツール。分類、Yes/No確認、スコア、ランキング、自由形式の質問に対応し、型付き回答と確率を返す。エージェント向けスキルとセットアップCLIも含む。READMEは応答が数百ミリ秒と説明しているが、独立計測値ではない。

## 目的・背景

- READMEでは、CI失敗の分類、質問に答えるファイルの選定、PR説明と変更内容の照合、指摘の深刻度判定など、小規模な分類判断をエージェントが行う用途を挙げている。Jevを文章生成モデルではなく意思決定モデルとして説明している。

## 依存関係

- Node.js 20以上。README記載のセットアップはnpmパッケージ @french-castle/jev-code をnpx経由で利用する。JevホストへのAPI接続が必要で、TypeSafe、OpenRouter、Vercel AI Gateway、OpenAI、または独自System One gatewayを選択する。

## 実行条件

- READMEは、選択したホストのAPIキーを環境変数に設定するか、setup時に入力するよう案内している。独自gatewayではURLも設定する。ホストの料金や利用条件はREADMEに記載されていない。

## 最短手順

- README記載の手順: `npx -y @french-castle/jev-code@latest setup` を実行し、必要に応じて対象エージェント名や `--project`、`--dry-run` を指定する。APIキーを設定し、`npx -y @french-castle/jev-code@latest doctor --live` で接続を確認後、エージェントを再起動する。

## 変更履歴

- 2026-11-11: 初回登録
