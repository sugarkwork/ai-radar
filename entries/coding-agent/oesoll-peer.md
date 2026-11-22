---
name: "peer"
genre: "coding-agent"
url: "https://github.com/oesoll/peer"
repo: "oesoll/peer"
flags: ["unverified"]
risk_notes: "Codex対応はREADMEでClaude対応より新しく、テストが少ないと説明されている。Claude Codeのクロスセッション受信方式は公開APIではなく、更新で動作が変わる可能性がある。"
stars: 13
forks: 0
open_issues: 0
size_kb: 17167
language: "Python"
created: "2026-10-31"
updated: "2026-11-16"
archived: false
license: "MIT"
commits_30d: 27
commits_90d: 27
commit_cadence: "daily"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119244765325594625"]
fetched_at: "2026-11-18T00:28:37.737506+00:00"
---

# peer

## 出来ること

- Claude CodeとCodexのセッション間で名前を指定してメッセージを送り、配信状態や応答を確認できる。近くのセッション一覧、応答待ち、履歴参照、セッション起動、複数マシン間の接続にも対応する。READMEによると、Claude Codeでは組み込みのクロスセッション受信経路を使い、Codexではpeer経由で起動したセッションにapp-serverのturn/startとturn/steerを使う。

## 目的・背景

- 複数のコーディングエージェント間の連絡を、ターミナル画面の読み取りや入力操作に頼らず行うためのツール。READMEは、ターミナルへの入力では承認プロンプトへの誤入力や未送信の見落としが起こりうると説明している。

## 依存関係

- Python 3.9以上が必要。tmuxを使うとpeer spawnと近接セッション優先の一覧表示が利用できる。tmuxの代わりにsmセッションレイヤーも利用できるとREADMEに記載されている。

## 実行条件

- 手動インストール例はシェルでinstall.shを実行し、peer installとpeer doctorを実行する。Claude Codeの受信設定やCodexの起動方法はオプションで、Codexセッションへの配信にはpeer経由での起動が必要。別マシンとのSSH接続には両側へのpeer導入とhosts.json設定が必要。SSHを使わない同一ネットワーク接続ではpair後にserveを起動する。

## 最短手順

- README記載の手動手順: `curl -fsSL https://raw.githubusercontent.com/oesoll/peer/main/install.sh | sh`、続けて `peer install --accept-inbound --codex-alias`、`peer doctor`。試用は `peer` で一覧を確認し、`peer say NAME "text"` でメッセージを送る。

## 変更履歴

- 2026-11-22: 初回登録
