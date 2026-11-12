---
name: "Motion Graphics Skill Pack"
genre: "coding-agent"
url: "https://github.com/charlie947/motion-graphics-skills"
repo: "charlie947/motion-graphics-skills"
stars: 648
forks: 86
open_issues: 2
size_kb: 12307
language: "Shell"
created: "2026-09-26"
updated: "2026-10-11"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 28
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:12:31.553664+00:00"
---

# Motion Graphics Skill Pack

## 出来ること

- READMEでは、ブランド設定、制作 brief の作成、参考動画の分析、プロモーション動画・解説動画・チャート・3Dタイトルなどの制作、リール用書き出しを行う15個のスキルを案内している。Claude Code と Codex での利用方法も記載されている。

## 目的・背景

- 作者は、After Effects や動画生成ツールを使わず、コードでアニメーションを作成してフレームを描画し、MP4にするために自身が使うワークフローと、修正を受けた草稿から得たルールをスキルとしてまとめたと説明している。これはREADMEにある作者の説明であり、独立した効果測定ではない。

## 依存関係

- READMEの導入手順は `npx skills add charlie947/motion-graphics-skills`。Claude Code向けの説明ではOpus 5.5を指定している。MP4書き出しにはHyperFramesを追加する方法が案内されている。各スキル固有の依存関係はREADMEだけでは確認できない。

## 実行条件

- READMEでは、Claude CodeまたはCodexで使う手順を説明している。Claude Codeでは最初に `brand-intake` を実行する手順が案内されている。Codexではプロジェクト内の `.agents/skills/` にスキルを配置し、新しいタスクで読み込まれることを確認する手順がある。

## 最短手順

- README記載の手順は、`npx skills add charlie947/motion-graphics-skills` で導入し、Claude Codeで `brand-intake` を先に実行すること。CodexではREADME掲載のコピー手順に従って `.agents/skills/` に配置する。

## 変更履歴

- 2026-11-12: 初回登録
