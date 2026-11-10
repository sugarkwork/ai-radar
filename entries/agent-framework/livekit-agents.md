---
repo: "livekit/agents"
name: "LiveKit Agents"
genre: "agent-framework"
url: "https://github.com/livekit/agents"
author: "LiveKit"
license: "Apache-2.0"
stars: 15158
language: "Python"
created: "2023-10-19"
updated: "2026-11-09"
forks: 4108
open_issues: 949
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 52726
archived: false
last_release: "livekit-agents@1.8.11"
last_release_at: "2026-11-05"
flags: []
risk_notes: "フレームワーク本体は Apache-2.0 だが、ターン検出モデルは別条件の LiveKit Model License（README に明記）。LiveKit Inference 経由の v1 ターン検出、ノイズキャンセリング、電話番号などのクラウド機能は LiveKit Cloud 依存で、Cloud は Build が $0（月1,000 agent session 分）から、Ship は $50/月〜、Scale は $500/月〜。各 STT/LLM/TTS プロバイダの API 利用料は別途従量課金。ターン検出の精度数値はベンダー自身の測定で第三者検証はない。open_issues の 931 は PR を含む GitHub の集計値。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/opensourcelab9/status/2113397488862605824"]
fetched_at: "2026-11-09T21:33:38Z"
---

# LiveKit Agents — リアルタイム音声AIエージェントフレームワーク

## 出来ること

- 音声エージェントの骨格を Agent（指示とツールを持つ振る舞い）、AgentSession（対話の管理）、entrypoint（セッション開始点）、AgentServer（ジョブ配分と起動）の4要素で組み立てられる。
- ターン検出: 意味と音響特徴の両方から発話終端を予測する transformer モデルを AgentSession が既定で有効化し、話し終わり前のかぶせを減らす。VAD のみ、STT の end-of-turn 信号、realtime モデル側の検出、手動制御にも切り替えられる。
- STT・LLM・TTS・realtime API を自由に組み合わせて差し替えられる。deepgram / openai / cartesia / elevenlabs / google / aws / azure など多数のプラグインが同リポジトリで配布され、LiveKit Inference を使えば1つの認証で複数プロバイダのモデルを呼べる。
- 電話（SIP）連携: LiveKit の telephony スタック経由で発信・着信でき、発信コール用のサンプル（outbound-caller-python）が README から案内されている。
- マルチモーダル: 音声だけでなく映像も扱え、カメラ映像を見ながら応答する Gemini Live のサンプルや、Tavus / Bithuman / LemonSlice などのアバター連携例がある。
- MCP 連携: MCP サーバが提供するツールを1行でエージェントに接続できる（examples/voice_agents/mcp に mcp-agent.py と server.py が同梱）。
- テスト/評価: pytest ベースで対話を流し、イベント列の期待値を検証できる。.judge(llm, intent=...) で別の LLM に応答内容を採点させる仕組みを持つ。
- ジョブのスケジューリングとディスパッチ API、クライアントとの RPC / Data API、主要プラットフォーム向け WebRTC クライアント SDK と組み合わせて配信できる。

## 目的・背景

- リアルタイム音声AIを毎回ゼロから組み立てる負担（音声伝送、ターン制御、割り込み処理、モデル接続）を引き受けるフレームワーク。README は「サーバ上で動く、プログラム可能なリアルタイム参加者」を作るためのものと位置づけている。
- 開発元は WebRTC メディアサーバ LiveKit を手がける LiveKit 社。リポジトリは 2023-10-19 作成、現在 stars 15,144 / forks 4,095。
- 本体は Apache-2.0 の完全オープンソースで、LiveKit server を含めて自前インフラに置ける。マネージドに運用したい場合は LiveKit Cloud を使う。
- 開発は活発で、直近30日・90日はいずれも取得上限の100件に達するコミット数。最新リリースは livekit-agents@1.8.11（2026-11-05）。

## 依存関係

- Python 3.10 以上 3.15 未満（pyproject の requires-python）。
- コア依存: livekit==1.2.0、livekit-api、livekit-protocol、livekit-local-inference、av、numpy、pydantic 2.x、openai SDK、httpx2、protobuf、opentelemetry、prometheus-client など。
- モデル接続は livekit-plugins-* の別パッケージ（deepgram、openai、cartesia、elevenlabs、google、azure、aws ほか）。導入時は pip install "livekit-agents[openai,deepgram,cartesia]" のように extra で指定する。
- 外部サービス: LiveKit server（OSS・セルフホスト可）または LiveKit Cloud、および利用する STT/LLM/TTS プロバイダのアカウントと API キー。LiveKit Inference を使う場合は Cloud の認証のみで複数モデルを呼べる。
- ライセンスは本体 Apache-2.0、ターン検出モデルは LiveKit Model License と別建て。

## 実行条件

- console モードでの試用は外部サーバ不要。ローカルのマイク/スピーカーだけで対話を確認できる。
- dev / start モードでは LIVEKIT_URL、LIVEKIT_API_KEY、LIVEKIT_API_SECRET の設定が必須（LiveKit Cloud かセルフホストの LiveKit server）。
- モデルは LiveKit Inference（Cloud 認証）か、各プロバイダの API キーを環境変数などで渡す。キーがない場合はセッションが起動できない。
- GPU は必須ではない。ターン検出の軽量版 v1-mini は CPU 上でローカルに動き、フル版 v1 は LiveKit Inference 側で推論される。
- 電話連携には SIP と電話番号の手配が別途必要。クラウドの拡張機能（推論・ノイズキャンセリング・電話）は LiveKit Cloud のプランと月次枠に依存する。
- ネットワーク: LiveKit server / Cloud への WebSocket 接続と、各モデルプロバイダへの HTTPS 到達性が必要。

## 最短手順

- 1. インストール: pip install "livekit-agents[openai,deepgram,cartesia]"（開発でソースから触る場合は uv sync --all-extras --dev）。
- 2. 環境変数を設定: LIVEKIT_URL / LIVEKIT_API_KEY / LIVEKIT_API_SECRET。
- 3. README のサンプルを myagent.py として保存（AgentServer + @server.rtc_session() の entrypoint で AgentSession に stt/llm/tts を渡し、Agent に instructions と tools を設定）。
- 4. まずローカルで確認: python myagent.py console（外部サーバ不要、ターミナルで音声対話）。
- 5. クライアントと繋ぐ: python myagent.py dev でホットリロード付き起動し、Agents Playground（https://agents-playground.livekit.io/）か任意の LiveKit クライアント SDK で接続。
- 6. 本番起動: python myagent.py start。
- 7. AI コーディングエージェントから使う場合: LiveKit Docs MCP サーバ（https://docs.livekit.io/mcp）をエージェントに登録し、併せて npx skills add livekit/agent-skills --skill livekit-agents で Agent Skill を導入すると、API の最新仕様と設計指針の両方が引ける。

## 変更履歴

- 2026-11-09: 初回登録
