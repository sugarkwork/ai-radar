---
name: "Orkas"
genre: "agent-framework"
url: "https://github.com/Orkas-AI/Orkas"
repo: "Orkas-AI/Orkas"
license: "MIT"
stars: 9183
language: "JavaScript"
created: "2026-04-29"
updated: "2026-11-10"
forks: 534
open_issues: 16
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 155729
archived: false
flags: ["unverified"]
risk_notes: "README記載の機能説明に基づく。各エージェントの実際の性能、動作条件、依存関係は確認していない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/awe0_io/status/2120092852919402640"]
fetched_at: "2026-11-10T22:27:28.634950+00:00"
---

# Orkas

## 出来ること

- VideoStudioの参照動画再現では、読み取り可能な動画ファイルと自分の素材を与え、構成・視覚的なスタイル・編集テンポを分析させて制作前に計画を確認する。ソーシャルプラットフォームの共有リンクから動画をダウンロードする機能はなく、カメラ動作や人物演技、フレーム単位の一致は保証されないとREADMEに記載されている。

## 目的・背景

- 単発の応答ではなく、目標・ルール・記憶・ファイルをプロジェクトに保持して、会話をまたいで作業を継続することを目的としている。データは利用者のコンピューターに保存され、完成した成果物はレビューに戻るとREADMEに記載されている。

## 依存関係

- READMEには、Claude Code、Codex、OpenCode、OpenClaw、Hermes-Agentをローカルセッションとして実行できるとある。また、Claude、OpenAI、Gemini、DeepSeek、Kimi、GLM、Qwen、MiniMax、DoubaoまたはローカルのOpenAI互換エンドポイントをモデル接続先として挙げている。インストール要件や依存パッケージの詳細は確認できない。

## 実行条件

- READMEはmacOSとWindows向けのパッケージ版を案内している。組み込みOrkasモデルは500クレジット付きでAPIキーなしで開始できると記載。独自キーやローカルOpenAI互換エンドポイントも利用できる。共有プロジェクト、クラウド同期、Webアプリ公開はパッケージ版のみで、公開には有料プランが必要と記載されている。

## 最短手順

- README記載の案内では、macOSまたはWindows向けパッケージをダウンロードし、Commanderに目標を伝える。独自のモデル接続先を使う場合は対応するキーまたはローカルOpenAI互換エンドポイントを設定する。

## 変更履歴

- 2026-11-11: 初回登録
