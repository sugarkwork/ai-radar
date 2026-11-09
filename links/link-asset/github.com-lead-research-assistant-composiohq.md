---
name: "Lead Research Assistant (ComposioHQ)"
genre: "link-asset"
url: "https://github.com/ComposioHQ/awesome-claude-skills/tree/master/lead-research-assistant"
author: "ComposioHQ"
pricing: "free"
pricing_detail: "無料。公開GitHubリポジトリで、SKILL.mdの取得・利用に課金もアカウントも不要。ただしGitHub APIのlicenseはnull、ルートと当該フォルダのLICENSEは404で、READMEのApache-2.0記載は個別skillの許諾を保証しない（2026-11-09確認）。ComposioのMCP Gatewayは別サービスの課金対象。"
signup_required: false
sources: ["https://github.com/ComposioHQ/awesome-claude-skills/tree/master/lead-research-assistant", "https://api.github.com/repos/ComposioHQ/awesome-claude-skills/contents/lead-research-assistant", "https://raw.githubusercontent.com/ComposioHQ/awesome-claude-skills/master/lead-research-assistant/SKILL.md", "https://github.com/ComposioHQ/awesome-claude-skills#readme", "https://x.com/Y0urDumble/status/2114428470168334365"]
first_seen: "2026-10-25"
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "投稿は『AIスタートアップを今月ローンチ予定から自動抽出』『48 leads / 12 pitches / 1 signed / $3,000–6,000 / 0 employees』と宣伝するが、SKILL.mdは製品理解→ICP定義→企業検索→1〜10の適合スコア→接触案の出力を指示する文面で、検索API・CRM連携・送信コードは同梱しない。数値と全自動性は投稿の主張で未検証。リポジトリAPIのlicenseはnullでLICENSEファイルは404、READMEのApache-2.0記載と個別skillの条件は一致しないため、再配布・商用利用の前に原文を確認する。当方で導入・実行はしていない。"
fetched_at: "2026-11-09T18:52:00Z"
type: "link"
---

# Lead Research Assistant — 見込み企業の調査と接触案を作るClaude Skill

## 目的

- 自社製品・ICPを入力に、対象企業の候補、適合スコア、意思決定者の役割、接触時の切り口を整理するSkill。営業・BD・マーケティングの下調べを短縮する用途。
- 投稿の『Claudeが一人で広告代理店を回す』という文脈ではなく、リード調査という単一工程の指示書。案件獲得や送信までを自動化するものではない。

## 何ができるか

- SKILL.md（6,587 bytes、2026-11-09取得）は、製品理解→ICP定義→企業検索→1〜10の適合スコア→企業名/サイト/スコア/意思決定者/接触戦略/会話の切り口/LinkedIn URLという出力形式、の順で調査を指示する。
- コード・スクリプト・referencesは同梱せず、ファイルはSKILL.md 1件のみ。企業検索やWeb閲覧は、Skillを読み込むエージェント側の検索ツールに依存する。
- Claude.aiのスキル取り込み、Claude Codeの ~/.config/claude-code/skills/ への配置、Claude Skills APIでの読み込みがREADMEに記載されている。

## 料金

- 無料。公開GitHubリポジトリで、閲覧・取得・利用に料金はかからない。
- リポジトリREADMEはApache-2.0と記載するが、GitHub APIのlicenseはnull（LICENSEファイルなし、ルートとlead-research-assistant配下とも404）。個別skillの再利用条件は未確認。
- ComposioのMCP Gateway（1,000以上のアプリ連携）は別サービスの課金対象で、このSkill自体はComposioアカウントを要求しない。

## 登録の要否

- 不要。GitHubからフォルダを取得し、利用するエージェントのskillsディレクトリに置く。APIキーも不要（検索機能はホスト側のツールによる）。
- 投稿の48 leads / 12 pitches / 1 signed / $3,000–6,000 / 0 employeesは投稿の主張で、このSkill単体では検証できない。

## 変更履歴

- 2026-11-09: 初回登録
