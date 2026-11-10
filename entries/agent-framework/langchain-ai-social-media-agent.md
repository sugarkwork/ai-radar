---
type: "repo"
name: "Social Media Agent（LangChain）"
genre: "agent-framework"
url: "https://github.com/langchain-ai/social-media-agent"
repo: "langchain-ai/social-media-agent"
license: "MIT"
stars: 3006
language: "TypeScript"
created: "2024-11-21"
updated: "2026-11-09"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① Supabase は README と .env.full.example 上「画像の保存」用で、投稿本文の保存先ではない。使用済みリンクは LangGraph の BaseStore（namespace saved_data/latent_space）に置かれる。② README に ToS・レート制限の記述は無い。実効上限は X API / LinkedIn API の契約プラン側で決まり、Arcade 経由でも同一アカウントの枠を消費する。③ 設計上そのままでは自動投稿にならない。interrupt で人間の承認が入るため、cron を回しても承認待ちで滞留する。④ Arcade だけでは X のメディアアップロードができず、X 開発者アカウントが別途必要。⑤ LinkedIn 企業ページ投稿は Advertising API の有効化＋ページ側ロール＋ページによるアプリ認証＋審査フォーム提出が前提で、審査待ちが出る。⑥ プロンプト既定値は LangChain 自身の AI 系ツイートを few-shot にしているため、他社ブランドでは BUSINESS_CONTEXT / TWEET_EXAMPLES の差し替えが実質必須。⑦ package.json の name/description が starter template のまま（example-graph / \"A starter template for creating a LangGraph workflow\"）で、README との整備差がある。⑧ langgraph.json に14グラフ登録されており機能は多いが、読むべきコード量も多い。⑨ `langgraph:in_mem:up` は毎回 @langchain/langgraph-cli の最新を npx で取得するため初回に対話承諾が必要で、CLI バージョンが固定されない。⑩ フル構成の外部依存は Anthropic / LangSmith / FireCrawl / Arcade / X / LinkedIn / Supabase ＋任意で Vertex AI / GitHub / Slack と多く、キー管理の方が本体より重い。"
forks: 549
open_issues: 21
commits_30d: 32
size_kb: 6323
archived: false
commits_90d: 96
commit_cadence: "daily"
fetched_at: "2026-11-09T21:33:32Z"
last_release: ""
last_release_at: ""
---

# Social Media Agent — URL 1本から X / LinkedIn 投稿を作り、人間の承認を挟んで投稿する LangGraph アプリ

## 出来ること

- `generate_post` グラフに URL を渡すと、FireCrawl で本文を取得 → 自社コンテキストとの関連性を判定 → X 用と LinkedIn 用の投稿文を別々に生成する
- 生成後にグラフが interrupt し、人間が本文を編集・承認・却下してから投稿する（HITL）。承認 UI は Agent Inbox（dev.agentinbox.ai にローカルグラフを登録するか、ローカル起動）か LangSmith
- 投稿処理は `upload_post` に分離され、X と LinkedIn を個別に扱える。企業ページ名義の投稿にも対応（`POST_TO_LINKEDIN_ORGANIZATION`）
- Slack チャンネルに流したリンクを `ingest_data` が拾い、`yarn cron:create` で作る日次 cron がまとめて投稿候補にする（LangChain 社内の運用そのもの）
- GitHub / X / YouTube の URL は専用パーサで本文以外のメタ情報も取る（basic 構成では無効）
- 画像の選択と Supabase の `images` バケットへのアップロード、投稿への添付
- 使用済みリンクを LangGraph の BaseStore に記録し、同じ URL の二重投稿を防ぐ（`SKIP_USED_URLS_CHECK` で無効化可）
- `generate_thread`（スレッド化）、`repurposer`（焼き直し）、`generate_report`（マーケレポート）、`verify_tweet` / `verify_reddit_post`（投稿前検証）など、langgraph.json には14グラフが登録されている

## 目的・背景

