---
name: "MiniMax H3の参照動画で走る女性のふくらはぎを柔らかく描くプロンプト調整"
genre: "prompt-design"
url: "https://make-profit.net/2026/11/07/genai-lab-59-minimax-h3-ref2va-rear-jogging-calf-softness-positive-prompt/"
published: "2026-11-07"
flags: ["unverified"]
risk_notes: "柔らかな厚みの指定で改善したという効果は、作者による1組・1seedの目視評価で、全コマでの改善や他seedでの再現性は確認されていない。記事自身も原因をH3の学習表現に帰する説明を観察に基づく推測としている。"
type: "article"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/Phantom_202601/status/2118840281009365015"]
fetched_at: "2026-11-13T14:07:18.938460+00:00"
---

# MiniMax H3の参照動画で走る女性のふくらはぎを柔らかく描くプロンプト調整

## テーマ

- MiniMax H3の参照動画生成で、走る女性の後ろ姿のふくらはぎが筋肉質に見える問題を扱う。動きとカメラはBlenderの白素体動画、容姿はキャラクターシート、形状の微調整はプロンプトに分担させる。

## 著者の主張

- 作者は、白素体を細くする方法ではふくらはぎの張りがあまり変わらなかったと報告。00015から00016では、同じseed・モデル・参照素材・ステップ数で、脚についてのプロンプト段落を変更し、「柔らかな厚み」「均等なふくらみ」「連続した丸い曲面」を肯定形で記述した。作者の目視評価では一部のコマの明暗が穏やかになった。参照の役割を明記するプロンプト形式は、MiniMax公式H3リポジトリのガイドにも記載されている。

## 裏取り・注意点

- 公式の参照モードガイドは、rewrite出力を6セクションで構成し、Picture・Videoなどの参照ラベルと役割を明確にするよう説明している。今回の形状指定が改善をもたらすという一般的な効果は公式資料で確認できない。記事の比較は作者による1組・1seedの目視評価で、寸法測定ではなく、他seedでの再現性も未確認。白素体を細くしても解決しなかった原因をH3の学習表現に求める説明も作者の推測である。

## 出典

- 記事（公開日2026-11-07）: https://make-profit.net/2026/11/07/genai-lab-59-minimax-h3-ref2va-rear-jogging-calf-softness-positive-prompt/
MiniMax公式H3参照モード・プロンプトガイド: https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md

## 変更履歴

- 2026-11-13: 初回登録
