---
repo: "smkrv/jev-calibrate"
name: "jev-calibrate"
genre: "eval"
url: "https://github.com/smkrv/jev-calibrate"
license: "MIT"
stars: 33
language: "TypeScript"
created: "2026-09-21"
updated: "2026-10-19"
forks: 1
open_issues: 2
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 11
size_kb: 147
archived: false
last_release: "v0.1.11"
flags: ["unverified"]
risk_notes: ["精度は著者が公開した同梱例の結果。独立した実行検証や、別データ・モデル版・プロバイダーでの再現性確認は行っていない。", "現在のAPI料金・データ保持条件と、最新リリースの年・タイムゾーンを含む公開日時は未確認。"]
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116142322543198271"]
fetched_at: "2026-11-10T12:56:36+00:00"
---

# jev-calibrate — Jevの判定を手元のラベルで評価するCLI

## 出来ること

- 真偽・選択・段階スコアの判定を質問単位で評価する。設定した指標に基づき、自動判定に使えるか、高信頼の回答だけ採用するか、順位付けにとどめるかを判断できる。

## 目的・背景

- Jevは入力と質問を受け取り、確率を返す。調整用データで条件や閾値を見直し、編集を止めてからホールドアウトで評価する。
- 著者の同梱例では、初稿の不満度判定は26件中18件が正解で、誤答8件のうち4件は信頼度0.94以上だった。少数の同梱例での報告であり、別の業務データでの精度は未確認。

## 依存関係

- TypeScript製で実行時のパッケージ依存はない。判定の取得にはTypeSafe、OpenRouter、または選んだプロバイダーと互換のAPIを使う。

## 実行条件

- Node.js 20以上。公開APIを使う場合はTYPESAFE_API_KEYまたはOPENROUTER_API_KEYを環境変数に設定する。コードはMITライセンス。APIの現行料金は未確認。
- lintはAPIを呼ばない。checkは例の入力を指定先に送るため、送信が許可されたデータで実行する。

## 最短手順

- `npm install -g jev-calibrate` でCLIを導入する。対象ディレクトリで `jev-calibrate init` を実行し、`questions.json` と `examples.jsonl` に質問と正解ラベルを記入する。
- シェル実行権限を持つAIエージェントからは、対象ディレクトリで `jev-calibrate lint` を呼び、次に `jev-calibrate check --split tune --json` の結果を読む。条件を変更したら再度checkを実行し、`jev-calibrate compare` で改善と回帰を確認する。
- 条件を確定してから `jev-calibrate check --split holdout --json` で評価する。結果を見て条件を変更した場合は、新しいラベル付きデータを最終評価に使う。

## 変更履歴

- 2026-11-11: 初回登録
