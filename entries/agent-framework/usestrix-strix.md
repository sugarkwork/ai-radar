---
repo: usestrix/strix
name: strix
genre: agent-framework
url: https://github.com/usestrix/strix
license: Apache-2.0
stars: 73803
language: Python
created: 2025-08-05
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-04
source_post: https://x.com/thegreatest_sv/status/2117687388214272339
sources: []
flags: []
risk_notes: "自律型のペネトレーションテストツール。所有者の許可がある対象（自社アプリ・検証環境・許可されたバグバウンティ範囲）に限って実行すること。無断のスキャンは不正アクセス禁止法・CFAA等に触れうる。"
forks: 8321
open_issues: 536
commits_30d: 64
size_kb: 17412
archived: false
commits_90d: 100
commit_cadence: daily
fetched_at: "2026-11-05T04:40:03Z"
last_release: v1.7.0
last_release_at: 2026-10-05
---

# Strix

## 出来ること

- 自律型のAIペネトレーションテストエージェント。コードを実際に動かし、脆弱性を見つけ、**動作するPoCで検証**してから報告する。静的分析ツールの誤検知を避けるのが狙い。
- 偵察・悪用・検証のためのツール群を最初から備え、複数のエージェントが協調して並列に調査する（マルチエージェント構成）。
- 対象の指定方法が広い:
  ```bash
  strix --target ./app-directory
  strix --target https://github.com/org/repo
  strix --target https://your-app.com
  strix --target ./openapi.yaml --target https://api.your-app.com
  strix --target postman://<collection-uuid> --target https://your-app.com
  ```
  `--instruction` で認証情報を渡した認証下のテスト、`--target-list` で複数対象の一括実行もできる。
- 修正パッチの提案と、コンプライアンス向けのペネトレーションレポート生成。GitHub Actions / CI に組み込み、PRごとにスキャンして不安全なコードを止める連携も用意されている。
- 実行結果は `strix_runs/<run-name>` に保存される。

## 目的・背景

2025-08 公開。人手のペネトレーションテスト（週単位）や静的スキャナ（誤検知が多い）の間を埋める位置づけで、PoCが動くこと自体を根拠にする。クラウド版（app.strix.ai）とエンタープライズ版も提供され、OSS版はローカルのDockerと自前のLLMキーで動く。

## 依存関係

- Docker（起動していること）。初回実行時にサンドボックスイメージを自動取得する。
- LLMのAPIキー（OpenAI、Anthropic、Google、OpenRouter など対応プロバイダ）。
- Python パッケージ `strix-agent` としても配布（pipx / uv / pip で導入可能）。

## 実行条件

- **許可された対象にのみ実行する**。自社アプリ、検証環境、参加中のバグバウンティの範囲など。
- ローカル実行はDockerとLLMキーが必須。クラウド版ならDockerもキーも不要（従量課金）。
- ライセンスは Apache-2.0。★7.4万・open issue 536件と規模が大きく、更新も活発（直近30日で64コミット）。

## 最短手順

```bash
curl -sSL https://strix.ai/install | bash

export STRIX_LLM="openrouter/z-ai/glm-5.3"
export LLM_API_KEY="<your-api-key>"

strix --target ./app-directory
```

## 変更履歴

- 2026-11-05: 初回登録（★73,802 / pushed 2026-11-05 / Apache-2.0 / v1.7.0）
