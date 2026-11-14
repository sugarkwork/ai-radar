---
name: "Introducing Arete-27B: Qwen3.8-27B Post-Trained To Reinforce Western Values"
genre: "article"
url: "https://nousresearch.com/arete"
published: "2026-11-06"
flags: ["unverified"]
risk_notes: "評価結果と能力維持の主張は記事著者による報告であり、独立検証とは確認できていない。記事自身が全ての関連挙動を解消したとは主張していない。"
type: "article"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/NFT_Chen/status/2118847554133918003"]
fetched_at: "2026-11-14T14:09:18.550064+00:00"
---

# Introducing Arete-27B: Qwen3.8-27B Post-Trained To Reinforce Western Values

## テーマ

- Qwen3.8-27Bを追加学習してArete-27Bを作成し、7つの価値観カテゴリを対象とする803プロンプト評価で、事実回答と公式的な政治的フレーミングを測定した研究報告。

## 著者の主張

- Nous Researchは、約5,280万トークンで2エポックの微調整を行い、評価上の事実スコアが2.32から2.98（5点満点）に上がり、公式的な党派フレーミングを含む回答が22%から約1%に下がったと報告する。自由表現カテゴリでは、事実スコアが0.89から2.44、該当回答率が60%から1%になったとしている。Hermes Benchの値はArete-27B 65.60%、ベースQwen 65.77%、Terminal-Bench-2.1はそれぞれ70%、67%と記載。これらはいずれも記事著者の評価・解釈である。

## 裏取り・注意点

- 記事は評価プロンプト、採点定義、モデル別結果、学習データ、学習設定を説明し、重み・評価セット・訓練データへのリンクを掲載する。採点にはGrok 4.7を使い、25件のパイロットを人手採点と照合したと説明。各モデルの反復回数や温度設定は表注に記載され、Areteのthinking-on結果は2/5回の暫定値。独立した再現実験はこの記事から確認できず、著者も対象挙動をすべて解消したとは主張していない。

## 出典

- Nous Research, “Introducing Arete-27B: Qwen3.8-27B Post-Trained To Reinforce Western Values” — https://nousresearch.com/arete

## 変更履歴

- 2026-11-14: 初回登録
