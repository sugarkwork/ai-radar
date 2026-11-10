---
repo: "Breakthrough/PySceneDetect"
name: "PySceneDetect"
genre: "video-gen"
url: "https://github.com/Breakthrough/PySceneDetect"
author: "Brandon Castellano (Breakthrough)"
license: "BSD-3-Clause"
stars: 5413
language: "Python"
created: "2014-06-04"
updated: "2026-11-08"
forks: 564
open_issues: 62
size_kb: 211655
archived: false
commits_30d: 43
commits_90d: 83
commit_cadence: "daily"
last_release: "v0.7.3"
last_release_at: "2026-11-08"
flags: []
risk_notes: ["精度指標（F1 等）は開発元自身が公開するベンチマークの値で、第三者の独立再現やこちらの実機追試は行っていない。処理速度は未計測。", "docs サイト（scenedetect.com/docs/latest）は v0.7.1 のままで、v0.7.2 で変更された detect-hist（threshold 0.20 / bins 128）と detect-hash（threshold 0.35 / size 8）の既定値はリリースノート側の記載を優先した。CLI リファレンス上の既定値表示は 0.7.1 時点のもの。", "open_issues=65 は GitHub の open_issues_count で、実測では issue 57 件 + PR 8 件の合計。", "genre=video-gen は分類上の近似。実体は映像の生成モデルではなく、カット検出・分割・フレーム抽出の解析ツール。"]
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-09T21:44:10Z"
---

# PySceneDetect — シーンカットを自動検出して長尺動画を分割・フレーム抽出する BSD-3-Clause の OSS

## 出来ること

- ハードカット検出: ContentDetector が隣接フレームの HSV 色差をスコア化（既定 threshold=27.0、min_scene_len=0.6s）。速いカメラ移動が多い映像では2パス方式の AdaptiveDetector（既定 threshold=3.0、window_width=2、min_content_val=15.0）が誤検出を抑える。
- 別系統の検出器: HistogramDetector（YUV の Y ヒストグラム差、フェードに強い）、HashDetector（知覚ハッシュのハミング距離）、ThresholdDetector（RGB 平均輝度によるフェードイン/アウト検出）。
- 検出結果に基づく動画分割: `split-video` が ffmpeg または mkvmerge を呼び出してシーンごとにファイル化（`--copy` で再エンコードなし、`-crf`/`-p` で画質指定）。
- プレビュー画像の抽出: `save-images` が各シーンの代表フレームを保存（既定3枚/シーン、`-n` で枚数、`-j`/`-p`/`-w` で JPEG/PNG/WebP、`-W`/`-H` でサイズ指定）。
- 編集ソフト向けのシーンリスト出力: CSV（`list-scenes`）、EDL、FCP7 XML / FCPXML、OTIO タイムライン、HTML、Aegisub 互換キーフレーム（`save-keyframes`、0.7.2 で追加）。
- Python API: `detect()` の1行呼び出しから、`open_video` + `SceneManager` + 検出器の組み合わせ、`split_video_ffmpeg` まで利用可能。映像入力を丸ごとメモリに載せずフレーム単位で処理する。

## 目的・背景

- 長尺の録画素材を編集前に整理する用途。カット点を人手で探す代わりに、シーン境界のタイムコード・フレーム番号を機械的に列挙し、分割やサムネイル生成まで一気に進められる。
- 2014年6月から継続するプロジェクトで、最新リリースは v0.7.2（2026-10-12 公開）。直近30日で34コミット、90日で74コミット、最終 push は 2026-11-07 と現在も活発に保守されている。
- ライセンスは BSD-3-Clause（LICENSE 冒頭が "BSD 3-Clause License / Copyright (C) 2014, Brandon Castellano"）。無料の OSS で、ソース・バイナリの再配布と商用利用が可能（再配布時は著作権表示と免責条項の同梱などの条件あり）。
- Python パッケージ名は `scenedetect`。OpenCV ベースの画像処理で完結するため、GPU やクラウド API を必要としない。

## 依存関係

- Python 3.10 以上。
- 必須（PyPI メタデータ）: click（~=8.0、8.3.0 のみ除外）、numpy、opencv-python、platformdirs、tqdm。
- 任意: pyav（av>=9.2）、moviepy をバックエンドとして追加可能。OpenCV を入れたくない場合は opencv-python-headless を使う `scenedetect-headless` を選択。
- 外部バイナリ: 動画分割（`split-video`）に ffmpeg または mkvmerge が必要。検出と画像抽出自体は Python 依存のみで動く。
- 依存を全部入りにしたい場合は Docker イメージ `ghcr.io/breakthrough/pyscenedetect`（ffmpeg/mkvmerge 同梱）。

## 実行条件

- CPU のみで動作（GPU 不要）。処理時間は動画の長さ・解像度に比例する。
- 入力は動画ファイルのほか画像シーケンスや URL も指定可能（`-i`）。
- 速度調整: `-d/--downscale`（既定は解像度に応じて自動、`-d 1` で無効）と `-fs/--frame-skip`（`-fs 1` で半分のフレームのみ処理）。精度と引き換えに高速化できる。
- 既定バックエンドは opencv。VFR 動画では `save-keyframes` のフレーム番号が概算になる（0.7.2 リリースノート記載の既知制限）。
- 閾値は素材依存。既定値のまま誤検出が多い場合は `-s` でフレームスコアを CSV 出力し、`content_val` の分布を見てから `-t` を調整する。

## 最短手順

- 1) インストール: `pip install scenedetect --upgrade`（Docker なら `docker run --rm -v "$(pwd):/files" ghcr.io/breakthrough/pyscenedetect -i /files/input.mp4 split-video -o /files`）。
- 2) AI エージェントからの基本呼び出し: `scenedetect -i input.mp4 detect-adaptive list-scenes split-video` → シーン一覧 CSV と分割済みクリップが出力ディレクトリに生成される。
- 3) サムネイルだけ欲しい場合: `scenedetect -i input.mp4 detect-content -t 27 save-images -n 3 -o frames/`。
- 4) フェードが多い素材: `scenedetect -i input.mp4 detect-threshold list-scenes`。ハードカットと併用したい場合は検出器コマンドを複数指定する。
- 5) Python から: `from scenedetect import detect, ContentDetector` / `scene_list = detect("input.mp4", ContentDetector())` → 返り値は各シーンの開始・終了フレームとタイムコードのタプル列。分割まで行うなら `split_video_ffmpeg("input.mp4", scene_list)`。
- 6) エージェント側では生成された `*-Scenes.csv` を読むか `scene_list` を JSON 化して受け取り、後続の編集・要約処理に渡す。閾値の再調整が必要なら `-s stats.csv` でフレームスコアを取得して `content_val` を見る。

## 変更履歴

- 2026-11-07: 初回登録
