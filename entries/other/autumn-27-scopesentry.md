---
repo: "Autumn-27/ScopeSentry"
name: "ScopeSentry"
genre: "other"
url: "https://github.com/Autumn-27/ScopeSentry"
license: "unknown"
stars: 2321
language: "Go"
created: "2024-02-27"
updated: "2026-10-11"
forks: 552
open_issues: 90
commits_30d: 4
commit_cadence: "weekly"
commits_90d: 10
size_kb: 95415
archived: false
author: "Autumn-27"
flags: ["unverified"]
risk_notes: "①悪用時の法的リスク: 許可なく第三者のドメイン・IP・Web アプリをスキャンすると、日本なら不正アクセス禁止法や各府県の迷惑防止条例、米国なら CFAA、中国なら网络安全法などに触れうる。資産の所有者であること、または書面のスキャン許可がある範囲だけを対象にし、レート制限と停止条件を決めてから使う。②実測性能が無い: 作者・README に処理量・スキャン速度・検出率の測定値やベンチマークは無く、本項でも実行検証していない。ノード数を増やしても実効速度は対象やネットワーク次第で、数値の裏付けは無い。③外部スキャナ/POC への依存: 脆弱性検査は nuclei v3.3.6 をライブラリとして内蔵し、subfinder v2.6.8 / httpx v1.6.10 / dnsx / tlsx / fingerprintx / gospider も libs/ に vendored している。バイナリを別途入れる必要は無い反面、追従は本体のリリース次第で、nuclei テンプレート（POC）の更新・誤検知の管理は利用者側の負担。④ライセンスの実態: GitHub API の license は null、/license とリポジトリ直下の LICENSE は 404（取得時点）。README 末尾は「All branches of this project follow AGPL-3.0」としつつ、商用利用には別途商用ライセンスが必要で、営利法人は使用・配布・改変の前に取得を求めるとする追加条項を置いており、AGPL-3.0 そのものと一致しない。法的に使う前提なら著者への確認が要る。⑤その他の未確認: ARTEX 連携は ARTEX 側 README に記載があるが ScopeSentry 側 README には無く、実際の同期動作は未検証。リソース要件（CPU/メモリ/ディスク）は README・compose に記載が無い。README の「Server：python - FastApi」は現行構成（Go 実装、.py ファイル 0）と一致しない。 ⑥ARTEX との関係: 投稿は ScopeSentry を「ARTEX 作者が貢献した」と述べるが、ARTEX のリポジトリ所有者は Hinln で、README は Autumn-27/norma を SDK として参照するのみ。同一著者であることは一次情報で断定できない。"
last_release: "v1.9.4"
last_release_at: "2026-08-23"
added: "2026-11-09"
first_seen: "2026-10-22"
fetched_at: "2026-11-09T04:18:28Z"
source_post: "https://x.com/wquguru/status/2113181135522214168"
sources: ["https://github.com/Autumn-27/ScopeSentry", "https://github.com/Autumn-27/ScopeSentry/blob/main/README.md", "https://github.com/Autumn-27/ScopeSentry/blob/main/single-host-deployment.yml", "https://github.com/Autumn-27/ScopeSentry/blob/main/SKILL.md", "https://github.com/Autumn-27/ScopeSentry-Scan", "https://github.com/Hinln/ARTEX", "https://www.scope-sentry.top/en/", "https://x.com/wquguru/status/2113181135522214168"]
type: "repo"
---

# ScopeSentry

## 出来ること

- 分散型の資産測絵（ASM）。サーバ1台と複数のスキャンノードで動き、ノードを選んでタスクを振り分ける。
- サブドメイン列挙とサブドメインテイクオーバー検出。subfinder / ksubdomain をプラグインとして実行する。
- ポートスキャンとサービス・Web フィンガープリント（fingerprintx、tlsx、wappalyzergo 相当を内蔵）。独自の Web フィンガープリント規則も追加できる。
- nuclei エンジンによる脆弱性スキャン。POC（nuclei テンプレート）のインポートに対応し、HTTP 資産には http プロトコルのテンプレートだけを絞って実行する。
- ディレクトリ探索、URL 抽出、クローラ、機密情報（PDF 内含む）検出、ページ改竄監視、資産のグルーピングと検索。
- Web UI（Vue）と MCP エンドポイント（/mcp、X-API-Key 認証）を持ち、MCP クライアントからプロジェクト・タスク・資産を操作できる。

