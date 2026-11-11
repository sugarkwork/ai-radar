---
name: "Machine Skill"
genre: "coding-agent"
url: "https://github.com/AirsupHQ/machine-skill"
repo: "AirsupHQ/machine-skill"
license: "MIT"
language: "JavaScript"
created: "2026-10-12"
updated: "2026-10-13"
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 8
archived: false
flags: ["unverified"]
risk_notes: "README記載の機能や数値はリポジトリの説明に基づき、独立検証していない。生成結果の精度や動作条件は未確認。"
stars: 625
forks: 83
open_issues: 4
size_kb: 17276
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Bober_smart/status/2116895220491276469"]
fetched_at: "2026-11-10T14:08:41.744771+00:00"
---

# Machine Skill

## 出来ること

- READMEでは、Claude Code向けAgent Skillとして、機械の説明から単一HTMLファイルのインタラクティブな3Dシミュレーションを生成し、録画スクリプトで映像化できると説明されている。例として、分解表示、断面表示、X線表示、スローモーション、ラベル表示、計算に基づく破損モードが挙げられている。

## 目的・背景

- 機械や装置の構造・動作を、実寸や物理計算を含む視覚的なシミュレーションとして表現し、操作や映像で共有することを目的としている。

## 依存関係

- READMEにはthree.js 0.170の記載がある。録画手順ではNode.jsとffmpegが必要とされている。

## 実行条件

- Claude CodeでAgent Skillを利用する手順が案内されている。生成されたHTMLはブラウザーで開く形式。録画にはNode.jsとffmpegが必要とREADMEに記載されている。

## 最短手順

- README記載の導入コマンドは `npx skills add AirsupHQ/machine-skill -g -a claude-code`。Claude Codeで `/machine a mechanical watch movement, the escapement ticking` のように機械を指定する。生成されたHTMLをブラウザーで開き、録画する場合は `node ~/.claude/skills/machine/scripts/record.mjs watch.html out/watch.mp4 --music freepd:Classical/Easy_Lemon` を実行する。

## 変更履歴

- 2026-11-11: 初回登録
