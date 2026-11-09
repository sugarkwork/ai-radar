---
name: "Claude Code ダイナミックワークフロー（Dynamic workflows）"
genre: "coding-agent"
url: "https://code.claude.com/docs/en/workflows"
author: "Anthropic"
flags: ["unverified"]
risk_notes: "投稿の主張のうち、ワークフロー機能そのもの（JSスクリプトで多数のサブエージェントを編成、`claude --effort ultracode`、`/deep-research`、`/workflows`、ステージごとのモデル指定、isolated copy での並列編集）は一次情報で確認できる。一方、(1)「Haiku 5.5 が全ファイルをスキャンし Sonnet 5.5 が修正する」という固定の役割分担はページに記載がなく、投稿者のレシピ。モデル名（Opus 5.5 / Sonnet 5.5 / Haiku 5.5）自体は Claude Code の model-config に存在するが、この分担は既定動作ではない。(2)「JEV がミリ秒でマイクロ分岐をルーティングする」は当該ページにも docs 索引にも一切登場せず、ワークフロー機能の一部ではない（JEV は外部解説では TypeSafe の意思決定モデルと説明される別製品で、Anthropic の機能ではない。TypeSafe 一次ページは JS 主体で本文確認できず、この帰属は第三者解説に基づく）。「Anthropic が共有した」という帰属と、JEV を機能の一部のように説明する点は誤り。(3) 動画のみで静止画像はなく、フレーム単位の照合はしていない。コスト面はページが「トークンが大幅に増える」「利用上限に早く達する」と明記しており、投稿の「Opus トークンを節約」は主観で、ページの警告とは方向が異なる。"
pricing: "paid"
pricing_detail: "Claude Code は Free プランでは利用不可。Pro $20/月（年払い $17/月、$200 一括）、Max $100/月、Ultra $200/月、Team 標準 $20/席/月（年払い、月払い $25）、Premium $100/席/月（月払い $125）、Enterprise は席課金＋API 従量。API 直接利用・Bedrock・Google Cloud Agent Platform・Microsoft Foundry ではトークン従量。"
signup_required: true
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/xsmryze/status/2113273069099688435"]
fetched_at: "2026-11-09T12:08:41Z"
---

# Claude Code のダイナミックワークフローで多数のサブエージェントを編成する

## 目的

- 1つの会話では捌ききれない規模の作業（コードベース全体のバグ掃討、500ファイルの移行、出典を突き合わせる調査）を、JavaScript のワークフロースクリプトに計画として持たせて実行するための Claude Code の機能。
- サブエージェントやスキルでは Claude がターンごとに次の手を決め、中間結果がコンテキストに溜まる。ワークフローではループ・分岐・中間結果をスクリプト側の変数が保持し、Claude のコンテキストには最終結果だけが残る。

## 何ができるか

- Claude がタスク用のワークフロースクリプトを書き、ランタイムがバックグラウンドで実行。セッションは応答可能なまま。1回の実行で数十〜数百エージェントを動かせる。
- 起動方法は3通り: プロンプトに `ultracode` を含める／`/effort ultracode` でセッション全体を自動ワークフロー化／`claude --effort ultracode` で最初から有効（effort は xhigh になる）。`--model opus` のようなモデル別名指定も CLI で可能。
- 組み込みの `/deep-research <質問>` がすぐ試せる例。Web 検索を複数角度に展開し、出典を取得・相互照合して引用付きレポートを返す（WebSearch ツールが必要）。
- `/workflows` で実行一覧・フェーズ別エージェント数・各エージェントのツール呼び出しと結果を確認。`p` で一時停止/再開、`x` で停止、`r` で再起動、`s` でスクリプトをコマンドとして保存。
- 保存したワークフローは `.claude/workflows/`（プロジェクト共有）または `~/.claude/workflows/`（個人）に置き `/名前` で再利用。`args` で入力を渡せる。プラグインに同梱して配布も可能。
- ステージごとにモデルを指定でき、指定がなければセッションのモデルが使われる。コスト抑制のため「強いモデルが不要なステージは小さめのモデルを」と案内されている。
- CLI・Desktop・IDE 拡張・`claude -p`（非対話）・Agent SDK で利用可能。`disableWorkflows` や `CLAUDE_CODE_DISABLE_WORKFLOWS=1` で無効化できる。
- AI からの呼び出し形式: CLI（`claude --effort ultracode`、`claude -p`）と Agent SDK の Workflow ツール。MCP サーバーではない。

## 料金

- 有料プラン（Pro / Max / Ultra / Team / Enterprise）、Anthropic API、Amazon Bedrock、Google Cloud Agent Platform、Microsoft Foundry で利用可能。Free プランでは Claude Code 自体が使えない。
- Pro $20/月（年払い $17/月、$200 一括）、Max $100/月、Ultra $200/月、Team 標準 $20/席/月（年払い）／$25（月払い）、Premium $100/席/月（年払い）／$125（月払い）。Enterprise は $20/席/月（年払い、20席〜）＋ API 従量。
- API 利用時はトークン従量。Enterprise の目安は開発者1人あたり実働日 約$13、月 $150–250。
- ワークフローは多数のエージェントを起動するため、同じ作業を会話で行うよりトークン消費が明確に増え、プランの利用上限・レート制限に算入される。まず小さな範囲で試すことが推奨されている。

## 登録の要否

- Claude アカウントと有料プラン、または Anthropic API キー（もしくは Bedrock / Google Cloud / Microsoft Foundry の契約）が必要。
- Pro プランでは `/config` の Dynamic workflows 行で有効化する。組織管理者は managed settings の `disableWorkflows` で全体無効化できる。

## 変更履歴

- 2026-11-09: 初回登録
