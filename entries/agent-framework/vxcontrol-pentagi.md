---
repo: "vxcontrol/pentagi"
name: "PentAGI"
genre: "agent-framework"
url: "https://github.com/vxcontrol/pentagi"
author: "VXControl"
license: "MIT"
stars: 33728
language: "Go"
created: "2025-01-06"
updated: "2026-10-22"
forks: 5277
open_issues: 69
size_kb: 60557
archived: false
commits_30d: 1
commits_90d: 14
commit_cadence: "monthly"
last_release: "v2.2.0"
last_release_at: "2026-10-05"
flags: ["unverified"]
risk_notes: "自律型ペネトレーションテスト基盤であり、動作は「対象への実際の攻撃」そのもの。README は利用者を \"Security engineers, penetration testers, researchers and red teams ... for authorized testing only\" と限定しており、自組織資産または書面で許可された範囲以外への実行は法律違反になり得る。既定の管理者アカウントは admin@pentagi.com / admin で、初回ログイン時に変更しないまま外部公開すると乗っ取りにつながる。サンドボックスへ Docker を渡す設定は特に危険で、リリースノートは CVE-2026-14784 について \"with `DOCKER_INSIDE=true`, as the shipped `.env.example` set it, the host Docker socket was mounted into every sandbox, so an agent steered by prompt injection could take over the host\" と説明し、2.2.0 で DOCKER_INSIDE の既定を false、ホストソケットの自動マウント廃止に変更した。README もソケットの bind mount を \"Not recommended\" と明記。プロンプトインジェクション耐性はモデルの指示追従性に依存し、完全には閉じないとリリースノート自身が述べている。機能面の注意: MCP サーバ、エージェントプロファイル、プラグイン、攻撃チェーン可視化、顧客向けレポートは PentAGI Enterprise（有償、別ライセンスキー）側で、本リポジトリの OSS 版には含まれない。Kali イメージの mcp タグはサンドボックス側のゲートウェイであり、PentAGI 本体の MCP サーバではない。有効性はベンダー自身の ctester レポートと主張に基づき、独立した第三者ベンチマークは未確認（ベンダー主張のみで独立検証なし）。LLM API 利用料は別途発生する。BAS／敵対エミュレーション製品ではないと README が明記しており、その用途には使えない。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/wquguru/status/2113181135522214168"]
fetched_at: "2026-11-09T05:01:41Z"
---

# PentAGI — サンドボックス内で20以上のツールを動かす自律ペネトレーションテスト基盤

## 出来ること

- 平文で目標を書くと、調査・開発・インフラ担当に分かれたサブエージェント群が計画を立て、nmap・Metasploit・sqlmap など20以上のツールを Docker サンドボックス内で実行してレポートを返す。
- 実行結果と成功パターンを PostgreSQL + pgvector に長期記憶として保持し、任意で Neo4j / Graphiti のナレッジグラフにホスト・サービス・所見を関係付きで残す。
- REST と GraphQL の両 API を Bearer トークンで操作でき、フローの作成・状態取得・停止を外部のエージェントや CI から自動化できる。OpenAPI (swagger/doc.json) と schema.graphqls が公開されている。
- LLM は OpenAI / Anthropic / Gemini / AWS Bedrock / Ollama / DeepSeek / GLM / Kimi / Qwen / MiniMax / Mistral / xAI と、任意の OpenAI 互換エンドポイント（Azure OpenAI 含む）から選べる。
- 同梱の ctester / etester でプロバイダとエージェント役割ごとの成功率、埋め込みプロバイダの整合性を実測できる。Grafana/Prometheus と Langfuse による監視・トレースにも対応。

## 目的・背景

- VXControl（ドバイのセキュリティエンジニアリング企業）が開発する自己ホスト型の自律ペネトレーションテスト環境。認可されたテストを自分のインフラ内で回し、データと推論先モデルを自分で選べることを狙っている。
- 投稿が挙げた「サンドボックス・記憶・20以上のツール」という3点は README の記述と一致する（一次情報で裏取り済み）。
- README は自ら適用範囲を限定している: CALDERA のような BAS／敵対エミュレーション製品ではなく、事前定義キャンペーンや攻撃計画を持つ製品ではない。フローレポートの JSON エクスポートも未サポート。
- ライセンスはコードが MIT（Copyright (c) 2025 PentAGI Development Team）。ただし VXControl Cloud Services（脅威インテリジェンス等）の利用は別ライセンスキーと規約に従う。

## 依存関係

- Docker と Docker Compose（Podman でも可）。イメージ取得のためネットワーク接続が必要。
- LLM: クラウドプロバイダの API キー、または Ollama / vLLM などのローカル推論サーバ。埋め込み用プロバイダも別途必要（記憶・Graphiti 用）。
- データ層: PostgreSQL + pgvector は必須、Neo4j + Graphiti は任意。Web 取得用に scraper コンテナ（vxcontrol/scraper）、監視に Grafana/Prometheus を任意で併用。
- API 利用時は Web UI で発行する Bearer トークン（有効期限 1分〜3年、発行時に一度だけ表示）が必要。

## 実行条件

- 最小構成は 2 vCPU / 4GB RAM / 20GB 空きディスク。Web UI と API は 8443 の HTTPS で待ち受ける。
- 初期管理者は admin@pentagi.com / admin。初回ログインで変更することが前提で、変更しないまま外部公開しない。
- 外部ネットワークから使う場合は PUBLIC_URL と SSL 証明書を設定する。複数インスタンスで基盤を共有する場合のみ TENANT_ID を設定。
- サンドボックスに docker を渡す要件がある場合も、ホストの docker.sock を bind mount せず、DOCKER_INSIDE_HOST で別デーモン（TLS 検証付き）を指定する。2.2.0 で DOCKER_INSIDE の既定は false。
- 対象は自組織資産、または書面で許可された範囲に限る。認可なき第三者への実行は違法行為になり得る。

## 最短手順

- ホストに導入: `mkdir -p pentagi && cd pentagi` → `wget -O installer.zip https://pentagi.com/downloads/linux/amd64/installer-latest.zip` → `unzip installer.zip && sudo ./installer`（Linux/macOS/Windows 版あり）。手動なら `.env` と `docker-compose.yml` を取得して `docker compose up -d`。
- https://localhost:8443 にログインし、Settings → API Tokens → Create Token でトークンを発行する（この時だけ表示されるので即保存）。
- AI から REST で読む: `curl https://<host>:8443/api/v1/flows -H "Authorization: Bearer $PENTAGI_TOKEN"`。
- AI から GraphQL で読む／書く: `curl -X POST https://<host>:8443/api/v1/graphql -H "Authorization: Bearer $PENTAGI_TOKEN" -H "Content-Type: application/json" -d '{"query":"{ flows { id title status } }"}'`。
- エージェントのツール定義は `https://<host>:8443/api/v1/swagger/doc.json`（OpenAPI）と `backend/pkg/graph/schema.graphqls` から生成し、function calling にそのまま渡す。`/api/v1/swagger/index.html` と `/api/v1/graphql/playground` で対話的に確認できる。
- MCP 経由で使いたい場合、OSS 版に MCP サーバは無いので上記 REST/GraphQL を薄くラップした MCP サーバを自前で用意する（MCP サーバ同梱は Enterprise 版の機能）。

## 変更履歴

- 2026-11-09: 初回登録
