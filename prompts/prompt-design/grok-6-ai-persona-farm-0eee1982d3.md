---
type: "prompt"
name: "Grok 6ボットで回すAIペルソナ農場（Persona Farm）構築プロンプト"
genre: "prompt-design"
url: "https://x.com/Y0urDumble/status/2112617746987098248"
author: "@Y0urDumble"
source_post: "https://x.com/Y0urDumble/status/2112617746987098248"
sources: ["https://x.com/Y0urDumble/status/2112617742427623707"]
first_seen: "2026-10-20"
added: "2026-11-08"
target: "Grok / xAI"
transcribed_from: "image"
prompt_sha1: "0eee1982d3484e2f4694dfe24626039a126a3fcc"
flags: ["unverified"]
risk_notes: "投稿の数値（16,286フォロワー/45本/391返信/$1,386）は本人のデモ動画（day 11/14・15,201フォロワー・40本・3/5トークン・$1,050・画面に illustrative）とも一致せず第三者検証なし。5体のペルソナ実アカウントと $GUS/$OTIS/$LARS のペルソナ由来トークンは未確認（同名の無関係トークンと Otis 株のみ）。自動投稿・大量返信・トークン発行を指示する内容で、各SNSの規約と暗号資産規制に触れ得る。"
fetched_at: "2026-11-08T08:52:03Z"
---

# Grok 6ボットで回すAIペルソナ農場（Persona Farm）構築プロンプト

## 目的

- Grok を「24時間動くAIキャラクタースタジオのリードエンジニア」として動かし、5体のAIインフルエンサーを運用する仕組みを一式コードで作らせるプロンプト。SCOUT（トレンド探索）/ CASTER（ペルソナ定義）/ DIRECTOR（8秒・9:16動画の生成）/ POSTER（投稿）/ FARMER（コメント返信）/ LAUNCHER（2,500フォロワーでトークン発行）の6モジュールに加え、farm.md とペルソナファイル、状態管理用SQLite、cron、launch gate、運用ダッシュボードまでを Node.js + TypeScript の1リポジトリとして実装させ、day 1 は dry-run で止めさせる。

## 前提

- - Grok（xAI）のチャットに貼る想定。画像はプロンプトプレビュー画面のスクリーンショットで、右上の「Copy prompt」はUIのボタンであり、本文には含めていない。
- 生成物の実行には Node.js、xAI API キー、X と TikTok の公式アップロードAPIのキー、トークン発行に使う暗号資産ウォレットが必要と本文に書かれている（キーは `.env` から読む）。
- 画像からの文字起こし（`transcribed_from: image`）。改行は画像の折り返し位置に合わせ、語句の追加・修正はしていない。
- 5体のペルソナ名・トークン名はプロンプト内では固定されておらず、`/personas` と実装時に生成される。

## プロンプト本文

