---
type: "repo"
name: "Herk Edit Kit（Nate Herk の AI 動画編集キット）"
genre: "video-gen"
url: "https://github.com/nateherkai/herk-edit-kit"
repo: "nateherkai/herk-edit-kit"
license: "MIT（LICENSE 本文は MIT。GitHub API は NOASSERTION。ブランド素材と pipeline 部分に別条件）"
stars: 2691
language: "HTML"
created: "2026-04-18"
updated: "2026-10-14"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
flags: []
risk_notes: "ライセンスは二段構え。ルート LICENSE は MIT（著作権 Nate Herk）だが末尾に「AIS（AI Automation Society）のロゴ・ブランドガイドライン画像・ブランドトークンCSS・一部サンプルの内容は AIS の財産で再利用許諾なし」と明記され、GitHub API も spdx NOASSERTION を返す。pipeline 部分は licenses/PIPELINE-USE-PERMISSION.txt の独自許可、hyperframes/gsap/hyperframes-cli/hyperframes-registry/website-to-hyperframes の5スキルは heygen-com/hyperframes（Apache-2.0）からの取り込みで skills-lock.json にソースとハッシュが記録されている。商用利用時は AIS 素材の差し替えが必須（README もそう指示）。\n\n未解決のセキュリティ指摘：issue #16（2026-10-08、未対応・未クローズ）で motion-showreel/scripts/kie.mjs の upload() が --ref / --image のパスを検証せず、任意のローカルファイルを base64 で Kie.ai に送る点が報告されている。エージェントが読んだ文字起こしやWebページ経由のプロンプトインジェクションで資格情報を外部送信させ得る。Kie.ai を使わない構成なら影響は無いが、生成B-rollを使うなら注意。\n\nメンテ体制：作者は Nate Herk 1人。全14コミットが同一作者で、日付が固まって飛ぶ（2026-04-18 の初回、09-08 の統合、09-25〜09-28、10-13〜10-14）。2026-10-14 以降 push が無く、30日コミットは4。open 13件のうち11件は未マージPR（2026-09-11〜10-29、うち最新の PR #19 は「silence cut の ffmpeg 呼び出しをテストしていない」というギャップ指摘で、これは実際にこちらの検証でも core の ffmpeg 経路がテスト対象外だと確認できた）。コントリビューションは取り込まれていない前提で読むべき。\n\nサイズ：クローン実測 788MB（video-projects の既存12プロジェクト 287MB、examples/showcase の完成動画 111MB を含む）。npm ci は 139パッケージ・約1分、npm audit は 8件（high 6 / moderate 2）を devDependencies 側で報告。初回レンダーで HyperFrames が Chrome を別途取得する（約115MB）。\n\n既定の文字起こしは ElevenLabs Scribe で音声を外部送信し課金される。README/TOOLS-AND-API-KEYS.md は Whisper API・ローカル Whisper・既存の word-level JSON の持ち込みを代替として明記しており、切り分けは誠実。Kie.ai は任意。\n\n軽微：cut-silences.mjs が出力する ffmpegCommand 文字列が \"-/filter_complex\" になっており（280行目）、コピペ用のコマンドとしては不正。ffmpeg 9 は解釈するので動作に支障は無いが、生成されるレシピ文字列を誰も検証していないことの表れ。\n\nレンダーは Chrome 前提。CPU のみのコンテナでは 8秒 1080p のドラフトに 8分8秒かかった（GPU 環境なら大幅に短い）。"
forks: 652
open_issues: 13
commits_30d: 4
commit_cadence: "weekly"
size_kb: 460128
archived: false
fetched_at: "2026-11-09T21:46:02Z"
last_release: ""
last_release_at: ""
commits_90d: 13
---

# Herk Edit Kit — 文字起こしから無音カット・字幕・モーショングラフィックまで、Codex / Claude Code に編集させる15スキル

## 出来ること

