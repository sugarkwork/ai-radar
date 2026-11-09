---
name: "Cold Email (marketingskills)"
genre: "link-asset"
url: "https://github.com/coreyhaines31/marketingskills/tree/main/skills/cold-email"
author: "coreyhaines31"
pricing: "free"
pricing_detail: "無料。MIT License（GitHub APIのSPDXで確認）。リポジトリはVerified Partnersのスポンサーで運営されるとREADMEに記載。紹介先の配信・検証・CRMツールの利用料は別途。"
signup_required: false
sources: ["https://github.com/coreyhaines31/marketingskills/tree/main/skills/cold-email", "https://api.github.com/repos/coreyhaines31/marketingskills", "https://raw.githubusercontent.com/coreyhaines31/marketingskills/main/skills/cold-email/SKILL.md", "https://github.com/coreyhaines31/marketingskills#readme", "https://raw.githubusercontent.com/coreyhaines31/marketingskills/main/LICENSE", "https://x.com/Y0urDumble/status/2114428470168334365"]
first_seen: "2026-10-25"
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "投稿は『全自動のコールドメール』と宣伝するが、SKILL.mdは文面・フォロー・配信ドメイン設定・返信分類のガイドで、送信基盤やリード抽出は含まず、Instantly等の外部ツールと別Skill（prospecting）に依存する。投稿の48 leads / 12 pitches / 1 signed / $3,000–6,000は未検証。LinkedIn自動化は各サービスの規約リスクがあるとSKILL.md自身が注記している。当方で導入・送信試験はしていない。"
fetched_at: "2026-11-09T18:52:00Z"
type: "link"
---

# Cold Email — B2Bコールドメールの文面・配信・返信対応をまとめたClaude Skill

## 目的

- コールドメールの件名・本文・フォロー・配信ドメイン設定・LinkedIn/電話を含むマルチチャネル手順・返信分類を1つのSkillにまとめたもの。
- 投稿の『広告代理店が全自動で回る』という文脈ではなく、アウトバウンドの文面と運用の指示書。リードリストの作成は別Skill（prospecting）に分離されている。

## 何ができるか

- SKILL.md（12,571 bytes、v2.2.1）は、製品マーケティング文脈の確認、4レベルのパーソナライズ、2〜4語の件名、3〜5通のフォロー、SPF/DKIM/DMARCと3〜4週間のメールボックスウォームアップ、バウンス2%未満、開封/クリックトラッキング停止、返信時に全チャネルを止める運用を指示する。
- references/ に deliverability、personalization、subject-lines、follow-up-sequences、frameworks、multichannel-cadence、reply-handling、benchmarks などを同梱し、evals/ も持つ。
- 送信・検証・CRMは同梱せず、Instantly / lemlist / Outreach / HeyReach / Truelist / Hunter / HubSpot / Attio / Close / Calendly などの外部ツール連携ガイドを参照する。LinkedIn自動化には各サービスの規約リスクがあると明記。

## 料金

- 無料。MIT License（GitHub APIのSPDXでMITを確認、LICENSE取得は200）。
- リポジトリはVerified Partnersのスポンサーで運営されるとREADMEに記載。紹介先ツールの利用料は別途かかる。

## 登録の要否

- Skillの取得・利用に登録は不要。`npx skills add coreyhaines31/marketingskills` またはClaude Codeのプラグイン機構で導入する。
- 実際に送信する場合は、メール配信サービス・送信ドメイン・認証情報が別途必要。投稿の実績数値は未検証。

## 変更履歴

- 2026-11-09: 初回登録
