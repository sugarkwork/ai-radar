---
name: "e2e"
genre: "agent-framework"
url: "https://github.com/e2e-inc/e2e"
repo: "e2e-inc/e2e"
flags: ["unverified"]
risk_notes: "エージェント実行には利用者自身のサブスクリプション、APIキー、またはローカルモデルが必要。料金や各モデルの利用条件はREADMEに記載なし。"
stars: 13799
forks: 732
open_issues: 81
size_kb: 113420
language: "TypeScript"
created: "2026-07-22"
updated: "2026-11-13"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/awe0_io/status/2118662503542706437"]
fetched_at: "2026-11-13T11:17:34.506881+00:00"
---

# e2e

## 出来ること

- Web・モバイルアプリのエンドツーエンドテストを作成できる。テスト内で自然言語の目標をエージェントに実行させ、locatorやassertionで結果を確認する。エージェントの操作を後続assertionが検証した場合、次回実行ではアプリに変化がない限り操作を記録から再生し、モデル呼び出しを行わないとREADMEは説明している。これはREADME記載の機能説明であり、独立した実測結果ではない。

## 目的・背景

- READMEは、Web・モバイルアプリのテストで自然言語による目標達成と、その結果の検証を同じテスト内で行うフレームワークとして紹介している。プロジェクトは1.0に向けた開発中で、APIと設定はマイナーリリース間でも変更される可能性がある。

## 依存関係

- README記載の構成では、WebエンジンはPlaywright経由でChromium、Firefox、WebKitを利用し、モバイルエンジンはagent-device経由でiOS・Androidのシミュレーター／エミュレーターを利用する。エージェント実行には利用者自身のサブスクリプション、APIキー、またはローカルモデルが必要。

## 実行条件

- Node.js環境でCLIを利用する。初期設定は `npx e2e init` を実行し、Webまたはモバイルのエンジンとモデルプロバイダーを選ぶ。READMEは、設定ファイルとサンプルテストが生成されると説明している。モデルを使わないエージェント手順のないテストも実行できる。

## 最短手順

- `npx e2e init` を実行し、エンジンとモデルプロバイダーを選択する。生成された設定とサンプルテストを使い、必要に応じてREADME記載の `e2e` パッケージから `test` と `expect` を読み込み、`app.open()`、`agent.act()`、`agent.assert()`、画面locatorのassertionを記述する。

## 変更履歴

- 2026-11-13: 初回登録
