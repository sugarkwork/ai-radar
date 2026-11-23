---
name: "InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image"
genre: "3d-motion"
url: "https://coolho1129.github.io/InstantHand-page/"
published: "2026-11-05"
flags: ["unverified"]
risk_notes: "公式実装のREADMEは、改変版diff-gaussian-rasterizationと事前学習済みチェックポイントが非商用研究用途に制限されるため、リポジトリ全体も非商用研究用途のみと記載。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Machinedelusion/status/2119272950503530717"]
fetched_at: "2026-11-18T15:34:05.193639+00:00"
---

# InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image

## テーマ

- 1枚の手画像からアニメーション可能な3D Gaussian hand avatarをフィードフォワードで再構成する手法InstantHandの研究記事。

## 著者の主張

- 著者らは、MANO・カメラ・マスクの推定値を入力に使い、テスト時の個別最適化なしで単一画像からアバターを構築すると説明している。輪郭の欠損・にじみを抑えるSoft Alpha Bandと、観測された外観の保持および隠れた部分の補完を行うReliability-gated Appearance Transferを提案。ページでは構築2.84秒、描画161 FPS、InterHand2.6MとHanCoでの評価結果を報告している。これらは著者側の報告値。

## 裏取り・注意点

- arXivの一次資料は2026-11-05提出と記載。公式実装READMEでは、構築2.84秒・描画161 FPSはA100 1基での値とされる。実装の利用条件は構成要素ごとに異なり、READMEは全体を非商用研究用途に限ると記載している。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- [研究プロジェクトページ](https://coolho1129.github.io/InstantHand-page/) · [arXiv論文](https://arxiv.org/abs/2611.08330) · [公式実装とREADME](https://github.com/coolho1129/InstantHand)

## 変更履歴

- 2026-11-23: 初回登録
