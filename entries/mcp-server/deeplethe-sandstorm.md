---
type: "repo"
name: "Sandstorm"
genre: "mcp-server"
url: "https://github.com/deeplethe/sandstorm"
author: "deeplethe"
repo: "deeplethe/sandstorm"
license: "Apache-2.0"
stars: 5124
language: "Rust"
created: "2026-05-11"
updated: "2026-11-01"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/Ryrenz/status/2117059702542455253"]
flags: []
risk_notes: "自前ホスト前提: Linux + cgroup v2 と gVisor の runsc が必要（Firecracker バックエンドは KVM 必須）。master は専用 CA で署名した証明書を使うため、クライアントは ca.pem を明示指定する必要がある。API トークンはサンドボックス内で任意コマンドを実行できる権限と等価なので、取り扱いに注意。E2B 互換エンドポイントは別リスナー (--e2b-bind / --e2b-domain) で公開される。"
forks: 403
open_issues: 14
commits_30d: 100
commit_cadence: "daily"
size_kb: 10635
archived: false
fetched_at: "2026-11-06T11:33:38Z"
last_release: "v0.6.0"
last_release_at: "2026-11-01"
source_post: "https://x.com/Ryrenz/status/2117059702542455253"
---

# Sandstorm — アイドル時スナップショットで1台に数千のエージェントサンドボックスを載せるランタイム

## 出来ること

- サンドボックスを hot / frozen / snapshot / detached の4段階で管理し、遊休中は一時停止・ディスクへスナップショット、リクエスト時に復帰させる（README 記載の目安: frozen から約0.1秒、ディスクから約0.2秒）
- gVisor コンテナと Firecracker microVM の2バックエンドを同一フリートで混在運用でき、各サンドボックスは独立したネットワーク名前空間を持つ
- 単一バイナリ sandstormd がマスター・ノード・Web コンソールを兼ね、ノードは NAT 配下からでもマスターへ外向き接続して参加できる
- MCP サーバ sandstorm-mcp が list_templates / spawn_sandboxes / exec_command / eval_code / branch_sandbox / kill_sandbox などのツールを公開し、エージェントが自分でサンドボックスを起動してコードを実行できる
- HTTP API (v1) でテンプレート作成（コンテナイメージから）、サンドボックス起動・exec・eval・ping・ブランチ（チェックポイント）・egress 制御を操作できる
- E2B 公式 SDK をそのまま向けられる互換リスナー（--e2b-bind / --e2b-domain）とレシピ recipes/e2b-codeinterpreter を同梱

## 目的・背景

- エージェントは実行の合間に長く待つため、コード実行サンドボックスはアイドル状態でもメモリを占有し続け、1台に少ししか載せられないという問題がある
- Sandstorm は待機中のサンドボックスを凍結・スナップショットしてメモリを解放し、要求が来たら素早く起こすことで、同時稼働数より多くのサンドボックスを1台に収容する
- 復帰はゲートウェイ経由の wake-on-traffic で行い、2秒以内に起動できない要求は待たせずに拒否する設計（README のレイテンシ表）
- v0.6 で gVisor が既定バックエンドになり、KVM なしのノードでも動作する

## 依存関係

- Linux ホストと cgroup v2
- gVisor の runsc を PATH に配置（既定バックエンド。KVM 不要）
- Firecracker バックエンドを使う場合は KVM が使えるホスト
- Web コンソールのビルドに Node 22.12 以降、ソースからビルドする場合は Rust
- Releases に x86_64 Linux 向けビルド済み tarball（sandstorm-v0.6.0-x86_64-linux.tar.gz）があり、ソースビルドを省略できる
- MCP サーバは pip install sandstorm-mcp（PyPI 公開、確認時点 0.3.0）で導入し、稼働中の master に接続する

## 実行条件

- 自分で master（とノード）をホストする必要があり、マネージドサービスではない
- master の API トークン（既定 /var/lib/sandstorm/pki/api-token）と CA 証明書（GET /ca.pem）を取得してクライアントに渡す
- master の証明書は 127.0.0.1 / localhost / --bind アドレスのみ有効なため、別名で接続する場合は --tls-san を付けて起動する
- サンドボックスを起動する前にテンプレート（コンテナイメージ由来）を1つ登録しておく
- v0.6 は master の API トークンに加え、spawn 時に返るサンドボックス個別トークン（`x-sandstorm-sandbox-token`）が exec/eval/ping/wait に必須。個別トークンは spawn 応答でしか返らないので保持する
- MCP 利用時は SANDSTORM_URL / SANDSTORM_TOKEN / SANDSTORM_CA を設定する（CA 未設定だと CERTIFICATE_VERIFY_FAILED で全ツールが失敗する）

## 最短手順

- 1. master + node を同居起動: `sudo ./sandstormd serve --master --node` → コンソールは https://127.0.0.1:8080
- 2. 認証情報を取得: `curl -k https://127.0.0.1:8080/ca.pem -o ca.pem`、トークンは `/var/lib/sandstorm/pki/api-token` を読む
- 3. テンプレートを1つ作る: コンソールの「+ From an image」または `POST /v1/templates/from-image`
- 4. AI から使う準備: `pip install sandstorm-mcp` し、MCP クライアント（Claude Desktop / Claude Code / Cursor など）に `SANDSTORM_URL=https://127.0.0.1:8080`, `SANDSTORM_TOKEN=<token>`, `SANDSTORM_CA=/abs/path/ca.pem` を渡して sandstorm-mcp を登録する
- 5. エージェント側の呼び出し: `list_templates` → `spawn_sandboxes`（template と個数 n）→ 返ってきた token を保持 → `exec_command` または `eval_code` でコードを実行 → 状態を残したい場合は `branch_sandbox` でタグ化 → `kill_sandbox`
- 6. 素の HTTP で呼ぶ場合: `Authorization` ヘッダに API トークンを Bearer 形式で入れ、`POST /v1/sandboxes` に `{"template":"base","port":8000}` を送る（応答の `token` はこの時だけ返るので保存）。次に `POST /v1/sandboxes/:id/exec` へ `{"args":["python3","-c","print(2+2)"],"timeout_secs":30}` と `x-sandstorm-sandbox-token` ヘッダにサンドボックスの token を付けて送る
- 7. 拠点を増やす場合: `scripts/fleet.sh up --master m1 --nodes n1,n2,n3 --listen 80` → `seed` → `verify`

## 変更履歴

- 2026-11-06: 初回登録
