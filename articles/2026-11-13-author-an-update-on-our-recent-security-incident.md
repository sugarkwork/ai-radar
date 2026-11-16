---
name: "An update on our recent security incident"
genre: "article"
url: "https://cursor.com/blog/security-incident-update"
published: "2026-11-13"
flags: []
type: "article"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/ueo0j/status/2122146243509973404"]
fetched_at: "2026-11-16T08:16:42.142206+00:00"
---

# An update on our recent security incident

## テーマ

- Cursorが2026年10月に確認したセキュリティインシデントについて、調査結果と影響範囲、対応をまとめた公式報告。

## 著者の主張

- Cursorの説明では、Fireworks向けに発行したアクセスキーが漏えいし、攻撃者は読み取り専用ストレージバケットからデータをコピーした。その中の一部のコーディングエージェントのトレースに未秘匿化の認証情報があり、そこからCursorの一部SaaSツールやアーカイブ済みの非本番ソースコードなどへアクセスされた。2026年10月29日には、CursorのVS Code拡張マーケットプレイスのキャッシュにClaude Code拡張の悪意あるコピーが置かれ、特定バージョンを要求した最大5,000人が約11時間影響を受けた可能性がある。Cursorは攻撃者の最後の活動を11月1日とし、インシデントは封じ込められたと報告している。

## 裏取り・注意点

- 公開日はCursor公式ブログの一覧でも2026年11月13日と確認。経路、人数、影響割合、封じ込め状況、実施した対策はCursor自身の調査・報告に基づくもので、独立した第三者検証ではない。Cursorは、非Privacy Mode利用者のエージェントトレースが0.05%未満に影響し、API認証情報が露出した顧客は0.01%未満と説明している。また、影響を受けた可能性がある拡張のバージョンと対応手順を案内しているため、該当環境の調査には公式記事内のセキュリティ通知を参照すること。

## 出典

- Cursor公式記事「An update on our recent security incident」: https://cursor.com/blog/security-incident-update
Cursor公式ブログ記事一覧（公開日確認）: https://cursor.com/blog/topic/company

## 変更履歴

- 2026-11-16: 初回登録
