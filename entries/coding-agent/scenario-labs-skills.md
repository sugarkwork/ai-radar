---
name: "Scenario Agent Skills"
genre: "coding-agent"
url: "https://github.com/scenario-labs/skills"
repo: "scenario-labs/skills"
stars: 3658
forks: 321
open_issues: 27
size_kb: 49134
language: "Python"
created: "2026-08-12"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/naka_1717/status/2118183433390465215"]
fetched_at: "2026-11-11T01:36:47.581530+00:00"
---

# Scenario Agent Skills

## 出来ること

- READMEでは、Claude Code、Cursor、Codex、CopilotなどのAIコーディングエージェントに、Scenarioを使った画像・動画・音声・テクスチャ・スカイボックス・3D素材・カスタム学習モデルの制作方法を案内するスキル集と説明されています。別途、ZBrush、Blender、Maya、Unreal Engine、Unity、Godot、Roblox Studioを操作する専門スキル群も収録されています。

## 目的・背景

- Scenarioを用いた制作のためのAgent Skillsを提供します。専門スキル群は、専門家のチュートリアル、講演、公式ドキュメントをもとに作成したとREADMEに記載されています。各ファミリーのREADMEには作成方法と検証状況が記録されるとの説明があります。

## 依存関係

- Scenario向けスキルにはScenario MCPサーバーへの接続が必要です。専門スキル群はScenario MCPサーバーではなく、対象のDCCソフトまたはゲームエンジンを必要とします。

## 実行条件

- Scenario MCPの利用にはScenarioアカウントでのOAuthサインイン、またはAPIキーを使う方法がREADMEに記載されています。専門スキル群は対象アプリケーションがマシンにインストールされている必要があります。

## 最短手順

- README記載の導入例は `npx skills add scenario-labs/skills --skill scenario` です。Scenario MCPクライアントには `https://mcp.scenario.com/mcp` を追加し、認証を設定します。レビュー済みの状態を使う方法として、installerのバージョンとコミットを固定する例も記載されています。

## 変更履歴

- 2026-11-11: 初回登録
