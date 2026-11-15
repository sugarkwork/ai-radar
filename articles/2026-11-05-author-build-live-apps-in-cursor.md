---
name: "Build Live Apps in Cursor"
genre: "article"
url: "https://cursor.com/changelog/build-live-apps"
published: "2026-11-05"
flags: ["unverified"]
risk_notes: "投稿にある「.env」やsource mapを含む個別の検査対象は、確認した公式記事では明記されていないため記載していない。"
type: "article"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/ganfanren_ai/status/2118941347017335099"]
fetched_at: "2026-11-15T05:29:45.184985+00:00"
---

# Build Live Apps in Cursor

## テーマ

- CursorのCloud AgentでWebアプリを作成し、公開リンクで共有する機能。

## 著者の主張

- Cursorは、Cloud Agentにアプリ作成を明示すると、Webアプリのひな型作成、必要に応じたPostgresの用意、Cursor SSOによる認証設定、ホスティングを行い、公開時に選んだ固有ドメインでアプリを公開できると説明している。GitHubまたはCursor Originのリポジトリからデプロイでき、公開前に決定的およびエージェントによるセキュリティチェックを実行する。チェック通過後、特定の人・グループ・チームと共有でき、個人プランでは一般公開も可能。Cursor API keyを使ってスクリプトやGrok Botからアプリを利用する方法も案内されている。

## 裏取り・注意点

- 公式記事では、機能の対象をダッシュボード、社内ツール、ポータルなどのWebアプリとして説明している。利用にはCloud Agentを有効にした有料プランが必要。ローカルでは使えず、Cloud Agentにアプリを作ることを明示する必要がある。セキュリティチェックに失敗した場合は修正を促し、チェック通過と明示的な公開操作の両方がそろうまで公開されないと説明している。これはCursor公式資料の機能説明であり、独立した実機検証の結果ではない。

## 出典

- Cursor公式更新記事「Build Live Apps in Cursor」https://cursor.com/changelog/build-live-apps （公開日: 2026-11-05、確認: 2026-11-15T05:29:45.184985+00:00）。関連する公式ドキュメント「Apps」https://prod.cursor.com/docs/cloud-agent/apps は、Cloud Agentが必要でローカル非対応であることと、アプリ公開時のセキュリティチェックを説明している。

## 変更履歴

- 2026-11-15: 初回登録
