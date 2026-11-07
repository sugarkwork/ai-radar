---
type: "repo"
name: "ffmpeg-skill — コーディングエージェントに渡すローカル動画編集ツール42本"
genre: "video-gen"
url: "https://github.com/kajisho5/ffmpeg-skill"
repo: "kajisho5/ffmpeg-skill"
license: "MIT"
stars: 4672
language: "Python"
created: "2026-09-03"
updated: "2026-11-06"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
flags: []
risk_notes: "実装は本物で、こちらで npx 導入→contract 42件→fit/check/look まで通したが、リスクは3点。(1) 実質ひとり開発：コミット270件が作者 kajisho5、146件が github-actions[bot]、53件が claude[bot]（2026-11-07 時点の contributors）。バス係数1で、方針変更やメンテ停止がそのまま影響する。(2) 壊しやすい速度：作成から2か月で 2.0.0 と 3.0.0 の2回の破壊的変更（--crf 廃止、FFmpeg 5.x / Python 3.9 切り捨て、cut.py の edit list・HEVC 保持の既定変更）。main 追従は危険で、タグ／npm バージョンで固定すべきと README 自身が書いている。(3) 数字の読み方：作成2か月で stars 4672・forks 379 に対し watchers 7。npm 週9,077DLと利用の実体はあるが、この stars 数を品質の裏付けとして扱わない。加えて README は作者の10本以上の姉妹リポジトリ（video-production-agent / remotion-ffmpeg-skill / qc-skill 等）への導線を兼ねており、宣伝面が大きい。macOS の素の Homebrew ffmpeg は libass/zscale を欠き doctor の ok が false になる（ffmpeg-full 前提）。リポジトリは 37MB で docs/demos の比重が大きい。"
forks: 379
open_issues: 15
commits_30d: 100
commit_cadence: "daily"
size_kb: 37273
archived: false
fetched_at: "2026-11-07T01:21:00Z"
last_release: "v3.2.0"
last_release_at: "2026-11-06"
---

# ffmpeg-skill — FFmpeg を「エージェントが検証できる42本のツール」に分解したローカル動画編集スキル

## 出来ること

- 分析：`probe.py` が長さ・fps（VFR判定込み）・解像度・回転・色・HDR形式（Dolby Vision 含む）・全音声ストリームを測る。`scenes.py` はシーン変化・音のピーク・ビート・ショット種別（静止/パン/モーション）、`cropdetect.py` は黒帯の実測、`look.py` はコンタクトシートPNGを書き出す（顔や被写体の検出はしない）
- 編集：`cut.py`（複数区間カット、まず `-c copy` で無劣化、必要時のみ再エンコード、`precision` とキーフレーム吸着を報告）、`join.py`（サイズ/fps/音声レイアウトを揃えて xfade）、`silence.py`（無音の除去、前後0.2秒のマージン、カット地点のレベル警告、`--filler` は計測済みの語タイミングのみ）、`fit.py`（尺合わせの速度変更/トリム、9:16 への pad/crop/blur、`--crop-x/-y` で寄せ位置指定）
- 音：`loudness.py` が2パス EBU R128 で -14 LUFS / -1 dBTP へ（書き出したファイルを測り直し、超えていれば再エンコード）、`audio.py` は声のクリーンアップ3段階・型付きコンプ/リミッタ/ゲート・BGMのダッキング、`sync.py` は音声相互相関で1ms精度のオフセットとドリフト補正、`multicam.py` は複数カメラの同期とスイッチ
- 字幕/画：`caption.py` は SRT/ASS の焼き込み、単語ごとのカラオケ、`--mode mux` で言語タグ付き複数トラック、プラットフォームの安全域に合わせた折返し、`overlay.py`（ロゴ/PiP/クロマキー）、`graphics.py`（ローワーサード・タイトル・プログレスバー・フックカード）、`color.py`（HDR10/HLG/DV→SDR、3D LUT、露出/コントラスト等の型付き補正）
- 配信：`export.py` のプリセット（youtube / reels / tiktok / shorts / x / linkedin / facebook / podcast / prores / dnxhr / alpha マスター / key-fill / gif / copy）、`check.py` がプラットフォーム仕様に PASS/WARN/FAIL を出し、失敗行には修正コマンドを添える。実測では 13項目中 loudness のみ FAIL（-21.8 LUFS）で `loudness.py -I -14` を提示した
- 編成：`render.py` が project.json から1本の編集を最後まで描画（`--template tiktok` などの配信テンプレート同梱、`--template all` で7媒体ぶんと比較表）、`batch.py` はフォルダ一括と `--watch`、`--export-timeline` で FCPXML/EDL/OTIO を書き出して Premiere/Resolve に渡せる
- エージェント向けの作り：全ツールが `--dry-run`（コマンドを印刷して実行しない）/`--json`（実行コマンド・出力のprobe・未計測項目 `unverified` を含む）/`--plan FILE`（入力の指紋付き計画を後で実行）/`--timeout`/`--overwrite` を持つ。生の ffmpeg 引数や filter_complex は受け付けず、シェルを経由しない
- MCP：`mcp/server.py` の `tools/list` は contract から生成され、既定で12本だけ広告（コンテキスト節約）、残り30本は名前指定の `tools/call` で到達可能、`FFMPEG_SKILL_MCP_FULL=1` で42本全部を列挙。手元で tools/list を叩いて12本を確認
- 導入：`npx ffmpeg-skill` で Claude Code（`~/.claude/skills/ffmpeg-skill`）、`--codex` で Codex（`~/.agents/skills/ffmpeg-skill`）、`--cursor`、`--all`、`--project`、`--dir`。Claude Code の plugin marketplace としても入る（`/plugin install ffmpeg-skill --marketplace kajisho5/ffmpeg-skill`）

