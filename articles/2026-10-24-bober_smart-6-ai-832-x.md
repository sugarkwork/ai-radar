---
name: "6つのAIツールを統合して就寝中に$832稼いだというX投稿（動画付き）"
genre: "article"
url: "https://x.com/Bober_smart/status/2114064355729740136"
published: "2026-10-24"
author: "@Bober_smart"
type: "article"
source_post: "https://x.com/Bober_smart/status/2114064355729740136"
sources: ["https://x.com/Bober_smart/status/2114064355729740136", "https://video.twimg.com/amplify_video/2114064304597078016/vid/avc1/1080x1350/HaNjirb46bcI1i8h.mp4?tag=29", "https://x.com/i/article/2078778232250183680", "https://threadnavigator.com/thread/2078784709253841039/", "https://api.github.com/repos/morluto/rea", "https://typesafe.ai/blog/introducing-system-one-models-and-jev", "https://www.anthropic.com/claude-opus-5-5", "https://openai.com/index/introducing-dots", "https://docs.x.ai/grok-bot/overview"]
first_seen: "2026-10-24"
added: "2026-11-09"
fetched_at: "2026-11-09T13:03:00Z"
flags: ["unverified", "low-quality"]
risk_notes: "【主張】6つのツール（Opus 5.5 / REA / Jev / Dots / Grok Bot / Obsidian）を統合し、就寝中に配送ドライバー向けの収益管理アプリを自動構築。243登録・31有料×$9=$832、費用はAPI $5.10＋ドメイン$4=$9.10で91倍、$15の上限で$55のドメインを回避した、と投稿は述べる。【確認できた】①投稿の実体（2026-10-24T18:39:54Z、likes 1,087 / views 130,279 / bookmarks 1,579、本文に外部URLは0件）。②動画の実体（HTTP 200、25,805,564 bytes、19.95秒、1080x1350・60fps、カットは3/9/12/18秒の4箇所）。③6ツールの実在：Claude Opus 5.5 は Anthropic が2026-09-22に公開（$4/$20 per MTok）、REA は morluto/rea（MIT、リバースエンジニアリング用MCP）、Jev は TypeSafe AI の System One モデル、Dots は OpenAI の常駐エージェント（2026-09-29）、Grok Bot は xAI の常駐Bot、Obsidian は実在のノートアプリ。【誤り・矛盾】①収益の算数が合わない：31人×$9＝$279で、$832には約92人の有料会員が必要。②著者自身の動画が$832を否定している：全フレームでヘッダーは REVENUE $279 / SIGNUPS 212 / PAID 31 / COST $7.70・36x で、$832はどこにも表示されない。登録者数も243ではなく212、コストも$9.10ではなく$7.70、予算上限も$15ではなく$10、ドメインも$4ではなく$3。③Jevの役割が製品仕様と正反対：Jevは文字列を生成しない意思決定モデルで、コードを書いたり「概念を実行」したりはできない。返信欄でも複数人が同じ点を問いただしている。④REAは「任意の主題を4分で深掘り」する調査ツールではなく、アプリやバイナリのリバースエンジニアリング用MCP。⑤DotsはOpenAIの常駐エージェントで、ChatGPT Pro / Business Premium が前提。「6つを1つのワークフローに織り込む」ツールではない。⑥成果物の証拠が無い：製品名・URL・コード・決済画面が無く、動画にもURLは1つも写らない。最終フレームは「1 live app • 6 lines of glue code」という演出。⑦引用記事は「Claude Second Brain & Folder Workflow: The Complete Guide」（2026-07-19）で、内容はMarkdownフォルダ＋CLAUDE.mdの索引運用。むしろ「Obsidianは不要」と明記しており、Obsidianに1,260 recordsを貯めたという本投稿の主張と噛み合わない。【未確認】アプリの実在、収益・登録・決済の実績、動画が実画面か（演出と判断）、$5.10のAPI費用の内訳、Obsidianの記録件数。返信欄では「31 x $9 = $279, not $832」「Jev writes code now?」「This is AI-generated fiction.」「This didn’t happen」などと批判され、取得できた範囲に著者の反論・説明は無い。本項目は主張の記録としてのみ扱い、実績値や再現手順として引用しないこと。"
---

# 6つのAIツールを統合して就寝中に$832稼いだというX投稿——動画は$279と表示

## テーマ

- 2026-10-24 の @Bober_smart の投稿。Claude Opus 5.5、REA、Jev、Dots、Grok Bot、Obsidian の6つを1つの系に統合し、人間が寝ている7時間で「配送ドライバーの収益管理アプリ」を市場調査から公開まで自動で作り、$832を稼いだと主張する。
- 添付は20秒の動画1本のみ。製品名・URL・コード・設定ファイル・料金ページは投稿にも動画にも無く、引用先は同著者のX記事（ログイン必須）1本。読者がそのまま再現できる手順は示されていない。
- 6つの名前はすべて実在する製品・モデルだが、投稿が与えている役割は実際の機能と一致しない。とくにJev（決定モデル）にコード生成をさせ、REA（リバースエンジニアリング用MCP）に市場調査をさせている点が構図の中心にある。

## 著者の主張