- `edit-video`：1本のトーキングヘッド素材を「ffprobe → 文字起こし → 無音カット → 言い間違い候補のレビュー → ビートシート → HyperFrames 合成 → lint/preflight → ドラフトレンダー」まで一気通貫で進める親スキル。各段は単独スキルとしても呼べる
- `cut-silences`：word-level タイムスタンプから EDL・リタイム済み文字起こし・ffmpeg フィルタスクリプトを生成。`--apply` で実際に切った MP4 を出す。0.55秒未満の間は残し、切る場合も文脈に応じて 0.14〜0.24秒の「息継ぎ」を残す（検証：8.0秒 → 3.96秒、映像3.933秒/音声3.960秒で A/V ずれ無し）
- `cut-mistakes`：言い直し・噛み・フィラーを検出して**候補**を出すだけ。人間が `approved-cuts.json` に承認した区間だけを `apply-cuts` が切り、以降の文字起こしをリタイムする（自動削除しない設計）
- `short-form-edit`：9:16 のリール / YouTube Shorts / 短尺広告。最初の3秒で「見続ける理由」を作ることを最優先ゲートに置き、キャプションのドリフト検証（`validate-plan.mjs`）と素材の重複・使い回し検証（`validate-footage.mjs`）を同梱
- `motion-showreel`：参照リールを解析して章ごとの技法を抽出し、音楽のビートグリッドを実測して15秒のブランドショーリールを組む。Kie.ai 経由の Suno 音楽・Seedream スチル・Kling カメラムーブの小さなクライアント付き
- `style-library`：モーショングラフィックのカード **406枚**（Vox Explainer / Kallaway の2スタイル、CSSトークンと編集可能スロット付き）。`registry.json` でメタ検索でき、`npm run catalog` で再生成
- `style-templates`：dark graph paper と left glass popout の2つのシーンテンプレート
- `video-storytelling` / `hyperframes-video-beats`：発話アンカー付きのビートシート作成と、外部サブコンポジションのタイミング検証（`validate-beat-sync.mjs`）
- `hyperframes` / `hyperframes-cli` / `hyperframes-registry` / `gsap`：HeyGen の HyperFrames（HTML/GSAP ベースのコンポジションを Chromium で撮って ffmpeg で固める）の使い方スキル
- `scripts/`：`transcribe-elevenlabs`、`preflight`、`build-edl-review`（EDL を HTML で目視レビュー）、`new-video`、`sync-codex-skills`（.claude → .agents ミラー生成）
- Codex と Claude Code の両対応。`.claude/skills/` が正で `.agents/skills/` に同一内容をミラー（`npm run check:skills` が差分ゼロを検証）

## 目的・背景

- Nate Herk（AI Automation Society）が自分の動画編集ワークフローを教材として公開したもの。元は 2026-04-18 公開の HyperFrames Student Kit、2026-09-08 に別の video-pipeline キットを履歴ごと統合、2026-10-14 に Herk Edit Kit へ改名。X の投稿（@heyrimsha）はこの改名後の姿を紹介している
- 設計思想は「検出は機械、判断は人間」。無音カットは決定的なルールで機械的に切り、言い間違いは候補を出して承認ファイルを経ないと切らない。README も「自動検出は編集案を出すだけで、編集判断は人間に残る」と明記
- 406枚のカードは draft 扱い。README が「選んだカードは自分のテキストと映像でテストせよ」「ライブラリのテンプレートは GSAP と Google Fonts を公開 CDN から読むので、最終書き出しではローカライズせよ」と注記
- docs/EDITING-PLAYBOOK.md に「Nate の家風」を実測値で書いている（ペーシング、レイアウト、キャプション、B-roll の順序、音のパレット）。short-form-edit はユーザーから受けた指摘を次回以降のルールとしてスキルに書き戻す運用を明示
- 12本の既存作例（video-projects/）と完成動画3本（examples/showcase）を同梱。うち2本は「AI エージェントがこのキットだけで編集した」と README が主張しており、生データと編集後を並べた比較動画もある

## 依存関係

