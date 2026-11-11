---
name: "reanimate"
genre: "coding-agent"
url: "https://github.com/NiazMorshed2007/reanimate"
repo: "NiazMorshed2007/reanimate"
license: "MIT"
stars: 1557
language: "JavaScript"
created: "2026-10-29"
updated: "2026-10-31"
forks: 136
open_issues: 7
commits_30d: 20
commit_cadence: "daily"
commits_90d: 20
size_kb: 59722
archived: false
flags: ["unverified"]
risk_notes: "Windows is untested. The README says the skill has only been tested with Claude Code, though other agents that read SKILL.md can install it."
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/ganfanren_ai/status/2118311436485321040"]
fetched_at: "2026-11-11T16:12:05.648487+00:00"
---

# reanimate

## 出来ること

- README describes a Claude Code skill that records animation references from a live site, screen recording, MP4, GIF, or Lottie file; builds an animation in the user's project using its existing tools; captures the result; and compares timing, easing, and pixels to guide further iterations. It documents CSS, Framer Motion, GSAP, and three.js as build options. Source: https://github.com/NiazMorshed2007/reanimate

## 目的・背景

- The README says agents may miss motion details when rebuilding from a link or screenshot in a single pass. The skill is intended to capture the reference and compare subsequent builds to it. This is the project author's description, not an independent evaluation. Source: https://github.com/NiazMorshed2007/reanimate

## 依存関係

- README states it needs Bun 1.1 or later and installs a static ffmpeg into the skill folder and Playwright Chromium into Playwright's usual cache on first run, about 250 MB together. It says no API keys are needed. Source: https://github.com/NiazMorshed2007/reanimate

## 実行条件

- README states macOS or Linux are supported; Windows is untested. Claude Code is the only agent the author says has been tested. Other agents that read SKILL.md can install it. Source: https://github.com/NiazMorshed2007/reanimate

## 最短手順

- Install with `npx skills add NiazMorshed2007/reanimate -g`. The README says to add `-a claude-code` to skip the agent selection question. In Claude Code, invoke `/reanimate` with a reference and destination, such as `/reanimate the hero entrance on https://example.com, into components/Hero.tsx`. Source: https://github.com/NiazMorshed2007/reanimate

## 変更履歴

- 2026-11-11: 初回登録
