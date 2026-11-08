---
name: "Higgsfield"
genre: "video-gen"
url: "https://higgsfield.ai/"
author: "Higgsfield Inc."
pricing: "freemium"
pricing_detail: "無料: Free プラン（Limited use、クレジット付与なし、利用できるモデルは少数、料金比較表では商用利用 Not included）。有料: クレジット制サブスク。2026-11-08 の料金ページ（年払い表示）は Starter 270 credits/月 $19、Plus 1,200 credits/月 $47（月払い $59）、Ultra 3,000 credits/月 $99（月払い $129）、税別・30% OFF のプロモーション中。2026-10-03 の公式ブログ表は Starter $15/月（月払い）、Plus $49/月（年払い $39/月）、Ultra $129/月（年払い $99/月）。クレジットは月次リセットで繰り越しなし、追加購入可。生成単価はモデル・解像度・尺で変わり、実行前に Generate ボタンへ表示（例: キャラクター生成 1.12 credits ≒ $0.06、Kling 3.0 720p 約7 credits/5秒、Seedance 2.0 1080p 約60 credits/5秒）。Unlimited と Free Generations は higgsfield.ai 上のみで MCP / CLI / Canvas / Supercomputer からは使えない。"
signup_required: true
flags: ["unverified"]
risk_notes: "【投稿の主張と実測の区別】ポストは架空のラッパー風ペルソナ「Marcel Duvall」が18日で9本・5.16M再生・817.8Kいいね・15.9Kフォロワー、推定$13Kを稼ぎ、$Marcel コインの時価総額が約$3.5Kだと述べるが、これらは投稿者の集計・推計で一次確認していない（フォロワー16Kはスクリーンショットとも一致）。返信で著者は「with the new higgsfield function its as easy as it can get!」とだけ書き、機能名は特定していない。投稿日（2026-10-17）と公式ブログのAI Influencer刷新（2026-10-03）から、AI Influencer＋Genjutsu の組み合わせとみられるが、これは推定であり投稿に明記はない。引用ポストの「$15で作れる」のリンク先 X 記事（2109318233866006528）はログインウォールで本文を取得できていない。ただし公式ブログの2026-10時点の料金表は Starter $15/月（月払い）で、当時の最安有料プランと一致する。現在の料金ページは Starter $19/月（年払い・プロモ表示）で、金額とクレジット数は変動する（未確認ではなく変動）。【未確認】無料プラン生成物の商用利用可否（規約4.4は出力の商用利用を制限しないとする一方、料金表は Free の Commercial use を Not included とする）。無料枠の透かしの有無。添付2枚目のキャラクターターンアラウンド画像はツールUIも透かしもなく、Higgsfield 製かは確認できない。ポスト内の映像が実際に本製品で作られたかも未確認。【リスク】実在人物の顔・声を使う場合は本人の同意が必須（規約5.3）。個人プランは入力・出力がモデル学習に使われうる。18歳以上。モデル・機能は予告なく変更・廃止されうる。無料枠・Unlimited は自動化や再販が禁止。"
type: "link"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/Y0urDumble/status/2111542395695182003"]
fetched_at: "2026-11-08T07:41:00Z"
---

# Higgsfield — 画像・動画の複数モデルとAIペルソナ制作を1つにまとめた生成プラットフォーム

## 目的

- 複数の画像・動画生成モデルを1つのアカウントとクレジットで使えるクリエイティブ基盤。公式は「AI-native creative suite」とうたい、自社モデル（Soul、Genjutsu、DoP など）と外部モデル（Seedance、Kling、Veo、Wan、Nano Banana など）を同じ画面に並べている。
- この投稿の文脈では、架空の人物アカウントを作る工程を担う。人物の見た目は AI Influencer スタジオでメニューから組み立て、動きは Genjutsu が参照動画から転写する。撮影もプロンプト設計もせずに、同じ人物の縦動画を繰り返し出せる点が「ペルソナ量産」の実体。
- 本項目はプラットフォーム全体（モデル群、MCP/API、料金、権利条件）を扱う。AI Influencer と Genjutsu はこのプラットフォーム内の機能で、それぞれ専用の製品ページを持つ。

## 何ができるか

