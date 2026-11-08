---
name: "AIペルソナの複製実演：上位動画12本を「8特性ゲノム」に分解し、双子アカウントを毎日投稿させる（@Y0urDumble）"
genre: "video-gen"
url: "https://x.com/Y0urDumble/status/2112288114073067862"
published: "2026-10-19"
author: "@Y0urDumble (Dumble)"
source_post: "https://x.com/Y0urDumble/status/2112288114073067862"
sources: ["https://x.com/Y0urDumble/status/2109342020921659784", "https://x.com/i/article/2109318233866006528", "https://www.tiktok.com/@john_stockman", "https://x.com/karpathy/status/2039805659525644595", "https://x.com/Y0urDumble/status/2112288114073067862"]
first_seen: "2026-11-08"
added: "2026-11-08"
type: "article"
flags: ["unverified", "low-quality"]
risk_notes: "主張と確認結果: (1) 8,912フォロワー・94.2%顔一致・$55・Day1→7の再生遷移は、動画内の自作ダッシュボード（TWIN LAB / dead internet test 01）のKPI表示が唯一の出所で、外部計測も第三者検証もない。画面のKPIは 336,935 / 12-56 / 8-8 / 94.2% / 8,912 と進行し、フッターは『spend $55 / week · humans in loop 0』で、本文の『$55 spent』とは単位が食い違う。(2) 双子アカウント @not_john.exe はX・TikTokのいずれでも発見できず、8,912フォロワーの受け皿を確認できない。(3) 元ネタのTikTok @john_stockman は実在し、bioに『Ai Influencer』と明記、2026-11-08時点のミラー集計で416.9Kフォロワー/11.01M likes/85本。投稿の336,935・8.75M likesは10/19時点のスナップショットとして整合的だが、『上位12本が10.6M〜232.8K』は確認できず（ミラーで見える直近20本は0.1〜1.23M）。(4) Karpathyの元ポストは実在（2026-04-02、現在22.0M views）で内容も一致するが、本人は16M viewsとは書いておらず、人物の複製は想定していない。(5) クローラのコード・配布物は無く（GitHubに著者アカウント無し、該当リポジトリ0件）、手順の実物は2026-10-11の記事にあるHiggsfield AI Influencer＋Genjutsuの操作と、自前スクリプトの説明に留まる。(6) 実在アカウントの動画・音源・顔を読み取り複製する行為は、TikTokのなりすまし/著作権ポリシー、音源権利、各プラットフォームのAI生成表示義務の確認が必要で、著者自身も記事でAI表示を推奨している。"
fetched_at: "2026-11-08T08:45:00Z"
---

# AIペルソナの複製実演：上位動画12本を「8特性ゲノム」に分解し、双子アカウントを毎日投稿させる（@Y0urDumble, 2026-10-19）

## テーマ

- - 2026年10月19日、@Y0urDumble（Dumble）が「AIインフルエンサーをクロールして双子を作り、8,912人がコピーをフォローした」と主張する24秒のデモ動画つきポスト。対象はTikTokのAIペルソナ @john_stockman（紫の前髪、ガソリンスタンドのSupra、深夜のジャンプスタイル）。
- 提示されているのは生成モデルの操作手順ではなく、**既存の当たりアカウントを「読んで」複製する逆算の型**。上位動画を再生数順に読み、ヒット要因を8つの特性（サウンド／キャプション／ドロップ／ファンダム／ビット／タグ／コラボ／ムーブ）に分解し、その特性から別キャラクターを組み立てて毎日投稿させる、という筋立て。
- ビルド側の具体手順（Higgsfield AI Influencer でキャラ生成 → 三面図シートで顔を固定 → Genjutsu でモーション転送 → 1日1本以上投稿）は、著者が引用している2026年10月11日のX Article にまとまっている。本ポストはその手順に「元アカウントの分析」を前置きした位置づけ。
- 引用元はAndrej Karpathyの「LLM Knowledge Bases」（2026-04-02）。`raw/` に資料を溜め、LLMにwikiを編纂させ、Obsidianで読むという知識管理の話で、著者はこれを「人物の観察」に流用したと述べる。
- クローラ本体のコード・リポジトリ・有料配布物は確認できない。読者が持ち帰れるのは、分析の観点（何が再生を生んだかを言語化する）と、プロフィール設計の進め方。

## 著者の主張

- - John の上位12本（10.6M再生から232.8Kまで）を1本ずつクロールする。動画はダウンロードせず、「なぜ当たったか」だけを読む。8本目で顔が判別でき、12本で顔が完成する。
- 抽出される特性は8つ。10.6Mの動画は Rae Sremmurd「No Type」、9.5Mの動画はキャプション無し、ほぼ毎回 #emo と #loganpaul、他にスプーキーなドロップ、#fnaf とのクロスオーバー、シャンプー案件のジョーク、絵文字少女とのコラボ、片足ジャンプスタイル。
- Claude Code がこの8特性から双子を構築し、顔が元と **94.2%** 一致する。
- 双子は1日1本投稿。Day1 1,240再生 → Day3 41,600 → Day4 FYPに載り212,400 → Day7 551,770再生・8,912フォロワー。費用 **$55**、人手ゼロ。
- 「FYPの半分はもうこうやって動いている」「毎日1つAIアカウントを解体する」としてフォローを促す。
- 引用元の記事側では、Higgsfield Starter 月$15（キャラ1体 約$0.06、無料枠あり）、ChatGPT Plus 月$20、Kling Motion Control を代替に挙げ、収益は動画単体ではなくミームコイン手数料・ブランド案件・アフィリエイトからと説明している。

