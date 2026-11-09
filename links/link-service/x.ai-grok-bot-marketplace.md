---
name: "Grok Bot Marketplace"
genre: "link-service"
url: "https://x.ai/bot/marketplace"
pricing: "paid"
pricing_detail: "$30/月のPremium以上が必要（Super $100/月、Ultra $200/月）。Freeと$8のPlusにはGrok Botが含まれない。マーケットプレイスのボット追加自体は無料。"
signup_required: true
author: "xAI"
source_post: "https://x.com/N01ennn/status/2114436702551072850"
flags: ["unverified"]
risk_notes: "「146」という総数は公式未確認（マーケットプレイスに総数の表示はなく、複数の第三者投稿がマーケット90＋ユースケース56と主張）。ボットの追加は無料だが、Grok Botの利用自体はPremium $30/月以上が必要で「完全無料」ではない。8体は第三者の出品で、品質・サポート・更新は作者依存（公式製ではない）。全ボットが1つのクラウドPCとファイル・ブラウザ・ログインを共有し、分離はユーザー単位のため、権限の広いアカウント連携は注意。投稿が引用する記事はログイン壁で本文未確認。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/N01ennn/status/2114436702551072850"]
fetched_at: "2026-11-09T20:25:41Z"
---

# Grok Bot Marketplace

## 目的

- xAI（Grok）の公式ボットマーケットプレイス。特定の仕事向けに設定済みの「Grok Bot」を探し、自分のアカウントに追加して業務を任せるためのリンク。
- 2026年10月の投稿が「SpaceXAIが146人の無料従業員をくれた」として8体のボット役割分担を紹介して話題になったが、その実体はこのマーケットに第三者が出品したボット群。公式ページに総数の表示はなく、146という数字（マーケット90＋ユースケース56）は投稿側の主張で未確認。

## 何ができるか

- Grok Botはクラウド上の実コンピュータを操作するエージェントで、公式説明は「It's an agent with access to a real computer in the cloud, so it can do all the things you can.」。ツールへのサインイン、ファイル・ブラウザ・ターミナルの操作まで行い、成果物を返す。
- マーケットのボットは用途別に設定済み。投稿が組んだ8体も実在し、作者は公式ページに明記されている: Projects Manager（Eric Zakariasson、仕事の割り振り）、Researchy（Farzad、Web検索つき調査・ファクトチェック）、PM bot（Ulysses Ng、何を出すかの線引き）、figma bro（John Bai、Figmaフレームをビルド仕様に変換）、Lingxi's Engineer Bot（Lingxi Li、リポジトリへの実装をクラウドエージェントで監督）、QA bot（Ulysses Ng、デプロイ後の受け入れチェック）、Stills & Clips Desk（Matt Palmer、静止画・短尺クリップ・キャプション生成）、Outbound Prospecting（Krista Letz、見込み客の調査と初回メッセージ下書き）。
- 複数のボットを同じスレッドに入れると作業を互いに引き継ぐ（「Put a few Bots in the same thread and they pass work between themselves.」）。一度作業を見せるとroutineとして保存し、次回から自動で回せる。
- MCP/API連携に対応し（「Grok Bot supports custom tooling, so it can interact with any MCP or API.」）、Slack・Notion・Drive・カレンダーなど既存ツールを繋いで使う。追加はマーケットの「Add」から行う。

## 料金

- ボットをマーケットから追加する操作自体は無料だが、Grok Botの利用にはXの有料サブスクリプションが必要（pricing: paid）。
- The X Subscriptionの月額は Free $0（Grok Bot非包含）、Plus $8（非包含）、Premium $30、Super $100、Ultra $200。公式FAQは「Grok Bot is included on Premium, Super, and Ultra. Plus does not include Grok Bot.」と明記している。
- ボットの利用量は席ごとの週次利用プールを共有し、別枠の追加プールではない（「Bot usage draws from that seat's shared weekly usage pool, not a separate additive pool.」）。超過分はトークンコストに応じた追加課金。

## 登録の要否

- Xアカウントでのサインアップと、Premium以上の有料プランへの加入が必要（signup_required: true）。無料プランではボットを追加しても動かせない。
- ボットは第三者の出品で、品質・サポート・更新は作者に依存する。導入前に個別ページで作者と説明を確認する。
- 全ボットが1つのクラウドPC（ファイル・ブラウザ・ログイン）を共有し、分離はユーザー単位。認証情報も共有されるため、権限の広いアカウントを繋ぐ場合は範囲を絞る。

## 変更履歴

- 2026-11-09: 初回登録
