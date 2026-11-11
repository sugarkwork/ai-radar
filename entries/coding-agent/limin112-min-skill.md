---
name: "min-skill"
genre: "coding-agent"
url: "https://github.com/limin112/min-skill"
repo: "limin112/min-skill"
flags: ["unverified"]
risk_notes: "各Skill・ツールの詳細な依存関係や実行条件は、それぞれのディレクトリにあるREADMEで確認が必要。 GitHub APIでライセンスを確認できていません。"
stars: 630
forks: 94
open_issues: 1
size_kb: 37677
language: "TypeScript"
created: "2026-05-18"
updated: "2026-11-05"
archived: false
license: "unknown"
commits_30d: 14
commits_90d: 31
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/superfang119/status/2118329991687712953"]
fetched_at: "2026-11-11T19:08:26.774499+00:00"
---

# min-skill

## 出来ること

- READMEによると、Claude Code向けSkillとして、概念解説動画の制作、OpenRouter無料モデルの確認とルーティング、Markdownから公众号向けHTMLへの変換、手書き文字の3D演出、記事からのデジタルヒューマン解説動画制作、SDR動画のHLG HDR変換、動画のショット単位での再制作を収録。また、Skillとは別にUU Term BridgeのCLIツールがある。出典: https://github.com/limin112/min-skill

## 目的・背景

- 作者自身が利用するClaude Code Skillとコマンドラインツールの合集。READMEは、必要なものを選んで導入する構成として説明している。出典: https://github.com/limin112/min-skill

## 依存関係

- READMEでは、Skillは`skills/`配下に置きClaude Codeで読み込む形式、ツールは`tools/`配下の独立CLIで各ツールのREADMEに従って導入する形式と説明している。個別の依存関係は各ディレクトリのREADMEを参照。出典: https://github.com/limin112/min-skill

## 実行条件

- SkillはClaude Codeへの配置後に再起動して有効化する手順が記載されている。全Skillをまとめて導入する方法と、単一Skillを選んでコピーする方法がある。ツールの実行条件は各ツールのREADMEを参照。出典: https://github.com/limin112/min-skill

## 最短手順

- 単一Skillの場合、対象フォルダを`~/.claude/skills/`へコピーし、Claude Codeを再起動する。READMEには`explain-video`の例がある。Windowsでは`~`の展開に関する注意が記載されている。出典: https://github.com/limin112/min-skill

## 変更履歴

- 2026-11-11: 初回登録
