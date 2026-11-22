---
name: "CUPS Web"
genre: "other"
url: "https://github.com/hanxi/cups-web"
repo: "hanxi/cups-web"
license: "MIT"
stars: 1528
language: "Go"
created: "2025-12-30"
updated: "2026-11-15"
forks: 193
open_issues: 3
commits_30d: 13
commit_cadence: "weekly"
commits_90d: 64
size_kb: 77655
archived: false
flags: ["unverified"]
risk_notes: "管理画面からアップロードした.debは、コンテナ内でrootとしてインストールスクリプトを実行する。信頼できる出所のパッケージのみを使う必要がある。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/bkdgiffug/status/2118967689159082344"]
fetched_at: "2026-11-16T22:01:07Z"
last_release: "v0.2.27"
last_release_at: "2026-11-15"
---

# CUPS Web

## 出来ること

- ブラウザーからファイルを送ってCUPS経由で印刷し、印刷記録を追跡するWebツール。READMEにはPDF・画像・Office文書などの印刷、スキャン、フォント管理、プリンタードライバー管理が記載されている。

## 目的・背景

- READMEでは、家庭や小規模オフィス向けのWeb印刷管理ツールとして説明されている。中国語フォントが不足した場合の文書レイアウト崩れを防ぐため、フォント管理と変換前の不足チェックも提供すると説明している。

## 依存関係

- README記載の構成要素にはCUPS、SQLite、LibreOffice（Office文書のPDF変換）、Ghostscript（スキャンPDF生成など）、SANEのscanimage（スキャン）が含まれる。機能やイメージによって必要要素は異なる。

## 実行条件

- READMEはDocker利用を案内し、スキャン機能にはscanimageとlibsane-hpaioを含むAIOイメージを記載している。プリンターやスキャナーの対応状況は機器・ドライバー・SANEバックエンドに依存する。

## 最短手順

- READMEの案内では、Docker Hubのイメージを利用するか、ソースからmake allでビルドする。スキャン機能については、masterタグのイメージが未更新の場合devタグを使うよう記載されている。READMEには実際の導入コマンドや接続設定の全容が含まれていないため、詳細はリポジトリの手順を確認する。

## 変更履歴

- 2026-11-15: 初回登録
