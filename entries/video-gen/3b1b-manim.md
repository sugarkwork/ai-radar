---
name: "ManimGL"
genre: "video-gen"
url: "https://github.com/3b1b/manim"
repo: "3b1b/manim"
stars: 96471
forks: 7925
open_issues: 519
size_kb: 77331
language: "Python"
created: "2015-03-22"
updated: "2026-09-09"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 15
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/naka_1717/status/2118647313166180716"]
fetched_at: "2026-11-13T09:12:51.804495+00:00"
---

# ManimGL

## 出来ること

- 数学解説動画向けに、コードで精密なアニメーションを作成するエンジン。READMEはシーン、アニメーション、オブジェクトの例を案内している。出典: https://github.com/3b1b/manim

## 目的・背景

- READMEによると、3Blue1Brownの作者が自身の動画をアニメーション化するために始めた個人プロジェクト。2020年にコミュニティ版がフォークされた。出典: https://github.com/3b1b/manim

## 依存関係

- Python 3.10以上、FFmpeg、OpenGLが必要。LaTeXは任意。LinuxではPangoと開発ヘッダーも必要。出典: https://github.com/3b1b/manim

## 実行条件

- README記載の基本例は `manimgl example_scenes.py OpeningManimExample`。CLIで実行すると、シンプルなシーンを再生するウィンドウが開くと説明されている。これはREADMEの記載であり、独立した実機確認ではない。出典: https://github.com/3b1b/manim

## 最短手順

- README記載の直接導入手順: `pip install manimgl` の後、`manimgl` を実行。リポジトリから導入する場合は、クローン後に `pip install -e .` を実行し、例として `manimgl example_scenes.py OpeningManimExample` を実行する。出典: https://github.com/3b1b/manim

## 変更履歴

- 2026-11-13: 初回登録