- 役割分担：Opus 5.5が設計する「頭脳」、Grok BotがXを24時間監視、REAが任意の主題を4分で深掘り、Jevが概念を自律実行、Dotsが6つを1つのワークフローに編み、Obsidianが1,260件を無損失で保管する。
- 一晩の進行（著者の記述）：23:40就寝 → 0:12にGrok Botが配送ドライバーの不満投稿1,900件を発見 → 1:05にREAが競合14件（最安$19/月）を調査 → 2:30にOpus 5.5が9画面・DB1つの設計を質問ゼロで作成 → 4:10にJevが実装・デプロイ・LP作成 → 5:45にDotsが30秒のプロモ動画と3つのフォーラム投稿を生成 → 7:20にObsidianが全記録を保存。
- 成果：「目覚めたら243登録・31有料（各$9）で$832」。費用はAPI $5.10＋ドメイン$4＝$9.10で91倍のリターン。Jevが$55のドメインを買おうとしたが$15の上限に当たり$4の代替を選んだ、という「自制」の逸話付き。
- 主張の核はツールではなく運用論：「AIに答えを求めるのが間違い。明確な目的・厳しい期限・金銭の上限を与えればよい」。コードは1行も書かず、ブラウザも開いていないと締める。

## 裏取り・注意点

- 投稿の実測（2026-11-09取得）：2026-10-24T18:39:54Z、likes 1,087 / views 130,279 / bookmarks 1,579 / replies 123。本文に外部URLは0件。動画はHTTP 200・25,805,564 bytes・19.95秒・1080x1350/60fpsで、カットは3/9/12/18秒の4箇所。
- 動画は実画面の録画ではなく、グレースケールの演出過多なダッシュボード（「MERGED AI SETUP」）。6ツールのアイコン、放射状の網絡図、`run night-shift --tools 6 --budget $10` の端末行、6枚のメトリクスパネルで構成される。
- その動画のヘッダーは全フレームで REVENUE $279 / SIGNUPS 212 / PAID 31 / COST $7.70・36x。$832は一度も出てこない。登録者数は243ではなく212、予算上限は$15ではなく$10、ドメインは$4ではなく$3、Obsidianは1,260件ではなく1,240 notes。動画の数字は投稿本文と一致せず、投稿に合わせて後から作られた演出とみられる。
- 算数：31人×$9＝$279。$832には約92人の有料会員が必要で、投稿自身の数字と矛盾する。返信欄でも「31 x $9 = $279, not $832」と複数人が指摘している。
- Jev（TypeSafe AI）は文字列を生成しない「System One」モデルで、事前に定義した選択肢から型付きの確率的意思決定を返すだけ。コードを書くことも「概念を実行」することもできない。公式ブログは「While Jev gives up string generation」と明記している。返信欄でも「Jevはただの決定エンジンでは？」「どうやってJevでコードを書いたのか」と繰り返し問われている。
- REA（morluto/rea、MIT、2026-04-14作成、stars 445,560）は、エージェントにGhidra/IDA/Hopper等を接続してアプリやバイナリを解析・再実装させるMCP。任意の主題を4分で調査するツールではない。DotsはOpenAIの常駐エージェント（2026-09-29、ChatGPT Pro/Business Premium向け）で、6ツールを編む接着剤ではない。Grok BotとObsidianは実在し、X監視・Markdown保管という役割は妥当。Opus 5.5も実在（2026-09-22公開、$4/$20 per MTok）。
- 成果物の証拠が無い：アプリ名・ドメイン・コード・登録画面・決済の記録が一切なく、動画にもURLは1つも写らない。最終フレームは「1 live app • 6 lines of glue code」という字幕で、実装の実体を示していない。著者のGitHub（Bobersmart、公開6リポジトリ）にも該当アプリは無い。
- 引用記事の実体：t.co は X Article 2078778232250183680 に解決するが、未ログインではログイン画面へリダイレクトされ本文を取得できない。ミラーで確認できるタイトルは「Claude Second Brain & Folder Workflow: The Complete Guide」（2026-07-19）。内容はMarkdownフォルダ＋CLAUDE.mdの索引運用で、むしろ「Obsidianは不要」と書いており、本投稿のObsidian収蔵庫の主張とは無関係。
- 返信欄の評価：算数とJevの能力を突く指摘が複数（jpkinca、Sevarojl、EastDallasBB、zamoth22、NexusAnarchy、mdowney、Coinosphere）。「AI-generated fiction」「This didn’t happen」「complete BS」といった批判もある一方、称賛・質問も多く、著者は質問に実質回答していない。$5.10というAPI費用の内訳も未確認（Opus 5.5の入力$4/MTokで単純換算すると約1.28M入力トークン相当）。

## 出典

- 投稿: https://x.com/Bober_smart/status/2114064355729740136 （2026-10-24）
- 動画: https://video.twimg.com/amplify_video/2114064304597078016/vid/avc1/1080x1350/HaNjirb46bcI1i8h.mp4?tag=29
- 引用記事: https://x.com/i/article/2078778232250183680 （ログイン必須。タイトルはミラー https://threadnavigator.com/thread/2078784709253841039/ で確認）
- Claude Opus 5.5: https://www.anthropic.com/claude-opus-5-5 （2026-09-22）
- Jev: https://typesafe.ai/blog/introducing-system-one-models-and-jev （2026-09-15）
- REA: https://github.com/morluto/rea / https://api.github.com/repos/morluto/rea
- Dots: https://openai.com/index/introducing-dots （2026-09-29）
- Grok Bot: https://docs.x.ai/grok-bot/overview

## 変更履歴

- 2026-11-09: 初回登録
