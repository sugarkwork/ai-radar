---
name: "devvm"
genre: "coding-agent"
url: "https://github.com/devvmhq/devvm"
repo: "devvmhq/devvm"
license: "MIT"
stars: 628
language: "Go"
created: "2026-11-06"
updated: "2026-11-14"
forks: 31
open_issues: 2
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 21510
archived: false
flags: ["unverified"]
risk_notes: "READMEではApple silicon Macとarm64/x86_64のLinuxでテスト済みとし、Intel Macでは未テストとしている。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/RoundtableSpace/status/2118874827683774478"]
fetched_at: "2026-11-14T17:06:57.264416+00:00"
---

# devvm

## 出来ること

- プロジェクトフォルダごとに独立したVMサンドボックスを用意する。プロジェクト内のファイルからツールチェーンを検出し、Claude Code、Codex、opencode、pi、Cursor CLIをVM内で実行できる。組み込みのdocker、nix、desktopレイヤーにも対応する。READMEは、VMが既定で許可リスト方式のネットワーク層を使い、シークレットはホスト側に置かれると説明している。

## 目的・背景

- プロジェクトのツールチェーンを備えた隔離環境で、利用者またはコーディングエージェントが作業を始められるようにする。プロジェクトを通常の共有マウントで使う方法に加え、作業ツリーと.gitに触れない独立クローンで作業し、後で変更を確認して取り込む方法も提供する。

## 依存関係

- VMのバックエンドにLimaを使用する。READMEの要件はmacOS 13以降またはLinux、arm64またはx86_64、Lima 2.2以降。macOSではHomebrewのインストール手順がLimaも導入し、Linux向けインストールスクリプトはLima、QEMUまたは/dev/kvmへのアクセスが必要な場合に確認を求めると記載されている。

## 実行条件

- 初回起動時にVMサイズ、各VMに含めるコーディングエージェント、ベースイメージの追加要素などを設定し、ベースイメージを作成する。READMEによれば作成には数分かかり、後続のVM起動は数秒。Apple silicon Macおよびarm64/x86_64 Linuxでテスト済みで、Intel Macは未テスト。

## 最短手順

- README記載の手順では、対応環境にdevvmをインストールし、`devvm doctor`で必要条件を確認する。次にプロジェクトディレクトリへ移動して`devvm`を実行し、VMの内容を確認して作成する。起動したVMのシェル内でエージェントを実行する。クローンで作業する場合は`devvm --clone`でVMを作り、後からホスト側で`git fetch devvm`し、変更を確認する。

## 変更履歴

- 2026-11-14: 初回登録
