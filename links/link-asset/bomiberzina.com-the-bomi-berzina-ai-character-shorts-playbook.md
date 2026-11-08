---
name: "The Bomi Berzina AI Character Shorts Playbook"
genre: "link-asset"
url: "https://bomiberzina.com/viral"
author: "Bomi Berzina（bomiberzina.com）"
pricing: "paid"
pricing_detail: "$9.99 USD の一回払い（サブスクなし）。8ページ・17ステップのPDFで、決済後すぐダウンロード＋メールでアクセスリンク。30日返金保証（領収メールへ返信）。別途 Higgsfield（有料、Ultra 9,000クレジットを推奨）と ChatGPT/Gemini、CapCut 等が必要で、動画クレジットは含まれない。"
signup_required: false
flags: ["unverified"]
risk_notes: "投稿の「10日で$13K」「10.6M再生」「最大5.6M」は投稿者自身の推計であり一次情報で確認していない。今回実測できたのは TikTok プロフィールの 23.6K フォロワー / 539.7K いいね / 13本（2026-11-08時点、レンダリング取得）で、個別動画の再生数は TikTok の WAF とログイン要求で取得できず未確認。Instagram は HTTP 200 だがログインウォールでプロフィールを読めない。価格 $9.99 は販売ページの表示と JSON-LD で確認し、Stripe の live セッションも実際に発行された（303）が、Stripe ページの金額は JS レンダリングで HTML から読めず、決済額そのものは未確認。PDF 本文は有料で、無料公開のプレビューは2ページ分（02, 04）のみ。17ステップのうち確認できたのは 01, 02, 05, 06, 07, 08 の6ステップとプロンプト2本（キャラクターシート用、Genjutsu の Object Swap 用）だけで、残り11ステップと残りのプロンプト本文は未確認。返金は商品ページに30日と明記されているが、リンク先の規約・返金ページ（smashcourses.com）は汎用文面で Bomi 商品を名指ししておらず、連絡先も商品ページは zenithlawassociates@gmail.com、規約ページは service@officeofagents.com で一致しない。手順06は他者のバイラル動画を第三者のダウンローダー（ytshortsdl.com / snaptik / igexport）で保存しキャラクターを差し替えるよう指示しており、著作権と各SNSの規約上のリスクがある。Jean Phil など他者キャラクターの世界観に便乗する手法も権利面で要注意。同一ドメインのルート https://bomiberzina.com は未発行の Solana ミームコイン「$BB」のプレローンチページ（価格 'Soon'、'CA DROPS AT LAUNCH'）で、ブランドがトークン販売と結び付いている点は別種の高リスクとして扱う。"
type: "link"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/Y0urDumble/status/2110431266990682466"]
fetched_at: "2026-11-08T06:01:30Z"
---

# The Bomi Berzina AI Character Shorts Playbook — 同一キャラクターでAIショートを量産する8ページ・17ステップ手順書（$9.99）

## 目的

- AI生成キャラクターを1体作り、そのキャラクターを毎回同じ見た目でショート動画に出演させ続けるための有料PDF手順書。動画の元ネタ探し→キャラクターの差し替え→書き出し→投稿までを17ステップに区切っている。
- 投稿で紹介されていた AI キャラクター「Bomi Berzina」の運用をそのまま商品化したもの。販売ページは「キャラクターが広告であり、各クリップが実績になる」という前提で、その制作工程を売っている。
- キャラクター側のアカウントは TikTok の @bomiberzina（表示名 Pokémog、プロフィールのリンクは bomiberzina.com）。2026-11-08 時点の表示は 23.6K フォロワー、539.7K いいね、13本の動画。

## 何ができるか

- PDF は8ページ・17ステップ。ステップ01で使用ツールとクレジット購入、02で画像生成による4面図のキャラクターシート作成、05で元になるバイラルクリップの選定、06で動画のダウンロード、07で Higgsfield の Genjutsu（Object Swap）によるキャラクター差し替え、08で生成と書き出し、という流れが公開プレビュー（ページ02と04）で確認できる。
- 公開プレビューにはプロンプトが全文で載っている。キャラクターシート用は「Create a photorealistic reference sheet of one original adult fictional character. Identity: [name, face shape and distinguishing feature]...」で始まるプレースホルダー入りのテンプレート、差し替え用は「Swap the main character for this character @image1 (character card) @image2 (character face).」の1文。どちらもコピーして使う前提で、画像参照の順序（カード→顔）まで指定されている。
- 必要なもの: 画像生成に ChatGPT または Gemini（Gemini は Nano Banana）、動画に Higgsfield（Genjutsu / Object Swap、720p）、編集に CapCut など。企画は「踊り・スタント・スポーツ・コメディ」など既に伸びているクリップを選び、30秒以内に収める。
- 残りのステップ（03, 04, 09〜17）とプロンプトの全文は有料部分にあり未確認。販売ページの記載では「キャラクターの顔プロンプト」「差し替えとオリジナル生成の2通り」「編集・キャプション・AIラベル・書き出し」までを含むとされている。
- 購入はブラウザから Stripe Checkout に進む方式で、専用アプリやAPIはない。決済後にPDFを即時ダウンロードし、同じアクセスリンクをメールでも受け取る。

## 料金

- $9.99 USD の一回払い。サブスクや追加課金の記載はなく、ページの構造化データも price 9.99 / priceCurrency USD / InStock。
- 30日返金保証。商品ページは「領収メールに返信すれば全額返金、質問なし」と明記。リンク先の返金ポリシーも既定30日・全額返金としているが、Bomi 商品を名指しした文面ではない。
- 別途コストが大きい。Higgsfield は有料で、PDF は Ultra の 9,000クレジット（有料プラン）を推奨している。ChatGPT/Gemini の有料プランと CapCut も前提で、動画クレジットは商品に含まれない。$9.99 は総コストの入り口に過ぎない。
- ライセンスは個人利用のみで、再販・再配布・再公開は不可（規約ページ）。

## 登録の要否

- アカウント登録は不要。Stripe Checkout でメールアドレスを入力して支払い、ダウンロードリンクをメールで受け取る。
- 購入前は本文を読めない。無料で見られるのは販売ページ上の2ページ分のプレビュー（ページ02と04）だけで、17ステップの全体とプロンプトの残りは購入後にしか確認できない。
- PDF の配布はメールアドレスに紐づくため、購入後の再ダウンロードはメールのアクセスリンクに依存する。

## 変更履歴

- 2026-11-08: 初回登録
