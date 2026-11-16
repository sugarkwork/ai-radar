---
name: "UnrealIRCd 6.2.7.1 released & hot-patch to fix 9 security issues, including one CRITICAL (CVE-2026-114713)"
genre: "article"
url: "https://forums.unrealircd.org/viewtopic.php?t=9487"
published: "2026-11-07"
flags: ["unverified"]
risk_notes: "脆弱性の影響や悪用状況、修正内容は投稿者の告知に基づく。独立した検証結果ではない。"
type: "article"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/ueo0j/status/2122146243509973404"]
fetched_at: "2026-11-16T08:22:49.798476+00:00"
---

# UnrealIRCd 6.2.7.1 released & hot-patch to fix 9 security issues, including one CRITICAL (CVE-2026-114713)

## テーマ

- UnrealIRCd 6.2.7.1のリリースと、重大な権限昇格問題を含む9件のセキュリティ問題への対処を告知する記事。

## 著者の主張

- 投稿者Syzopは、通常ユーザーがサーバーまたはIRCOp権限でコマンドを実行できる重大な問題（CVE-2026-114713）を含む9件を修正したと説明している。記事では、UnrealIRCd 6の一部ネットワークで再起動不要のホットパッチが使えること、また6.2.7.1への更新も選べることを案内。ホットパッチ後の確認例として、module-status出力にパッチバンドル名または修正版のバージョンが表示されることを挙げている。これらは投稿者による報告・手順である。

## 裏取り・注意点

- 記事本文には、ホットパッチ対象のバージョン範囲、適用手順、適用後の確認方法が記載されている。重大問題への一時的なSPAMFILTER回避策も示されるが、記事は他の8件も修正するためホットパッチまたは更新を続けるよう述べている。実環境での適用や脆弱性の独立検証はこの資料からは確認できない。EOL版の扱いは版によって異なるため、対象版と公式更新情報を確認する必要がある。

## 出典

- UnrealIRCd Forumsのリリース告知（Syzop、2026-11-07）。重大問題、対処手順、修正項目の説明は投稿本文に基づく。 https://forums.unrealircd.org/viewtopic.php?t=9487

## 変更履歴

- 2026-11-16: 初回登録
