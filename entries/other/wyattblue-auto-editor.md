---
repo: "WyattBlue/auto-editor"
name: "Auto-Editor"
genre: "other"
url: "https://github.com/WyattBlue/auto-editor"
license: "Unlicense"
stars: 5824
language: "Nim"
created: "2020-04-30"
updated: "2026-11-08"
forks: 725
open_issues: 0
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 121526
archived: false
flags: ["unverified"]
risk_notes: "commits_30d/90d は GitHub API の per_page=100 上限に達しており、実数は100件超（30日窓で返った最古のコミットが 2026-10-19）。効果の測定は合成素材1本（10秒・320x240）で行ったもので、実収録でのカット精度や話し言葉の語尾保持は独立検証していない。PyPI 版は 29.3.1（2025-11-04）で更新が止まっており pip 導入は非推奨。24時間超の素材、字幕・データストリームのみの入力は非対応。"
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-09T21:41:35Z"
last_release: "31.8.0"
last_release_at: "2026-10-30"
---

# Auto-Editor — 無音カットで粗編集を自動化する動画編集CLI

## 出来ること

- 音声のラウドネス（既定 `audio:threshold=0.04`）、モーション、黒フレーム、字幕の語句一致から「切る区間」を判定し、初稿を書き出す。入力は動画・音声のほか、yt-dlp 導入時の URL、`:mic` でのマイク録音にも対応
- `--margin` でカット前後に残す余白を調整する。既定は 0.2 秒で、`--margin 0.3s,1.5sec` のように前半と後半を別々に指定できる。`--smooth 0.2s,0.1s` は短すぎるカットとクリップを間引く
- ラベルを増やして段階制御できる。`--edit:2 audio:-12dB --when:2 speed:1.5` で「無音はカット、小さい音はそのまま、大きい音は1.5倍速」を1コマンドで書ける（ラベルは 0-255、重なった場合は大きい番号が優先）
- 手動レンジを自動判定と併用できる：`--cut 0,30`（先頭30フレームを削除）、`--keep 0,30sec`（先頭30秒を強制保持）、`--set-speed 2,0,30`（2倍速）。`--edit 1` / `--edit 0` で自動判定を止め、手動編集だけにもできる
- NLE への受け渡し：`--export premiere`、`--export resolve`（.fcpxml を生成）、`final-cut-pro`、`shotcut`、`kdenlive`、`clip-sequence`。実際に Resolve 向け .fcpxml の生成を確認
- `--preview`（`--stats`）で書き出さずにカット量を確認できる。10秒の合成素材では output 5.70 秒（-43%）、clips 2 / cuts 2 と表示された
- 書き出しの調整：`-b:v 230k`（ビットレート指定）、`-crf 23`（品質ベース）、`-c:v hevc`、`--scale 0.5`（解像度半減）、`-anorm ebu`（EBU R128 ラウドネス正規化）

## 目的・背景

- 本編集の前に、長い収録から無音（デッドスペース）を切り落とす「ファーストパス」を自動化する道具。README は「Before doing the real editing, you first cut out the "dead space" which is typically silence. This is known as a "first pass".」と位置づけている
- 作者 WyattBlue が Nim で実装し、2020-04-30 に公開。現在 5803 stars / 720 forks、最終 push は 2026-11-07。GitHub のオープン Issue は 0 件で、 bug tracker は Discussions を指している
- CLI 本体は Unlicense（パブリックドメイン）。同じ作者の GUI アプリ（app.auto-editor.com）は別製品で、リポジトリの資産は Unlicense、アプリ固有の資産は別ライセンスと README に明記されている
- 投稿の「Remove silent sections / adjust the padding around cuts」という説明は、README の `--margin` の説明と一致する。ただし投稿は発見源として扱い、性能の根拠にはしていない

## 依存関係

- 公式バイナリ（Releases）は FFmpeg を静的リンクした自己完結ビルド。PATH から ffmpeg/ffprobe を外した状態（`env PATH=/usr/bin:/bin`）でも 31.8.0 が動作し、カットと再エンコードが通った
- ソースからビルドする場合のみツールチェーンが必要：nim / nimble / cmake / meson / ninja。`nimble makeff` で依存を取得して静的ビルド、`nimble brewmake` は FFmpeg ライブラリを要求する動的ビルド
- 任意：yt-dlp を入れると URL を直接入力できる。Python は不要。PyPI の auto-editor は 29.3.1（2025-11-04）で止まっており、公式ドキュメントは「The auto-editor cli is no longer being published on pip.」と明記している
- GUI アプリは別製品。無料評価は 6 回・3200x1800 までで、以降は買い切りライセンス（価格は公式サイトの checkout を参照）

## 実行条件

- OS：Windows（x86_64 / aarch64）、macOS（arm64）、Linux（x86_64 / aarch64 / armv7）の公式バイナリ。macOS・Linux は `chmod +x` が必要で、未署名のため「Unknown developer」警告が出る
- 入力の制約：字幕・データストリームのみのファイルは不可。映像・音声は24時間以下、フレーム数は 60fps×24時間相当まで。対応コーデックは同梱 FFmpeg に依存する
- 判定は音量ベースなので、定常ノイズや BGM が乗った素材では無音を誤判定しうる。`--edit motion` への切り替え、閾値（`audio:-19dB` など）の調整、`--preview` での下見を前提にする
- 出力は再エンコードされる。既定は品質優先でファイルが大きくなりやすく、`-b:v` / `-crf` で調整する。処理時間は素材長とエンコーダ次第（10秒・320x240 の合成素材では 0.3 秒）
- ライセンスは Unlicense のため商用利用・改変・再配布に制限はない。ただし Releases のバイナリは「may be under various open source licenses」と README にある

## 最短手順

- 公式バイナリを取得する（Linux x86_64・31.8.0 の例）：
```
curl -L -o auto-editor https://github.com/WyattBlue/auto-editor/releases/download/31.8.0/auto-editor-linux-x86_64
chmod +x auto-editor
./auto-editor --version   # => 31.8.0
```
macOS は `brew install auto-editor`、Arch Linux は `yay -S auto-editor` でも入る
- まず下見。書き出さずにカット量を確認する：
```
./auto-editor input.mp4 --preview
```
- 既定（音声閾値 0.04、前後 0.2 秒の余白）で書き出す：
```
./auto-editor input.mp4 --margin 0.2sec -o cut.mp4
```
語尾が切れるときは後ろ側を伸ばす：`--margin 0.3s,1.5sec`
- NLE に渡す（DaVinci Resolve の例。.fcpxml が生成される）：
```
./auto-editor input.mp4 --export resolve -o timeline.fcpxml
```
- AI エージェントから呼ぶ。リポジトリ同梱の Skill を追加すると、Claude Code などがコマンド体系を読んだ状態で操作できる：
```
npx skills add WyattBlue/auto-editor
```
エージェントのシェルツールからは、下見→実行の2段が安全：
```
auto-editor input.mp4 --preview
auto-editor input.mp4 --edit audio:threshold=0.04 --margin 0.2sec -o cut.mp4
```
長い素材では `--preview` の output 秒数と clips/cuts 件数を読ませてから本実行する

## 変更履歴

- 2026-11-07: 初回登録
