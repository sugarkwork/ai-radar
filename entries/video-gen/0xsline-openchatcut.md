---
repo: "0xsline/OpenChatCut"
name: "OpenChatCut"
genre: "video-gen"
url: "https://github.com/0xsline/OpenChatCut"
license: "AGPL-3.0"
stars: 3021
language: "TypeScript"
created: "2026-07-15"
updated: "2026-11-06"
forks: 453
open_issues: 31
commits_30d: 67
commit_cadence: "daily"
commits_90d: 100
size_kb: 122864
archived: false
author: "0xsline"
flags: ["unverified"]
risk_notes: "同一性: forkではなく上流そのもの（fork=false、parentなし）。効果測定は作者自身のM4 Max 1台・2セグメントのみの予備計測で、第三者による再現やプロジェクト全体の速度検証はない。MCP経由の編集フロー（begin_edit_session→review_edit_session→承認）はREADME記載であり、当方ではアプリを実行して動作確認していない。macOSビルドは未署名・未公証で初回に手動許可が必要。ライセンスは AGPL-3.0 のため、改変版をネットワークサービスとして提供するとソース開示義務が生じる。MCPブリッジは単一ユーザー・単一マシン前提でマルチテナント非対応。スキル数「26」はREADME記載の値で、レート制限によりディレクトリを直接数えて照合できていない。"
last_release: "v0.2.17"
last_release_at: "2026-10-15"
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-09T21:43:47Z"
---

# OpenChatCut — 実タイムラインをMCP経由でAIエージェントが編集するローカル優先のOSS動画エディタ

## 出来ること

- マルチトラックの実タイムライン（映像・音声、移動/トリム/分割/リップル、トランジション、LUT、クロマキー、キーフレーム、WebGLエフェクト）を自然言語の指示で編集し、生成物ではなく後から手編集・undoできるプロジェクトとして保持する。
- 文字起こしベース編集: 単語単位のテキスト編集、無音・言い直しの圧縮、話者分離、字幕の自動生成・翻訳・SRT書き出し。
- Codex / Claude Code など外部MCPクライアントから、ビルトインエージェントと同一の編集ツールを呼ぶ。編集はまず下書きとして作られ、内容を確認して承認すると1回のundo単位でタイムラインに原子的に適用される。
- 書き出し: MP4（VideoToolbox / NVENC のハードウェア支援、フォールバックでソフトウェア）、音声、字幕、FCPXML、プロジェクト全体。Remotion + FFmpeg でレンダリング。
- 画像・動画・音声・音楽・効果音の生成ジョブ、オンライン素材検索、モーショングラフィックステンプレート、人物セグメンテーションによる字幕の顔よけ・自動リフレーム。
- Agent Skill を同梱し、`npx skills add 0xsline/OpenChatCut` でクライアント側に入れて『Set up OpenChatCut』と指示するとMCP接続が登録され、専門スキルを必要時に読み込む構成（READMEでは26スキルと記載）。

## 目的・背景

- 商用 ChatCut の代替を名乗る独立したOSS（AGPL、ChatCut社とは無関係）。ワンショット生成で編集不能な動画が出るツールでも、タイムライン操作だけの従来型エディタでもなく、会話による指示とトラック/クリップ単位の精密編集を同じプロジェクトで扱うことを狙う。
- 背景にある問題意識は「AIに編集させると結果が編集不能な塊になる」こと。ここでは全ての変更が tracks / clips / transitions / captions / effects として実データに書き込まれ、差分の確認・却下・undoが可能なまま残る。
- プロジェクトとメディアは既定でローカル（~/.openchatcut）に保存し、APIキーはサーバ側に置く設計。クラウド機能はキーを設定したものだけが有効になり、未設定でもローカル編集は動く。

## 依存関係

