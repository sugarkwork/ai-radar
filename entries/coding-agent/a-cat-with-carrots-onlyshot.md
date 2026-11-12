---
name: "OnlyShot"
genre: "coding-agent"
url: "https://github.com/A-cat-with-carrots/OnlyShot"
repo: "A-cat-with-carrots/OnlyShot"
flags: ["unverified"]
risk_notes: "README記載の积分・費用は作者による2026-05時点の実測報告であり、独立実測ではない。"
stars: 408
forks: 43
open_issues: 0
size_kb: 361
language: "Python"
created: "2026-05-05"
updated: "2026-11-12"
archived: false
license: "MIT"
commits_30d: 11
commits_90d: 11
commit_cadence: "weekly"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/AIExplorerTim/status/2118530314645672201"]
fetched_at: "2026-11-12T12:11:31.217038+00:00"
---

# OnlyShot

## 出来ること

- READMEによると、Claude Code Skill「ai-short-drama」は短劇の市場情報、脚本、設定、分镜、分镜图、動画生成、字幕・AI标识付き初剪までを段階的に扱う。動画生成には即梦 dreamina CLIを連携できる。出典: https://github.com/A-cat-with-carrots/OnlyShot

## 目的・背景

- READMEは、脚本から出片までの工程をファイル単位で進める短劇制作パイプラインとして説明している。分镜图を先に作り、構図を確認してから動画化する手順も記載されている。出典: https://github.com/A-cat-with-carrots/OnlyShot

## 依存関係

- README記載の依存関係はClaude Code（必須）、Python 3.10+（scriptsの実行時）、dreamina CLI（出图・出片時）、ffmpeg（初剪時）。dreaminaを使わず、脚本・分镜とprompt作成まで行う軽量モードも記載されている。出典: https://github.com/A-cat-with-carrots/OnlyShot

## 実行条件

- READMEの案内では、SkillをClaude Codeのskillsディレクトリへ配置し、Claude Codeを再起動して使用する。動画生成や初剪などの工程では、それぞれdreamina CLI、Python、ffmpegが必要となる。出典: https://github.com/A-cat-with-carrots/OnlyShot

## 最短手順

- README記載の導入例: `git clone https://github.com/A-cat-with-carrots/OnlyShot ~/.claude/skills/ai-short-drama`。配置後にClaude Codeを再起動し、制作したい短劇の題材を伝える。出图・出片の前に、READMEは `--dry-run` による积分見積もり確認も案内している。出典: https://github.com/A-cat-with-carrots/OnlyShot

## 変更履歴

- 2026-11-12: 初回登録
