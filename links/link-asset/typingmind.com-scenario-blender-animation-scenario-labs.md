---
name: "Scenario Blender Animation（scenario-labs）"
genre: "link-asset"
url: "https://www.typingmind.com/skills/scenario-labs-scenario-blender-animation"
author: "scenario-labs（Scenario）"
pricing: "free"
pricing_detail: "スキルは MIT・無料（GitHub: scenario-labs/skills）。TypingMind への取り込みも無料で、かかるのは自前 API キーのトークン代のみ。TypingMind アプリ本体は買い切りライセンス制（金額は未確認）。"
signup_required: true
flags: ["unverified"]
risk_notes: "TypingMind 経由での利用はアプリのアカウント（買い切りライセンス）が前提。アプリの具体価格はページに静的表示が無く未確認。ページの stars/forks 表示（970/114）は GitHub API 実測（3535/307）と乖離しており、ページ側のメタ情報は古い。スキルは単体完結せず scenario-blender-expert などを前提とするため、フォルダ単体をコピーすると不足する（未導入時はツールスキーマから進み gap を明示する挙動）。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2113374545302200732"]
fetched_at: "2026-11-08T20:07:36Z"
---

# Scenario Blender Animation — Blender のキャラアニメを「測定して直す」スキル（TypingMind 配布ページ）

## 目的

- Blender で Python 経由のキャラクター／物体アニメを作るとき、エージェントが「再生して目で見る」代わりに数値で判断できるようにするための SKILL.md。バウンシングボール、歩行・走行サイクル、ジャンプ、演技カット、リップシンク、目の動き、ステップドキーでのブロッキング、スプライン化、タイミングと間隔、アーク、オーバーラップ、スクワッシュ＆ストレッチ、グラフエディタのハンドル、NLA まで対象。
- 投稿の「/scenario-blender-animation handles the dance」が指す実体。配布元は Scenario（scenario.com）の GitHub org、scenario-labs/skills の skills/dcc/blender/ 配下。

## 何ができるか

- アニメの「浮いた感じ」「固い」「滑る」「ポップする」「被写体が小さすぎる」「膝が抜ける」といった症状に対して、フレームごとの位置・スペーシングチャート・アーク検査・フレーミング・オニオンスキン画像・カーブプロット・playblast を計測して直す手順を指示する。
- 判断基準を明文化：ブロッキングはステップドのまま長く保持し、スプライン化は短く遅く。全ブロッキングを一括で Bezier 変換しない（5.2.1 で実測、素朴な変換は次の動きの 84% がホールド中にドリフト、ピラー化すると 0）。コンタクト（着地）をホールド扱いすると体の速度が 0.101 → 0.007 m/frame に落ちて浮いて見える、といった数値付きの注意がある。
- 同梱の scripts/bx_anim.py（約103KB）がキーイング、ブロッキング→スプライン、カーブ検査、計測、ステージング、playblast、膝抜け・反転・バランス検査、オニオンスキン／カーブ画像生成を担当。references/ に procedures.md（API）、critique.md、expert-notes.md、sources.md。
- AI からの呼び方：Agent Skills 形式なので、TypingMind なら Plugins → Skills → Install from GitHub にフォルダ URL を貼るだけ。Claude Code ならフォルダを .claude/skills/ にコピーして再起動。モデル側は名前と description だけを常時保持し、依頼が一致したときだけ本文を読む。
- 単体では実行チャネルを持たず、scenario-blender-expert（Blender への実行経路とレビューループ）を前提にする。リグは scenario-blender-rigging、絵コンテは scenario-blender-previs-storyboard の担当。

## 料金

- 無料。スキルは MIT ライセンスで GitHub（scenario-labs/skills）に公開されており、ページの FAQ も「published on GitHub by scenario-labs under the MIT license. You only pay your own AI provider for the tokens you use.」と明記。
- TypingMind 経由で使う場合は TypingMind アプリのライセンス（買い切り、API キーは自前）が別途必要。金額はページの静的 HTML に表示が無く未確認。GitHub から直接 clone する使い方なら TypingMind は不要。

## 登録の要否

- GitHub から直接使う場合は登録不要（public リポジトリを clone してスキルフォルダをコピー）。
- TypingMind の画面から取り込む場合は TypingMind のアカウント（アプリのライセンス）が必要。

## 変更履歴

- 2026-11-09: 初回登録
