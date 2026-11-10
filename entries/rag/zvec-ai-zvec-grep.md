---
type: "repo"
name: "zvec-ai/zvec-grep"
genre: "rag"
url: "https://github.com/zvec-ai/zvec-grep"
author: "zvec-ai"
source_post: "https://x.com/QwenDevs/status/2118667290048970829"
sources: ["https://x.com/qwendevs/status/2118667290048970829?a=LGoBcuo-iakPFGZtcvM&s=46", "https://x.com/QwenDevs/status/2118667290048970829", "https://x.com/ZvecAI/status/2117643850609213775", "https://zvec.org/en/blog/2026-11-03-zvec-grep-rust/", "https://github.com/zvec-ai/zvec-grep", "https://api.github.com/repos/zvec-ai/zvec-grep", "https://raw.githubusercontent.com/zvec-ai/zvec-grep/main/README.md", "https://registry.npmjs.org/@zvec/zvec-grep"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "起動26.8ms・索引構築64.5%短縮等は開発元のApple M3 Pro単一環境の比較。第三者追試でもWindowsでの計測でもない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "zvec-ai/zvec-grep"
license: "Apache-2.0"
language: "Rust"
created: "2026-07-10"
updated: "2026-11-09"
stars: 4298
forks: 263
open_issues: 90
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 77691
archived: false
fetched_at: "2026-11-09T21:42:46Z"
last_release: "v0.3.0"
last_release_at: "2026-11-03"
---

# zvec-ai/zvec-grep

## 出来ること

ripgrep、BM25、ベクトル検索を統合したローカル検索CLI「zg」。MCP経由でコーディングエージェントから利用できるRust版0.3.0の紹介。

## 目的・背景

紹介対象は `zvec-ai/zvec-grep`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:24.527561+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

macOS/Linux/Windows向け。意味検索には別途ローカル埋め込みモデルと索引構築が必要。

## 実行条件

起動26.8ms・索引構築64.5%短縮等は開発元のApple M3 Pro単一環境の比較。第三者追試でもWindowsでの計測でもない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/zvec-ai/zvec-grep#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @QwenDevs: https://x.com/QwenDevs/status/2118667290048970829
- 対象資料: https://github.com/zvec-ai/zvec-grep
- 参照: https://x.com/ZvecAI/status/2117643850609213775
- 参照: https://zvec.org/en/blog/2026-11-03-zvec-grep-rust/
- 参照: https://api.github.com/repos/zvec-ai/zvec-grep
- 参照: https://raw.githubusercontent.com/zvec-ai/zvec-grep/main/README.md
- 参照: https://registry.npmjs.org/@zvec/zvec-grep

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
