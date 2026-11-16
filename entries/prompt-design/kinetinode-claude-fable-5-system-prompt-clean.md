---
name: "Universal Fable 5 System Prompt"
genre: "prompt-design"
url: "https://github.com/KinetiNode/claude-fable-5-system-prompt-clean"
repo: "KinetiNode/claude-fable-5-system-prompt-clean"
license: "MIT"
stars: 525
language: "unknown"
created: "2026-07-19"
updated: "2026-08-08"
forks: 112
open_issues: 1
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 34
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/ruyi3699/status/2119046206965899745"]
fetched_at: "2026-11-16T09:24:31.719721+00:00"
---

# Universal Fable 5 System Prompt

## 出来ること

- Claude Fable 5 / Mythos 5の公開システムプロンプトから、XML形式、ツール連携、製品固有の指示などClaude固有の実装要素を除き、他のモデルにも適用できる行動指針を抽出したプロンプトを提供する。core、balanced、completeの3種類を収録。READMEではClaude、ChatGPT、Gemini、DeepSeek、Qwen、Grok、GLMなどの指示追従型LLMを対象としている。

## 目的・背景

- 元のプロンプトに含まれるClaudeの本番環境向け実装要素を取り除き、モデル間で再利用しやすい行動指針を残すことを目的とする。プロジェクトは元のAnthropicプロンプトを置き換えたり、改善を主張したりするものではなく、移植性を重視すると説明している。

## 依存関係

- READMEに記載なし。

## 実行条件

- 選んだプロンプトの内容をAPIプラットフォームのsystem prompt / system instructions欄へ貼り付ける。対応する消費者向けインターフェースでは、custom instructions、custom GPT system prompt、Gemsなどにも利用できる。

## 最短手順

- 1. 用途に応じて `universal/core.md`、`universal/balanced.md`、`universal/complete.md` のいずれかを選ぶ。
2. ファイルの内容をモデルのsystem promptまたはsystem instructions欄へ貼り付ける。
3. カスタム指示に対応したインターフェースでは、その指示欄へ設定する。

## 変更履歴

- 2026-11-16: 初回登録