- LangChain 社が自社マーケティングで実際に回しているエージェントをそのまま公開したもの。ブログやリポジトリの URL を渡すと、同社のトーンで X と LinkedIn の投稿を作るのが一次目的
- 設計の中心は「勝手に投稿しない」こと。認証（OAuth）と投稿内容の確認の両方を interrupt で人間に返すので、エージェントは下書きを作るところで止まる
- プロンプトは `BUSINESS_CONTEXT` / `TWEET_EXAMPLES` / `POST_STRUCTURE_INSTRUCTIONS` / `POST_CONTENT_RULES` の4点に分かれ、few-shot のツイート例を差し替えるのがスタイル調整の主手段。既定値は AI 系ツイートなので他業種では書き換えが前提
- 実体は LangGraph のサーバアプリで、pip の CLI ツールではない。`langgraph dev` でグラフを立て、スクリプトと Agent Inbox がその API を叩く構成

## 依存関係

- Node.js 22（langgraph.json の node_version）、yarn 1.22.22、TypeScript
- LLM: Anthropic API（既定）。YouTube 解析まで有効にするなら Google Vertex AI の資格情報も
- 実行基盤: LangGraph CLI（`npx @langchain/langgraph-cli`）と LangSmith API キー（サーバ起動に必須、無料枠で足りる）
- スクレイピング: FireCrawl
- 認証: Arcade（`ARCADE_API_KEY` + `TWITTER_USER_ID` / `LINKEDIN_USER_ID`）か、自前の X / LinkedIn 開発者アプリ（`TWITTER_CLIENT_ID` 等、`LINKEDIN_CLIENT_ID` 等）の二択。README は併用不可と明記
- 画像: Supabase（`images` バケットを public、アップロード上限5MB以上に設定）。basic 構成では不要
- 任意: GitHub の fine-grained token、Slack アプリ（`SLACK_BOT_TOKEN`）、`SESSION_SECRET`（`openssl rand -hex 64`）
- `yarn langgraph:up`（watch 付きの本番寄り起動）は Docker が要る。手軽な方は `langgraph:in_mem:up`

## 実行条件

- X へのメディア（画像）アップロードだけは Arcade では賄えず、X 開発者アカウントの作成が別途必須。テキストのみなら Arcade だけで足りる
- LinkedIn の企業ページ投稿は `Advertising API` 製品の有効化、ページ側の ADMINISTRATOR 等のロール、ページによるアプリ認証、審査フォーム提出が前提。個人投稿でも `Share on LinkedIn` 製品の有効化が要る
- OAuth のコールバックは `http://localhost:3000/auth/twitter/callback` と `/auth/linkedin/callback` 固定。`yarn start:auth` でローカルに認証サーバを立て、返ってきた token を .env に貼る
- グラフサーバは 54367 番。Agent Inbox には Graph ID `generate_post` と API URL `http://localhost:54367` を登録する
- README には利用規約やレート制限の記述がない。実効上限は X API / LinkedIn API の契約プラン側で決まり、Arcade 経由でも同じアカウントの枠を消費する
- フル構成の外部サービスは8前後になり、キー管理の手間が本体より重い

## 最短手順

```bash
git clone https://github.com/langchain-ai/social-media-agent.git
cd social-media-agent
yarn install
cp .env.quickstart.example .env      # フル構成なら .env.full.example
# ANTHROPIC_API_KEY / LANGCHAIN_API_KEY / FIRECRAWL_API_KEY / ARCADE_API_KEY /
# TWITTER_USER_ID / LINKEDIN_USER_ID を記入
yarn langgraph:in_mem:up             # 実体は npx @langchain/langgraph-cli dev --port 54367
```

- 起動後、別ターミナルで `yarn generate_post` → LangSmith か Agent Inbox で interrupt を開き、編集して承認
- 自前アプリで認証する場合: `yarn start:auth` → http://localhost:3000 でログイン → 端末に出る JSON の token を .env に反映
- 定期運用: Slack 連携後に `scripts/crons/create-cron.ts` の `slackChannelId` を書き換え、`yarn cron:create`（`yarn cron:list` / `yarn cron:delete` で管理）
- 状態確認: `yarn get:used_links`（使用済み・承認待ちリンク）、`yarn get:scheduled_runs`（予約済み実行）

## 変更履歴

- 2026-11-07: 初回登録
