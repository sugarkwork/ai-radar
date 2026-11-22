---
name: "RTK (Rust Token Killer)"
genre: "coding-agent"
url: "https://github.com/rtk-ai/rtk"
repo: "rtk-ai/rtk"
license: "Apache-2.0"
stars: 86937
language: "Rust"
created: "2026-01-22"
updated: "2026-11-17"
forks: 5584
open_issues: 1670
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 20442
archived: false
flags: ["unverified"]
risk_notes: "READMEはライセンス表示をApache-2.0とBUSL-1.1の併記としている一方、取得済みAPIデータはApache-2.0を示している。適用されるライセンス条件は未確認。削減率はREADME記載の作者側の説明であり、独立した実測ではない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:14:23.081035+00:00"
---

# RTK (Rust Token Killer)

## 出来ること

- AIコーディングエージェントが読むシェルコマンド出力を圧縮する。READMEはテスト、diff、ログ、ビルド出力など100以上のコマンドを挙げ、`rtk gain`で削減状況を確認できるとしている。また、`rtk bypass`でコマンドをフィルターせず実行し、全出力を得る手順も示している。

## 目的・背景

- コマンド出力を短くし、エージェントが読む入力トークンを減らすことを目的とする。READMEは、コマンド出力の削減率がそのまま費用削減率になるわけではないと説明し、トークン数はbytes / 4で推定するため絶対値は概算としている。

## 依存関係

- READMEから依存関係の詳細は確認できない。

## 実行条件

- READMEに記載された導入方法は、macOSおよびLinuxのHomebrew、Windowsのwinget、Linux・macOS・WSLのインストールスクリプト。導入後に`rtk init -g`を実行し、エージェントを再起動する手順が示されている。

## 最短手順

- Homebrewなら`brew install rtk`、Windowsなら`winget install rtk-ai.rtk`で導入し、`rtk init -g`を実行してエージェントを再起動する。削減状況は`rtk gain`で確認する。

## 変更履歴

- 2026-11-22: 初回登録
