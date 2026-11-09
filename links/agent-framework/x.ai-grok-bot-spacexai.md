---
type: "link"
name: "Grok Bot（SpaceXAI）"
genre: "agent-framework"
url: "https://x.ai/bot"
author: "SpaceXAI（旧 xAI）/ Anysphere"
pricing: "paid"
pricing_detail: "Premium $30/月、Super $100/月、Ultra $200/月（月払い、週次利用枠込み・超過はトークン課金）。Teams / Enterprise は問い合わせ。2026-11 時点の公式ページ記載。"
signup_required: true
added: "2026-11-09"
fetched_at: "2026-11-09T10:35:09Z"
flags: ["unverified"]
risk_notes: "確認できたこと: Grok Bot は SpaceXAI（2026-07 に xAI から改称、2026-10 に SpaceX Super Intelligence / SpaceXSI へ再改称。2026-08-14 に Cursor の Anysphere 買収完了）の製品で、公式ページ https://x.ai/bot に料金（Premium $30 / Super $100 / Ultra $200 月額、週次利用枠込み、超過はトークン課金）、Teams/Enterprise の提供、Cursor アカウントでの SSO、常駐クラウドPCの仕様（ユーザー単位で共有、Bot 単位ではない）が記載されている。公式ドキュメント docs.x.ai/grok-bot も実在（307リダイレクトの先で本文取得）。未確認・誤り: 投稿の『80+ GrokBot agents with /loop and /goal』『85% of engineers run 10+ agents』『Chief of Staff agent』という引用は、本人の講演映像・書き起こし・公式ページのいずれにも確認できない。講演（添付動画 55:47、同一内容の公開版 38:02）は信頼構築と pstack の話で、GrokBot のチーム構築チュートリアルではない。/loop と /goal は Cursor Agent のスラッシュコマンドで、Grok Bot 側の相当機能は routines（スケジュール実行）。Grok Bot に公開の Bot 操作 API があるかはドキュメント上確認できず、記載があるのは MCP / 任意APIへの接続（内向き）のみ。投稿の引用元X記事2件は非ログインでログイン画面へリダイレクトされ本文を読めないことを実際に確認済み。"
sources: ["https://x.ai/bot", "https://x.ai/bot/use-cases", "https://x.ai/bot/marketplace", "https://docs.x.ai/grok-bot", "https://x.ai/news/introducing-grok-bot", "https://cursor.com/docs/agent/overview", "https://en.wikipedia.org/wiki/xAI_(company)", "https://x.com/xsmryze/status/2109764661356671245"]
source_post: "https://x.com/xsmryze/status/2109764661356671245"
first_seen: "2026-10-12"
---

# Grok Bot — 常駐クラウドPCを持つ「AI同僚」を複数並列で動かす SpaceXAI の製品

## 目的

- チャット相手ではなく、仕事を最後まで進める『AIの同僚』を複数持つための製品。各 Bot は名前・役割・記憶を持ち、ユーザーごとの常駐クラウドコンピュータ上でアプリやWebサイトにログインして作業する。
- 人が介在するのは承認のときだけ、という設計。Bot 同士で作業を引き継ぎ、判断が必要な場面で戻ってくる。

## 何ができるか

- Bot の並列実行: プロジェクト用・アウトバウンド用・社内システム用など役割ごとに Bot を作り、同時に走らせる。ユーザーがノートPCを閉じても継続する。
- 常駐クラウドPC: Bot は1台のマシン（ファイル、ブラウザ、ログイン）を共有する。分離は Bot 単位ではなくユーザー単位。API のないサイトでも人間と同じ操作で使える。
- routines: タスクを定期実行として登録できる（毎朝のブリーフィング、毎週の集計など）。
- 接続: Slack、Notion、Google Drive/Calendar/Gmail、Granola、Teams などのコネクタと、MCP / 任意のAPI。
- テンプレート: 公式の use cases と marketplace に、Chief of Staff、Sales Outbound、Bug Reproduction、Product Performance、SEO/AEO Auditor、Talent Scout などの Bot が公開され、自分のアカウントに追加できる。
- 統制: 機密操作を Auto Review に通す、Enterprise では DLP・証明書・プロキシ・ネットワーク制御を起動時に設定する、学習オプトアウト、保存時・通信時の暗号化。

## 料金

- Premium $30/月、Super $100/月（Premium の3.5倍の利用枠、ピーク時の優先モデルアクセス）、Ultra $200/月（Premium の12倍、新製品・新モデルへの最速アクセス）。いずれも月払い。
- 各プランに週次の Grok Bot 利用枠が含まれ、超過分はトークン費用に基づいて課金される。
- Teams / Enterprise は問い合わせ。Enterprise は既に Cursor の席位を持たない組織メンバーにも展開できるとされる。
- 注意: 2026-08-11 のローンチ時は SuperGrok / SuperGrok Plus / SuperGrok Heavy、Cursor Pro / Pro+ / Ultra、Cursor Teams Standard / Premium が対象で、Enterprise は waitlist だった（公式ローンチ記事）。現在の公式ページは Premium / Super / Ultra の3階層を前面に出しており、既存 Cursor プランの扱いはページ上に明記がない（未確認）。

## 登録の要否

- 必要。Cursor アカウントでサインインし、いずれかのプランを契約する。Grok Bot は Cursor の SSO・認証・privacy mode を共用する。
- アカウントなしでできるのは use cases / marketplace の閲覧と、各 Bot の説明確認まで。実行には契約が必要。
- 企業利用は営業経由。管理者がネットワーク・DLP・監査を設定する前提。

## 変更履歴

- 2026-11-09: 初回登録
