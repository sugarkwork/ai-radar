---
name: "Lyra 2.0: Explorable Generative 3D Worlds"
genre: "article"
url: "https://nv-tlabs.github.io/Project-Lyra/"
published: "2026-04-14"
flags: []
type: "article"
added: "2026-11-14"
first_seen: "2026-11-14"
risk_notes: ""
sources: ["https://x.com/NVIDIAAI/status/2118800021013643269"]
fetched_at: "2026-11-14T09:09:58.828025+00:00"
---

# Lyra 2.0: Explorable Generative 3D Worlds

## テーマ

- NVIDIAのLyra 2.0は、入力画像からカメラ経路に沿った動画を生成し、フィードフォワード再構成で探索可能な3Dシーンにする研究です。公式ページでは、出力を3D Gaussian Splattingまたはメッシュにできると説明しています。出典：[公式プロジェクトページ](https://nv-tlabs.github.io/Project-Lyra/)

## 著者の主張

- 著者らは、フレームごとの3D形状を使って関連する過去フレームを検索し、自己拡張した履歴で学習することで、空間忘却と時間的なドリフトを抑え、より長く一貫した軌跡を生成すると説明しています。これは論文著者の説明であり、ここで独立に実測した結果ではありません。出典：[公式プロジェクトページ](https://nv-tlabs.github.io/Project-Lyra/)、[論文概要](https://arxiv.org/abs/2604.13036)

## 裏取り・注意点

- 公式ページは入力画像とユーザー定義のカメラ軌跡から動画セグメントを生成し、点群を次の探索に戻す手順を記載しています。また、GUI・学習コード、モデル重み・推論コードの公開を告知しています。長時間・複雑な探索では既存手法に空間忘却や累積ドリフトが生じるという課題も著者ら自身が記載しており、効果の説明は論文上の報告として扱います。出典：[公式プロジェクトページ](https://nv-tlabs.github.io/Project-Lyra/)

## 出典

- NVIDIA公式プロジェクトページ：https://nv-tlabs.github.io/Project-Lyra/\n論文（arXiv）：https://arxiv.org/abs/2604.13036

## 変更履歴

- 2026-11-14: 初回登録
