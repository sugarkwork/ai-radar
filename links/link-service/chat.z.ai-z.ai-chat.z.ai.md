---
type: "link"
name: "Z.ai (chat.z.ai)"
genre: "link-service"
url: "https://chat.z.ai/"
author: "Z.ai / Zhipu AI"
pricing: "freemium"
pricing_detail: "チャット UI はゲストセッションで利用開始でき、UI 自体の有料プランは公開料金表に見当たらない。API は従量課金（per 1M tokens, USD）: GLM-5.3 入力 $1.4 / 出力 $4.4、GLM-5.3-Flash 入力 $0.15 / 出力 $0.50、GLM-4.7-Flash・GLM-4.5-Flash は無料。Coding Plan は $18/月〜（Lite/Pro/Max、5時間・週次のクレジット制）。"
signup_required: false
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/KBlueleaf/status/2116459910347313274"]
flags: []
risk_notes: "chat.z.ai 自体はチャット UI で、UI から API キーは発行できない（enable_api_key=false）。エージェントから使う場合は別ドメインの api.z.ai（OpenAI 互換）のキーが必要で、対象 URL と API のホストが異なる。料金・モデル名は流動的（GLM-5.3 系は 2026-11 時点、価格は Limited-time 表記あり）。投稿本文（Tokenomos / vLLM）は本対象と無関係。"
fetched_at: "2026-11-06T21:06:07Z"
source_post: "https://x.com/KBlueleaf/status/2116459910347313274"
---

# Z.ai (chat.z.ai) — GLM-5.3 系チャットと OpenAI 互換 API

## 目的

- Z.ai（Zhipu AI）のチャット/エージェント画面。GLM-5.3 系をブラウザで試し、同じモデルを API 経由でエージェントから呼ぶための入口。

## 何ができるか

- ブラウザ: chat.z.ai で GLM-5.3 / GLM-5.2 / GLM-5.3-Flash と会話。コード生成、長めのタスク、Web 検索、スライド/ポスター作成などの内蔵ツールを UI から使える。
- API: https://api.z.ai/api/paas/v4 が OpenAI 互換（POST /chat/completions、model="glm-5.3" 等）。OpenAI SDK の base_url を差し替え、Bearer に API キーを渡すだけで呼べる。
- CLI/エージェント: GLM Coding Plan のキーで Claude Code / Codex / OpenCode / Cline / ZCode など 20+ ツールのバックエンドとして利用できる。
- 制約: chat.z.ai 自体は API キーを発行しない（/api/config の enable_api_key=false）。AI に使わせる場合は api.z.ai 側のキーを使う。UI 内の MCP ツール（Web 検索、PPT 作成など）は UI 専用で、外部から MCP として叩く公開エンドポイントではない。

## 料金

- チャット UI: ゲストセッションで利用開始可。UI 用の有料プランは公開料金表には見当たらない（公開されているのは API の料金）。
- API 従量（per 1M tokens, USD）: GLM-5.3 入力 $1.4 / キャッシュ入力 $0.26 / 出力 $4.4、GLM-5.3-Flash $0.15 / $0.03 / $0.50、GLM-5.3-FlashX $0.37 / $0.075 / $1.25。
- 無料: GLM-4.7-Flash と GLM-4.5-Flash は入出力とも $0。Web Search は $0.01/回。
- Coding Plan: $18/月〜（Lite 2,000 クレジット/5時間・10,000/週、Pro 12,000/60,000、Max 28,000/140,000）。

## 登録の要否

- チャット UI: 必須ではない（/api/v1/auths/ が role=guest のセッションを返す）。
- API / Coding Plan: アカウント登録と API キー発行が必要（https://z.ai/manage-apikey/apikey-list でキーを発行し、課金は z.ai/manage-apikey/billing）。

## 変更履歴

- 2026-11-06: 初回登録
