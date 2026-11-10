---
repo: "MTG/essentia"
name: "Essentia"
genre: "tts-audio"
url: "https://github.com/MTG/essentia"
license: "AGPL-3.0"
stars: 3801
language: "C++"
created: "2013-06-03"
updated: "2026-11-05"
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 644
open_issues: 448
commits_30d: 15
commits_90d: 37
commit_cadence: "weekly"
size_kb: 314150
archived: false
fetched_at: "2026-11-09T21:43:21Z"
last_release: "v2.0.1"
last_release_at: "2014-02-11"
---

# Essentia

## 出来ること

- 音声・音楽の解析ライブラリ（C++ 実装、Python バインディング付き）。BPM・キー・コード・ラウドネス・スペクトル特徴・MFCC・オンセット検出など数百のアルゴリズムを提供。
- 音楽情報検索（MIR）向けの特徴量抽出をまとめて回せる。バッチ処理向けの CLI（`essentia_streaming_extractor_music`）も同梱。
- **生成ではなく解析**のツール。音声生成パイプラインの前処理・評価（テンポ／ラウドネス正規化など）に使う位置づけ。

## 目的・背景

バルセロナ UPF の Music Technology Group による 2013 年からの長期プロジェクト。音楽解析の学術標準のひとつで、Freesound や AcousticBrainz の基盤にも使われた。ポストでは音声系10選に混ぜて紹介されているが、他の9つ（生成・変換・分離）とは役割が異なる。

## 依存関係

- Python から使う場合: `pip install essentia`（Linux x86_64 / i686 の wheel あり）。TensorFlow 連携版は `pip install essentia-tensorflow`。
- C++ から使う場合は CMake ビルド＋FFmpeg / libav 系の依存。

## 実行条件

- **AGPL-3.0**。生成物やネットワーク越しの提供に AGPL の条件が及ぶため、商用サービスに組み込む場合は法務確認が必要。
- Linux x86_64 の wheel が前提。macOS / Windows は自前ビルドまたは未提供＝未確認。
- 解析のみなので GPU 不要。

## 最短手順

```bash
pip install essentia
python -c "import essentia.standard as es; a=es.MonoLoader(filename='t.wav')(); print(es.RhythmExtractor2013()(a)[0])"
```

## 変更履歴

- 2026-11-03: 初回登録（star 3,791 / pushed 2026-10-22 / AGPL-3.0）
