---
name: "The components of agent memory"
genre: "article"
url: "https://www.anthropic.com/research/components-of-agent-memory"
author: "Anthropic Engineering"
published: "2026-11-06"
flags: ["unverified"]
risk_notes: "評価はAnthropicの報告に基づく。独立再現、別タスクへの一般化、記憶の保守に必要な計算コストは未検証。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Nursing_DX/status/2119274934631555421"]
fetched_at: "2026-11-10T06:17:03Z"
---

# The components of agent memory

## テーマ

- エージェントがセッションをまたいで使う記憶を、検索可能な実行記録、メモ、wikiなどの記憶表現、各セッションの開始時に読み込むコンテキストの4層に整理する設計。

## 著者の主張

- セッション間に実行記録を見直す dreaming により、誤ったメモの訂正やwikiの更新ができる。Anthropicは、Pokémon Redの試行で誤った位置情報を記録と照合して修正すると、エージェントが次の街に到達した事例を報告している。

## 裏取り・注意点

- CL-Bench 1.0のデータベース課題では、各質問を新しいセッションで始め、セッション間で保持される記憶ディレクトリを参照できるようにしている。この評価と、Pokémon Redで dreaming によるメモ訂正を試した事例は別の実験。記事は記憶の維持に計算資源が必要で、点検の頻度や対象を調整する余地があると述べている。

## 出典

- https://www.anthropic.com/research/components-of-agent-memory

## 変更履歴

- 2026-11-10: 初回登録
