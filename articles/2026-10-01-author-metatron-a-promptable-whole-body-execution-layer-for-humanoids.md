---
name: "Metatron — A Promptable Whole-Body Execution Layer for Humanoids"
genre: "article"
url: "https://research.nvidia.com/labs/par/projects/metatron/"
published: "2026-10-01"
flags: ["unverified"]
risk_notes: "実演値や改善の説明はNVIDIA掲載資料の報告であり、独立検証ではない。歩行品質・安定性の改善は定性的評価と明記されている。"
type: "article"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/AlecSaysThings/status/2119160757602427144"]
fetched_at: "2026-11-17T06:24:25.047076+00:00"
---

# Metatron — A Promptable Whole-Body Execution Layer for Humanoids

## テーマ

- Metatronは、部分的な目標指定からヒューマノイドの全身運動を生成する実行層と、その目標を与えるプログラム可能なスキル層を組み合わせる研究プロジェクト。NVIDIA Researchのページは、制御器を一度学習して凍結し、個別の行動はスキルの目標指定コードで表す構成を説明している。

## 著者の主張

- 公式ページによると、手足や胴体の位置、進行方向・速度、目標時刻など必要な部分目標を与え、残りの身体協調を制御器に任せる。コーディングエージェントはシミュレーションでスキルを作成・調整でき、実行時にはスキルが目標を制御器へ渡す。論文要旨は、実機Unitree G1で歩行、回復、物体操作、着座に同一の凍結済みチェックポイントを用いたと報告し、シミュレーションでは登攀やアクロバットも扱うとしている。

## 裏取り・注意点

- 公式プロジェクトページには実機録画とシミュレーション例が掲載されている。ページ自身が歩行品質・安定性の改善を定性的評価としていること、障害物情報やボールの投入時刻をタスクコード側から与える例があることに留意。掲載された動作例や数値は作者側の報告であり、独立実測ではない。

## 出典

- NVIDIA Research, “Metatron — A Promptable Whole-Body Execution Layer for Humanoids” https://research.nvidia.com/labs/par/projects/metatron/ （ページ内の機能説明、スキル生成手順、実機・シミュレーション例）。論文リンク先のPDF https://research.nvidia.com/labs/par/projects/metatron/assets/metatron-paper.pdf?v=de2411a21822 （論文要旨と評価対象）。公開日はNVIDIA Researchの出版物ページに「October 2026」と記載されている。

## 変更履歴

- 2026-11-22: 初回登録
