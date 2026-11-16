---
name: "AWS Secrets Manager のクロスアカウント複製対応"
genre: "article"
url: "https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-cross-account/"
published: "2026-11-13"
flags: []
type: "article"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/ueo0j/status/2122146243509973404"]
fetched_at: "2026-11-16T08:20:31.366817+00:00"
---

# AWS Secrets Manager のクロスアカウント複製対応

## テーマ

- AWS Secrets Managerで、プライマリシークレットの値を別AWSアカウントのレプリカへ複製する機能の発表。

## 著者の主張

- AWSは、レプリカをクロスアカウントアクセス、バックアップ、災害復旧に利用でき、プライマリの値の変更やローテーションに応じて自動更新されると説明している。レプリカは独立したリソースで、レプリカ側アカウント所有のカスタマーマネージドKMSキーで暗号化される。これはAWS公式記事による機能説明であり、独立した実機検証の結果ではない。

## 裏取り・注意点

- AWS公式ユーザーガイドでは、複製は非同期で結果整合性があり、更新が即時に反映されない場合があると説明している。プライマリとレプリカは同一リージョンである必要があり、プライマリごとにクロスアカウントレプリカは1つまで。レプリカにはカスタマーマネージドKMSキーが必要。複製の構成には両アカウントの所有者が関与する。料金の詳細はAWSの料金ページ参照。

## 出典

- AWS What's New（2026-11-13）: https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-cross-account/
AWS Secrets Manager User Guide: https://docs.aws.amazon.com/secretsmanager/latest/userguide/cross-account-replicate-secrets.html

## 変更履歴

- 2026-11-16: 初回登録
