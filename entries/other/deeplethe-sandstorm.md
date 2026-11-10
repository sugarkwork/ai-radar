---
type: "repo"
name: "Sandstorm（アイドル状態のエージェントsandboxをスナップショットして1台に数千個載せる）"
genre: "other"
url: "https://github.com/deeplethe/sandstorm"
repo: "deeplethe/sandstorm"
license: "Apache-2.0"
stars: 5955
language: "Rust"
created: "2026-05-11"
updated: "2026-11-01"
added: "2026-11-06"
first_seen: "2026-11-02"
sources: ["https://x.com/Ryrenz/status/2117059702542455253"]
flags: []
risk_notes: "レイテンシと密度の数値はすべて作者の計測（計測日 2026-10-31、ホスト構成が列ごとに異なるため各列は独立に読む必要がある、とREADME自身が明記）。Firecracker の 512MiB/1GiB 構成は各1サンプルのみ。E2B セルフホストとの比較はセットアップされておらず、PVM 下のメモリは未計測。投稿の『3600+ star』は取得時点で5124。Firecracker バックエンドには KVM が要る（gVisor は不要）。master は TLS を自前CAで切るため、コンソールはブラウザ警告を越えて開く。sandbox 内で動かすコードの安全性は sandbox の分離性能に依存するので、gVisor/Firecracker の既定設定を変える場合は自分で評価が要る。"
forks: 490
open_issues: 14
commits_30d: 100
commit_cadence: "daily"
size_kb: 10635
archived: false
fetched_at: "2026-11-09T21:40:49Z"
last_release: "v0.6.0"
last_release_at: "2026-11-01"
commits_90d: 100
---

# Sandstorm — 遊んでいるエージェントのsandboxを凍結・スナップショットして、1台に桁違いの数を載せるRust製ランタイム

## 出来ること

- **4段のsandboxライフサイクル**でアイドルを段階的に落とす：`hot`（実行中・メモリ保持）→ `frozen`（一時停止、コールドページは zswap、復帰 約0.1秒）→ `snapshot`（ディスクにチェックポイント、メモリ解放、復帰 約0.2秒）→ `detached`（ボリュームだけ残す、次回はコールドスタート）
- 2種類のバックエンドを**同一フリートで混在**させられる：gVisor コンテナと Firecracker マイクロVM。それぞれが独立したリソースプールを形成し、sandbox ごとに専用のネットワーク名前空間を持つ
- **master / node 構成**：master が SQLite に望ましい状態を持ち、sandbox の配置を決める。node はアドレス＋ペアリングコードで参加するか、NAT の内側から外へ dial して参加する
- **トラフィックで起こす**：各 node のゲートウェイがリクエストを受けると sandbox を起こして転送する
- **node の自己防衛**：メモリが逼迫すると新規受付を拒否するので、SSH が落ちない
- **バイナリ1つ**：`sandstormd` が master・node・Webコンソールを兼ねる
- Webコンソールで sandbox の状態、段の遷移、node の残容量、作成数/分、API p99 を見られる
- ウォームテンプレート（アプリを起動済みの状態のイメージから復帰させる、opt-in）も使える

## 目的・背景

- エージェント用のコード実行 sandbox は、実際にはほとんどの時間アイドルなのにメモリを掴み続ける。その結果1台に十数個しか載らない。Sandstorm は「同時に動かす数」ではなく「同時に保持できる数」を増やす方向で解いている
- 作者の計測（2026-10-31）：ウォームテンプレートからの起動は Firecracker で 84ms（KVM機で100ms）、ディスクからの復帰は 64MiB アプリで 130〜150ms。比較では Docker+gVisor 685ms、microsandbox 1.1秒、Kata 3.4秒。実行中 sandbox のスナップショットは 30ms（比較対象 CubeSandbox は 304ms）
- 密度：gVisor node（2コア2GB）で 64MiB アプリを約12個まで同時に起動状態に保てる。トラフィック試験は node あたり sandbox 40個・一部に集中する形で行い、p50 は 6〜10ms、p99 は約2秒（復帰待ちのリクエスト）
- 2秒以内に起動できない起こし要求はキューに積まず拒否する（gVisor node は同時2件復帰・4件待ちなので、10件同時に起こすと6件応答・残りは即503）
- 開発元は DeepLethe

## 依存関係

- Linux（**cgroup v2**）、gVisor の `runsc` が PATH にあること、Rust ツールチェーン、コンソールのビルドに Node 22.12 以上
- Firecracker バックエンドを使う場合は KVM が要る（gVisor は KVM 不要）
- master の状態は SQLite。ノード間は master 経由で接続
- Webコンソールは `npm --prefix web/console ci && npm --prefix web/console run build`

## 実行条件

- 単体起動なら master と node を1プロセスで兼ねられる（`sandstormd serve --master --node`）。コンソールは `https://127.0.0.1:8080`、自前CAのためブラウザ警告を越えて開く。APIトークンは `/var/lib/sandstorm/pki/api-token`
- **`sudo` が必要**（sandbox のネットワーク名前空間と cgroup を扱うため）
- フリートにする場合は各マシンへ SSH できることが前提（`scripts/fleet.sh`）
- クライアントが別マシンから繋ぐ場合、master 証明書にその名前を `--tls-san` で入れておく必要がある
- sandbox の上限密度はホストのメモリとスワップ量に強く依存する（PVM ホストでスワップ無しの場合、64MiB アプリが約8個までという計測がある）
- 耐障害性・マルチテナント分離の強度は自分で評価すること。README は性能比較が中心で、セキュリティ監査の記載は無い

## 最短手順

```bash
# 1) 前提: Linux + cgroup v2、gVisor の runsc、Rust、Node 22.12+
git clone https://github.com/deeplethe/sandstorm.git && cd sandstorm

# 2) コンソールのビルドとバイナリのビルド
npm --prefix web/console ci && npm --prefix web/console run build
cargo build --release -p sandstorm-core

# 3) master と node を1プロセスで起動
sudo ./target/release/sandstormd serve --master --node
#   コンソール: https://127.0.0.1:8080
#   APIトークン: /var/lib/sandstorm/pki/api-token
#   → 「+ From an image」でテンプレートを作り、そこから sandbox を起動

# 4) 複数台のフリートにする場合
scripts/fleet.sh up --master m1 --nodes n1,n2,n3 --listen 80
scripts/fleet.sh seed       # 各ノードにテンプレートを配る
scripts/fleet.sh verify     # 1つ起動して動作確認
```

コンソールでできることは全て HTTP API からも実行できる（`docs/API.md`）。

## 変更履歴

- 2026-11-06: 初回登録
