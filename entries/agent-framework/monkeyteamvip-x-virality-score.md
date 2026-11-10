---
repo: "monkeyteamvip/x-virality-score"
name: "X Virality Score"
genre: "agent-framework"
url: "https://github.com/monkeyteamvip/x-virality-score"
license: "MIT"
stars: 35
language: "HTML"
created: "2026-09-16"
updated: "2026-10-27"
forks: 19
open_issues: 0
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 26
size_kb: 7915
archived: false
author: "kiosa / @thegreatest_sv（commits と ARTICLE.md のハンドル表記で確認）"
flags: ["unverified"]
risk_notes: "①主張と実測の差: 投稿は「1投稿あたり10万インプレッション」「月500万ビュー」を掲げるが、これは著者の主張で、著者自身が返信で「100K views を保証しない実験的ツール」と訂正している。返信には直近15投稿が2K〜47Kだったという反論と、コミュニティノート相当の指摘（実験的な手動ツール、公開ボードはプレースホルダーの静的デモ）が付いている。②著者の公開ボード data.json（2026-11-08分、2026-11-09 11:05 MSK 更新）では、本人のベスト投稿は21,377 views、当日合計26,146 views、ウォッチリスト29人中7位。少なくともこの日の実績は「10万/投稿」と一致しない。③引用元の X 記事（x.com/i/article/2100215736375373824）はログイン必須で、curl ではログイン画面へリダイレクトされ本文・配布条件を確認できない。④リポジトリ内 ARTICLE.md は「1投稿 約2.08M views」を挙げるが単発の事例で、ツールによる効果の測定ではない。同ファイルに「This is experimental. No big promise.」「Demo / case-study board (this article's example — not yours by default)」と明記がある。⑤返信に添付された画像はインプレッションのスクリーンショットではなく、とんがり帽子で座る男性の風刺イラストだった（vision で確認、数値・UIなし）。インプレッション主張の裏付けにならない。⑥投稿のプロモ動画は UI のアニメーションで、「VIRAL VIEWS 1,052,489」「2.08M views」等は演出上の数値であり実測ではない。実際の画面かと問われた著者も「It's on the experimental stage now」と答えており、動画を実装済みUIの証拠にはできない。⑦コミュニティノートの「公開ボードはプレースホルダーの静的デモ」という記述は、公開ボードが実際に26件のヒット（5,295〜147,225 views）を含む data.json を読むため、そのままは確認できなかった（ノート側の記述が不正確）。ただしページ自体は静的で、事業者が再公開するまで更新されない。⑧料金・提供条件: リポジトリは MIT で無料だが、X の閲覧/API 条件、Grok Bot マーケットプレイスの提供条件・レート制限は未確認。⑨再現性: サンプルは架空データで、pipeline/ は X を呼ばない。実データ取得は利用者の X セッションかボットの読み取りツールに依存し、取得失敗は stale として残る（2026-11-09 11:00 MSK の refresh では19件が stale）。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114419470693507261"]
fetched_at: "2026-11-09T21:33:55Z"
last_release: "v8.0.0"
last_release_at: "2026-10-27"
---

# X Virality Score — Grok Bot と Python で毎朝のX投稿ネタを組み立てる無料テンプレート

## 出来ること

- ウォッチリスト（15〜30アカウント、フォロワー5万くらいまでが目安）の前日オリジナル投稿を views 床で抽出する。既定は5,000 views 以上、10,000 以上に星。返信は除外。自引用は数字には含めるがバッジ付きで区別する。
- 直近24時間のキーワード表（検索語ごとに最大25投稿のサンプル、前24時間との比較）と、ヒット投稿から抽出した型のブリーフ（コールドオープン、番号付きリスト、固有名詞のツール、ソフトCTA）を作る。
- トップ10投稿の英語リライト草案を、型のブリーフから生成する。事実は変えず新しい数字は足さない、原文の語句は使わない、という方針。各草案に短い動画 Tip が付く。
- 投稿アイデア5〜8件（各ビジュアル付き）と記事アイデア2〜3件を出す。
- ウォッチリスト外の直近48時間の約20投稿（outsiders）を同じキーワード処理にかけ、リスト外の「今日の空気」を別枠で見せる。
- GitHub Pages で配信する静的ボード（X Score、Day Target、DONE / NOT DONE、デイリー順位、フォロワー増減、TOP10 草案、パターン層）。
- 実行経路は2つ: Grok Bot（マーケットプレイス）経由か、Python スクリプト単体。AI から使える形は「ローカル CLI（pipeline/run_day.sh）+ Grok Bot の読み取り専用Xツール」で、MCP サーバや公開 API は無い。投稿・いいね・返信は自分でやる前提で、ボットは代行しない。

