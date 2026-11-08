---
name: "実写→1980s OVA調スタイルLoRAの学習レシピ（MiniMax H3 / AI Toolkit）"
genre: "video-gen"
url: "https://x.com/julienaiart/status/2118896078670143797"
author: "@JulienAIArt"
published: "2026-11-07"
type: "article"
added: "2026-11-08"
first_seen: "2026-11-07"
sources: ["https://x.com/julienaiart/status/2118896078670143797", "https://github.com/ostris/ai-toolkit"]
flags: ["unverified"]
risk_notes: "数値・手法はすべて本人申告で第三者検証なし。LoRAの重み・データセットは未公開で、次週Adobe MAX（Dellブース 11/10-11）での解説予告のみ。RTX PRO 6000（24GB超VRAM）で約30時間・4,000stepの条件は、A4000 16GBでは同条件の再現が非現実的。lossは1,000stepで頭打ちだが品質は2,500stepまで改善、4,000stepで過学習という報告も本人計測。"
fetched_at: "2026-11-08T06:40:00Z"
---

# 実写→1980s OVA調スタイルLoRAの学習レシピ

## テーマ

- 実写動画を参照入力に取る MiniMax H3 の Reference-to-Video 向けに、**1980年代OVA風の画風**を学習させるスタイルLoRAの作成報告。
- 学習ツールは `ostris/ai-toolkit`（MIT、12.6k stars、2026-11-04更新）。描画は ComfyUI。

## 著者の主張

- **画風**: 実写写真と、同じ構図でOVA風に描き直した画像のペアを **21組** 用意し、スタイルを学習。
- **動き**: 短尺アニメクリップ **10本** を「自分自身を正解」とした対で使い、動きの模倣を学習。
- **学習条件**: RTX PRO 6000 搭載 Dell T2 で約 **30時間**、**4,000 step**、**rank 16**。
- **収束**: loss は1,000stepで頭打ちになるが、品質は2,500stepまで改善し、4,000stepでは過学習。
- 「実写の構図を保ったまま、動きと画風だけをOVA調に寄せられる」という主張。

## 裏取り・注意点

- ai-toolkit が MIT で公開され、MiniMax H3 の Reference-to-Video が実在することは確認できる。ただし**このLoRA自体の重み・データセットは未公開**で、再現に必要な素材が揃っていない。
- 21組・10本・30時間・4,000step・rank16 はすべて**本人申告**。第三者の追試、学習ログ、サンプル比較は提示されていない。
- 24GB超VRAMのGPUで30時間級の学習を前提とする。**RTX A4000 16GBでは同条件の再現は現実的でない**（解像度・batch・rankを落とす必要がある）。
- 次週の Adobe MAX（Dellブース、11/10-11）で解説予定とだけ告知されており、資料はまだ無い。
- 権利面: 参照に使った実写・アニメクリップの権利は不明。配布時は元素材の許諾が必要。

## 出典

- 投稿: https://x.com/julienaiart/status/2118896078670143797 （2026-11-07、@JulienAIArt）
- 学習ツール: https://github.com/ostris/ai-toolkit （MIT）
- 関連: MiniMax H3 Reference-to-Video（既出エントリあり）

## 変更履歴

- 2026-11-08: 初回登録（配布物が無いため「保留」だったものを、レシピ情報として収録）
