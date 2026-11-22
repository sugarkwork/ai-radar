---
name: "SU Motion Top 12"
genre: "prompt-design"
url: "https://github.com/doublesq97-ui/su-motion-top12"
repo: "doublesq97-ui/su-motion-top12"
license: "MIT"
stars: 5
language: "HTML"
created: "2026-07-13"
updated: "2026-07-28"
forks: 0
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 14439
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/Sukiea1008/status/2122512547438096467"]
fetched_at: "2026-11-17T06:22:14.736750+00:00"
---

# SU Motion Top 12

## 出来ること

- README では、12 種の高頻度 Motion について選定、実装、検証の指針を提供すると説明されています。各 Motion には意図、トリガー、反例、時間、イージング、低機能時の代替策が含まれると記載されています。Web は CSS、Web Animations API、GSAP、Motion、Canvas などに適応し、Video は HyperFrames または Remotion 向けにフレーム、ショット、タイムラインへ変換する方針です。

## 目的・背景

- 動かすための実行ライブラリではなく、AI が主な UI Motion を選ぶ際の判断基準と一貫した品質基準を提供することが目的です。README は Core 12 を高頻度で再利用しやすいパターンに絞った安定セットと位置づけ、完全なジェスチャー、Sheet、Shared Element、コンポーネント単位のマイクロインタラクションは対象外としています。

## 依存関係

- README の手動導入手順は Git clone と `npm run validate` を示しています。Web 実装では対象プロジェクトの既存技術スタックを使い、動画では HyperFrames を既定とし、ユーザー指定または既存の Remotion プロジェクトがある場合は Remotion を使うと説明されています。個別の実行時依存関係はREADME本文からは特定できません。

## 実行条件

- README は Codex の Skill として配置する方法を案内し、導入後は Codex がローカル Skill として検出すると説明しています。手動導入では `~/.codex/skills/su-motion-top12` に clone し、そこで `npm run validate` を実行します。Web と Video の実装・検証条件は対象エンジンとプロジェクトに応じます。

## 最短手順

- Codex に「リンク：https://github.com/doublesq97-ui/su-motion-top12 のオープンソースプロジェクトをインストールし、使い方を教えて」と依頼する方法が README に記載されています。呼び出し例は「用 su-motion-top12 为这个产品 Hero 选择并实现一个克制的入场动效」です。手動の場合は `git clone https://github.com/doublesq97-ui/su-motion-top12.git ~/.codex/skills/su-motion-top12` の後、ディレクトリ内で `npm run validate` を実行します。

## 変更履歴

- 2026-11-22: 初回登録
