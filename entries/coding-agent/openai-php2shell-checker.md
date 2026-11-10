---
repo: "openai/php2shell-checker"
name: "PHP Version Checker"
genre: "coding-agent"
url: "https://github.com/openai/php2shell-checker"
license: "Apache-2.0"
stars: 1468
forks: 147
open_issues: 2
size_kb: 34
language: "JavaScript"
created: "2026-10-21"
updated: "2026-10-22"
archived: false
commits_30d: 8
commits_90d: 8
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "READMEとスキル文書を確認した。コードは実行しておらず、実環境での判定結果、Node.jsの最低対応バージョン、各ベンダーの修正情報との照合は未検証。公開Releasesページにはリリースの掲載がなく、最新リリースAPIは未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2115051156703772686"]
fetched_at: "2026-11-10T11:48:17Z"
---

# PHP Version Checker — CodexでPHP2Shellの修正状況を確認

## 出来ること

- URLモードは管理対象サイトがHTTPヘッダーで公開するPHP版数を読み取り、OK、POTENTIALLY VULNERABLE、UNKNOWNのいずれかを返す。JSON出力にも対応する。攻撃用のリクエストは送信しない。
- サーバー用スキルは、サイトを処理しているPHPとそのパッケージを特定し、配布元の勧告と照合する手順を提供する。

## 目的・背景

- READMEが示す上流の修正版は8.2.35、8.3.36、8.4.27、8.5.12。URLモードはこれらの修正版より古い版や、5.4〜5.6、7.0〜7.4、8.0、8.1を警告対象とする。
- URLモードのOKは表示上の版数が上流の修正基準を満たすという意味に限られる。ヘッダーが伏せられていればUNKNOWNとなり、配布元による修正のバックポートはヘッダーから判定できない。

## 依存関係

- スキルとして使う場合はCodexと同梱のphpcheck-urlまたはphpcheck-serverを使う。URLチェッカーの直接実行にはNode.jsを使う。リポジトリのライセンスはApache-2.0。

## 実行条件

- URLモードには管理対象サイトへのHTTP接続が必要。X-Powered-ByとServerを読み、HEADが405または501を返した場合だけGETに切り替える。リダイレクト先と本文は調べない。
- サーバー側の確認には、実際にサイトを処理しているPHPのバイナリやモジュールと、そのパッケージを調べられる権限が必要。更新後にワーカーが再起動したかも確認する。

## 最短手順

- Codexで `$skill-installer install both skills from https://github.com/openai/php2shell-checker` を依頼する。
- 管理対象サイトのURLを `$phpcheck-url` に渡す。サーバーにアクセスできる場合は `$phpcheck-server` でサイトを処理しているPHPの修正状況を確認する。

## 変更履歴

- 2026-11-10: 初回登録
