---
name: "SCKit abuses ScreenConnect to deploy remote access and target technician sessions"
genre: "article"
url: "https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/"
published: "2026-11-13"
flags: ["unverified"]
risk_notes: "初期侵入経路は調査中と記事に記載されている。"
type: "article"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/ueo0j/status/2122146243509973404"]
fetched_at: "2026-11-16T08:23:29.151988+00:00"
---

# SCKit abuses ScreenConnect to deploy remote access and target technician sessions

## テーマ

- Microsoft Security Researchによる、SCKitがScreenConnectを悪用して不正なリモートアクセスを設置し、接続する技術者の端末や管理セッションを標的にする活動の分析。

## 著者の主張

- Microsoftは、侵害されたScreenConnect環境を通じて顧客端末に追加のリモートアクセスクライアントとSCKitを展開する活動を確認したと報告している。記事は攻撃の構成要素、永続化、技術者のブラウザー認証情報を狙う機能を説明し、調査用のMicrosoft Defender XDRハンティングクエリと緩和手順を提示する。

## 裏取り・注意点

- 記事はMicrosoft Threat Intelligenceによる観測と分析を報告する一次資料であり、独立した実機検証の報告ではない。記事によれば、ConnectWiseのクラウドホスト環境への侵入経路は調査中。サーバー側拡張機能への経路と、顧客端末から接続技術者へ広がる経路は別の攻撃面として説明されている。

## 出典

- Microsoft Security Blog, “SCKit abuses ScreenConnect to deploy remote access and target technician sessions” (2026-11-13): https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/

## 変更履歴

- 2026-11-16: 初回登録
