---
repo: "Hinln/ARTEX"
name: "ARTEX"
genre: "agent-framework"
url: "https://github.com/Hinln/ARTEX"
license: "AGPL-3.0"
stars: 1443
language: "Go"
created: "2026-10-08"
updated: "2026-10-08"
forks: 1961
open_issues: 4
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 100
size_kb: 9601
archived: false
author: "Hinln（上流は Autumn-27/ARTEX v0.3.15 のバックアップ）"
flags: ["unverified"]
risk_notes: "①認可前提: README は「オンラインシステムへの実行は認可の有無を問わず禁止」と明記し、対象はローカルの隔離環境に限るとする。実運用で使うなら著者の許諾と法的根拠の両方が要る。②危険な既定値: worker は Bash/HTTP を実ツールで実行する。0.3.15 の変更履歴は、内蔵の破壊的 HTTP 規則が DELETE メソッドしか見ておらず、GET/POST の削除系エンドポイント（例 `/api/user/delete?id=1`）を実際に叩いてデータを消し得たと述べ、deny 規則を追加したとしている。0.3.15 未満は破壊的操作を止められない前提で扱うべき。③承認ゲートの範囲は未検証: guard/intercept とタスク単位 intercept_rules は存在するが、既定で何が承認待ちになるかの一覧は README・CHANGELOG から特定できない。④MITM の鍵管理: 記録プロキシが CA を発行して TLS を復号し、Bash/HTTP を留痕する。CA 秘密鍵と traffic データの保管・削除は利用者責任で、第三者環境に置くと通信内容がそのまま残る。⑤サプライチェーン: 本リポジトリは上流のバックアップで、Hinln 名義のコミット 1 本が自己更新の取得先を Hinln/ARTEX Releases に変更している。更新は zip 取得→SHA256SUMS 照合→`-h` スモークテスト→入替（3 回失敗でロールバック）という実装だが、配布元が単一アカウントである点は変わらない。取得時点で Releases と tags は 0 件のため更新経路は動かない。⑥記述の不整合: README は「これは私有リポジトリ」として ARTEX_UPDATE_GITHUB_TOKEN（Contents: read）の設定を求めるが、API 上 private=false。トークン前提の更新手順は現状と一致しない。⑦上流の消失: Autumn-27/ARTEX は API 404 で作者の公開リポジトリ一覧にも無い。fork 1941 > star 1427 という比率は一斉ミラーと整合するが、各 fork が同一内容とは限らず、本項では上流タグとのハッシュ照合をしていない。⑧未検証: 本項はコード・README・compose の静的確認のみで、実行・ベンチ・検出率の検証はしていない。効果の数値的裏付けは無い。"
last_release: ""
last_release_at: ""
added: "2026-11-09"
first_seen: "2026-10-22"
fetched_at: "2026-11-09T21:33:14Z"
source_post: "https://x.com/wquguru/status/2113181135522214168"
sources: ["https://github.com/Hinln/ARTEX", "https://api.github.com/repos/Hinln/ARTEX", "https://github.com/Hinln/ARTEX/blob/main/README.md", "https://github.com/Hinln/ARTEX/blob/main/docker-compose.yml", "https://github.com/Hinln/ARTEX/blob/main/go.mod", "https://github.com/Hinln/ARTEX/blob/main/CHANGELOG.md", "https://github.com/Hinln/ARTEX/blob/main/skills/api-recon/SKILL.md", "https://artex-demo.vercel.app/", "https://x.com/wquguru/status/2113181135522214168"]
type: "repo"
---

# ARTEX — LLM マルチエージェントの侵入テスト基盤（上流 v0.3.15 のバックアップ）

## 出来ること

- LLM のマルチエージェントで Web アプリの侵入テストを回す自ホスト型システム。Go の単一バイナリに Next.js の UI を埋め込み、PostgreSQL に状態を持つ。
- 二重グラフ: 全タスク共有の「資産グラフ」（root_domain → subdomain → ip / service → app → endpoint）と、タスクごとの「探索グラフ」（goal / intent / fact / finding / hint）。両者は anchors で結ばれ、ある資産がどの intent でどう測られたかを双方向に辿れる。
- planner が intent を発行し、worker が 1 本ずつ引き受けて実ツール（Bash / HTTP / Kali 系）で実行、結果をグラフに書き戻すと再び planner が起きるイベント駆動ループ。planner はタスク単位の todolist を跨いで保持するため、注入→ credential 取得→横移動のような多段の連鎖を順序立てて進められる。
- worker 間で実行過程そのものを検索・共有する（search_all_worker_traces / get_worker_trace）。fact になっていない観察も後続の worker が再利用できる。
- 記録型 MITM プロキシ（:8788）が TLS を復号して Bash/HTTP を留痕し、証跡を finding に紐づける。承認ゲート（guard / intercept）と人間参加のチャット（mainagent）を持つ。
- ScopeSentry の API からドメイン / サブドメイン / IP / ポート / サイト / エンドポイントを同期し、資産図に直接取り込む。
- 補助機能: レポート、通知（DingTalk / 飛書 / WeCom / Webhook / Telegram / メール）、タスクアーカイブ、脆弱性の再テスト用 retester エージェント、skills/ の SKILL.md、リモート MCP への接続、LLM プロファイル切替。