- AI Influencer（キャラクタースタジオ）: 19項目の設定（Character type は Average / Bold / Extreme、体型・顔・髪・アクセサリなど）で人物を作る。顔写真のアップロードは任意で、使うと顔の特徴を引き継ぐ。1回の生成でクローズアップのポートレートと全身カットが返る。作った人物は element として保存でき、Cinema Studio では @ でシーンに呼び出せる。
- Genjutsu（動きの転写）: 4〜30秒の参照動画から動き・カメラ・タイミングを取り出し、キャラクターに frame for frame で演じさせる Motion transfer と、商品・衣装・小道具だけを差し替える Objects swap の2モード。出力は 480p / 720p / 1080p、参照画像は最大30枚。Trending Genjutsu のフィードがフォーマット集として機能する。
- モデル群: 料金ページには Seedance 2.0 / 2.5、Kling 3.0 / 2.6、Veo 3.1、Wan 3.0、Hailuo 2.3、Nano Banana Pro、Soul 2.0、FLUX.2、GPT Image 2.6、Seedream 5.0 などが並び、動画は5秒あたり数クレジット〜100クレジット超まで価格差がある。
- API: api.higgsfield.ai の REST API で、モデルごとのエンドポイントに投げて request_id を受け取り、status_url をポーリングするか webhook で完了を受け取る。Python / TypeScript SDK があり、Genjutsu Motion transfer は POST https://api.higgsfield.ai/higgsfield/genjutsu/motion-transfer/v1.0。認証は API キーIDとシークレットのペア。
- MCP / CLI: 公式 MCP サーバー（https://mcp.higgsfield.ai/mcp）を Claude、Claude Code、ChatGPT、各種 MCP クライアントに追加すると、API キーなし（クライアント側 OAuth）で35以上のモデル・ツールを呼べる。CLI と ChatGPT プラグインも用意されている。
- 制限: プランの Unlimited と Free Generations は Web 上だけで、MCP / CLI / Canvas / Supercomputer からは使えない。新モデル・新機能は順次ロールアウトで、全ユーザーが同時に使えるとは限らない。生成物の保存は少なくとも7日で、それ以降は消える。

## 料金

- 無料: Free プランは「Limited use」でクレジットが付かず、使えるモデルも少数。ヘルプセンターは「You can generate without a paid plan, but access is limited to a small set of models and doesn't include credits.」と説明する。料金比較表では Free の商用利用は Not included。
- 有料: クレジット制の月額サブスク。2026-11-08 の料金ページ（年払い表示、30% OFF 中）は Starter 270 credits/月 $19、Plus 1,200 credits/月 $47（月払い $59）、Ultra 3,000 credits/月 $99（月払い $129）。2026-10-03 の公式ブログ表は Starter $15/月（月払い）、Plus $49/月（年払い $39/月）、Ultra $129/月（年払い $99/月）で、同じ公式内でも時期により金額とクレジット数が動く。税別、地域差あり。
- 消費: クレジットは生成ごとに減り、コストは実行前に Generate ボタンへ表示される。キャラクター1体は 1.12 credits（20 credits = $1 で約 $0.06）。動画はモデルと解像度で大きく変わり、例として Kling 3.0 720p が約7 credits/5秒、Seedance 2.0 1080p が約60 credits/5秒、Genjutsu Lite 1080p が5回分の無料枠という形で配布される。
- クレジットは毎月リセットされ繰り越せない。追加の Credit Pack と Auto-Refill があり、上位プランは並列生成数と Unlimited 対象モデルが増える。Unlimited は人間の個人利用向けで、自動化・資格情報の共有・再販は禁止。

## 登録の要否

- 要アカウント。メール等でサインアップし、18歳以上であることと利用規約への同意を求められる。支払いなしでも試せるが、クレジットが無いため本格的な動画生成には有料プランが必要。
- MCP を使う場合はクライアントに https://mcp.higgsfield.ai/mcp を追加して OAuth で接続する（API キー不要）。REST API を使う場合は console.higgsfield.ai で API キーを発行し、Key ID と Secret を Authorization ヘッダーに載せる。
- 権利: 規約 4.4 は入力・出力の所有権を主張せず、出力の商用利用を制限しない。解約後も出力の権利は残り、顧客への再許諾も可能。ただし実在人物の顔・声を入れる場合は本人の同意が必要で、個人認証目的の利用や生体テンプレートの入力は禁止。個人プランでは入力・出力がモデル学習に使われうる（Enterprise は対象外）。

## 変更履歴

- 2026-11-08: 初回登録
