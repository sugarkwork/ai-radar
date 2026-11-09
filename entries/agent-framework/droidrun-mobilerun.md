---
repo: "droidrun/mobilerun"
name: "Mobilerun"
genre: "agent-framework"
url: "https://github.com/droidrun/mobilerun"
author: "droidrun"
license: "MIT"
stars: 10004
language: "Python"
created: "2025-04-12"
updated: "2026-11-08"
forks: 1086
open_issues: 38
commits_30d: 94
commit_cadence: "daily"
commits_90d: 100
size_kb: 108480
archived: false
last_release: "v0.7.4"
last_release_at: "2026-10-27"
flags: ["unverified"]
risk_notes: "投稿の主張のうち一次情報で確認できたのは「root不要」「ADB経由で実機を操作」「MIT」まで。未確認/誤り: (1)「300+機種・40ブランド対応」は README・docs に記載がなく、要件は Android 8.0(API 26)+ のみ。(2)「家庭内Wi-FiのADBは誰でも命令できる抜け穴」は誤りで、公式docsは Android 11+ のワイヤレスデバッグにペアリングコード(or QR)による adb pair を必須と明記。(3)「3ツールのエージェントをMCPとしてClaude Codeに接続」は repo の実装と不一致。repo 内 mobilerun/mcp は外部MCPサーバーをツールとして取り込むクライアント側で、MCPサーバーは提供していない。コーディングエージェント連携は別リポジトリの Markdown スキル mobile-harness 経由。(4) エージェントの操作は9種(click/long_press/type/system_button/swipe/open_app/get_state/take_screenshot/complete)で「3ツール」ではない。(5)「1言でTelegramを開きChatGPTを入れる」動作は docs/README に実演記録がなく、Play Store 経由の自動インストールは未確認(Portal は URL からの APK インストールには対応)。(6) 引用記事 https://x.com/i/article/2109686434210693120 はログイン要求で本文未取得。(7) ベンチマーク 100% AndroidWorld / 98.34% iOSWorld はベンダー自己申告で第三者追試なし。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/N01ennn/status/2114070418394927499"]
fetched_at: "2026-11-09T13:09:34Z"
---

# Mobilerun — 実機Android/iOSを自然言語で操作するMITのモバイルエージェント基盤

## 出来ること

- 自然言語のゴールを渡すと、エージェントが画面を読み、tap・swipe・文字入力・アプリ起動まで自分で組み立てて実行する(Android 実機/エミュレータ、iOS 実機/シミュレータ)。
- UI の accessibility tree とスクリーンショットを併用する。ツリーが薄いアプリでは `--vision` / `--vision-only` でスクショのみ制御に切り替えられる。
- `--reasoning` で Manager が計画し Executor が操作する多段モード、既定の direct モードではエージェントが Python コードを生成して実行する。
- CLI(`mobilerun run`)・Python API(`MobileAgent`)・Docker の3経路。Pydantic による構造化出力、カスタムツール登録、アプリ別の指示を書く app cards、認証情報管理、Phoenix/Langfuse のトレースに対応。
- 複数端末の並列実行(端末ごとに `MobileAgent` を立てる)、trajectory の保存、QA/回帰テストや API の無いアプリからのデータ抽出に使える。
- LLM は Gemini・OpenAI・Anthropic・xAI・DeepSeek・Ollama・OpenRouter・OpenAI互換から選択。API キーか OAuth、ローカル Ollama なら無料で回せる。

## 目的・背景

- モバイルアプリのテスト/QA と、実機上で動く AI エージェントの実行を同じ基盤で扱うための OSS。Appium のようなセレクタ記述ではなく、ゴール文と画面状態から操作を決める。
- エージェントに渡すのは「画面を見る・タップする・入力する」に相当するモバイル専用ツール群で、汎用のコンピュータ操作ツールを画面サイズに流用する設計ではない。
- 本体は MIT。周辺は Portal(Android アプリ、Kotlin)、mobilerun-ios、iOS Portal、mobile-harness(エージェント向けスキル)、Mobilerun Cloud(ホスト型端末)に分かれており、クラウドは別課金の製品。
- 旧 droidrun 名からの移行期にあり、リポジトリ内に `compat/droidrun` の互換シムと `droidrun` 設定ディレクトリの記述が残る。2025-04-12 作成、現在 10,004 stars。