## 目的・背景

- 単発のスキャナではなく「偵察 → 意図 → 実行 → 証拠 → 再テスト」のループをエージェントに回させるオーケストレーション層。投稿が言う『資産グラフ＋人間参加』の実体は、この二重グラフと承認ゲートを指す。
- 本リポジトリは本家 Autumn-27/ARTEX v0.3.15 の「源码备份」。取得時点で本家の API は 404 を返し、作者 Autumn-27 の公開リポジトリ一覧（20 件）にも ARTEX は無い。つまり本家は参照できず、このバックアップが実質的な入手元になっている。
- バックアップは byte 一致の複製ではない。Hinln 名義のコミットが 1 本だけ追加され（2026-10-08「fix: use Hinln/ARTEX for authenticated release updates」）、自己更新の取得先を Hinln/ARTEX に書き換えている。他の 99 件は上流の履歴。
- ライセンスは AGPL-3.0。README はこれとは別に、学習・ローカル検証以外の利用を禁じる追加の制限と免責を掲げている。AGPL-3.0 は追加制限を認めないため、この併記の法的扱いは利用前に確認が必要。

## 依存関係

- PostgreSQL が必須（compose は postgres:16-alpine、既定ユーザー / DB 名は artex、DSN は ARTEX_PG_DSN で上書き可）。
- Go 1.26.3。go.mod の主要依存は norma v0.4.3（エージェント SDK）、pgx v5.10.0、go-mitmproxy v1.9.2、projectdiscovery/dnsx、golang-jwt v5。
- LLM の API キー（ANTHROPIC_API_KEY か OPENAI_API_KEY。UI の「LLM 配置」でも設定可）。切り替えは ARTEX_LLM_PROVIDER / MODEL / BASE_URL / PROXY。
- Docker 運用ならイメージ autumn27/artex（nmap・ripgrep・curl・playwright などを同梱）。ソースからビルドする場合は Node.js（npm ci と next build:static）も要る。
- スキルは ./skills/<name>/SKILL.md、永続データは ./data に置かれ、compose では bind mount される。

## 実行条件

- 単一プロセスで UI・API・SSE を :8787、MITM 記録プロキシを :8788 に出す。compose は 8788 を 127.0.0.1 のみに公開する。
- 初回アクセス時に /setup で管理者パスワードを設定する。ログインのユーザー名は実装上 "ARTEX" 固定、パスワードのみ可変。
- 配布形態は Docker Compose とソースビルドが確実。Linux / macOS / Windows の単体バイナリを想定した記述はあるが、取得時点で Releases と tags は 0 件（/releases/latest は 404）なので、README の「Releases から zip を落とす」手順は使えない。
- 対象のテスト許可が前提。README は「認可の有無を問わず、オンラインのサイトやサービスへの実行を禁止」と明記しており、隔離したローカル環境での検証に限るとしている。
- UI だけ見たい場合は https://artex-demo.vercel.app/ が公開されている（取得時点で 200、モックデータのデモ）。

## 最短手順

- AI / 外部ツールからは REST + JWT で操作する。MCP は ARTEX が接続する側（クライアント）で、ARTEX 自身を MCP サーバとして公開する実装は無い。
- 1) 起動: `.env` に POSTGRES_PASSWORD（任意で ANTHROPIC_API_KEY）を書いて `docker compose up -d`。http://localhost:8787 が開く。
- 2) 認証: 初回は `curl -s -X POST http://localhost:8787/api/auth/init -H 'Content-Type: application/json' -d '{"password":"<強いパスワード>"}'`。以後は `POST /api/auth/login` に `{"username":"ARTEX","password":"..."}` を投げ、返る `{"token":...}` を使う。
- 3) タスク作成: `curl -s -X POST http://localhost:8787/api/tasks -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' -d '{"description":"<対象の説明>","goal":"<達成したいこと>"}'`。本文は createTaskReq の description / goal（ほかに llm_profile_ids、company_ids、timeout_seconds、seed_first_intent、coverage_enabled、intercept_rules など）。
- 4) 監視: `GET /api/tasks/{id}` で状態、`GET /api/logs/stream`（SSE）で実行ログを購読する。
- 5) スキルとして使わせるなら `skills/<name>/SKILL.md` を作る。frontmatter は `name` と `description`、本文に手順と禁止事項を書く（同梱の api-recon / playwright-cli / scopesentry が実例）。
- 6) リモート MCP を使う場合は「システム設定」で http（Streamable HTTP）か sse を選び、URL と `Authorization: Bearer <token>` を登録する（旧 SSE は `/sse` を指定）。

## 変更履歴

- 2026-11-09: 初回登録
