---
name: "Eddie Woo の対数講義――「何倍になるまでの時間」を1本の対数で読む"
genre: "article"
url: "https://www.youtube.com/watch?v=ntBWrcbAhaY"
published: "2026-09-14"
author: "xsmryze"
flags: ["unverified"]
risk_notes: "主張: 投資が何倍になるまでの時間は対数1本で、Eddie Woo の5分の講義がそれを自明にする、という投稿。確認できたこと: Eddie Woo はシドニーの公立高校数学教師で、YouTube @misterwootube は登録者2.01M・5,043本・191,145,357回再生（2026-11-09取得）。添付動画は7分51秒の実授業映像で、白板の LOGARITHMS / 2^5=32 / log_2 32=5 / log_3 81=4 と 2,4,8,16,32・3,9,27,81 の説明が Woo の「Introduction to Logarithms (1 of 2: Definition)」（7:52, 2017-08-30）の内容と一致。数学も正しい（log_3 81=4、倍加時間 ln2/ln(1+r)、Rule of 72 は近似）。未確認: 引用元X記事（x.com/i/article/2087190920026365952）の本文はログイン要求で取得できず、fetch_article.py も失敗。動画の音声は未転記で、投稿の「5分で」は実際の7分51秒と一致しない。Rule of 72 は近似であり、実務では変動リターン・手数料・税金で変わる点は投稿に無い。"
type: "article"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/xsmryze/status/2099540913714299009"]
fetched_at: "2026-11-09T09:32:39Z"
---

# Eddie Woo：投資の倍加時間は「1本の対数」で読める

## テーマ

- オーストラリア・シドニーの公立高校数学教師 Eddie Woo（YouTube「misterwootube」、登録者2.01M）の対数導入授業を、X の投稿者が「投資が何倍になるまでの時間」に結びつけて紹介した投稿（2026-09-14）。
- 添付は 1920x1080・7分51秒の授業映像。白板に「LOGARITHMS」と 2^5=32、log_2 32=5、log_3 81=4 が書かれ、2,4,8,16,32 と 3,9,27,81 の数え上げで対数を説明する場面が実際に確認できる。

## 著者の主張

- 「何倍になるまでの時間」を求める問いは、対数1本に還元できる。
- 倍々機械 2,4,8,16,32 で「何回倍にしたか」が log。3倍機械なら log_3 81 = 4（3,9,27,81）。
- 「32倍になったなら、どれだけの時間成長していたか」が対数の問いであり、その講義は無料で公開されている、というのが投稿の骨子。

## 裏取り・注意点

- 数学は正しい。定義は b^x = y ⇔ log_b y = x（OpenStax College Algebra 2e 6.3）。log_2 32 = 5、log_3 81 = 4 は 2^5=32、3^4=81 として確認できる。
- 倍加時間は t = ln2 / ln(1+r) ≈ 0.693/r（離散複利）。実測値は 1%→69.66年、5%→14.21年、8%→9.01年、10%→7.27年、20%→3.80年。連続複利なら ln2/r ≈ 69.3/r。
- Rule of 72（72/r）の誤差は 1%で+3.4%、5%で+1.4%、8%でほぼ0（-0.07%）、10%で-1.0%、20%で-5.3%。低率ほど精度が高く、高率では過小評価になる。SEC も「rule of thumb」と明記している。
- 実務では収益率が一定でなく（ボラティリティ）、手数料・税金・インフレが乗る。SEC の例では年4%・20年で年1%の手数料が $100,000 を約 $179,000 に減らす（0.25%なら約 $208,000）。「対数1本」は理想化された前提での結論。
- 投稿は「5分で自明にする」と書くが、添付動画は7分51秒。引用元のX記事本文はログイン要求で取得できず未確認（fetch_article.py も失敗）。動画の音声は未転記で、話者が Woo 本人であることは映像・内容の一致からの推定にとどまる。

## 出典

- 投稿: https://x.com/xsmryze/status/2099540913714299009 （2026-09-14T16:48:56Z）
- 講義: https://www.youtube.com/watch?v=ntBWrcbAhaY （Introduction to Logarithms (1 of 2: Definition), 2017-08-30, 7:52）
- チャンネル: https://www.youtube.com/@misterwootube/about
- 本人公式サイト: https://misterwootube.com/about
- 対数の定義: https://openstax.org/books/college-algebra-2e/pages/6-3-logarithmic-functions
- Rule of 72: https://en.wikipedia.org/wiki/Rule_of_72 / https://www.sec.gov/investor/students/tips.htm
- 手数料の影響: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated

## 変更履歴

- 2026-11-09: 初回登録
