---
repo: "coreyhaines31/marketingskills"
name: "Marketing Skills (cold-email)"
genre: "prompt-design"
url: "https://github.com/coreyhaines31/marketingskills"
license: "MIT"
stars: 59400
language: "JavaScript"
created: "2026-01-15"
updated: "2026-11-09"
forks: 8675
open_issues: 83
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 7013
archived: false
last_release: "v2.14.8"
last_release_at: "2026-11-09"
author: "Corey Haines"
flags: ["unverified"]
risk_notes: "投稿の『48 leads / 12 pitches / 1 signed』『Claudeが全部やる』『15秒スポット $3,000–6,000』は投稿者の宣伝で、リポジトリにも一次情報にも裏付けがない（未確認）。確認できたのは、cold-email がコールドメールの文面・件名・フォロー・配信設計・返信処理の指示書であり、リード探索（同リポジトリの prospecting、または投稿がリンクする別リポジトリの lead-research-assistant）、送信、契約、3D動画、請求を実行するコードを含まないこと。投稿の『storyboard』『AIスタートアップの発見』はこのスキルの機能ではなく、SKILL.md に storyboard の記述はない。ベンチマークはベンダー由来で、スキルには測定済みの返信率・受注実績がない。効果は利用者のリスト品質・製品・ドメイン評判に依存する。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2114428470168334365"]
fetched_at: "2026-11-09T21:41:42Z"
---

# Marketing Skills：AIエージェント向けマーケティングスキル集（cold-email）

## 出来ること

- cold-email スキルは、B2Bコールドメールの本文・件名・3〜5通のフォローアップ・返信の分類と一次対応・マルチチャネル連鎖の書き方をエージェントに与える。送信そのものは行わず、送信ツールの設計と文面を指示する。
- 配信設計も対象：セカンダリドメインの使用、SPF/DKIM/DMARC、メールボックスの3〜4週間ウォームアップ、送信直前のリスト検証、バウンス2%未満、開封・クリックトラッキングOFF、オプトアウト文と郵送先住所の記載。
- references/ に10本の資料（benchmarks、deliverability、personalization、subject-lines、follow-up-sequences、frameworks、linkedin-outreach、multichannel-cadence、outbound-plays、reply-handling）を同梱する。
- リポジトリ全体は53スキル（CRO、コピーライティング、SEO、広告、分析など）と、任意で使う66個のゼロ依存Node CLIツール（tools/clis）を含む。
- cold-email はリードリストの作成を含まない。上流は prospecting、ライフサイクルメールは emails、電話台本は sales-enablement に分かれている。

## 目的・背景

- Corey Haines（Conversion Factory / Swipe Files）が作る、AIコーディングエージェント向けのマーケティング技能集。MITライセンスで無償公開され、PRとパートナー企業の支援で運営されている。
- 設計の中心は Agent Skills 仕様に沿った markdown スキルで、product-marketing スキルが作る .agents/product-marketing.md を全スキルが最初に参照し、製品・顧客・ポジショニングの文脈を共有する。
- 投稿は「Claudeが広告代理店を1人で回す」スタックの一部としてこの cold-email を挙げるが、それは投稿者の宣伝であり、リポジトリ側の主張ではない。

## 依存関係

- Agent Skills 仕様に対応するエージェント（Claude Code、OpenAI Codex、Cursor、Windsurf など）。インストールは npx skills（Node.js/npx）か、Claude Code / Codex のプラグイン機構を使う。
- 任意：product-marketing スキルが生成する .agents/product-marketing.md。無くても動作し、不足情報はエージェントが質問する。
- 送信・検証・CRM・予約は同梱されず、Instantly、lemlist、Outreach、Truelist、Hunter、HubSpot、Attio、Close、Calendly などの外部SaaS/APIを別途接続する。
- tools/clis のCLIツールを使う場合のみ Node 18+。スキル本体は markdown のみでビルド不要。

## 実行条件

- エージェントが SKILL.md を読めること（.claude/skills/ または .agents/skills/ に配置）。
- 実送信には、認証済みの送信用セカンダリドメイン（SPF/DKIM/DMARC）とウォームアップ済みメールボックス、ESP/CRMアカウントが必要。
- 各国・地域の迷惑メール規制（オプトアウトと郵送先住所の記載）を満たす責任は利用者側にある。
- このスキルは文面と手順の提供のみで、送信・契約・請求・動画制作は行わない。

## 最短手順

- Claude Code に入れる：npx skills add coreyhaines31/marketingskills --skill cold-email -a claude-code
- Claude Code のプラグイン経由なら：/plugin marketplace add coreyhaines31/marketingskills → /plugin install marketing-skills
- 先に product-marketing スキルで .agents/product-marketing.md を作り、製品・顧客・ポジショニングを渡す。
- エージェントに「cold-email スキルで、〜向けの1通目と3通のフォローを書いて」と依頼するか、/cold-email を実行する。
- 送信前に Instantly などのESPを接続し、返信webhookで全チャネル停止と返信トリアージを設定する。

## 変更履歴

- 2026-11-09: 初回登録
