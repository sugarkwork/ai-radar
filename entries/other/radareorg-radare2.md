---
name: "radare2"
genre: "other"
url: "https://github.com/radareorg/radare2"
repo: "radareorg/radare2"
license: "unknown"
stars: 25456
language: "C"
created: "2012-07-03"
updated: "2026-11-18"
forks: 3454
open_issues: 788
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 217267
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでlicenseがunknown。READMEは本体をLGPLv3と説明している一方、プラグインごとにライセンスが異なるとしている。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:20:03.437614+00:00"
---

# radare2

## 出来ること

- READMEによると、radare2はバイナリの解析、エミュレーション、デバッグ、変更、逆アセンブルに対応する低レベルのコマンドラインツールとライブラリ・プラグイン群。ローカルファイルやカーネルメモリを扱い、ローカルまたはリモートのgdb/windbgサーバー経由でプログラムをデバッグできる。組み込みJavaScriptインタープリターやr2pipeによるスクリプト実行も説明されている。

## 目的・背景

- READMEでは、フォレンジック向けのコマンドライン16進エディターとして始まり、現在はリバースエンジニアリング向けのフレームワークになったと説明している。

## 依存関係

- ソースビルドではmeson/ninja（muon/samuも可）またはmakeがサポートされる。WindowsビルドにはmesonとMSVCまたはmingwが必要とREADMEに記載。

## 実行条件

- READMEはWindows、Linux、Darwinなどの対応OSと、多数のCPUアーキテクチャ・ファイル形式を列挙している。実行環境や個別機能の詳細条件は公式インストール資料を参照。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の推奨ソース導入手順は `git clone https://github.com/radareorg/radare2` の後に `radare2/sys/install.sh` を実行。基本操作例は `r2 /bin/ls` でファイルを読み取り専用で開き、`aaa` で解析、`afl` で関数一覧、`px 32` で16進表示、`q` で終了。

## 変更履歴

- 2026-11-23: 初回登録
