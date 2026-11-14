---
name: "blender-ai-copilot-lab"
genre: "agent-framework"
url: "https://github.com/precygtrucqui1981/blender-ai-copilot-lab"
repo: "precygtrucqui1981/blender-ai-copilot-lab"
license: "MIT"
stars: 187
forks: 5
created: "2026-11-12"
updated: "2026-11-12"
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 3
size_kb: 8
archived: false
flags: ["unverified"]
risk_notes: "README記載の機能と対象環境は作者の説明に基づく。独立した動作確認は行っていない。"
open_issues: 38
language: "unknown"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/TheArthiAI/status/2121435010939142280"]
fetched_at: "2026-11-14T04:09:24.616371+00:00"
---

# blender-ai-copilot-lab

## 出来ること

- Blender内の拡張として、managerが依頼を受け入れ条件付きのタスクに分解し、workerが27種類の監督付きシーン操作ツールで実行、reviewerが承認または具体的な指摘を返す。タスクボードで進捗・試行・指摘を確認でき、ブロックされたタスクには修正を1回試行する。各変更には名前付きUndo手順があり、操作ごとの承認にも対応するとREADMEは説明している。MCPサーバー機能も記載されている。

## 目的・背景

- READMEによると、長いチャットで計画や失敗の記録が失われる問題に対し、依頼を構造化し、順序立てたシーン編集とレビューを行う監督付き実験環境を提供する。

## 依存関係

- README記載の対象はWindows x64およびBlender 4.2以降。拡張のZIPをBlenderからインストールする。OpenAI、Anthropic Claude、Google Gemini、OpenRouter、OpenCode Zen、Ollama、Custom APIのプロバイダーが記載されている。接続先によっては認証情報が必要。

## 実行条件

- BlenderのPreferencesから拡張ZIPをインストールして有効化し、3D ViewportのNパネルにあるMCP Proを開く。プロバイダー、接続情報、モデルを設定してBlender内でメッセージを送るかStudio Windowを開く。チームチェーンはmanagerが1人、workerとreviewerが各1人以上で、タスクは逐次実行されるとREADMEに記載。

## 最短手順

- 1. GitHub ReleasesからREADME記載のmcp-for-blender-pro.zipを取得する。2. BlenderでEdit → Preferences → Get Extensions → メニュー → Install from Diskを選び、ZIPを指定する。3. mcp-for-blender-proを有効化し、3D Viewport → N → MCP Proを開く。4. プロバイダー、接続情報、モデルを設定する。5. Blender内でメッセージを送るかOpen Studio Windowを選ぶ。

## 変更履歴

- 2026-11-14: 初回登録