```
<prompt>

<role> You are Grok, running as the lead engineer of a 24/7 AI character studio. You do not just write posts,
you design, build, and operate the whole system end to end: six Grok bots that cast, film, post, and grow AI
influencers, plus a live control dashboard the operator watches. You write real, runnable code. </role>

<mission> Ship a working studio that launches 5 AI influencers on day 1. Each one posts one 8 second 9:16 video
a day, talks to its audience in its own voice, and gets a token on its own narrative only after it earns 2,500
real followers. The operator only approves the gates. </mission>

<stack> Node.js with TypeScript, SQLite for state, a cron scheduler for the loops, the xAI API for every bot
call, Grok Imagine for the video renders, and the official X and TikTok upload APIs with the operator's own keys
from a .env file. One repo, one command to start: npm run farm. </stack>

<farm_md> Create farm.md plus one file per persona in /personas. Each file locks the name, handle, look written
so every render is the same face, voice, 12 behavioral traits, niche, banned topics, and posting time. Every bot
re-reads its persona file at the start of every loop, so the character never drifts. </farm_md>

<bot_line> Build six bots as separate modules in /bots. SCOUT ranks trends by views, 72 hour growth, and whether
a creator already owns the format. CASTER writes a new persona file for an open trend. DIRECTOR renders one 8s
video per persona per day. POSTER uploads it on schedule. FARMER replies to comments in the persona's voice.
LAUNCHER watches the follower count and opens the launch gate at 2,500. </bot_line>

<dashboard> Build a single page dashboard in /dashboard, dark theme, monospace, wireframe panels with corner
markers. Top row: followers, videos, tokens live, creator fees, replies. Left panel: farm.md with the cost per
video. Center: the six bots on a moving line, each one lights up when it acts, with the current job under it.
Below: 5 persona cards with follower count, progress to 2,500 and a sparkline, then 5 token cards with bonding
progress and fees. Bottom: launch gate, cost vs a $45 freelancer per video, and a live session log. Stream every
event to it over a websocket. </dashboard>

<launch_gate> Hold every token behind a hard gate in code: 2,500 real followers, 14 videos posted, and a manual
sign-off where the operator signs the launch from their own wallet. The bot never signs, never buys, and never
shills the token in replies. The token page states it belongs to an AI character and promises nothing. Fees
split across the configured wallets. </launch_gate>

<guardrails> Every upload carries the platform's AI-generated label and an "AI character" line in the bio. No
real person's face, name, or voice, no imitation of existing creators, no fake accounts, no bought followers, no
fake engagement. If a commenter asks, the character says it is AI. A kill switch per persona, checked before
every upload. </guardrails>

<cost_model> Log the cost of every call: render, caption, post, and replies, rolled up to a cost per video. Show
it on the dashboard next to the freelancer baseline. Never estimate silently, label every estimate.
</cost_model>

<nightly_review> Every night, review each persona: views, follow rate, reply sentiment, and cost per video.
Rewrite the persona file where it drifts, retire formats that stopped working, and pause any persona a platform
flags. </nightly_review>

<output> Deliver the full repo: farm.md, the 5 persona files, the six bot modules, the scheduler, the launch
gate, the dashboard, the .env.example, and a README with setup steps. Then run day 1 in dry-run mode and show me
the dashboard before anything posts. </output>

<final_check> Before going live, challenge yourself. Is every video labeled as AI? Could anyone mistake a
persona for a real person? Is any gate decided by a bot instead of code? Does the studio survive an API outage
or a platform policy change? End with a section titled "WHAT COULD GO WRONG?" </final_check>

</prompt>
```

## 使い方

- 1. Grok のチャットにプロンプト本文をそのまま貼る。farm.md、5つのペルソナファイル、6ボットのモジュール、スケジューラ、launch gate、ダッシュボード、`.env.example`、README が返る想定。
2. 返ってきたリポジトリをローカルに置き、`.env` に自分の API キーとウォレット設定を入れる（本文は `npm run farm` の一発起動を想定）。
3. 本文の指示どおり、day 1 は dry-run でダッシュボードだけを確認し、投稿は行わない。
4. 実際に動かす前に、X・TikTok の自動化ポリシーと、暗号資産の販売・勧誘に関する法令を確認する（下記「注意点」）。

## 注意点

- - **数値は達成記録ではない。** 投稿は「day 12 で16,286フォロワー / 45本 / 391返信 / $1,386」と主張するが、同じ投稿に添付された本人のデモ動画は day 03→11/14、フォロワー15,201、動画40本、トークン3/5、fees $1,050 で、画面に `illustrative`（説明用の見本）と明記されている。投稿の数字はデモの最終表示とも一致せず、第三者による検証もない。
- **ペルソナの実アカウントは未確認。** デモ内のハンドルは `@uncle.gus` `@otis.oldmoney` `@Lars.bowlcut` の形式（ドット入り）で、X のハンドルとしては成立しない。X 検索でも Uncle Gus / Otis / Lars / Dexter / Rocco に対応する運用アカウントは見つからず、TikTok は WAF で直接確認できなかった。
- **トークンは未確認。** `$GUS` `$OTIS` `$LARS` を調べると、pump.fun の猫・蛙系ミームコインや上場企業 Otis（エレベーター）など無関係な同名資産だけが見つかり、AIペルソナの物語に紐づくトークンは確認できなかった（pump.fun の検索APIは Cloudflare で直接照会できず）。
- **コスト $0.38/本は設計値。** デモの内訳は render $0.31 + caption $0.01 + post $0.00 + replies $0.06 = $0.38 で、実測の請求額ではない。$45/本のフリーランス比較も本文中の前提値。
- **規約・法務リスク。** 自動投稿と人格を装った大量返信はプラットフォームの自動化・スパム規定に触れ得る。2,500フォロワー到達でミームコインを発行する設計は、暗号資産の販売・勧誘に関する各国の規制対象になり得る。本文自身が AI ラベルやなりすまし禁止などのガードレールを置いているが、順守を保証するものではない。
- 本項目は指示文の記録であり、実行・運用を推奨するものではない。

## 変更履歴

- 2026-11-08: 初回登録
