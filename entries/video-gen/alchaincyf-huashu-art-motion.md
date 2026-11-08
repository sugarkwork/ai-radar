---
repo: "alchaincyf/huashu-art-motion"
name: "huashu-art-motion"
type: "repo"
genre: "video-gen"
url: "https://github.com/alchaincyf/huashu-art-motion"
license: "MIT"
stars: 6502
language: "JavaScript"
created: "2026-10-06"
updated: "2026-10-16"
forks: 648
open_issues: 9
commits_30d: 18
commit_cadence: "weekly"
commits_90d: 22
size_kb: 78640
archived: false
flags: ["unverified"]
risk_notes: "投稿の「導入から10分で完成」「Opus 5.5 が作った」は制作者・紹介者の主張で、第三者の計測ではない。README/SKILL.md 内で画風数は「実装済み36種＋研究配方16〜17種（カード計53枚）」と数え方が揺れ、研究配方は作者自身が未検証と明記している。画風の一致度を定量評価した公開ベンチマークはない。"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/sumika45379/status/2111947940193587341"]
fetched_at: "2026-11-08T10:52:30Z"
---

# huashu-art-motion — 画風をコードで描くアニメ生成スキル（Claude Code / Codex 向け）

## 出来ること

- 同じ部屋・少女・猫の構図のまま、画風だけを時代順に切り替える「アートヒストリー早送り」を作る。実装済み36画風＋研究配方16〜17種（カード計53枚、`references/风格配方/`）。
- 解説アニメの文法を9種用意（Kurzgesagt、Vox、白板、3Blue1Brown、storytime、kinetic type、発表会風UI、财经图表、解説者リード）。うち8種は動作するデモと JSON spec 駆動のパラメータ化クリップ付き。
- 参考アニメを渡すと、カット割り・ビートグリッド・画面のどこが動くかを `scripts/analyze/breakdown.py` で数値化し、その仕組みをコードで組み直す。
- 1本の絵の中をキャラクターが左から右へ歩き、境界を越えた瞬間に世界と画風が変わる「長巻」の骨格と3世界のデモ。
- 人物は自前のキャラクター素材か画像生成モデルのフレームを合成。どちらも無い場合は手と後ろ姿だけを描く。
- 音楽もコード合成（BPM グリッド、モチーフの楽器替え、終わりの効果音列）。外部の音源は不要。
- 出力は既定 1920×1080・30fps。横/縦、アルファ付きのクリップも作れ、ffmpeg で連結する。

## 目的・背景

- 作者は花叔（alchaincyf）。リポジトリ公開は 2026-10-06、最新リリースは v1.2.0（2026-10-16）。
- 起点は Tak（@cherry_mx_reds）の「Art History Speedrun」。単なる復刻ではなく、画風ごとに「絵の中で何が動くか」を再利用できる形で貯めるのが目的で、SKILL.md はモデル能力で「開闊档（Claude Opus 5.5 以上）」と「軌道档（その他）」に手順を分けている。
- 紹介元の Voxyz_ai 投稿（2026-10-12、25.5万表示）の動画は実在する。41.27秒・1920×1080・30fps で、字幕は 40,000 BC → 655 AD（敦煌壁画・盛唐）→ 1642（Rembrandt · chiaroscuro）→ 1903（Picasso · période bleue）→ 1962（POP ART）→ 1985（8-BIT）→ 2017 → 2026（Flat vector illustration）。女性・猫・部屋の構図は固定で、タイトルは「TEA ACROSS THE AGES」、末尾に「Opus 5.5」のクレジットがある。画風遷移そのものは映像で確認できる。
- 「導入から10分で完成」は投稿者の主張で、こちらでは再計測していない。

## 依存関係

- 必須: uv、ffmpeg、Playwright Chromium（初回に `uv run --with playwright playwright install chromium`）。
- レンダー/QA の Python 依存: playwright、numpy、pillow（qa.py の PEP 723 ヘッダ）。
- 導入は Node の `npx skills add alchaincyf/huashu-art-motion`。
- 人物を出す場合のみ、自前のキャラクター絵か画像生成モデルへの接続が要る。音声は任意（既存録音の利用、システム音声、声の複製を必要時だけ設定）。
- 同梱フォントは SIL OFL。筆順データの一部 `reference_films/spacex/spacex_wb/assets/strokes.js` は Arphic Public License。
- 作者の関連配布: nuwa-skill（スキル生成）、darwin-skill（スキル改善）。nexu-io/open-design が MIT のまま適応版を収録している。

## 実行条件

- 手順書・風格カードは中国語。エージェントには「中国語の docs を読んで日本語で応答する」よう指示する運用が前提。
- 描画はヘッドレス Chromium 上の Canvas/SVG。乱数はシード固定で、同一時刻の再レンダーはピクセル一致（決定論的）。
- `deliver.py` のゲート: 中段に 0.3 秒以上続く「ほぼ単色・エッジなし」の空画面は赤、青紫の背景が全編の 30% 以上は赤（12% 以上で黄）、速い運動フレームの比率が 0.035 未満は赤。赤のときは完成ファイルをコピーしない。
- 空画面は色ではなくエッジで判定するため、黒背景の線画や白板の筆跡は誤検知しない。青紫が題材上必要な場合だけ `--allow-blue-purple "理由"` で黄に落とせる。
- GitHub 上のサイズは 78,640KB（デモ映像・画像アセット込み）。GPU 要件の記載はない。
- ライセンスはコードと文書が MIT（商用利用可）。例外として花叔のキャラクター画像・キャラクターフレーム・総覧図・デモ映像は MIT 対象外、Clawd（Anthropic のマスコット）の同人デモも MIT 対象外、フォントは各 OFL、strokes.js は Arphic。

## 最短手順

- 1. スキルを入れる: `npx skills add alchaincyf/huashu-art-motion`
- 2. 依存を確認する: `uv --version`、`ffmpeg -version`、`uv run --with playwright playwright install chromium`
- 3. AI に渡す依頼文の例（Claude Code / Codex など）:
「huashu-art-motion を使って15秒のアニメを作って。docs は中国語なので読んで、返事は日本語で。
1) 先に uv / ffmpeg / Playwright Chromium の有無を確認し、無いものの入れ方を教えて。
2) 題材・誰向けか・横/縦を聞いたうえで、references/风格配方/INDEX.md から合う画風を3つ（★★★優先）選び、同じ構図で3案の静止画を1枚ずつ見せて。サンプルの部屋はコピーしない。
3) 選んだら各シーンに主動作1つ＋その画風の母題ループ2つ。音楽を付けるなら BPM グリッドに合わせる。
4) 人物を出すなら、自前のキャラ絵 / 画像生成 / 手と後ろ姿のみ、を先に確認して。
5) レンダリング後は qa.py → 制作に参加していないエージェントの審片（审片/ に記録）→ deliver.py の順。赤があれば直して再レンダーしてから渡して。」
- 4. 手元で1フレーム試す: `uv run --with playwright python scripts/engine/render.py --solo 09_postimp --stills 0.3 --out 試渲`
- 5. spec から短いクリップを出す: `uv run --with playwright python scripts/engine/render.py --spec scripts/engine/examples/t3_finance_chart.json --out 财经图表.mp4`
- 6. 35枚の総覧は同じ部屋の構図で作られている。新作では構図を題材に合わせて引き直す（README も明記）。

## 変更履歴

- 2026-11-08: 初回登録
