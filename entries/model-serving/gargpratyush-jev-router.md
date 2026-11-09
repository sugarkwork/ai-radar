---
repo: "gargpratyush/jev-router"
name: "jev-router"
genre: "model-serving"
url: "https://github.com/gargpratyush/jev-router"
author: "gargpratyush"
type: "repo"
license: "MIT"
stars: 659
language: "JavaScript"
created: "2026-09-16"
updated: "2026-09-19"
forks: 102
open_issues: 54
commits_30d: 0
commits_90d: 48
commit_cadence: "monthly"
size_kb: 365
archived: false
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "README にベンチマークが無く、ルーティング精度やコスト削減額は作者の設計主張と自己計測コメントのみで第三者検証が無い。2026-09-19 以降コミットが無く open issue は 54 件。Claude Code / Codex の非公開リクエスト形式に依存するため上流仕様の変更で壊れうる（README も JEV_DUMP での診断を案内）。プロンプト本文はルーティング判定のため TypeSafe に送信される。"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114378197932617766"]
fetched_at: "2026-11-09T16:44:06Z"
---

# jev-router — Claude Code / Codex をターン毎に安いモデルへ振り分けるルータ

## 出来ること

- 各ユーザーターン冒頭でプロンプトの複雑さを判定し、fast（Haiku）/ balanced（Sonnet）/ strong（Opus）/ long（Fable）の tier を選んで実モデルIDへ差し替える。Claude Code と OpenAI Codex の両方に対応。
- Claude Code のステータスラインに直前ターンの選択（例: ⚡ haiku p=0.98）を表示し、/model で「Jev Router」を選ぶとルーティング再開、具体モデルを選ぶと手動固定になる。
- `/jev-explain`（Codex では `$jev-explain`）で、直前の判定に使った複雑度・推論要求・ツール複雑度・文脈サイズ・確信度を表示する。
- 「use opus」「use luna」などの明示指示を最優先し、低確信度では降格せず、Jev 障害・タイムアウト時は現在のモデルを維持する（fail-open）。
- ツールループ継続とサブエージェントはターン開始時の tier に固定し、不要なモデル切替とプロンプトキャッシュの破棄を避ける。

## 目的・背景

- 些細なメッセージにも最も強いモデル(=strong tier)を使うとコストが膨らむため、ターン単位で「そのタスクを一発で完遂できる最安モデル」に振り分ける。
- 既存 CLI のログイン・ツール・セッション・権限プロンプトをそのまま使い、ANTHROPIC_BASE_URL（Claude Code）や一時カスタムプロバイダ（Codex）の差し替えだけでルーティングを挿入する。
- 判定は TypeSafe の Jev（System One）への1回の分類呼び出しで、モデルカタログ・現在モデル・概算文脈長とプロンプト本文を渡す。判定に使うプロンプト本文は TypeSafe に送信される。

## 依存関係

- Node.js 20.12 以上。npm パッケージ `jev-router` 0.3.0 の実行時依存は `@typesafe-ai/sdk` ^0.6.0 のみ。
- Claude Code（`claude login` 済み）または OpenAI Codex（`codex login` 済み）のいずれか。既存サブスクのログインがあれば Anthropic / OpenAI の API キーは不要。
- TypeSafe の API キー（`JEV_API_KEY`、`TYPESAFE_API_KEY` でも可）を `~/.jev-router.env` または起動ディレクトリの `.env` に置く。

## 実行条件

- Node 20.12+ が必要。作者の検証環境は Windows 上の Claude Code v2.1.101 / Codex v0.154.0 で、macOS・Linux や他バージョンでの動作は README に記載がない。
- Jev API は入力トークン課金で $42/Btok（$0.042/Mtok）、出力は無料。ルーティング呼び出しは新規ターンにつき1回。
- Fable tier（long）は追加クレジット課金のため既定で無効。使うには `JEV_ALLOW_FABLE=1` を設定する。
- ルーティング精度・節約額のベンチマークや第三者検証は無く、効果は作者の設計主張にとどまる。上流 CLI のリクエスト形式変更で壊れる可能性がある。

## 最短手順

- 1. インストール: `npm install -g jev-router`
- 2. キー設定: `echo "JEV_API_KEY=..." > ~/.jev-router.env`（キーは TypeSafe で取得）
- 3. Claude Code をルータ経由で起動: `jev-claude`（引数はそのまま転送される。例: `jev-claude --resume`、`jev-claude -p "fix the failing test"`）
- 4. AI（Claude Code）から使う場合: 非対話呼び出しは `jev-claude -p "<依頼>"`、起動中のセッションでは `/jev-explain` で直前ターンの判定根拠を確認できる。Codex なら `jev-codex exec "<依頼>"` と `$jev-explain`。
- 5. ルーティングを止める/再開する: `/model` で具体モデルを選ぶと手動固定、`Jev Router` を選ぶと自動ルーティングに戻る。

## 変更履歴

- 2026-11-09: 初回登録