- ソースから動かす場合: Node.js 24.22.1 以上 25 未満 + npm（package.json の engines で強制、.nvmrc あり）。
- デスクトップ版: Electron 43。プレビューと書き出し: Remotion 4 と ffmpeg-static（FFmpegの別途インストールは不要）。
- MCP: @modelcontextprotocol/sdk による Streamable HTTP サーバ。クライアントは Codex（app/CLI）、Claude Code、Qoder、Qwen Work（千问办公）をREADMEが明示。
- ビルトインエージェントのモデル: 各社APIキー（Anthropic/OpenAI/Gemini ほか）、または Codex CLI 0.146.0 以上のサブスクリプション連携。Claude はサブスク認証ではなく Claude Code 側のMCP接続を使う。
- 任意: 画像/動画/音声生成・文字起こし・Web検索（Firecrawl または Parallel）は対応サービスのAPIキー設定時のみ有効。ONNX Runtime（人物セグメンテーション）は Linux x64 で任意のCUDAプロバイダを追加ダウンロード。
- DaVinci Resolve / Premiere への依存はない（FCPXML書き出しで受け渡し可能）。Python は不要。

## 実行条件

- 配布ビルド: macOS（Apple Silicon / Intel の DMG）、Windows x64、Linux x64 AppImage。macOS版は未署名・未公証のため初回起動時にOS側の手動許可が要る。
- ソース実行はブラウザのセキュアコンテキスト必須。http://localhost か http://127.0.0.1、またはHTTPSで開く。LAN IPやリバースプロキシの平文HTTPでは Web Crypto / WebCodecs / クリップボードが無効になりエディタが開かない。
- MCPでタイムラインを触るにはエディタを起動して対象プロジェクトを開いておく（一覧・作成・移動系ツールのみ未起動でも可）。
- MCPを外部公開する場合は OPENCHATCUT_MCP_TOKEN と OPENCHATCUT_EDITOR_URL を設定し、ネットワークを制限する。単一ユーザー・単一マシン前提でマルチテナント用途には向かない。
- ライセンスは AGPL-3.0。改変版をネットワーク越しに提供する場合はソース開示義務が生じる。

## 最短手順

- 1. 導入: Releases のインストーラ（v0.2.17）を使うか、ソースなら Node 24 系で `npm install` → `cp .env.example .env.local` → `npm run dev` し、http://localhost:5199 を開く（デスクトップ開発は `npm run desktop:dev`）。
- 2. スキルの導入: `npx skills add 0xsline/OpenChatCut` を実行し、エージェントに `Set up OpenChatCut` と指示する。ルータとなるスキルがMCP接続を登録し、専門スキルを必要時に読み込む。
- 3. Codex の設定（~/.codex/config.toml）:
[mcp_servers.openchatcut]
url = "http://localhost:5199/api/external-mcp/mcp"
- 4. Claude Code の設定:
claude mcp add --transport http openchatcut http://localhost:5199/api/external-mcp/mcp
リポジトリ同梱の .mcp.json は次の内容:
{"mcpServers":{"openchatcut":{"type":"http","url":"http://localhost:5199/api/external-mcp/mcp","headers":{"x-openchatcut-mcp-client":"claude-code","x-openchatcut-mcp-surface":"external"}}}}
- 5. 使い方: OpenChatCutでプロジェクトを開いた状態で、エージェントに「begin_edit_session で編集セッションを開始し、8秒の位置の第2音声トラックに効果音を追加、隣接クリップ間にグリッチトランジションを入れて review_edit_session で提出、承認待ちにして」と依頼する。approvalMode は manual（既定）か auto。manual ならエディタ上でプレビュー→選択→承認/却下、auto なら review_edit_session で即適用。適用結果は1回のundoで戻せる。
- 6. 注意: 外部セッションで公開されるのは下書き安全な読み書きツールのみ。生成・書き出し・プロジェクト削除など即時副作用のあるツールは、却下時に巻き戻せないため外部セッションからは使えない。

## 変更履歴

- 2026-11-07: 初回登録
