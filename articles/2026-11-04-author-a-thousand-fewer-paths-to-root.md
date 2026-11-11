---
name: "A thousand fewer paths to root"
genre: "article"
url: "https://openai.com/index/a-thousand-fewer-paths-to-root/"
published: "2026-11-04"
flags: []
type: "article"
added: "2026-11-11"
first_seen: "2026-11-11"
risk_notes: ""
sources: ["https://x.com/neuronxwhite/status/2118220433715822612"]
fetched_at: "2026-11-11T04:17:25Z"
---

# A thousand fewer paths to root

## テーマ

- OpenAIが、Linuxカーネルを対象に脆弱性の発見、動的検証、悪用可能性の評価、パッチ生成を行う自律型パイプラインを研究環境で評価した記事。

## 著者の主張

- OpenAIは、2026年10月の実験で2,308件の候補を調べ、1,724件を再現し、1,169件の動作するローカル権限昇格exploitと、948件の一意なLPEに対応するパッチを作成したと報告。全工程のAPIクレジット費用は1,213,430ドル。記事は、防御側による継続的な調査と修正、モデル能力の変化に応じた再スキャンを提案している。これらはOpenAIの実験報告であり、独立実測としては扱わない。

## 裏取り・注意点

- OpenAIの説明では、検証は隔離VM上で行われ、候補の再現性や攻撃経路は人間のレビューも受けた。初期実行では、成功と判定された200件のうち20件が割り当てられた脆弱性とは別の0-dayを使ってrootを得ており、その後に制約と独立確認を追加したという。費用は使用モデル、対象設定、ワークフローに依存し、記事は十分なハーネス改善で削減できる可能性があるとしている。賞金額との比較は過去の公表額に基づく仮想評価。

## 出典

- [OpenAI公式記事「A thousand fewer paths to root」](https://openai.com/index/a-thousand-fewer-paths-to-root/)（公開日: 2026-11-04）。

## 変更履歴

- 2026-11-11: 初回登録
