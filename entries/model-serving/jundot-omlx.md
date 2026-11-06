---
type: "repo"
name: "oMLX（Apple Silicon向けLLM推論サーバ、メニューバーから管理）"
genre: "model-serving"
url: "https://github.com/jundot/omlx"
repo: "jundot/omlx"
license: "Apache-2.0"
stars: 23405
language: "Python"
created: "2026-02-13"
updated: 2026-11-05
added: "2026-11-06"
first_seen: "2026-11-05"
sources: ["https://x.com/ai_hakase_/status/2118132025563468009", "https://omlx.ai"]
flags: []
risk_notes: "**macOS 15.0 以降 + Apple Silicon 専用**。Linux/NVIDIA 機では動かない。ネイティブカスタムカーネル（GLM-5.2 / MiniMax M3 / Qwen3.5 系に必要）を有効にするにはフル Xcode と Metal ツールチェーンが要り、無い場合は汎用経路に静かにフォールバックして大幅に遅くなる（GLM-5.2 の fused DSA prefill で約30倍差、という作者計測）。公式DMGはカーネル同梱なのでXcode不要。投稿が主題にしている『2台のMacによる分散推論』は**開発版 v0.7.4.dev1 のみ**の機能で、安定版 v0.7.3 には入っていない。投稿の高速化率（DeepSeek V4.1 Flash の64Kプロンプトで+195%、3,123 tok/s）は作者計測で、独立検証はしていない。"
forks: 2101
open_issues: 537
commits_30d: 100
commit_cadence: daily
size_kb: 88582
archived: false
fetched_at: "2026-11-06T09:14:37Z"
last_release: v0.7.4.dev1
last_release_at: 2026-11-04
commits_90d: 100
---

# oMLX — Macのメニューバーから運用する、継続バッチング＋階層KVキャッシュ付きのLLM推論サーバ

## 出来ること

- Apple Silicon 上で **OpenAI互換API**（`http://localhost:8000/v1`）を立てる。LLM・VLM・embedding・reranker を、モデルディレクトリ配下のサブフォルダから自動で発見する
- **継続バッチング**で同時リクエストを捌く
- **階層KVキャッシュ**：ホットなメモリ層とコールドなSSD層の2段でKVを保持する。会話の途中でコンテキストが変わっても過去の文脈が残るので、長い会話の再計算を避けられる
- **メニューバーアプリ**で管理：モデルディレクトリの指定、サーバ起動、初回モデルのダウンロードまでを Welcome 画面が3ステップで案内する。日常モデルをメモリに固定し、重いモデルはオンデマンドで入れ替え、コンテキスト上限も設定できる
- 内蔵チャットUI（`http://localhost:8000/admin/chat`）と管理ダッシュボード
- **MCP対応（任意）**：`pip install mcp` して再起動すると読み込まれる
- 接続先として案内されているクライアント：OpenClaw、OpenCode、Codex、Hermes Agent、Copilot、DeepSeek Harness
- CLI：`omlx start` / `stop` / `restart` で常駐サーバを管理、`omlx serve --model-dir <path>` で前景実行。Homebrew の `brew services` にも委譲できる
- **分散推論（開発版のみ）**：2台のMacをペアリングし、プロンプトの先頭レイヤー計算を分担させる。大容量メモリ機（M3 Ultra 512GB など）と高GPU性能機（M5 Max など）の組み合わせを想定し、通信は Thunderbolt か 5GbE で足りる（RDMA 不要）。設定は Global Settings の「Enable Distributed Inference」とクラスタタブでのペアリング
- DeepSeek V4.1 / Qwen3.8 Flash-Next の個別最適化、TTSモデルのサポートも入っている

## 目的・背景

- 作者の問題意識は「既存のLLMサーバは便利さと制御のどちらかを諦めさせられる」。常用モデルをメモリにピン留めし、重いモデルは要求時に自動で入れ替え、コンテキスト上限を決め、それをメニューバーから操作したい、という要件から作られている
- 分散推論はプリフィル（プロンプトの先頭計算）がボトルネックだという観察から、レイヤー単位で2台に分割する方向を採っている。投稿では DeepSeek V4.1 Flash の64Kプロンプト処理が M5 Max 128GB との併用で最大 +195%（3,123 tok/s）と紹介されているが、これは作者計測
- 投稿は日本語圏のアカウントによる v0.7.4.dev1 のリリース告知で、**安定版は v0.7.3** であることが明記されている

## 依存関係

- macOS 15.0（Sequoia）以上、Python 3.11〜3.13、Apple Silicon（M1/M2/M3/M4/M5）
- 導入経路は3つ：公式 `.dmg`（カーネル同梱・アプリ内自動更新・`~/.omlx/bin/omlx` CLIシム付き）、Homebrew（`brew tap jundot/omlx https://github.com/jundot/omlx` → `brew install jundot/omlx/omlx`）、ソースから（`make install`）
- **ネイティブカスタムカーネル**を使うにはフル Xcode と Metal ツールチェーン（`xcodebuild -downloadComponent MetalToolchain`）。Command Line Tools だけでは足りない
- MCP を使う場合は `pip install mcp` してから `omlx restart`
- モデルは `~/.omlx/models` など指定ディレクトリに置く（`OMLX_MODEL_DIR` / `OMLX_PORT` などの環境変数、または `~/.omlx/settings.json`）

## 実行条件

- **Apple Silicon の Mac 専用**。Intel Mac、Linux、Windows は対象外
- GLM-5.2 / MiniMax M3 / Qwen3.5 系は**カスタムカーネルが実質必須**。無いと汎用経路に静かに落ちて大幅に遅くなり、メモリ使用量も増える。導入後に `python -c "from omlx.custom_kernels import native_kernel_status; print(native_kernel_status())"` で確認できる
- 分散推論は **v0.7.4.dev1（開発版）のみ**。安定運用したい場合は v0.7.3 を使う、と投稿も README も案内している
- ログは `$(brew --prefix)/var/log/omlx.log`（サービス）と `~/.omlx/logs/server.log`（構造化ログ）

## 最短手順

```bash
# 1) 入れる（いちばん簡単なのは公式DMG: Releases から .dmg を取得して Applications へ）
#    Homebrew を使う場合:
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx --with-custom-kernel   # カーネル込み（フルXcodeが必要）
#    フルXcode が無い場合はカーネル無しで:
#    brew install jundot/omlx/omlx

# 2) 常駐サーバとして起動
omlx start

# 3) モデルディレクトリを指定して前景で動かす場合
omlx serve --model-dir ~/models
#   OpenAI互換: http://localhost:8000/v1
#   チャットUI:  http://localhost:8000/admin/chat

# 4) カスタムカーネルが効いているか確認
python -c "from omlx.custom_kernels import native_kernel_status; print(native_kernel_status())"

# 5) MCP を使う場合
/opt/homebrew/opt/omlx/libexec/bin/pip install mcp
omlx restart
```

## 変更履歴

- 2026-11-06: 初回登録
