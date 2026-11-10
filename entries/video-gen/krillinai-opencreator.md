---
type: "repo"
name: "OpenCreator"
genre: "video-gen"
url: "https://github.com/krillinai/OpenCreator"
repo: "krillinai/OpenCreator"
license: "Apache-2.0"
stars: 14269
language: "TypeScript"
created: "2024-12-17"
updated: "2026-11-09"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 旧 KrillinAI（動画翻訳・吹替）のリポジトリを改名・拡張したもので、14,191★の大半は KrillinAI 時代に付いた。現行の Codex ベース構成になってからの実績を示す数字ではない。② エージェントループは自前実装ではなく Codex CLI そのもの。モデル利用料は Codex 側（ChatGPT サインインか API キー）で、OpenCreator はその周囲の Runtime・UI・制作ツールを足す立場。③ コードは Apache-2.0 だが、アカウント・サブスク・クレジット・公式モデルサービスは open-creator.ai の Gateway 経由（Stripe Checkout / Billing Portal、ブラウザでのデバイス認証）。ローカル完結も可能だが、その場合は外部プロバイダのキーを自分で用意する。④ Desktop 配布は macOS arm64/x64 と Windows x64 のみで Linux 版は無い。Linux はソースからの Web か KrillinAI CLI アーカイブになる。⑤ リポジトリは約390MB（mp4 デモ約186MB、template 約52MB、assets 209MB）。--depth 1 でも取得量はほぼ変わらない。⑥ 発見元の「編集」は字幕編集・原稿編集が中心で、タイムライン型の動画編集は無い。Auto Clips と Digital Avatar は README 上 In development。⑦ CLI（krillinai-cli）は Go 製で、ソースからのビルドには Go ツールチェーンが要る（`.runtime/build` に出力）。リリースの tar.gz は約12MB で Go 不要だが、アーカイブ内の実行ファイル配置は未確認。⑧ CLI は `config/config.toml` をプロセス cwd から読む仕様で、作業ディレクトリ依存の罠がある。⑨ ffmpeg/ffprobe/yt-dlp は CLI 経路では自前で PATH に置く必要がある（Desktop は yt-dlp を同梱管理）。⑩ commits_30d の 100 は GitHub API の取得上限に当たっている可能性がある。"
forks: 1590
open_issues: 47
commits_30d: 100
size_kb: 399603
archived: false
commits_90d: 100
commit_cadence: "daily"
fetched_at: "2026-11-09T21:45:26Z"
last_release: "v3.3.1"
last_release_at: "2026-11-08"
---

# OpenCreator — Codex を実行エンジンにした制作ワークスペース（旧 KrillinAI）

## 出来ること

- 動画翻訳: ローカル/公開動画を取り込み、クラウドまたはローカルの Whisper 系で文字起こし → LLM で文分割・用語・翻訳 → バイリンガル字幕・吹替・声サンプル・字幕スタイル・横/縦構成を設定し、SRT・音声・動画で書き出し。元言語123・訳先124（ピンイン含む）
- 字幕だけの翻訳: SRT を読み込み、元動画・吹替・レンダリング無しで翻訳と確認ができる
- 字幕エディタ: 再生に同期した波形とタイムライン、キュー単位の分割・結合、置換、スタイルのプレビュー
- 動画ダウンローダ: YouTube / Bilibili / X / TikTok / Instagram / Douyin / Facebook / 小红书 / Pinterest / Reddit の単体動画を解析し、フォーマット比較のうえ動画か音声を保存。プラットフォーム字幕があれば SRT で取得
- 画像生成: GPT Image / Seedream 4.0 / Kling / Gemini（Nano Banana）をプロンプトと参照画像から。比率と枚数を指定して個別にダウンロード
- 動画生成: Seedance 2.5 / Kling v2.1 Master / Veo 3.1。比率・解像度・尺を設定し、生成し直しと版ごとの保存
- TTS: 原稿から声・速度・感情を選んでナレーション。Aliyun / OpenAI / MiniMax / Edge TTS / Volcengine に対応
- 記事・小红书投稿・ショート動画台本（トピックや素材から構成→本文、Markdown/HTML/PDF 書き出し）、棒人間アニメ（台本→ナレーション→絵コンテ→字幕→動画）、サムネ複数案の生成
- エージェント会話: Codex CLI をそのまま実行エンジンにし、プロジェクト単位の会話、バックグラウンド Run、承認、添付、Skills、MCP、スケジュール、メモリ、診断を1画面で扱う。可視ワークスペースと会話は同一の状態機械を共有する
- `skills/` に Codex Skill を7本同梱（CLI 操作、字幕、TTS、横レンダー、縦レンダー、カバー、pipeline の dry-run 検証）。エージェントが KrillinAI CLI を叩く形のワークフローになっている

## 目的・背景

