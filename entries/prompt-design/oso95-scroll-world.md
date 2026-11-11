---
name: "scroll-world"
genre: "prompt-design"
url: "https://github.com/oso95/scroll-world"
repo: "oso95/scroll-world"
license: "MIT"
stars: 10920
language: "JavaScript"
created: "2026-07-06"
updated: "2026-07-29"
forks: 1190
open_issues: 10
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 49
archived: false
flags: ["unverified"]
risk_notes: "生成には外部サービスのCLI、認証情報、クレジットまたは従量課金が必要。README記載の価格や効果は独立検証していない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116967509735747833"]
fetched_at: "2026-11-10T14:10:51.867000+00:00"
---

# scroll-world

## 出来ること

- 業界やブランド向けに、スクロール位置でカメラ飛行を制御し、場面を途切れなくつなぐランディングページを生成する。シーン画像、場面内への移動動画、場面間の接続動画と、設定駆動のスクロールエンジンを用意する。

## 目的・背景

- Appleのスクロール連動型ページのように、カメラが複数のシーンを連続して移動する演出を、任意の業界やブランド向けに作るエージェントスキル。

## 依存関係

- README記載の要件はMonid CLIとAPIキー・残高、または認証済みHiggsfield CLIとクレジット、ffmpeg/ffprobe、Python 3とPillow。Codex CLIは画像生成に使う場合のみ任意。

## 実行条件

- スキルが対象・ブランド情報・アートディレクション・シーン順・モバイル版の要否・予算を聞き取り、生成前に見積もりを提示する。素材生成には課金サービスを利用し、生成した動画・画像ファイルはリポジトリに含まれない。

## 最短手順

- Codexなどでは `npx skills add oso95/scroll-world -a codex` で導入し、`$scroll-world` または自然文で起動する。

## 変更履歴

- 2026-11-11: 初回登録