## 目的・背景

- 「ffmpeg を知っている」エージェントは推測する——フレームレートを仮定し、コンテナに入らないコーデックを選び、ストリームコピーで足りるファイルを再エンコードし、結果を開かずに done と言う。このリポジトリはその推測を、実測と再計測に置き換えるのが目的
- 設計の核は SPEC（Self-Producing Execution Contract）：各ツールの `input_schema` を手書きせず、そのスクリプトの argparse パーサーから実行時に導出する。contract・MCP の inputSchema・ドキュメントが同じ1点に追従し、ずれたら CI が落ちる
- 作者 kajisho5 は動画制作まわりのスキルを10本以上公開しており、本リポジトリはその中の「手」（切る・測る・書き出す）に限定される。何を切るか、どのテイクが良いか、字幕に何を書くかは判断せず、上位のエージェントに委ねる。依存は一方向で、ここから他リポジトリを呼ばない
- 検証の思想は論文としても公開されている（Zenodo, doi:10.5281/zenodo.23720216）。README 自身が「このリポジトリはその規律に部分的にしか適合していない」と書いており、誇張を避ける姿勢が見える
- 境界が明示されている：顔・商品・被写体の検出はしない、自動リフレーミングはしない（`--crop-x/-y` を呼び出し側が決める）、`redact.py --mode delogo` は1px境界の補間であって inpainting ではない、`scenes.py --highlights` は音量か尺の代理指標でランクするだけ

## 依存関係

- FFmpeg 6.1 以上（3.0.0 で 5.x を切り捨て。6.1 未満は `kind: missing_tool` / `ffmpeg_unsupported` で拒否）。必須コンポーネントは libx264・aac と、drawtext / subtitles(libass) / loudnorm / xfade / acrossfade / amix / overlay / scdet / silencedetect / cropdetect / tile / tpad / boxblur / hqdn3d / yadif / reverse / rotate / showwaves / v360 / xstack / vidstabdetect・vidstabtransform
- 任意：libx265・prores_ks・zscale(libzimg)・libmp3lame・libopus・libvorbis・ass フィルタ（使うフラグのときだけ必要）
- Python 3.10 以上、標準ライブラリのみ（サードパーティ依存ゼロ）
- Node 16 以上は `npx` インストーラを使う場合だけ。Node なしでも SKILL.md / scripts / templates / references / docs / mcp / package.json をコピーすれば動く
- 任意：字幕の自動起こし（`caption.py --transcribe`、`silence.py --filler --transcribe`）に parakeet-mlx / faster-whisper / openai-whisper のいずれか。初回にモデルをダウンロードする。無くてもそれ以外は全部動き、`--transcribe` はインストール行を示して拒否する

