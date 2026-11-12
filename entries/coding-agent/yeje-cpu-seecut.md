---
name: "SeeCut"
genre: "coding-agent"
url: "https://github.com/YeJe-cpu/SeeCut"
flags: ["unverified"]
risk_notes: "README says the workflow has only been tested on macOS. The author reports Claude Code tested and other skill-capable agents theoretically compatible; those other agents are not independently verified here. An Antigravity CLI account and sufficient usage quota are required for video review and self-iteration. GitHub APIでライセンスを確認できていません。"
repo: "YeJe-cpu/SeeCut"
stars: 453
forks: 84
open_issues: 0
size_kb: 301
language: "JavaScript"
created: "2026-09-25"
updated: "2026-10-30"
archived: false
license: "unknown"
commits_30d: 2
commits_90d: 11
commit_cadence: "monthly"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/ganfanren_ai/status/2118557404522824008"]
fetched_at: "2026-11-12T16:17:30.117896+00:00"
---

# SeeCut

## 出来ること

- A coding-agent skill for turning live-action or AI-avatar talking-head footage into edited short videos. The README describes analyzing source material, finding real visual evidence, arranging and rendering shots, and using Gemini through Antigravity CLI to review video and iterate on edits. It can also provide a layered project package; producing a Jianying draft is optional and depends on a draft engine.

## 目的・背景

- The project targets short, visually engaging talking-head videos, with visual treatments chosen to follow the spoken content. The README says its review loop checks each version for hard defects and compares it with the previous version, accepting an iteration only when it wins both comparison runs. These are the author's descriptions of the workflow, not independent measurements.

## 依存関係

- Core requirements listed in the README: a coding agent; Antigravity CLI (agy) for video understanding and review; HyperFrames CLI; ffmpeg; Node.js 22 or later; Python 3; faster-whisper; and playwright-core installed in the project directory. Optional components include an image-generation tool, a sound-effects library, and Easy 剪映 for generating an editable Jianying draft. The README says digital-avatar production additionally needs voice synthesis and a HeyGen account/API wallet; its documented workflow uses Doubao speech synthesis and HeyGen.

## 実行条件

- The README says the project has been tested only on macOS. Antigravity CLI requires a supported Google account region; the README says changing IP alone does not resolve an ineligible account. It also notes that proxy configuration may be needed for downloads and that the HyperFrames proxy variable must be uppercase HTTPS_PROXY. A 20–30 second sample is recommended before processing a longer video; the README says material over 60 seconds prompts the skill to ask first. A 25-second sample is reported to take about one hour, with longer footage taking longer.

## 最短手順

- Prepare a folder containing a 20–30 second vertical, waist-up talking-head clip and optionally 3–6 screenshots of things mentioned in the clip. Install the core requirements, then run `zsh skill/seecut/scripts/preflight.sh` until required checks pass. Copy `skill/seecut` into `~/.claude/skills/` or the agent's skills directory, start a new conversation, and run `/seecut 素材：<your folder>`. The README says the output includes a rendered video, a layered project package, and a delivery report.

## 変更履歴

- 2026-11-12: 初回登録
