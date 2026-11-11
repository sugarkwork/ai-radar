---
repo: "ollaya-dev/ollaya"
name: "Ollaya"
genre: "model-serving"
url: "https://github.com/ollaya-dev/ollaya"
license: "Apache-2.0"
stars: 1454
language: "Rust"
created: "2026-09-23"
updated: "2026-11-06"
forks: 90
open_issues: 10
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 10442
archived: false
flags: ["unverified"]
risk_notes: "速度・精度は開発元の公開測定で、今回の調査では再実行していない。個別ワークロードでの精度、遅延、費用削減、各モデルの利用条件は未確認。GitHubの最新版リンクはv0.18.0を返したが、mainのREADMEには0.19.0の測定への言及があり、最新リリースのタグと公開日時は確定していない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116142322543198271"]
fetched_at: "2026-11-10T12:57:09Z"
---

# Ollaya — 判断モデルをローカルで配信するJev互換サーバー

## 出来ること

- テキストやJSONと型付きの質問を渡し、分類やチケットの振り分けに使える構造化された回答を取得できる。CLI、ローカルHTTP API、MCPに対応する。

## 目的・背景

- 自由文の生成を必要としない判断を専用モデルに任せるための推論サーバー。TypeSafe互換の `/v1/systemone` を備え、既存クライアントは接続先とモデル名を変更して利用できる。
- 開発元のREADMEでは、型付き判断タスクで `winnow:e4b` の正解率を0.724、RTX 5090で5問を処理した時間を113 msと報告している。自分のデータでの精度や手元の機材での速度は別途評価が必要。

## 依存関係

- モデルに応じてONNX RuntimeまたはGGUF用のllama.cppを使う。モデル取得には配布元へのネットワーク接続と重みの保存領域が必要。Apache-2.0はOllaya本体のライセンスで、モデルの条件は配布元で個別に確認する。

## 実行条件

- 公式READMEはLinux（x86_64またはarm64、glibc 2.38以上）、macOS（Apple silicon）、Windows（x64）向けの導入方法を案内している。CPUでも動作し、GPU対応はモデルのバックエンドと機材に依存する。ローカル推論の費用は自前の計算資源に依存する。

## 最短手順

- 公式配布ページから環境に合うOllayaを導入し、`ollaya serve` で起動して `ollaya pull laya` でモデルを取得する。 [公式配布ページ](https://ollaya.dev/download)
- Claude Codeで `claude mcp add ollaya -- ollaya mcp` を実行して登録する。ClaudeにMCPツール `decide` を使うよう指示し、`model` に `laya`、`state` に分類したいチケット本文、`questions` に分類用の型付き質問を渡す。 [公式スキル定義](https://github.com/ollaya-dev/ollaya/blob/main/skills/ollaya-decisions/SKILL.md)

## 変更履歴

- 2026-11-11: 初回登録
