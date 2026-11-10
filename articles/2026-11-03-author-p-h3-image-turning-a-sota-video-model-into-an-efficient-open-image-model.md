---
name: "P-H3-Image: Turning a SOTA Video Model into an Efficient Open Image Model"
genre: "article"
url: "https://www.pruna.ai/blog/oss-p-h3-image-launch"
published: "2026-11-03"
flags: ["unverified"]
risk_notes: "編集入力の上限は記事では9枚、公式モデルカード2件では編集対象を含めて8枚。9枚入力の動作、生成速度、VRAM使用量、出力品質は独立検証していない。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/PrunaAI/status/2117663564487926043"]
fetched_at: "2026-11-10T10:14:02Z"
---

# P-H3-Imageの技術解説：MiniMax-H3を画像生成・編集向けに転用

## テーマ

- Pruna AIが動画モデルMiniMax-H3を画像生成・編集向けに転用した設計を解説する。記事にはDiffusersの実行例と、編集で変更する箇所と保持する箇所を指定するプロンプトの書き方がある。

## 著者の主張

- Pruna AIは、テキストエンコーダの蒸留や静止画向けデコーダの学習を行い、拡散のサンプリングを50ステップから8ステップに短縮したと説明する。B200 1基で4 MPの画像を生成した比較では、MiniMax-H3の12.4秒に対してP-H3-Imageは2.6秒だったと報告している。

## 裏取り・注意点

- Pruna AIの公開モデルカードでは、Diffusersのbf16構成は8 MPでプロンプト拡張器込み約101 GBのGPUメモリを使用する。ComfyUIの量子化構成では8 MPでピーク約21 GBとされ、公開ワークフローも案内されている。いずれも開発元の報告値。 [Diffusersモデルカード](https://huggingface.co/PrunaAI/P-H3-Image)・[ComfyUIモデルカード](https://huggingface.co/PrunaAI/P-H3-Image-Comfy)
- 編集入力の上限は公式記事の9枚と、両モデルカードの8枚（編集対象1枚を含む）で食い違う。9枚入力の動作と出力品質は未検証。 [公式記事](https://www.pruna.ai/blog/oss-p-h3-image-launch)・[Diffusersモデルカード](https://huggingface.co/PrunaAI/P-H3-Image)・[ComfyUIモデルカード](https://huggingface.co/PrunaAI/P-H3-Image-Comfy)
- 重みにはMiniMax H3 Community Licenseが適用される。公式記事は、別途許諾がない場合の対象地域の制限と、製品での帰属表示要件を案内している。 [公式記事](https://www.pruna.ai/blog/oss-p-h3-image-launch)

## 出典

- [Pruna AI公式技術記事（2026年11月3日）](https://www.pruna.ai/blog/oss-p-h3-image-launch)
- [Pruna AI公式Diffusersモデルカード](https://huggingface.co/PrunaAI/P-H3-Image)
- [Pruna AI公式ComfyUIモデルカード](https://huggingface.co/PrunaAI/P-H3-Image-Comfy)

## 変更履歴

- 2026-11-10: 初回登録
