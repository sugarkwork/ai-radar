---
repo: "ibelick/ui-skills"
name: "UI Skills"
genre: "coding-agent"
url: "https://github.com/ibelick/ui-skills"
last_release: "v0.2.3"
flags: ["unverified"]
risk_notes: ["create-canvasの動作、生成結果の品質、ブラウザー互換性や性能は未実測。対応フレームワークの範囲と公開MCPの料金・利用上限は未確認。最新リリースのタグはGitHubで確認したが、公開日時の年とタイムゾーンは確認できていない。"]
stars: 10912
forks: 521
open_issues: 22
size_kb: 2730
language: "TypeScript"
created: "2026-01-07"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 85
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/sumika45379/status/2115420830910029989"]
fetched_at: "2026-11-10T12:15:35+00:00"
---

# UI Skills — 既存のUI部品で画面案を比較するエージェント向けスキル集

## 出来ること

- create-canvasは、既存コンポーネントを使った操作可能な画面案を、プロジェクト内のキャンバスに並べるための実装指示を提供する。別案を頼まれた場合は元の案を残し、別案に新しいID、固有の名前、独立した状態を持たせるよう定めている。

## 目的・背景

- 画面案の構成をソースコードで管理し、会話で特定の案を指しながら比較と修正を続けるための設計。案の保持はスキルに記載された仕様で、生成結果の再現性は未実測。

## 依存関係

- 対象プロジェクトのフレームワーク、コンポーネント、デザイントークン、テーマを再利用する。MCP経由で取得する場合は、公開MCPエンドポイントを設定できるエージェントが必要。

## 実行条件

- エージェントが対象リポジトリのソースを編集でき、生成したプレビューを対象アプリで表示できる環境を使う。スキルは、合成データやモックで実サービスへのリクエストと書き込みを防いでからプレビューを表示するよう求める。リポジトリのライセンスはMIT。公開MCPの料金と利用上限は未確認。

## 最短手順

- エージェントのMCP設定に https://www.ui-skills.com/mcp を追加し、エージェントに `list_skills` で `create-canvas` を探し、`get_skill` で取得するよう依頼する。
- 対象プロジェクトを開き、エージェントに「create-canvasを使って、既存のカード部品と合成データで元案と余白を詰めた別案を並べて」と依頼する。

## 変更履歴

- 2026-11-10: 初回登録
