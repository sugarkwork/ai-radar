---
name: "Microsoft confirms Windows activation failures after November updates"
genre: "article"
url: "https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-activation-failures-after-november-updates/"
published: "2026-11-13"
flags: ["unverified"]
risk_notes: "記事は修正が数日以内に提供される見込みと報じていますが、現在の修正提供状況はこの記事から確認できません。Microsoft のサービス通知への直接リンクも記事内で確認できません。"
type: "article"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/ueo0j/status/2122146243509973404"]
fetched_at: "2026-11-16T08:25:20.643976+00:00"
---

# Microsoft confirms Windows activation failures after November updates

## テーマ

- 2026年11月の Windows 更新後に発生する、Windows のライセンス認証およびライセンス管理の失敗。

## 著者の主張

- 記事によると、Windows 10 21H2/22H2、Windows 11 23H2、Windows Server 2019/2022/2025 で、特定の slmgr.vbs コマンド実行時に 0x80041008（Invalid parameter (SWbemObjectEx)）が発生する場合がある。影響するコマンドとして `/skms-domain` と `/ipk` を挙げている。記事は、適切な KMS クライアントキーと構成があり、対象の slmgr.vbs コマンドを実行しないデバイスは影響を受けないとする。

## 裏取り・注意点

- 記事は Microsoft のサービス通知を引用・要約していますが、その通知への直接リンクは確認できません。影響条件と対処状況を適用判断に使う場合は、Microsoft の最新通知で確認してください。記事公開時点では修正が数日以内に提供される見込みとされています。

## 出典

- BleepingComputer 記事（著者: Sergiu Gatlan、公開日: 2026-11-13）: https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-activation-failures-after-november-updates/

## 変更履歴

- 2026-11-16: 初回登録
