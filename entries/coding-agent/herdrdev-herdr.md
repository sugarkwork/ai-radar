---
type: "repo"
repo: "herdrdev/herdr"
name: "herdr"
genre: "coding-agent"
url: "https://github.com/herdrdev/herdr"
license: "Apache-2.0"
stars: 49491
language: "Rust"
created: "2026-03-27"
updated: "2026-11-07"
forks: 3993
open_issues: 455
commits_30d: 49
commits_90d: "100+"
commit_cadence: "daily"
size_kb: 49708
archived: false
added: "2026-11-09"
fetched_at: "2026-11-09T03:42:27Z"
flags: ["unverified"]
risk_notes: "Apache-2.0。再起動後は保存レイアウトや対応エージェントのセッションを復元できる場合があるが、プロセス継続とは異なる。 実行・品質は未検証。"
sources: ["https://x.com/i/status/2119588334615802105", "https://github.com/herdrdev/herdr"]
---

# herdr

## 出来ること

ターミナル上の複数エージェントを分割表示し、切断後もバックグラウンドで動かし、稼働・待機・停止状態を見られる。

## 目的・背景

コーディングエージェントをラップせずターミナルを管理するRust製ランタイム。SSH接続先もまとめられる。

## 依存関係

対応CLIとターミナル。SSH利用時は接続先の環境。

## 実行条件

クライアント切断中の処理は継続するが、マシン再起動後に元プロセス自体は生存しない。

## 最短手順

公式の対応OS向けリリースまたはパッケージマネージャーから導入し、ターミナルで `herdr` を起動する。

## 注意点

Apache-2.0。再起動後は保存レイアウトや対応エージェントのセッションを復元できる場合があるが、プロセス継続とは異なる。 実行・品質は未検証。

## 出典

- [公式リポジトリ](https://github.com/herdrdev/herdr)
- [紹介投稿](https://x.com/i/status/2119588334615802105)
