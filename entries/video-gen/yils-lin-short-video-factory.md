---
type: "repo"
name: "short-video-factory（AI Short Video Factory / 短视频工厂）"
genre: "video-gen"
url: "https://github.com/YILS-LIN/short-video-factory"
repo: "YILS-LIN/short-video-factory"
license: "AGPL-3.0"
stars: 6095
language: "TypeScript"
created: "2025-07-09"
updated: "2026-11-09"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① GUI 専用で CLI も bin も無い。操作は Electron の IPC 経由のみで、エージェントから直接叩ける入り口が無い（自動化するなら UI 操作か中間ファイルの再利用）。② AGPL-3.0 のため、改変して配布・SaaS 提供する場合はソース開示義務が及ぶ。③ LLM は外部 API キーが必須で、同梱モデルは無い。ローカル運用は OpenAI 互換サーバを apiUrl に入れる形でしか成立せず、README・公式ドキュメントに手順が無い（未検証）。④ TTS は EdgeTTS のみ。キー不要な代わりに Microsoft の公開エンドポイント依存で、v1.3.0 でも認証変更による 403 を修正した履歴がある。他 TTS は roadmap の未着手項目。⑤ 本番ビルドは匿名利用統計を stat.yils.blog へ送る実装があり、README にオプトアウトの記載が無い。⑥ Electron 22（2022年）で、サポートは既に終了している。⑦ ★6,058 に対し v1.3.0 の Windows setup の DL は 1,065 で、スター数は利用実績の指標にならない。⑧ リリース間隔が空く（v1.2.2 が 2026-04、v1.3.0 が 2026-10）。⑨ リポジトリは 8,621KB だが配布物は 107〜267MB（ffmpeg 同梱）。"
forks: 836
open_issues: 18
commits_30d: 26
size_kb: 8757
archived: false
commits_90d: 44
commit_cadence: "daily"
fetched_at: "2026-11-09T21:47:07Z"
last_release: "v1.4.0"
last_release_at: "2026-11-09"
---

# short-video-factory — 台本生成・読み上げ・字幕・自動編集を1つのデスクトップアプリに畳んだ縦型ショート量産ツール

## 出来ること

- プロンプトから台本を生成する。接続先は OpenAI 互換 / OpenAI Chat / OpenAI Responses / Anthropic Messages の4プロトコルで、独自ヘッダ、temperature・top_p・最大出力トークン、システムプロンプトの差し替えまで設定画面から触れる
- 生成文の類似度を測り、閾値を超えたら自動で書き直す「多様性」制御を持つ。同じ商品で似た台本が並ぶのを避けるための仕組み
- EdgeTTS で台本を読み上げ、SRT 字幕を起こし、ffmpeg で映像・音声・字幕を合成する。v1.3.0 で字幕レンダリングエンジンが変わり、映像とは別に SRT 単体でも書き出せる
- シーンごとに素材クリップを自動で割り当てて混剪する。尺の指定に対して複数素材から選び、プレビューと本番で同じ素材列を再現できる
- プリセットを保存し、バッチタスクで連続レンダリングする。1本ずつGUIで操作せず、素材と設定を置いたら回し続ける使い方
- pixi.js ベースのエフェクト／字幕演出、中国語・英語のUI切り替え、SQLite への素材・プリセット保存、診断情報のエクスポート、アプリ内アップデート確認

## 目的・背景

- 商品マーケティング用や引用・啓発系の縦型ショートを、動画編集ソフトの操作を覚えずに量産するのが目的。素材は手元のクリップ、文字起こしと編集はアプリ内で完結する
- 「編集機能」より「工程の連結」が本体で、台本→読み上げ→字幕→割り付け→書き出しが1画面の設定に収まっている。出力はプロジェクトファイルではなく mp4 と srt
- 作者は個人（YILS）。中国語圏の利用が中心で、WeChat の交流グループと百度・夸克网盘のミラーを案内している。英語READMEは用意されているが、詳細な使用手册は中国語の公式サイト側
- スポンサー枠にクラウド事業者（Jalapeno Cloud、Seedance の供給元）が入っており、映像生成AIそのものは内蔵していない。あくまで手持ち素材の編集側

## 依存関係

- LLM: 外部APIキーが必須。同梱モデルもローカル推論も無い。ローカルモデルは「OpenAI 互換で待ち受けるサーバを apiUrl に指定する」形でのみ成立するが、README・公式ドキュメントに手順は無く未検証
- TTS: EdgeTTS のみ（無料・キー不要）。Microsoft の公開エンドポイントに依存するため、仕様変更で 403 になる履歴があり、v1.3.0 で修正済み。他の TTS API は roadmap の未着手項目
- 実行時: 同梱の ffmpeg-static、better-sqlite3（ネイティブ、prebuilt を同梱）、Electron 22、Vue 3 + Vuetify、pixi.js
- ビルド: Node.js 22.17.0 以上、pnpm 10.12.4（preinstall で pnpm 以外を拒否）、electron-builder、macOS の universal ビルドは lipo スクリプト

## 実行条件

- GUI 専用。package.json に bin は無く、CLI サブコマンドもヘッドレスAPIも無い。処理は Electron の IPC で起動するため、外部プロセスやエージェントから呼ぶ手段は用意されていない
- 配布ビルドは3種。v1.3.0 は Windows x64 の NSIS setup（106.7MB）、macOS universal の dmg（267.2MB）、Linux x86_64 の AppImage（147.7MB）。署名・公証の状態は README に記載が無い
- ネットワーク: 台本生成で LLM の API、読み上げで EdgeTTS のエンドポイントに接続する。素材の取り込みと書き出しはローカル
- 匿名の利用統計を本番ビルドで送信する実装がある（自前の Umami 互換エンドポイント）。README にオプトアウト手順の記載は無い
- ライセンスは AGPL-3.0。改変して配布したりホスト型サービスとして提供する場合はソース開示義務が及ぶ。社内利用の可否は組織の判断
- リポジトリは 8,621KB・231ファイルだが、配布物は ffmpeg 同梱で 100MB 超。★6,058 に対し v1.3.0 の Windows setup の DL は 1,065 で、スター数は利用実績の指標にならない

## 最短手順

配布ビルドを使う（v1.3.0、Linux の例）:

```bash
gh release download v1.3.0 -R YILS-LIN/short-video-factory -p '*linux-x86_64.AppImage'
chmod +x short-video-factory-1.3.0-linux-x86_64.AppImage
./short-video-factory-1.3.0-linux-x86_64.AppImage
```

- Windows は `short-video-factory-1.3.0-win-x64-setup.exe` を実行、macOS は `short-video-factory-1.3.0-mac-universal-installer.dmg` を開いて Applications へ
- 起動後、設定で LLM の protocol / apiUrl / apiKey / modelName を入れて接続テストを実行 → 素材フォルダを読み込む → プロンプトと尺・本数を指定して台本生成 → 音声合成 → 合成
- 量産はプリセットを保存し、バッチタスクに登録して連続実行する

ソースから動かす:

```bash
git clone --depth 1 https://github.com/YILS-LIN/short-video-factory.git
cd short-video-factory
pnpm install
pnpm dev     # 開発起動（Vite + Electron）
pnpm build   # 配布物を release/<version>/ に生成
```

## 変更履歴

- 2026-11-07: 初回登録
