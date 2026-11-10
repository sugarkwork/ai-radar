---
type: "repo"
name: "opensandbox-group/OpenSandbox"
genre: "agent-framework"
url: "https://github.com/opensandbox-group/OpenSandbox"
author: "opensandbox-group"
source_post: "https://x.com/0xJokker/status/2119144012644757738"
sources: ["https://x.com/0xJokker/status/2119144012644757738", "https://github.com/opensandbox-group/OpenSandbox"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "64ms P50・125.4ms P99等は開発側ベンチ。隔離の強さは設定・バックエンドによるため、秘密情報やネットワークの安全性を一括保証しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "opensandbox-group/OpenSandbox"
license: "Apache-2.0"
language: "Python"
created: "2025-12-17"
updated: "2026-11-09"
stars: 16881
forks: 1589
open_issues: 161
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 118748
archived: false
fetched_at: "2026-11-09T21:34:19Z"
last_release: "release-1.2.0"
last_release_at: "2026-10-27"
---

# opensandbox-group/OpenSandbox

## 出来ること

エージェントコードを隔離環境で動かすOpenSandbox。Dockerローカル、Kubernetes、Firecracker、MCP/SDKやCredential Vaultを案内。

## 目的・背景

紹介対象は `opensandbox-group/OpenSandbox`。対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:26.878245+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Pythonと対象コンテナ/仮想化基盤。配布名・レジストリ等はAlibaba系の実装であることを原チェック確認。

## 実行条件

64ms P50・125.4ms P99等は開発側ベンチ。隔離の強さは設定・バックエンドによるため、秘密情報やネットワークの安全性を一括保証しない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/opensandbox-group/OpenSandbox#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @0xJokker: https://x.com/0xJokker/status/2119144012644757738
- 対象資料: https://github.com/opensandbox-group/OpenSandbox

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
