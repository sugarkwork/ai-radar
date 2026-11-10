---
name: "Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights"
genre: "article"
url: "https://rikiyat.github.io/blog/weight-space-programming/"
published: "2026-11-02"
flags: ["unverified"]
risk_notes: "掲載スコアと重み編集の再現性は独立に検証していない。GPT-6 Astraの利用条件・料金、公開ログの再利用ライセンスは未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/rikiyatakehi/status/2117313742891327994"]
fetched_at: "2026-11-10T08:39:25Z"
---

# LLMによる重みの直接編集でQwen3.5-0.8Bの推論ループを減らす実験

## テーマ

- 汎用LLMがニューラルネットの重みを読み取り、自然言語で指定された課題に合わせて直接書き換える Weight-Space Programming の初期実験。

## 著者の主張

- 著者らは、GPT-6 AstraにQwen3.5-0.8Bの重みを読み込んだPython環境と練習問題を与え、勾配計算や学習を許さずに重みを編集させた。50回のフォワードパスを許した条件では、推論の反復に関わると見立てた方向を抑えるため、131,072個の重み（0.016%）を変更した。
- 同一のサンプリング設定で、MATH-500は7.9%から48.1%、IFEvalは21.0%から62.3%に上昇したと著者らは報告している。MATH-500で出力がトークン上限に達した割合は93.0%から33.1%に下がった。

## 裏取り・注意点

- 著者記事の実験8で編集条件と評価表を確認した。50回はバッチ単位のフォワードパス予算で、各回に複数の練習問題を処理できる。
- 反復が少ないGemma 3 270Mでは、同記事の追加実験で明確な改善を確認できなかったと著者らは述べている。掲載値は著者による評価で、独立再現は未実施。GPT-6 Astraの利用条件・料金とログの再利用ライセンスは未確認。

## 出典

- Rikiya Takehi、Jayden Teoh、Alex Zhang、Omar Khattabの公開記事（2026年11月2日）。 https://rikiyat.github.io/blog/weight-space-programming/
- 著者の実験ログ公開先。 https://github.com/RikiyaT/lm_understand-logs

## 変更履歴

- 2026-11-10: 初回登録
