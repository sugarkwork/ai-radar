---
repo: "wheresryan22/anatomy"
name: "Anatomy"
genre: "video-gen"
url: "https://github.com/wheresryan22/anatomy"
license: "MIT"
stars: 24347
language: "JavaScript"
created: "2026-10-08"
updated: 2026-10-18
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: []
risk_notes: ""
forks: 2032
open_issues: 71
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 12817
archived: false
fetched_at: "2026-11-03T15:43:31Z"
last_release: v1.1.0
last_release_at: 2026-10-12
---

# Anatomy

## 出来ること

- 概念を「実際に動く等角投影（アイソメトリック）図」として組み上げて説明するエージェントスキル。部品・運動・リアルタイム数値表示を持つ精巧な図を SVG / WebGL / 3D で出力する。
- 出力は静止画ではなく、操作できるページ（分解・回転・パーツ単位の注視）。例: Raptor エンジンを11アセンブリに分解、1984年風デスク機（約85ソリッド）、アーケード筐体（約240ソリッド＋15ケーブル）。
- 生成物は「自分のもの」として渡される: Node のビルドスクリプト＋それが書き出す単体ページ（React 版はジオメトリのモジュール群＋サーバー／クライアントコンポーネント）。
- 幾何の妥当性を検査する仕組みを持つ（例: 配管が他の部品を貫通していないことを静止時・分解時・その間の全フレームで検証）。

## 目的・背景

Claude Code 向けスキルとして 2026-10 公開。技術解説・科普動画のビジュアル工程を担う部品で、完成した動画そのものを作るツールではない（ナレーションや編集は別途）。Antigravity / OpenCode / Codex / MiniMax Code でも動く。

## 依存関係

- Node.js 20.10 以上。ただし `skills` CLI（v1.7.1）での導入は Node 22.20 以上を要求。
- 追加の npm 依存ゼロ、API キー不要（Node 標準モジュールのみで完結）。
- 撮影用の `scripts/capture.mjs` は Playwright 等ではなくヘッドレスブラウザの起動を前提とする（README に Node スクリプトとして記載）。

## 実行条件

- エージェント（Claude Code 等）が SKILL.md を読んで図を生成する形式。人手でのコーディングは想定されていない。
- リポジトリはサンプル込みで約 10MB（skills CLI はリポジトリ全体をコピーする）。
- 出力は HTML なので閲覧はブラウザのみ。動画化する場合は別途スクリーンキャプチャが必要。

## 最短手順

```bash
npx skills add wheresryan22/anatomy -g -a claude-code
# 例題をローカルで生成
node examples/dial-indicator/build.mjs
```

## 変更履歴

- 2026-11-03: 初回登録（star 24,345 / pushed 2026-10-18 / MIT / Node 20.10+・依存ゼロ）