## 依存関係

- Python 3.11 / 3.12 / 3.13(3.14 は非対応)。`uv tool install mobilerun` または `uv pip install mobilerun`。
- Android Debug Bridge(adb)。端末側は Portal APK `com.mobilerun.portal` を推奨(アクセシビリティサービスで UI ツリー・ジェスチャ・スクショを提供)。Portal 無しでも `device.portal_mode: disabled` で ADB+UIAutomator のみ運用可。
- LLM プロバイダの API キー(`GOOGLE_API_KEY` / `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `XAI_API_KEY` / `DEEPSEEK_API_KEY` など)か、ローカル Ollama。Anthropic は `mobilerun[anthropic]` の追加インストールが必要。
- iOS 実機は `mobilerun-ios` と WebDriverAgent(USB)、シミュレータは iOS Portal アプリ。Linux では usbmuxd が要る。
- 主要依存: llama-index 系、mcp(1.28〜2.0)、async_adbutils、pydantic、httpx、mobilerun-sdk / mobilerun-core-local。

## 実行条件

- 端末で開発者オプションを有効化し、USB デバッグを ON。USB 接続して `adb devices` で `device` と出ること(初回は端末側で「常に許可」)。
- Android は 8.0(API 26)以上。Portal のファイル操作は Android 11 以上のみ。root は不要。
- Wi-Fi 運用は Android 11+ のワイヤレスデバッグで、端末に出るペアリングコードを使った `adb pair IP:PAIRING_PORT` が必須。同一ネットワーク上でもコード無しには接続できない。Android 10 以下は USB で `adb tcpip 5555` を一度実行する。
- Portal 利用時は初回に「他のアプリの上に重ねて表示」などを許可。スクショ・通知・不明なアプリのインストールは必要になった時だけ許可する。
- LLM の利用料は自前の API キーに発生する(フレームワーク自体は無料)。Mobilerun Cloud を使う場合のみ別途サブスクリプション。

## 最短手順

- 1. インストール: `uv tool install mobilerun`(Python 3.11〜3.13)。
- 2. 端末準備: USB 接続 → `mobilerun setup`(互換 Portal APK を取得して導入し、アクセシビリティサービスを有効化)→ `mobilerun ping` が「Portal is installed and accessible.」を返せば疎通OK。
- 3. LLM 設定: `mobilerun configure` でプロバイダ・認証方式・モデルを保存(または環境変数 `GOOGLE_API_KEY` 等)。
- 4. AI から呼ぶ最短経路(CLI): `mobilerun run "Open the settings app and tell me the Android version"`。複雑なタスクは `--reasoning --vision --steps 30`、画面のみのアプリは `--vision-only`。
- 5. AI から呼ぶ経路(Python API): `from mobilerun import MobileAgent, MobileConfig` → `agent = MobileAgent(goal="...", config=MobileConfig())` → `result = await agent.run()`。`result.success / reason / steps` をそのままエージェントの戻り値にできる。
- 6. コーディングエージェント(Claude Code / Codex)に操作させたい場合は、本体ではなく別リポジトリのスキルを使う: `npx skills add droidrun/mobile-harness`、またはエージェントに「Set up https://github.com/droidrun/mobile-harness for me. Read install.md ...」と渡す。Claude Code はプラグイン(`/plugin marketplace add droidrun/mobile-harness`)でも入る。
- 7. 注意: 本リポジトリは MCP サーバーを提供しない(`mobilerun/mcp` は外部 MCP ツールを取り込むクライアント側)。MCP 経由で繋ぎたい場合は Mobilerun Cloud 側の MCP を用いる。

## 変更履歴

- 2026-11-09: 初回登録
