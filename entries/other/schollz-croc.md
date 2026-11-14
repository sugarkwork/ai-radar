---
name: "croc"
genre: "other"
url: "https://github.com/schollz/croc"
repo: "schollz/croc"
stars: 40930
forks: 1655
open_issues: 3
size_kb: 12989
language: "Go"
created: "2017-10-17"
updated: "2026-11-13"
archived: false
license: "MIT"
commits_30d: 74
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/awe0_io/status/2118741799170875870"]
fetched_at: "2026-11-14T00:16:37.327647+00:00"
---

# croc

## 出来ること

- コンピューター間でファイルやフォルダーを転送するCLIです。READMEでは、リレーへのフォールバックを備えたP2P転送、PAKEを用いたエンドツーエンド暗号化、複数ファイル転送、中断した転送の再開、IPv6優先とIPv4へのフォールバック、プロキシ利用を機能として説明しています。これらはREADMEに記載された機能で、独立した実測結果ではありません。

## 目的・背景

- READMEでは、異なるコンピューター間でファイルやフォルダーを簡単に転送するツールとして紹介されています。ローカルサーバーの設置やポートフォワーディングは不要と説明されています。

## 依存関係

- READMEに記載されたビルド手順ではGo 1.27.3以降が必要です。インストール方法として、OS別パッケージ、リリースバイナリ、Docker、Conda、ソースからのビルドが紹介されています。

## 実行条件

- 送信側と受信側でcrocを利用します。READMEにはWindows、Linux、Mac、ブラウザー間の転送に対応するとあります。Docker利用時はDockerが必要で、転送範囲は現在のディレクトリとそのサブディレクトリに限られると説明されています。

## 最短手順

- 送信側で `croc send [file(s)-or-folder]` を実行し、表示されたコードフレーズを受信側に共有します。受信側は `croc code-phrase` を実行します。コードフレーズはPAKEによる鍵合意に使われるとREADMEに記載されています。

## 変更履歴

- 2026-11-14: 初回登録
