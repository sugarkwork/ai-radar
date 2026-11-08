---
name: "Jev（TypeSafe AI）"
genre: "link-service"
url: "https://typesafe.ai/"
author: "TypeSafe AI"
pricing: "paid"
pricing_detail: "$42 / 10億入力トークン（$0.042 / 100万トークン）、出力トークンは無料。無料枠・トライアルの公式記載はなし。Enterprise は個別見積り（上限引き上げ・ZDR・SOC2 Type II）。"
signup_required: true
flags: ["unverified"]
risk_notes: "投稿が掲げる数値（10,000タスクを20秒、9,214件をOpusに渡さない、8レーンで衝突0、41,096行、12.7x fewer Opus calls、Jev費用$0.38）は投稿本文と添付動画の中だけの主張で、一次情報の裏付けがない。添付動画は実アプリの画面ではなく演出されたモックで、同じ動画内でも Jev 費用が $0.25 から $0.38 へ変化し、41,096 行は画面に現れない。Jev 自体（TypeSafe AI の System One モデル、$42/10億入力トークン、HTTP API/SDK/agent skill）は公式サイトとドキュメントで確認できるが、公式は「コーディングエージェントの LLM を置き換えるものではない」と明記しており、投稿の8レーン並列構成の再現手順は公開されていない。無料枠の有無、コンソールの課金開始条件は未確認。"
type: "link"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/Y0urDumble/status/2108977887126630649"]
fetched_at: "2026-11-08T04:07:21+00:00"
---

# Jev — 型付きの意思決定だけを返す TypeSafe の System One モデル

## 目的

- 高性能LLMにバックログ全体を投げる前に、「些細・定型・難しい」の判断だけを安く速く済ませ、難しい案件だけをLLMに渡すための判断レイヤー。
- LLMにJSONを出力させてパースする代わりに、型付きの選択・スコア・真偽値・信頼度を受け取り、閾値判定や分岐はコード側で持つ。

## 何ができるか

- 1リクエストで state（テキスト／JSON／画像）に対する複数の質問を並列評価し、質問ごとに1つの回答を返す。
- 質問型は Choice（選択肢から1つ、各選択肢の確率と confidence）、Score（ルーブリック上の段階評価）、Noul（真偽の確率 0〜1）、Box（画像内の矩形、1.14 のみ）。
- 用途はトリアージ・ルーティング、分類、採点、LLM出力や引用の検証、ツール実行前のガードレール。
- 呼び出し方は HTTP API（POST https://api.typesafe.ai/v1/systemone）、公式 Python SDK（pip install typesafe-sdk）、公式 JavaScript/TypeScript SDK、Claude Code などのエージェント向け skills（npx skills add typesafe-ai/skills --skill typesafe-ai）。MCP サーバーの提供は公式ドキュメントに見当たらない（未確認）。
- 入力はテキストと PNG/JPEG 画像。音声・動画は非対応。既定のコンテキストは 1リクエスト 64k・1質問 32k で、Long context ヘッダ指定時に 262k。

## 料金

- $42 / 10億入力トークン（$0.042 / 100万トークン）。出力トークンは無料。
- jev-1.14.0 と jev-1.13.0 は同一料金で、Long context も同じ単価。
- 無料枠・トライアルの公式記載はなし。コンソールに Playground はあるが、その課金条件は未確認。
- 上限引き上げ・ゼロ保持（ZDR）・SOC2 Type II が必要な場合は Enterprise として個別相談。

## 登録の要否

- 必要。API キーは TypeSafe コンソール（console.typesafe.ai/keys）でアカウント作成後に発行する。
- ブラウザの Playground でも試せるが、いずれもコンソールへのログインが前提。

## 変更履歴

- 2026-11-08: 初回登録
