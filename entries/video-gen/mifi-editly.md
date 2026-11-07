---
repo: "mifi/editly"
name: "editly"
genre: "video-gen"
url: "https://github.com/mifi/editly"
author: "mifi"
license: "MIT"
stars: 5590
language: "TypeScript"
created: "2020-04-15T14:23:56Z"
updated: "2025-05-12T07:03:44Z"
forks: 386
open_issues: 80
size_kb: 729
archived: false
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
last_release: "v0.15.0-rc.1"
last_release_at: "2025-01-19T15:06:09Z"
flags: []
risk_notes: "直近30日・90日のコミットはいずれも0件(最終コミット 2025-02-20、pushed_at は 2025-05-12)で、commit_cadence は stale。最新リリースは 2025-01-19 の v0.15.0-rc.1 で、タグ名どおり RC(リリースノート本文も『a new release (candidate)』)であり、正式版 0.15.0 は未公開。npm の dist-tags は latest=0.14.2 / next=0.15.0-rc.1 のため、通常のグローバル導入では TypeScript 化・ESM 化前の 0.14.2 が入る(README の ESM 前提の記述と齟齬)。リリースノートに『After a couple years of inactivity, editly now has a new maintainer』とあり、2022〜2024年に長期停滞した履歴がある。open_issues は80件。node-canvas と headless-gl のネイティブビルドが必要で、ビルド環境が無い場合は Docker かビルド済み環境に頼る必要がある。README に非推奨(deprecated)の明記は無い。"
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-07T18:50:04Z"
---

# Editly — JSON/JavaScript の編集プランから動画を書き出す宣言型NLE(CLI + JS API)

## 出来ること

- クリップ・画像・音声・タイトルを並べた編集プラン(JSON / JSON5 / JavaScript オブジェクト)から、mp4 / mkv / gif を1コマンドで書き出す。
- 任意の解像度・アスペクト比へ変換(1:1、9:16、16:9 など)。入力のアスペクト比が違っても自動でスケール+レターボックスし、FPS も変換する。
- トランジションは gl-transitions の全種類に加え directional-*、random、dummy。`defaults.transition` で既定値、`clips[].transition` で区間ごとに指定。
- レイヤー: video / image / image-overlay(PiP) / title / subtitle / title-background / news-title / slide-in-text / fill-color / linear-gradient / radial-gradient / rainbow-colors / pause / canvas(HTML5 Canvas 関数) / fabric(Fabric.js) / gl(GLSL シェーダ)。
- 音声: audioFilePath でBGM、audioTracks[] で任意開始時刻の複数トラック、clipsAudioVolume / mixVolume でミックス比、audioNorm(dynaudnorm)でダッキングと正規化、クロスフェードは audioInCurve / audioOutCurve。
- cutFrom / cutTo で切り出した区間を clip.duration に合わせて自動で速度調整(音声レイヤーは 0.5x〜100x の範囲)。
- `--fast` で低解像度・低FPSのプレビューを先に回せる。customOutputArgs で ffmpeg の出力オプションをそのまま渡せる。

## 目的・背景

- 「動画編集をコードで」がコンセプトの宣言型ノンリニア編集ツール。同じプランを使い回し、素材だけ差し替えた量産・バッチ編集を再現可能にするのが狙い。
- ffmpeg-concat に触発されつつ、中間ファイルを書き出さないストリーミング編集で高速・省ストレージだと README は主張(数値ベンチマークは未掲載、当方でも未計測)。
- 作者は Mikael Finstad(mifi)。LosslessCut と同じ作者で、README でも LosslessCut との併用を推奨している。MIT の無料 OSS(寄付歓迎)。
- 2020-04-15 作成、stars 5,590 / forks 386。2022〜2024年に長期停滞し、2025-01 に新メンテナ(Brandon Keepers)の下で TypeScript 化と v0.15.0-rc.1 が出たが、2025-02-20 を最後にコミットが止まっている。

