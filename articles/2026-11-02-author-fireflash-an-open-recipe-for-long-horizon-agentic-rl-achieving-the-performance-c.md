---
name: "FireFlash: An Open Recipe for Long-Horizon Agentic RL Achieving the Performance-Cost Pareto Frontier"
genre: "article"
url: "https://agenteconomics.org/posts/agentic-rl-recipe"
published: "2026-11-02"
flags: ["unverified"]
risk_notes: "ベンチマーク値、コスト、学習効率は記事の著者による報告で、この記事の記述だけでは独立した再現・検証を確認できない。評価は著者らのハーネスで実施したと説明されている。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119401057461616765"]
fetched_at: "2026-11-20T05:09:40.918666+00:00"
---

# FireFlash: An Open Recipe for Long-Horizon Agentic RL Achieving the Performance-Cost Pareto Frontier

## テーマ

- 長期のエージェント型タスクに向けたFireFlashの強化学習レシピを紹介する記事。環境・タスクの選定、報酬設計、実行ハーネス、非同期学習の構成を説明している。

## 著者の主張

- 著者らは、GLM-5.3-Flashを基にした300B規模のモデルを、NVIDIA B300 GPU 64枚、5日未満で学習したと報告している。記事ではTerminal-Bench 4.0で46.2%、DeepSWE v1.1で68.8%、SWE-Bench Pro Verifiedで63.3%とし、タスクの初期成功率による選別、各タスクと採点器の検証、長時間実行向けハーネス、古い低精度ロールアウトを扱うGRPO構成などを説明している。これらの性能・費用値は著者らの報告である。

## 裏取り・注意点

- 記事本文と公開日（2026-11-02）を確認した。記事によれば評価は学習時と同じ著者らのハーネスで行われている。記載されたベンチマーク値や費用について、記事本文から独立した再現・検証は確認できない。記事は「full recipe」を公開すると述べているが、本文の記載だけではモデル重みや全レシピの公開状況までは確認できない。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- Agent Economics, “FireFlash: An Open Recipe for Long-Horizon Agentic RL Achieving the Performance-Cost Pareto Frontier” — https://agenteconomics.org/posts/agentic-rl-recipe

## 変更履歴

- 2026-11-23: 初回登録
