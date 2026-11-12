---
name: "Three.js Skills for Claude Code"
genre: "coding-agent"
url: "https://github.com/CloudAI-X/threejs-skills"
repo: "CloudAI-X/threejs-skills"
license: "MIT"
stars: 4148
language: "unknown"
created: "2026-01-19"
updated: "2026-10-19"
forks: 477
open_issues: 0
commits_30d: 20
commit_cadence: "daily"
commits_90d: 20
size_kb: 169
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/kursormaxx/status/2118673610722144590"]
fetched_at: "2026-11-12T11:12:17.566111+00:00"
---

# Three.js Skills for Claude Code

## 出来ること

- Claude Codeでthree.jsを使う際の参照知識として、シーン構成、ジオメトリ、マテリアル、照明、テクスチャ、アニメーション、各種ローダー、シェーダー、ポストプロセス、インタラクション、性能、React Three Fiber、glTFアセット処理を扱う。READMEではthree.js r186（three@0.186）、React Three Fiber 9.8とdrei 10.7、gltf-transform 4.5を対象としている。

## 目的・背景

- READMEによると、学習データに複数のthree.jsリリースが混在することで古いAPIを使うコードが生成される問題に対応し、現行API、例、古いパターンの注意点をClaude Codeに提供する。

## 依存関係

- READMEに記載された対象はthree.js r186、React Three Fiber 9.8とdrei 10.7、gltf-transform 4.5。導入にはskills CLIまたは手動配置の方法が記載されている。

## 実行条件

- Claude Codeのスキルとして利用する。全プロジェクト向けは~/.claude/skills/、プロジェクト単位は.claude/skills/に配置する手順が記載されている。

## 最短手順

- README記載のCLI手順は `npx skills add cloudai-x/threejs-skills`。手動の場合はリポジトリのskills/*をClaude Codeのスキル配置先へコピーする。

## 変更履歴

- 2026-11-12: 初回登録
