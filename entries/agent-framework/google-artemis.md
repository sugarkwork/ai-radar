---
repo: "google/artemis"
name: "ARTEMIS"
genre: agent-framework
url: "https://github.com/google/artemis"
license: "Apache-2.0"
stars: 16511
language: "Python"
created: "2026-08-13"
updated: 2026-10-01
added: "2026-11-04"
first_seen: "2026-11-04"
source_post: "https://x.com/bkdgiffug/status/2117913241326387519"
sources: []
flags: []
risk_notes: ""
forks: 1815
open_issues: 183
size_kb: 25762
archived: false
commits_30d: 0
commits_90d: 100
commit_cadence: monthly
fetched_at: "2026-11-04T13:04:06Z"
---

# ARTEMIS（Android 自動化エージェント）

## 出来ること

- 自然言語の指示で Android 実機／エミュレータを操作する。アプリをまたいだ操作（マップで経路を引く → YouTube で曲を再生、など）を1つの指示で実行する。
- 要素インデックスを優先し、取れない画面では座標・視覚での位置推定にフォールバックする。カスタム UI でも操作できる。
- 実行ログとスクリーンショットを取得する。**MCP サーバーを内蔵**し、Claude Code / Codex / Antigravity / Windsurf / Cursor などから端末を操作して Logcat と画面を回収できる。
- APK のインストール、想定外のポップアップ処理、安定性テスト（探索実行）を含むテスト運用向けの機能を持つ。
- Fast / Pro の2プロファイル。Fast は観測→行動のループを非同期の履歴要約で回し、1ステップ3〜5秒程度と説明されている。
- Web UI（`artemis ui`）で画面ミラーリング、指示の送出、実行リプレイを確認できる。

## 目的・背景

Android の UI テスト・自動操作を、壊れやすい座標スクリプトではなく自然言語の指示に置き換える Google のリポジトリ。AI コーディングアシスタントから端末を直接動かす経路（MCP）を用意している点が、他の Android 自動化ツールとの違い。

## 依存関係

- Python 3.12 以降（`uv` で管理）。
- ADB、scrcpy、FFmpeg。`start.sh` が不足分の検出と導入を行う。
- 操作対象の Android 実機（USB デバッグ有効）またはエミュレータ。
- 画面理解に使うマルチモーダルモデル（Gemini / Claude / GPT-4o / Qwen-VL 系）の API アクセス。

## 実行条件

- ライセンスは Apache-2.0。★16,494、fork 1,813、issue 183（2026-11-04 時点）。
- **最終 push は 2026-10-01 で、直近30日のコミットは 0**。活発な開発が続いているわけではない点は導入前に確認する。
- README の「AndroidWorld 99%+ のタスク完了」は作者側の主張で、独立検証は本エントリでは行っていない。
- 実機の USB デバッグを有効にする必要がある。端末の画面内容がモデル API に送られる構成なので、機密情報の扱いは運用側で決める。

## 最短手順

```bash
git clone https://github.com/google/artemis.git && cd artemis
./start.sh                       # 依存導入 + http://localhost:8000 の Web UI
uv run artemis run "Open Settings, find Battery and tell me current level" --profile flash
uv run artemis mcp --install all # Claude Code / Codex などへ MCP を登録
```

## 変更履歴

- 2026-11-04: 初回登録（★16,494 / Apache-2.0 / 最終push 2026-10-01 / commits_30d 0）
