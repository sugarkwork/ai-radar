---
name: "VINO: Revisiting 3D Representation Learning with Volume Transformers"
genre: "article"
url: "https://adriankruse.github.io/VINO/"
published: "2026-11-04"
flags: []
type: "article"
added: "2026-11-14"
first_seen: "2026-11-14"
risk_notes: ""
sources: ["https://x.com/tokufxug/status/2118891131102777379"]
fetched_at: "2026-11-14T21:12:35.480816+00:00"
---

# VINO: Revisiting 3D Representation Learning with Volume Transformers

## テーマ

- VINOは、ラベルなしの3Dシーン点群から意味表現を学習する自己教師ありフレームワーク。Volume Transformer（Volt）を用い、ビュー間の表現照合、可視コンテキストからのマスク領域予測、2Dから3Dへの知識蒸留を設計している。

## 著者の主張

- 著者らは、3Dのみの事前学習でScanNet200の線形プロービングmIoUが35.9、2D教師あり蒸留を加えた場合は40.4と報告している。また、6つのベンチマークで従来手法を上回る線形プロービング結果を得たと述べている。これらは論文著者による実験報告であり、独立した実測を示すものではない。

## 裏取り・注意点

- 公式ページは、教師がクリーンな全体ビューから目標を作り、学生が強く拡張した局所ビューやマスク済みビューを処理する方式を説明している。マスクしたトークンを学生エンコーダーから除き、可視トークンのみを使う予測器で補う。2D蒸留を含む値と含まない値は別条件の結果であり、性能は線形プロービングのベンチマーク報告として解釈する。コード・重みの利用条件や料金は、この確認範囲では特定できない。

## 出典

- [公式プロジェクトページ](https://adriankruse.github.io/VINO/)；[論文（arXiv:2611.07176）](https://arxiv.org/pdf/2611.07176)。

## 変更履歴

- 2026-11-14: 初回登録