## 目的・背景

- 毎朝「今日は何を書くか」をゼロから決めるコストを下げるための個人用デスク。前日伸びた投稿 → 型 → 草案、の順で判断材料を昼前に揃える。
- 著者は @thegreatest_sv（リポジトリ内 ARTICLE.md にハンドル表記、コミットも kiosa 名義）。ARTICLE.md は「experimental. No big promise.」と位置づけ、初心者が流行を追うための小さな机だと説明している。
- 投稿がうたう「100k impressions / 月5M views」は主張で、公開ボードの実データ（2026-11-08: 本人ベスト21,377 views）とは一致しない。導入判断は「他人の伸びた投稿を毎朝棚卸しする仕組み」として見るのが妥当。
- 設計上、収集と配信は分離されている。pipeline/ は X を呼ばず、生JSONを受け取ってボードと ping を作るだけ。取得は自分の X セッションかボットの読み取りツールに任せる。

## 依存関係

- Python 3（README の要件はこれだけ）。ボードは board/index.html と board/data.json の2ファイルで、ビルド工程は無い。
- GitHub アカウント（fork か template、GitHub Pages）と X アカウント（読み取り用セッション、または Grok Bot の読み取り専用Xツール）。
- Grok Bot を使う場合はマーケットプレイスから追加（https://x.ai/bot/BIvSSU3sukmkTpMeSnft- は HTTP 200 を確認）。追加条件・料金は未確認。
- config/watchlist.json と board/data.json は .gitignore 対象。ウォッチリストと生ダイジェストを公開しないため、ボードは別の公開リポジトリに置く構成が推奨されている。

## 実行条件

- ネットワーク: ボード配信に GitHub Pages、データ取得に X への読み取りアクセスが必要。pipeline/ 自体はネットワークを要さない（入力JSONのみ）。
- 5分のオフライン確認: clone → bash scripts/smoke_day.sh → board/.smoke-preview を python3 -m http.server 8765 で配信。サンプルは架空データで、X アカウントも不要。
- 想定規模: ウォッチリスト15〜30件、outsiders 約20件/48時間、キーワードは検索語あたり最大25件のサンプル。公開ボードの data.json は実測で約535KB（ヒット26件）。
- 取得失敗は stale として残り、そのままボードに出る（2026-11-09 11:00 MSK の refresh では2,852件要求・2,833件更新・19件 stale）。数字は「その時点のスナップショット」であって保証値ではない。
- X 側の閲覧条件（レート制限、ログイン状態、API 利用可否）は未確認。記事本文も X ログイン必須で読めなかった。

## 最短手順

- https://github.com/monkeyteamvip/x-virality-score を fork するか clone する。
- bash scripts/smoke_day.sh を実行し、board/.smoke-preview を 8765 番で配信してダミーボード（@your_handle、X Score、Day Target）を確認する。
- cp config/watchlist.example.json config/watchlist.json、cp board/data.example.json board/data.json。brand_handle、operator、timezone、min_views / star_views、board_url を自分の値にする。
- board/index.html と data.json を別の公開リポジトリ直下に置き、Settings → Pages → Deploy from branch（main / root）で公開する。URL は https://<user>.github.io/<repo>/。
- Grok Bot に AGENTS.md を読ませる（初回に handle・TZ・床値・ウォッチリストを聞き、勝手にアカウントを作らない）か、自分で digests/<日付>/ に生JSONを置いて pipeline/run_day.sh を回す。
- ボードの X Score / Day Target / TOP10 草案を見て1本選び、自分の声に直して手動で投稿する。2本目は余力があれば。

## 変更履歴

- 2026-11-09: 初回登録
