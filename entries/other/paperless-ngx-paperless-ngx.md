---
repo: "paperless-ngx/paperless-ngx"
name: "Paperless-ngx"
genre: "other"
url: "https://github.com/paperless-ngx/paperless-ngx"
license: "GPL-3.0"
stars: 47969
forks: 3372
open_issues: 9
size_kb: 234527
language: "Python"
created: "2022-02-12"
updated: "2026-11-10"
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "OCR精度、検索性能、外部AIからの接続は実機で未検証。最新リリースのタグと公開日時は /releases/latest で未確認。コミット数は両期間とも取得上限のため100件以上。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117960732184633699"]
fetched_at: "2026-11-10T11:14:04+00:00"
---

# Paperless-ngx — スキャン文書をOCRで全文検索できるセルフホスト型アーカイブ

## 出来ること

- 領収書、請求書、契約書などを取り込み、OCRで抽出したテキストをWeb UIやREST APIから全文検索できる。

## 目的・背景

- 紙の書類を検索可能なアーカイブにする。ローカルOCRにはOCRmyPDFとTesseractを使う。検索機能は公式仕様で確認したもので、OCR精度や検索性能は未測定。

## 依存関係

- 公式のコンテナ構成にはDockerとDocker Compose、Redis互換のメッセージブローカーが必要。同梱Composeの既定ブローカーはValkey。新規導入では公式ガイドがPostgreSQLを推奨する。

## 実行条件

- GPL-3.0。READMEによると保存データは平文なので、機密文書を扱う場合は信頼できるホストとバックアップを用意する。日本語のOCRには言語データを追加し、OCR言語を `jpn` に設定する。

## 最短手順

- [公式セットアップ](https://docs.paperless-ngx.com/setup/)に沿ってデータベースに対応するComposeファイルと環境設定を用意し、`docker compose up -d` で起動する。Web UIで初期ユーザーを作成し、テスト用のPDFを取り込んで本文の語句で検索する。
- AIから呼ぶには、文書の閲覧権限を持つ専用ユーザーのプロフィールでAPIトークンを作る。エージェント側のHTTPツールで `Authorization: Token <token>` を付け、`GET /api/documents/?query=<URLエンコード済み検索語>` を呼び出す。トークンはツール側の秘密設定に置き、結果から必要な文書だけをAIに渡す。[公式REST API](https://docs.paperless-ngx.com/api/)

## 変更履歴

- 2026-11-10: 初回登録