- 旧 KrillinAI の改名・拡張版。README は「Agent ループを再実装しない」と明言し、OpenAI Codex をエンジンとして、その周りにローカル Runtime（Fastify デーモン）、React の可視ワークスペース、Electron ホストを被せる構成を取る
- 制作ツールはそれぞれ状態機械として実装され、視覚操作と自然言語の指示が同じ状態にイベントを投げる。現在の工程・設定・進捗・版・成果物が両方の画面に射影されるので、会話とワークスペースで作業をやり直さなくてよい
- データは既定でローカル。`.runtime/app.sqlite` にプロジェクト・Run・スケジュール・メモリ・承認が入り、デーモンは 127.0.0.1 のみで待ち受け、ヘルスチェック以外は Bearer トークンを要求する。資格情報は OS の資格情報ストアに置く
- 発見元の投稿の要約（台本・画像・ボイス・翻訳・編集を Codex に与える制作ワークスペース）は README の記載と概ね一致する。ただし「編集」の実体は字幕編集と原稿編集で、クリップを並べる動画編集ではない点は読み替えが必要

## 依存関係

- Codex CLI（実モデル実行に必須）。ChatGPT のサインインか API キー設定が必要。npm の `@openai/codex` は latest 0.167.0（2026-11-07 時点）
- Web をソースから動かす場合: Node.js 22 以上、pnpm 9.15.0（`packageManager` で固定）、corepack
- KrillinAI CLI をソースからビルドする場合: Go ツールチェーン（ビルドスクリプトが `go build` を呼び、`go version` をメタデータに記録する）、ffmpeg / ffprobe / yt-dlp
- 外部サービス: LLM は OpenAI 互換（base_url / api_key / model）、文字起こしは openai / fasterwhisper / whisperkit / whisper.cpp / aliyun / volcengine、TTS は openai / aliyun / edge-tts / minimax / volcengine、画像は OpenAI Images 互換
- アカウント: サインインはブラウザで `open-creator.ai/device` を開いて承認し、デーモンが独自セッションを取得する。サブスクとクレジットは Gateway 経由
- Desktop は Electron で、Web ビルドをそのまま読み OS 機能だけを足す

## 実行条件

- Desktop の配布物は macOS（arm64 / x64）と Windows x64 のみ。Linux 用のデスクトップ配布は無い
- ソースからの実行はリポジトリ全体の取得が前提で約390MB（mp4 デモ約186MB、template 52MB、assets 209MB）。`--depth 1` でも同規模
- ライセンスは Apache-2.0（コード）。ホスト版 Gateway と公式モデルサービスは別物として扱う
- UI は43言語、日本語 README は `docs/ja/README.md`
- CLI 単体でも字幕・吹替・レンダリング・カバー生成は動くが、可視ワークスペースと会話 UI は Web / Desktop 側。CLI だけでは「ワークスペース」にはならない
- open issues 43、直近30日のコミット 100（API 取得上限の可能性あり）、最終更新 2026-11-05

## 最短手順

- デスクトップ（最短）: https://github.com/krillinai/OpenCreator/releases/latest から macOS か Windows x64 のインストーラ（v3.3.0、約490〜540MB）を取得して起動。初回に既存の Codex 設定（サインイン/API キー）を再利用するか別プロバイダを入力する
- Codex CLI を先に用意する場合: `npm i -g @openai/codex && codex --version && codex login`
- Web をソースから: `git clone --depth 1 https://github.com/krillinai/OpenCreator.git && cd OpenCreator && corepack enable && pnpm install && pnpm web:dev` → `http://127.0.0.1:19861/`
- デーモンだけ動かす: `pnpm daemon:dev`（ループバックのみで待ち受け、接続先と一時トークンを stdout に1回だけ出す）
- CLI をリリースから使う: `KrillinAI-CLI-3.3.0-linux-x64.tar.gz`（約12MB）を取得して展開し、展開先ルートで `cp config/config-example.toml config/config.toml` を作って `[llm]` `[transcribe]` `[tts]` を埋める（アーカイブ内の実行ファイル名と配置は未確認）
- CLI をソースからビルド: `pnpm krillinai:build` → `KRX=$PWD/.runtime/build/krillinai/$(node -p "process.platform+'-'+process.arch")/bin/krillinai-cli`（同シェル）
- 字幕→縦動画の最小例: `cd runtime/krillinai && "$KRX" subtitle <URL or 動画パス> --origin-lang en --target-lang ja --workdir /abs/tasks/demo --prepare-video` → `"$KRX" render-vertical --workdir /abs/tasks/demo`
- CLI の成果物は `krillinai_manifest.json` を正とする。`--dry-run` でコマンド形を検証し、`pipeline` は dry-run 専用（本実行は `unsupported_command`）
- Codex のスキルとして使う場合: `skills/krillinai-*` を有効な `$CODEX_HOME` のスキルディレクトリに置く。OpenCreator 外の Codex で読み込めるかは未確認

## 変更履歴

- 2026-11-07: 初回登録