## 依存関係

- Node.js(0.15 系は Node 18 以上、ESM only)。package.json に engines 指定は無い。
- ffmpeg と ffprobe が PATH に必要(読み込み・フィルタ・エンコードは ffmpeg 側が担う)。
- `canvas`(node-canvas)^2.11.2 — cairo / pango / jpeg / gif / rsvg の開発パッケージが要るネイティブモジュール。タイトル描画や canvas レイヤーが依存。
- `gl`(headless-gl)^8.1.6 — X11 / GL の開発ヘッダ(libgl1-mesa-dev、libglew-dev、libglu1-mesa-dev、libxi-dev)が必要。トランジションと gl レイヤーはこの上で動く。
- その他: fabric ^6.5.4、gl-transitions ^1.43.0、gl-shader、gl-texture2d、ndarray、execa ^9.5.2、json5、meow、p-map。
- ネイティブビルドが通らない環境向けに Dockerfile / docker-compose.yml がある。Dockerfile は node:lts-bookworm でビルド依存を入れて `npm run build` し、実行ステージで ffmpeg + xvfb + libcairo2 + libpango1.0 + libgif7 + librsvg2-2 を導入、ENTRYPOINT は `xvfb-run`。

## 実行条件

- OS は Windows / macOS / Linux。Linux は headless-gl のシステム依存を別途導入する必要がある。
- npm の dist-tags は latest=0.14.2 / next=0.15.0-rc.1。0.15 系(ESM/TypeScript)を使うには `@next` タグ指定が要る。
- 入力はローカルファイルパスが基本。リモート URL を渡すには `allowRemoteRequests: true`(既定 false)が必要。
- 出力形式は outPath の拡張子で決まる(.mp4 / .mkv / .gif)。幅・高さ・FPS を省略すると最初の入力動画の値に合わせられる(`--fast` 時は低解像度)。
- 無料。MIT ライセンスで、著作権表示とライセンス文の保持が条件。SaaS ではなくローカル実行のみ。
- ネイティブモジュールのロードに失敗する場合、README は `--build-from-source` を付けた再インストールを案内している(ビルドツールチェーンが必要)。

## 最短手順

- 1) 依存を用意: `ffmpeg` / `ffprobe` を PATH に通し、`npm i -g editly@next`(0.15 系)または `npm i -g editly`(0.14.2)。
- 2) 最小スペックを spec.json5 として保存:
- { outPath: 'out.mp4', width: 1280, height: 720, fps: 30, defaults: { duration: 3, transition: { name: 'random', duration: 0.5 } }, clips: [ { layers: [ { type: 'title', text: 'Hello Editly' } ] }, { duration: 4, layers: [ { type: 'video', path: 'clip.mp4', cutFrom: 2, cutTo: 6 } ] } ], audioFilePath: 'music.mp3' }
- 3) 実行: `editly spec.json5 --out out.mp4`(`--fast` で低解像度プレビュー)。
- 4) AIエージェントから呼ぶ手順: ツール実行1回で `editly spec.json5 --out /abs/path/out.mp4` を叩き、終了コードと出力ファイルの存在・サイズを確認する。素材パスは絶対パスで渡す。npx 経由なら `npx --yes editly@next spec.json5 --out out.mp4`。
- 5) その場で組み立てるなら JS API: `import editly from 'editly'; await editly({ outPath: 'out.mp4', clips: [{ layers: [{ type: 'title', text: 'Hi' }] }] });`
- 6) ネイティブビルドを避けるなら Docker: `docker compose run editly bash -c "cd examples && editly audio1.json5 --out /outputs/out.mp4"` の後 `docker cp editly:/outputs/out.mp4 .`。
- 7) 検証: `ffprobe -v error -show_entries format=duration,size -of json out.mp4` で尺とサイズを確認。

## 変更履歴

- 2026-11-07: 初回登録