- Node.js 22 以上（package.json の engines が >=22。検証は Node 26.12.1 / npm 12.0.2）
- FFmpeg + ffprobe（カットとレンダーに必須。検証は ffmpeg 9.0.1）
- Chrome / Chromium（HyperFrames のキャプチャに必須。未検出なら `HYPERFRAMES_BROWSER_PATH` で既存バイナリを指すか `npx hyperframes browser ensure`。後者は展開に unzip を要求する）
- devDependencies は3点：hyperframes 0.7.109（npm 公開パッケージ、最新は 0.9.19）、gsap 3.14.2、playwright ^1.59.1。レンダーは完全ローカル
- 任意（有料）：ElevenLabs Scribe の API キー（既定の文字起こし）、Kie.ai のキー（生成B-roll・画像・Suno 音楽）、ElevenLabs の効果音生成
- 代替（無料〜）：OpenAI Whisper API、ローカル Whisper / whisper.cpp、または自前の word-level JSON（`{words:[{text,start,end}], audio_duration_secs}`）を持ち込む
- 自分の素材：映像・ロゴ・フォント・音楽・効果音。キットにストック素材や音楽サブスクは含まれない

## 実行条件

- API キー無しで通る範囲（検証済み）：`npm ci` → `npm test`（11/11）→ `npm run check`（716ファイル/406カード 0エラー）→ `npm run demo` → `npx hyperframes lint`（0 errors, 0 warnings）→ ドラフトレンダー（1080p30・8.0秒の MP4 が生成）。合成の文字起こし（examples/editing/source.json）とダミー映像があれば cut-silences の本番カットもキー無しで動く
- 有料が要る範囲：実際の素材の文字起こし（既定は ElevenLabs Scribe＝音声を外部送信）、生成B-roll/画像/音楽（Kie.ai）。README に金額の記載は無く、各サービスの料金とクレジットを自分で確認する前提
- ライセンス：MIT ベースだが (1) AIS のロゴ・ブランドトークン・一部サンプルは再利用不可で自分のブランドに差し替える必要があり、(2) pipeline 由来部分は独自の use permission、(3) 5スキルは Apache-2.0 の HyperFrames 由来。GitHub のライセンス判定は NOASSERTION
- 規模：クローン実測 788MB（既存プロジェクト 287MB＋完成動画 111MB を含む）。`npm ci` 139パッケージ・約1分、`npm audit` 8件（high 6）。初回レンダーで Chrome 約115MB を追加取得
- レンダー速度：CPU のみのコンテナで 8秒/1080p のドラフトに 8分8秒。実尺の長尺を扱うなら GPU か相応のマシンが要る
- 検証環境：Linux（WSL）/ Node 26.12.1 / ffmpeg 9.0.1 / chrome-headless-shell 152。README は Windows・macOS・Linux を想定（作者の検証記録は Windows + Node 24.15.0 + FFmpeg 8.1.1 + HyperFrames 0.7.109）
- 音楽・音声の権利、実在人物の肖像、プラットフォーム規約は利用者責任。README は「公開は別アクションで、指示があってから」と明記

## 最短手順

```bash
git clone --depth 1 https://github.com/nateherkai/herk-edit-kit.git
cd herk-edit-kit
npm ci                 # 139 packages, 約1分
npm run setup          # ツール確認と .env 生成（既存 .env は保持）
npm test               # 11/11 pass
npm run check          # 716 files / 406 cards / 0 errors

# 1) キー無しで描画まで通す
npm run demo
cd video-projects/demo
npx hyperframes lint                       # 0 errors, 0 warnings
npx hyperframes render --quality draft --output renders/demo.mp4
# Chrome が無い場合: export HYPERFRAMES_BROWSER_PATH=/path/to/chrome-headless-shell

# 2) 自分の素材を切る（エージェント無しでも可）
cd ../..
npm run new-video -- my-video
cp /path/to/raw.mp4 video-projects/my-video/assets/raw.mp4
node scripts/transcribe-elevenlabs.mjs video-projects/my-video/assets/raw.mp4   # または word-level JSON を自作
node .claude/skills/cut-silences/scripts/cut-silences.mjs \
  video-projects/my-video/assets/raw.json --video video-projects/my-video/assets/raw.mp4 \
  --out-dir video-projects/my-video/assets --output video-projects/my-video/assets/silenced.mp4 --apply

# 3) エージェントに任せる（リポジトリを Claude Code / Codex で開く）
#   Claude Code: /edit-video   Codex: $edit-video
#   「Use edit-video to edit my recording at <path>. Tighten dead air, show me the
#     proposed mistake cuts, use the dark graph-paper style. Produce a reviewed draft.」
```


## 変更履歴

- 2026-11-07: 初回登録