## 実行条件

- 完全ローカル。APIキー・アカウント・クラウド不要で、映像はアップロードされない。ネットワークが要るのは npm 導入時と、任意の音声認識モデルの初回取得だけ
- macOS は `brew install ffmpeg-full` が前提（素の `ffmpeg` formula は subtitles/drawtext/zscale を欠く）。keg-only なので PATH に無いことが多く、その場合スキルが同一 prefix の `ffmpeg-full` を自分で探して使う（`doctor --json` の `ffmpeg_path` / `ffmpeg_source` に出る）
- Ubuntu/Debian は `sudo apt install ffmpeg`、Windows は `winget install Gyan.FFmpeg`。Git Bash では python.org 版の Python が `python` 名になるため、素のスクリプト例の `python3` を読み替える必要がある（インストーラと doctor/contract は吸収済み）
- `doctor` の `ok` は「どれか1つのツールが要求する部品が欠けたら false」。個別ツールの可否は `doctor --json` の `tools` を見る。検出できない場合は missing ではなく unknown として扱う設計
- 既存ファイルは `--overwrite` なしで拒否。入力と同じパスへの出力は常に拒否。入力を書き換えない（テストが実行後のハッシュを照合）
- `--timeout` 既定1800秒、`FFMPEG_SKILL_TIMEOUT` で変更、0で無効。超過時は ffmpeg を kill し部分出力を消して `kind: timeout`（exit 124）
- 3.x は道具名・引数・JSONキー・終了コードの互換を 4.0 まで約束。ただし 2.0.0 / 3.0.0 で既に破壊的変更があるので、main 追従ではなくタグか npm バージョンで固定する

## 最短手順

```bash
# 0. FFmpeg（6.1以上、libass と zscale 入りのビルド）
sudo apt install ffmpeg            # macOS: brew install ffmpeg-full / Windows: winget install Gyan.FFmpeg

# 1. スキルを導入（用途で1つ選ぶ）
npx ffmpeg-skill                   # Claude Code → ~/.claude/skills/ffmpeg-skill
npx ffmpeg-skill --codex           # Codex       → ~/.agents/skills/ffmpeg-skill（Cursor もここを読む）
npx ffmpeg-skill --cursor          # Cursor
# Claude Code のプラグインとして: /plugin install ffmpeg-skill --marketplace kajisho5/ffmpeg-skill

# 2. 環境と契約の確認
npx ffmpeg-skill doctor
npx ffmpeg-skill contract --json | head -40     # tools は 42 件

# 3. ツールを直接叩く（エージェントがやることと同じ）
S=~/.claude/skills/ffmpeg-skill/scripts
python3 $S/probe.py in.mp4 --compact
python3 $S/fit.py in.mp4 --duration 5 --aspect 9:16 --fit crop --json
python3 $S/check.py in_fit.mp4 --platform tiktok
python3 $S/look.py in_fit.mp4 -o sheet.png      # 仕上がりをPNGで見る

# 4. エージェントには依頼文で投げる
#   「interview.mp4 の 0:45-3:10 と 5:00-6:30 を残して60秒、リール用に」
```

- 導入後の確認は `npx ffmpeg-skill doctor` の `ok` だけで判断しない。`doctor --json` の `tools` で使いたいツール個別の `usable` を見る（libvidstab が無いビルドなら stabilize だけ落ちる、など）。
- この検証では合成映像（testsrc2 8秒 1280x720 + sine）で `probe` → `fit --duration 5 --aspect 9:16 --fit crop` → `check --platform tiktok` → `look` を通し、5.000s / 406x720 / 30fps の出力と13項目の判定、コンタクトシートPNGの生成まで確認した。

## 変更履歴

- 2026-11-07: 初回登録
