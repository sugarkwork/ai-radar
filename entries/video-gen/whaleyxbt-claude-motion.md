---
name: "claude-motion"
genre: "video-gen"
url: "https://github.com/whaleyxbt/claude-motion"
repo: "whaleyxbt/claude-motion"
stars: 951
forks: 119
open_issues: 0
size_kb: 14821
language: "JavaScript"
created: "2026-09-29"
updated: "2026-11-08"
archived: false
license: "MIT"
commits_30d: 4
commits_90d: 15
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:11:44.233762+00:00"
---

# claude-motion

## 出来ること

- コーディングエージェント向けに、モーションデザインのルール、ビートごとのフレーム確認と修正ループ、タイムラインに同期した音声生成を提供する。Webページとして作ったシミュレーションをフレーム単位で描画し、60 fpsの動画にキャプチャする手順もある。README記載の機能説明であり、個別環境での動作を独立に確認したものではない。

## 目的・背景

- READMEは、RemotionのAPI知識に加えて、デザイン上の判断基準、フレームの自己レビュー、音声制作機能をエージェントに与えるツールキットとして説明している。

## 依存関係

- README記載の基本要件はNode 20以上、Python 3、ffmpeg。シミュレーションのキャプチャ手順ではPlaywrightのChromiumもインストールする。MCPサーバーは任意で、READMEはMCPなしでも利用できるとしている。

## 実行条件

- READMEによるとClaude CodeとCursorでは`.claude/skills/`のスキルを利用でき、Codex、OpenCodeなどでは`AGENTS.md`を読むエージェントが対象。シミュレーションの動画化にはnpm依存関係とPlaywright Chromiumのセットアップが記載されている。

## 最短手順

- 通常の動画例は、リポジトリを取得して`npm install`、`npm run build`を実行する手順がREADMEにある。Webシミュレーションは`npm install`と`npx playwright install chromium`の後、`npm run sims`でHTMLを生成し、`npm run capture`でキャプチャする。これらはREADME記載の手順であり、ここでは実行していない。

## 変更履歴

- 2026-11-12: 初回登録