## 裏取り・注意点

- - **動画の実体**: 添付mp4は24.15秒・1080x1350。1〜23.5秒からフレームを抜いて確認すると、画面は「TWIN LAB / dead internet test 01」と題した自作ダッシュボード風の演出で、`~/twin-lab $ claude --crawl @john_stockman --build twin-01 --post daily` の入力行、CRAWL FEED（`#01 10.6M` / `#02 9.5M` / `#03 4.9M` / `#04 1.5M` / `#05 631K` …）、GENOME（SOUND 1.00 / CAPTION .40 / DROP .20 / FANDOM .16 / BIT .06 / TAGS .05 / COLLAB .04 / MOVE .02）、`TWIN-01 · @not_john.exe queued` が並ぶ。KPIは 336,935 / 12/56 / 8/8 / 94.2% / 8,912 と進み、フッターは「spend $55 / week · humans in loop 0」。実ターミナルの録画か演出かは判別できないが、**数字はすべて本人が作った画面の表示**で、外部計測ではない。
- **本文と画面の不一致**: 本文は「$55 spent」（総額）、画面は「$55 / week」（週額）。内訳（Claude Code の利用料、Higgsfield のクレジット、API代）は提示されていない。
- **双子アカウントが確認できない**: 画面の `@not_john.exe` はXでもTikTokでも発見できず、8,912フォロワーの受け皿を外部から確認できない。8,912 は画面KPIのみ。
- **元ネタは実在する**: TikTok @john_stockman は実在し、bioに「Ai Influencer」と案件用メール、85本の動画。2026-11-08時点の第三者ミラー集計で 416.9Kフォロワー / 11.01M likes / 平均57.1万再生。投稿の336,935フォロワー・8.75M likes は10/19時点のスナップショットとして整合的で、その後 386.5K（10/26頃）→416.9K（11/08）と単調に増えている。
- **未確認**: 「上位12本が10.6M〜232.8K」。ミラーで見える直近20本は 0.1〜1.23M で、10.6Mの動画は特定できていない。平均57万再生×85本＝約4,900万再生なので裾の厚い分布自体は否定できないが、順位と本数は裏取れていない。
- **Karpathy の引用**: 元ポスト「LLM Knowledge Bases」は実在（2026-04-02、現在22.0M views / 61K likes）。内容（`raw/` に資料→LLMがmdのwikiを編纂→Obsidianで閲覧→Q&Aとlint）も著者の要約と一致する。ただし本人は「16M views」とは書いておらず、人物やペルソナの複製は想定していない。著者の「同じロジック」は比喩で、手法の同一性は主張にすぎない。
- **コードが無い**: GitHubに著者アカウント（Y0urDumble）は存在せず、「ai influencer clone crawler」に該当するリポジトリも0件。クローラは再現物がなく、手順は「分析の観点」と記事側のHiggsfield操作に留まる。再現するには自前でスクレイピングと生成を組む必要がある。
- **権利・規約**: 実在アカウントの動画内容・音源・顔を読み取り、別アカウントで再現する行為は、TikTokのなりすまし（impersonation）ポリシー、著作権・肖像、音源ライセンス、各プラットフォームのAI生成コンテンツ表示義務の確認が必要。記事も「AI生成であることを明示せよ」と書いており、参照元の音源は「トレンド音源を使え」で権利を解決していない。
- **位置づけ**: 同じ著者の10月11日記事（Higgsfield AI Influencer＋Genjutsuの6ステップ、Starter $15/月）と10月16日の「家族で増やす」プレイブックの続編。新規なのは「上位動画のヒット要因を特性に分解してから作る」という前置きの型で、生成手順そのものは既存記事の範囲を出ない。

## 出典

- - 投稿（動画つき）: https://x.com/Y0urDumble/status/2112288114073067862 （2026-10-19T21:01:45Z、@Y0urDumble）
- 引用元の記事: https://x.com/i/article/2109318233866006528 （公開 2026-10-11T17:55:02Z、同著者。本文は投稿 https://x.com/Y0urDumble/status/2109342020921659784 経由で取得）
- 元ネタのAIペルソナ: https://www.tiktok.com/@john_stockman （bio「Ai Influencer」。数値はミラー https://urlebird.com/user/john_stockman/ の2026-11-08時点の集計）
- Andrej Karpathy「LLM Knowledge Bases」: https://x.com/karpathy/status/2039805659525644595 （2026-04-02）
- Higgsfield 料金: https://higgsfield.ai/pricing
- Higgsfield AI Influencer: https://higgsfield.ai/ai-influencer
- Higgsfield Genjutsu ヘルプ: https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-genjutsu
- TikTok なりすましポリシー: https://support.tiktok.com/en/using-tiktok/following-and-engaging-with-people/impersonation

## 変更履歴

- 2026-11-08: 初回登録

## 変更履歴

- 2026-11-08: 初回登録
