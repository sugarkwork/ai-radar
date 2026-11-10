---
repo: "Balanov/latch"
name: "LATCH"
genre: agent-framework
url: "https://github.com/Balanov/latch"
license: "MIT"
stars: 63
language: "JavaScript"
created: "2026-11-04"
updated: "2026-11-09"
added: "2026-11-05"
first_seen: "2026-11-04"
source_post: "https://x.com/RoundtableSpace/status/2118117449782460643"
sources: []
flags: []
risk_notes: ""
forks: 1
open_issues: 0
size_kb: 2460
archived: false
commits_30d: 21
commits_90d: 21
commit_cadence: "daily"
fetched_at: "2026-11-09T21:32:27Z"
last_release: ""
last_release_at: ""
---

# LATCH

## 出来ること

- エージェントとサービス（＝買い手と売り手）のあいだに置く、JSON/HTTPS の小さな契約。SDK 不要で、`GET /.well-known/latch.json` の1枚のカードと 5 オペレーションだけで成立する。
  - `ask` … 副作用なしで読む
  - `quote` … 見積り＋その内容の SHA-256 ダイジェストを返す（実行はしない）
  - `approve` … 人間側の信頼できるホストで、そのダイジェストに紐づけて承認する
  - `commit` … ダイジェスト＋承認＋`Idempotency-Key` を付けて初めて実行する
  - `status` … タスク状態と `provider_assertion` の受領証を返す
- 承認した見積りと実際の内容が一致しない場合は、接続を張る前に中断する。再試行時は同じ冪等キーを使い回す。
- Node.js 20+ の参照実装（クライアント／サーバ／CLI）が単一の ESM ファイルで、実行時依存はゼロ。任意で単一ライタの永続ストア、呼び出し元スコープの認証、MCP stdio ブリッジも付く。

## 目的・背景

エージェントに購買を任せると「何をいくらで買ったか」が曖昧なまま実行されやすい。LATCH は決済や ID の仕組みを置き換えず、**見積り→人間の承認→冪等な実行→受領証**という境界だけを定義する。MCP・A2A・OpenAPI・AP2 などとは併用する前提で、レジストリ・アカウント・テレメトリ・ホステッドプロキシ・決済レールは持たない（作者の設計方針）。

## 依存関係

- Node.js 20 以降。ライブラリ利用は `latch-protocol` の `createLatchServer()` / `listen()`。
- 新規サービスを作る場合は `npx --yes github:Balanov/latch init my-latch-service`。

## 実行条件

- **実験段階**。README が「wire version 0.1 / implementation 0.2.0（experimental）」と明記している。仕様が変わりうる。
- デモの注文はすべてシミュレーションで、支払い・製造・配送は起きない。決済レールは含まないので、実際に課金するには自前で接続する。
- `quote` と `commit` は別ハンドラとして実装する必要がある（`quote` は効果を起こさず、要約・条件・期限だけ返す）。書き込み権限を持つサービスでは、この分離が承認の意味を担保する。

## 最短手順

```bash
git clone https://github.com/Balanov/latch.git
cd latch
npm test
node latch.mjs demo --trace examples/trace.json
```

```bash
node latch.mjs demo --port 8787          # プロバイダ側
node latch.mjs quote http://127.0.0.1:8787 print3d.order '{...}'
node latch.mjs commit http://127.0.0.1:8787 off_XXXX \
  --digest sha256-XXXX --yes sha256-XXXX # 見直したダイジェストをそのまま再入力
```

## 変更履歴

- 2026-11-05: 初回登録（★164 / MIT / 公開当日 / 実装 0.2.0・wire 0.1 の実験版）
