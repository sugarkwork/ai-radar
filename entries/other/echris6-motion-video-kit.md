---
repo: "echris6/motion-video-kit"
name: "Motion Video Kit"
genre: "other"
url: "https://github.com/echris6/motion-video-kit"
license: "MIT"
stars: 1366
language: "Python"
created: "2026-09-27"
updated: "2026-10-14"
forks: 121
open_issues: 0
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 7
size_kb: 68
archived: false
flags: ["unverified"]
risk_notes: "スター1366・フォーク121に対し、コミットは90日で7件（作成2026-09-27、最終push 2026-10-14）で、X投稿経由の注目が先行した可能性がある。作例3本の動画・レンダー結果はリポジトリに含まれず（git tree に mp4 等なし）、成果物品質は第三者が確認できない。効果測定・ベンチマークはなく、効果は作者の自己申告の範囲。HyperFrames でのレンダリング（component-lab.html の npx 手順）は当方では未実行。"
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-07T18:06:00Z"
---

# Motion Video Kit

## 出来ること

- 15〜40秒のビジネス向けローンチ風CMを、AI生成映像＋HTML/GSAPのモーション（必要ならThree.js）で作るためのClaude Codeスキル。SKILL.md が「ブリーフ→参考選定→絵コンテ→素材→部品単体→本編→批評→音→納品」の9段階の手順を定義している。
- 「Gauntlet」と呼ぶ独立批評ループ。作った本人は採点せず、レンダリング結果だけを見る新しい批評エージェントが毎ラウンド判定し、次の周回で前回の指摘を1件ずつ検証する。部品用・本編用・検証用・絵コンテ用の批評プロンプト4種を同梱（references/critic-prompts.md）。
- 数値で測れる品質チェックをスクリプト化。scripts/frozen-time.sh はフレーム間差分から「止まって見える区間」を秒で列挙、scripts/loudness.sh は ffmpeg の ebur128 で統合ラウドネス・LRA・トゥルーピークを出す、scripts/contact-sheet.sh は批評用のコンタクトシートを作る。
- 音の作り込み。scripts/backtime-music.py は曲を切らずに「曲自身の終わり」をエンドカードに合わせて後方から合わせ込み（任意で±1.7%程度のバリスピード）、scripts/solve-sfx-gains.py は効果音ごとに帯域内ターゲットへゲインを解き、2–8kHz の持ち上がりに上限をかける。offline-mix.py / sfx-candidates.py / soften-sfx.sh も同梱。
- 28本のローンチフィルム分析ノート（references/launch-film-notes.md、各本に「見どころ→仕組み→転用」）、6原則＋16機構のモーション文法（motion-grammar.md）、数値＋目視の出荷基準（quality-bar.md）。
- Three.js 部品を単体で回す templates/component-lab.html（HyperFrames 対応のシーク可能なタイムライン）と、3Dアンカーに追従するラベル/ピンを描く templates/projected-overlays.js。
- ビジネス側の型も含む。業種別の買い手根拠と価格アンカー、パイロット提案テンプレ、誇大表現を禁じるルール（references/business-offers.md と SKILL.md の Non-negotiables）。

## 目的・背景

- 28本のプロ制作SaaSローンチフィルムを研究し（motion-grammar.md によれば48分・81,647フレームの数値解析＋全編の目視＋主要トランジションのコマ送り）、さらに自作品3本を批評ループで何十周も直した記録から原則を抽出したもの。
- 「映像はAI生成、動きはコード」という分担。AI生成クリップは4〜5秒・カメラ移動は控えめに作り、ジオメトリが歪んだら隠さず作り直す、という運用が SKILL.md に書かれている。
- 想定読者は代理店ではなく、実際の中小ビジネス（屋根、不動産、EC、B2B SaaS）のCMを作る人。音を消しても「何の商売で、次に何をすべきか」が伝わることを必須条件にしている。
- 価格アンカーや市場価格は2026年9月時点の公開情報のスナップショットで、引用前に再確認するよう README が注意している。

## 依存関係

- ffmpeg / ffprobe（ebur128 フィルタ付き）が必須。計測系スクリプト（frozen-time.sh / loudness.sh / contact-sheet.sh / soften-sfx.sh）と Python スクリプトの音声入出力がすべて ffmpeg 経由になっている。
- Python 3 と numpy、scipy。backtime-music.py は scipy.signal.resample_poly、offline-mix.py と solve-sfx-gains.py は scipy.signal の butter/sosfilt を import しており、sfx-candidates.py は numpy のみ。
- レンダリングは HyperFrames を推奨（README: 「It works best with HyperFrames for rendering」）。Node 22+ が必要で、component-lab.html のコメントに npx hyperframes snapshot . と npx hyperframes render . の実行例がある。HyperFrames は HeyGen 製で、配布サイトに「Free and open source.」と明記されている。
- スキル本体は特定レンダラに依存しない。README は「the principles, prompts and checks are renderer-agnostic」とし、他LLMでは SKILL.md と必要な references をコンテキストに貼る運用を挙げている。
- AI映像生成（image-to-video）は外部サービスを別途使う前提で、特定モデルの指定はない。

## 実行条件

- Claude Code のスキルとして使う場合、business-motion-film/ を ~/.claude/skills/ または <project>/.claude/skills/ にコピーする。
- 尺は15〜40秒、30秒作品で12〜15カット、1ビート1.4〜3.5秒、0.6秒を超える静止は最終CTA以外は不可、という前提が SKILL.md / quality-bar.md にある。
- 実在企業の案件では、クライアント承認済みの素材と事実だけを使う。実素材がない場合は「Fictional brand · Concept film · AI-generated imagery」と明示したコンセプト映像として扱う。
- APIキーはファイルに書かず、必要なコマンドはユーザー自身のターミナルで実行させる方針（SKILL.md の作業スタイル）。
- ライセンスは MIT（テキスト・スクリプト・テンプレート）。参照フィルムの映像は再配布せず、リンクのみを収録している。

## 最短手順

- git clone https://github.com/echris6/motion-video-kit.git
- cp -r motion-video-kit/business-motion-film ~/.claude/skills/   （全プロジェクトで使う場合。プロジェクト単位なら cp -r motion-video-kit/business-motion-film <your-project>/.claude/skills/）
- Claude Code を起動し、ビジネスCM／サンプルリール／エクスプレイナーの作成、または既存カットのレビューを依頼する（README: 「ask for a business commercial, sample reel or explainer, or for a review of one, and the skill loads」）。
- Codex など他のLLMでは business-motion-film/SKILL.md と、その工程で必要な references/ のファイルをプロンプトに貼る。
- 書き出した動画に scripts/frozen-time.sh film.mp4 と scripts/loudness.sh film.mp4 を実行し、基準を満たすまで修正→再レンダーする。
- 曲を後方から合わせる場合は python3 scripts/backtime-music.py track.mp3 --list-hits で終端候補を出し、耳で確認した時刻を --hit に渡して書き出す。

## 変更履歴

- 2026-11-07: 初回登録
