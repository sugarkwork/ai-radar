---
name: "Spring AI TypeSafe"
genre: "agent-framework"
url: "https://github.com/spring-ai-community/spring-ai-typesafe"
repo: "spring-ai-community/spring-ai-typesafe"
stars: 64
forks: 19
open_issues: 19
size_kb: 1530
language: "Java"
created: "2026-09-20"
updated: "2026-10-05"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 30
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2120147118237114757"]
fetched_at: "2026-11-11T06:10:44.581808+00:00"
---

# Spring AI TypeSafe

## 出来ること

- JavaクライアントでTypeSafe AIのSystem One API（jev）を利用し、状態と型付き質問を渡して構造化された回答を取得できる。READMEによると、Spring AI連携にはModel-as-a-judge、guardrail、RAGの後処理、tool indexが含まれる。

## 目的・背景

- READMEでは、jevをチャットモデルではなく、同じ状態に対する複数の型付き質問へ回答するAPIとして説明している。広いルーブリックのプロンプトではなく、個別の質問をコードで組み合わせるパターンを示している。

## 依存関係

- Java 17以降が必要。READMEによると、typesafe-spring-aiにはSpring AI 2.0.1以降が必要。Spring Bootを使わないJava構成ではtypesafe-java-sdkのみを使用できる。

## 実行条件

- API利用にはTYPESAFE_API_KEYの設定が必要。Spring Boot starterはspring.ai.typesafe.api-keyプロパティからキーを読み取る。通常のビルドはオフラインで実行でき、ライブ統合テストはintegration-testsプロファイルとTYPESAFE_API_KEY環境変数の両方が必要とREADMEに記載されている。

## 最短手順

- Maven依存関係としてorg.springaicommunity:spring-ai-starter-typesafe:0.4.0を追加し、TYPESAFE_API_KEYを設定する。SDKを直接使う場合は、状態とNoul、Choice、Scoreなどの型付き質問を含むSystemOneRequestを構築し、TypeSafeClientでSystem One APIを呼び出す。

## 変更履歴

- 2026-11-11: 初回登録
