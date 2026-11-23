---
name: "Reimagining research papers as interactive and reliable AI agents"
genre: "article"
url: "https://www.nature.com/articles/s41586-026-11044-y"
published: "2026-09-16"
flags: ["unverified"]
risk_notes: "91.2% ± 1.6% は計算生物学論文100本から作成した300件のチュートリアル由来ベンチマークでの著者報告値。自由形式の科学的妥当性全般を示す数値ではなく、論文も未解決の科学的解釈には人間の関与が必要としている。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ctxzz/status/2119199477072384201"]
fetched_at: "2026-11-19T01:12:17.888837+00:00"
---

# Reimagining research papers as interactive and reliable AI agents

## テーマ

- 研究論文と関連コードを解析し、手法・データ・ワークフローを自然言語で扱えるAIエージェントにするPaper2Agentの枠組み。論文由来のMCPサーバーを構築し、対応するエージェントからツールや資料を利用できるようにする。

## 著者の主張

- 著者らは、計算生物学論文100本のうち74本をエージェント化し、抽出した599ツール中593ツールが自動検証を通過したと報告。300件のチュートリアル由来質問では、Sonnet 4を用いたPaper2Agentが91.2% ± 1.6%の正答率を示し、論文とリポジトリを直接与えたClaude Codeの80.3% ± 2.3%を上回った。論文ではAlphaGenome、Scanpy、TISSUE等の事例も示している。

## 裏取り・注意点

- Nature掲載論文で公開日、手法、評価条件と数値を確認。74/100、593/599、91.2% ± 1.6%はいずれも著者らの実験結果であり、独立した追試結果ではない。論文は、実行可能コードやデータの不足、環境構築の失敗などでエージェント化できない論文があること、自由形式の科学的解釈には人間の関与が必要であることも記載している。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- Nature掲載論文: https://www.nature.com/articles/s41586-026-11044-y
著者の公開リポジトリ: https://github.com/jmiao24/Paper2Agent

## 変更履歴

- 2026-11-23: 初回登録