## 目的・背景

- 外部公開資産の把握を自前で回すためのプラットフォーム。調査会社の SaaS ではなく、MongoDB と Redis を backend にした自前ホスト型で、対象の登録からスキャン、結果の蓄積・検索までを1か所に集める。
- README は「新しい脆弱性が出たときに、対象資産にそのコンポーネントが無いかを素早く確認する」用途を挙げている。日次の網羅スキャンよりも、既知資産に対する再確認を回す設計思想。
- タスクは単一ターゲット単位でノードに配信される。SKILL.md は根域名を一度に流すと1ノードに負荷が偏るとし、子域名収集と後続モジュールを2段階に分ける運用を推奨している。
- AI 側からは MCP 経由で資産を引けるため、偵察結果をエージェントの入力にする使い方ができる。ARTEX（リポジトリは Hinln/ARTEX。AI 侵入テスト基盤）は資産同期機能で ScopeSentry の資産を資産グラフに取り込む。

## 依存関係

- サーバは Go（go.mod の toolchain は go1.24.6、.go ファイル 259 本、.py は 0）。README の「Server：python - FastApi」は現行構成と一致しない古い記述。
- スキャナは別リポジトリ Autumn-27/ScopeSentry-Scan（Go）。nuclei v3.3.6、subfinder v2.6.8、httpx v1.6.10、dnsx v1.2.2、tlsx、fingerprintx、gospider を libs/ に vendored し、ライブラリとして組み込む。nuclei などの外部バイナリを別途インストールする必要は無い。
- データストアは MongoDB 7.0.28 と Redis 7.0.11（compose で固定タグ）。
- 配布物は Docker イメージ（autumn27/scopesentry:latest、autumn27/scopesentry-scan:latest）と、Releases の単体バイナリ（linux / darwin / windows の amd64 zip、約 40MB）。
- プラグインは traefik/yaegi の Go インタプリタで実行され、プラグインマーケットから追加できる。

## 実行条件

- Linux ホスト推奨。スキャン用コンテナが network_mode: host で動くため、Docker Desktop の macOS / Windows ではそのままでは動かない。
- docker-compose 実行前に .env の MONGO_INITDB_ROOT_PASSWORD と REDIS_PASSWORD を変更する（初期値は mongodb_password / redis_password）。Web UI は 8082、MongoDB は 27017、Redis は 6379 をホストに公開する。
- 初回ログインの管理者パスワードとプラグイン二次認証パスワードは docker logs scope-sentry で確認する。
- CPU・メモリ・ディスクの要件は README にも compose にも記載が無い。スキャン対象数と並列度から自分で見積もる必要がある。
- サーバとスキャンのバージョンは別管理（version.json は server 1.9.4 / scan 1.9.1）。ノード追加時は接続先 MongoDB / Redis と一意な NodeName を設定する。
- 対象のスキャン許可（自社資産または書面許可）が前提。インターネットへ直接出す場合は 8082 と MCP エンドポイントの認証・TLS を前段で保護する。

## 最短手順

- git clone https://github.com/Autumn-27/ScopeSentry.git && cd ScopeSentry
- vi .env  # MONGO_INITDB_ROOT_PASSWORD と REDIS_PASSWORD を変更する
- docker-compose -f single-host-deployment.yml up -d  # mongodb / redis / scope-sentry / scopesentry-scan の4コンテナが起動
- docker logs scope-sentry  # 初期ユーザーのパスワードとプラグイン二次認証パスワードを控える
- ブラウザで http://<ホスト>:8082 を開いてログインし、プロジェクトとタスクを作成する
- ノードを増やす場合: git clone https://github.com/Autumn-27/ScopeSentry-Scan.git && cd ScopeSentry-Scan/build && vi .env（NodeName を一意に）&& docker-compose -f scan-docker-compose.yml up -d

## 変更履歴

- 2026-11-09: 初回登録
