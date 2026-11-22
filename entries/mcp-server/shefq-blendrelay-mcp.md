---
name: "BlendRelay MCP"
genre: "mcp-server"
url: "https://github.com/shefq/blendrelay-mcp"
repo: "shefq/blendrelay-mcp"
license: "MIT"
stars: 34
language: "Python"
created: "2026-09-10"
updated: "2026-11-09"
forks: 3
open_issues: 2
commits_30d: 10
commit_cadence: "weekly"
commits_90d: 38
size_kb: 2921
archived: false
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/thegreatest_sv/status/2119129564047982889"]
fetched_at: "2026-11-17T02:17:48.882758+00:00"
---

# BlendRelay MCP

## 出来ること

- Blenderの開いているシーンをAIエージェントから確認・更新する。シーンやオブジェクトの生成、選択オブジェクトやEdit Modeで選択したメッシュ要素の編集、参照画像・ビューポートのスケッチ・対象領域の指定、マテリアルやライティング、カメラ、モディファイア、Geometry Nodes、アニメーション、レンダーの作成に対応するとREADMEに記載。自動チェックポイントの保存・復元機能も記載されている。

## 目的・背景

- Blenderでのプロンプトベースの3Dモデリングやシーン生成・編集を、Codex、Claude Code、AntigravityなどのMCP対応エージェントから行うためのオープンソースアドオン兼MCPサーバー。

## 依存関係

- READMEではBlender 4.5以降、uvxまたはPython 3.11以降とpip、およびサポート対象のAIコマンドラインエージェント（OpenAI Codex CLI、Google Antigravity CLI、Anthropic Claude Code）のいずれかを必要条件としている。

## 実行条件

- Blenderを一度起動してからセットアップする。導入後にBlenderを再起動し、アドオンを有効にしてBlendRelayパネルから接続する。外部MCPクライアントから接続する場合も、BlenderとBlendRelayアドオンを起動・接続しておく必要がある。

## 最短手順

- README記載の手順では、PowerShellまたはターミナルで `uvx blendrelay-mcp setup` を実行し、Blenderを再起動する。PreferencesのAdd-ons / Get ExtensionsでBlendRelay MCPを有効にし、3D ViewportのサイドバーにあるBlendRelayタブからConnectを押す。Codex CLIの場合は `codex mcp add blendrelay -- uvx blendrelay-mcp mcp` で登録する。

## 変更履歴

- 2026-11-22: 初回登録
