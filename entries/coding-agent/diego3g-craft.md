---
name: "craft"
genre: "coding-agent"
url: "https://github.com/diego3g/craft"
repo: "diego3g/craft"
license: "unknown"
stars: 186
language: "JavaScript"
created: "2026-11-15"
updated: "2026-11-17"
forks: 7
open_issues: 0
commits_30d: 23
commit_cadence: "daily"
commits_90d: 23
size_kb: 208
archived: false
flags: ["unverified"]
risk_notes: "READMEではFigmaアダプターは実際の実行で未テストとされています。GitHub APIのlicense値はunknownですが、READMEのLicense欄はMITです。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/GitTrend0x/status/2122653626900332544"]
fetched_at: "2026-11-17T23:29:52.235866+00:00"
---

# craft

## 出来ること

- READMEによると、画面設計時に短いデザインブリーフを作り、画面の状態を列挙し、既存デザインシステムの部品を使い、提出前に自己レビューするワークフローを提供します。craft-setup、craft、craft-states、craft-explore、craft-system、craft-sync、craft-critiqueなどのスキルが記載されています。

## 目的・背景

- READMEは、AIエージェントによるUI設計で画面の状態を網羅し、デザインシステムとの一貫性を保つことを目的として説明しています。設計判断を記録し、必要な場面で利用者の確認を求める手順も紹介されています。

## 依存関係

- READMEはPaper、pen.dev、Figma、またはHTMLを利用するアダプターを説明しています。Claude Codeなどではプラグインとして、Codex、OpenCode、Cursorなどではskills CLIまたはskillsフォルダーの手動コピーで導入する方法が記載されています。各ツールの追加依存関係はREADMEだけでは確認できません。

## 実行条件

- README記載の導入例は、Claude Codeではプラグインコマンド、その他の対応エージェントでは `npx skills add diego3g/craft` です。Figmaアダプターは実際の実行で未テストとREADMEに記載されています。

## 最短手順

- Codexなどでは `npx skills add diego3g/craft -a codex` で導入し、README記載のルーティングをプロジェクトのAGENTS.mdに追加します。既存デザインシステムがある場合はcraft-sync、ない場合はcraft-setupから始める手順が案内されています。

## 変更履歴

- 2026-11-22: 初回登録
