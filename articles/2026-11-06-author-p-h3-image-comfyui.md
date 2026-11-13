---
name: "P-H3-Imageの使い方：ComfyUIワークフローの解説"
genre: "article"
url: "https://note.com/ai_hakase/n/n391c06d816c2"
published: "2026-11-06"
flags: ["low-quality", "unverified"]
risk_notes: "記事中のプロンプト書き換えモデル名が公式資料と食い違う。無制限に無料という表現も条件を明示していない。 記事は日本語プロンプトの書き換えにGemma 4 12Bを使うと説明するが、Pruna AIの公式資料ではプロンプトアップサンプラーはQwen3.5-9Bベースとされている。また「何枚でも無料」はローカル利用にかかる環境費用やライセンス条件を含めて保証されたものではない。利用地域などの条件は公式ライセンスを確認すること。"
type: "article"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/ai_hakase_/status/2118624255520932266"]
fetched_at: "2026-11-13T00:10:35Z"
---

# P-H3-Imageの使い方：ComfyUIワークフローの解説

## テーマ

- Pruna AIの画像生成・編集モデルP-H3-ImageをComfyUIで使うための解説記事。モデルの概要、プロンプトの書き方、参照画像を使った編集、および配布ワークフローとセットアップ手順を扱う。

## 著者の主張

- 著者は、P-H3-Imageが8ステップで8メガピクセル相当の画像を生成でき、最大8枚の画像を使った編集にも対応すると説明する。また、短い日本語の指示を詳しいプロンプトに書き換える仕組みや、ComfyUIのワークフローをローカルまたはRunpodで使う手順を紹介している。これらは記事内の説明・主張であり、独立した実機検証としては扱わない。

## 裏取り・注意点

- Pruna AIの公式モデルカードは、8ステップ・8メガピクセルの生成、最大8枚の入力画像による編集、プロンプトアップサンプラーの利用を記載している。またアップサンプラーはQwen3.5-9Bベースとされ、記事のGemma 4 12Bという説明とは異なる。公式資料は小さな文字や密な文字、手、小さな人物などの限界も説明している。ローカル実行には大きなモデルファイルと対応環境が必要で、ライセンス上の利用地域等の条件もある。出典：[Pruna AI ComfyUIモデルカード](https://huggingface.co/PrunaAI/P-H3-Image-Comfy)、[Pruna AIモデルカード](https://huggingface.co/PrunaAI/P-H3-Image)。

## 出典

- 対象記事（2026年11月6日公開）：https://note.com/ai_hakase/n/n391c06d816c2
Pruna AI公式ComfyUIモデルカード：https://huggingface.co/PrunaAI/P-H3-Image-Comfy
Pruna AI公式モデルカード：https://huggingface.co/PrunaAI/P-H3-Image

## 変更履歴

- 2026-11-13: 初回登録
