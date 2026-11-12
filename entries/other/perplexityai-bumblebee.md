---
name: "Bumblebee"
genre: "other"
url: "https://github.com/perplexityai/bumblebee"
repo: "perplexityai/bumblebee"
stars: 5148
forks: 464
open_issues: 49
size_kb: 173
language: "Go"
created: "2026-05-20"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 7
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/rvaniaaaa/status/2120861156801647094"]
fetched_at: "2026-11-12T15:08:49.664301+00:00"
---

# Bumblebee

## 出来ること

- macOS・Linuxの開発端末で、パッケージ、エディタ・ブラウザ拡張、対応するMCP設定などのメタデータを読み取り、NDJSON形式のコンポーネント記録を出力する。露出カタログを指定すると、既知の対象との一致を検出できる。READMEは「read-only exposure checks」と説明している。出典: https://github.com/perplexityai/bumblebee

## 目的・背景

- アドバイザリで指定されたパッケージ、拡張機能、バージョンが開発端末のオンディスクメタデータに存在するかを確認するためのインベントリ収集ツール。READMEでは、SBOMやEDRとは異なる、端末上のローカル状態を把握する用途として説明されている。出典: https://github.com/perplexityai/bumblebee

## 依存関係

- Go 1.25以降が必要。READMEによれば、単一の静的バイナリで、標準ライブラリ以外の依存関係はない。出典: https://github.com/perplexityai/bumblebee

## 実行条件

- baseline、project、deepの3プロファイルがある。各実行は1回のスキャン後に終了し、定期実行の頻度はcron、launchd、systemd、MDMなど外部の実行環境が担う。baselineとprojectはホームディレクトリ直下をスキャンせず、deepでは明示したrootが必要。出典: https://github.com/perplexityai/bumblebee

## 最短手順

- README記載の手順では、Go 1.25以降の環境で `go install github.com/perplexityai/bumblebee/cmd/bumblebee@latest` を実行してインストールし、`bumblebee scan --profile baseline > inventory.ndjson` で基本インベントリを出力する。出典: https://github.com/perplexityai/bumblebee

## 変更履歴

- 2026-11-12: 初回登録
