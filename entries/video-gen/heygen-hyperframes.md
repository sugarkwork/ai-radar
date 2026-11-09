---
repo: heygen-com/hyperframes
name: HyperFrames
genre: video-gen
url: https://github.com/heygen-com/hyperframes
license: Apache-2.0
stars: 78902
language: TypeScript
created: 2026-03-10
updated: 2026-11-04
added: 2026-11-03
sources: ["https://x.com/y0urdumble/status/2117396633889427646", "https://x.com/cy160909/status/2118998213474529750?a=8TSEfffrrLfNp3_AMmc&s=46", "https://x.com/CY160909/status/2118998213474529750", "https://github.com/heygen-com/hyperframes/blob/main/skills/reverse-any-video/SKILL.md", "https://hyperframes.studio/pricing", "https://github.com/JuneYaooo/rea-video", "https://api.github.com/repos/JuneYaooo/rea-video"]
forks: 7262
open_issues: 231
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 530675
archived: false
fetched_at: "2026-11-04T22:53:08Z"
last_release: v0.9.13
last_release_at: 2026-11-04
type: "repo"
author: "heygen-com"
source_post: "https://x.com/CY160909/status/2118998213474529750"
first_seen: "2026-11-07"
amplifiers: []
flags: ["unverified"]
risk_notes: "コードのApacheと有料Reverse機能を区別する。元映像の分解・再現は著作権や素材の利用許諾を要する。 今回の動作・推論・生成・性能は未検証。"
---

# HyperFrames

## 出来ること

- HTML（CSS / GSAP アニメーション）で書いたシーンを、そのまま動画にレンダリングする。キャッチコピーは "Write HTML. Render video. Built for agents."
- フレーム単位のタイムラインを手で組む代わりに、DOM の状態を時間軸に沿って評価してフレームを吐く。
- エージェント（Claude Code 等）に HTML を書かせる用途を想定した設計。`npx hyperframes skills update` でコーディングエージェント向けのスキルを入れ、`init` → `preview`（ブラウザでライブリロード）→ `render`（MP4 書き出し）の流れで作る。Claude Code / Codex / Cursor / Gemini CLI などに対応。
- デスクトップアプリ **HyperFrames Studio**（macOS / Windows / Linux、無料）も配布。Pro プランは HeyGen の動画・画像・音声・音楽モデルを追加する、と案内している。
- 内部で FFmpeg を使用。TypeScript 実装、npm パッケージ `hyperframes` として配布。

## 目的・背景

HeyGen が公開しているオープンソースの「HTML → 動画」フレームワーク。Remotion が React コンポーネントを要求するのに対し、素の HTML/CSS を入力にできるため、LLM に生成させやすい。2026-03 公開、7.8 万 star・7,200 fork。リポジトリサイズは約 530MB（docs・サンプル込み）で、クローンには注意。

## 依存関係

- Node.js 22+
- npm パッケージ `hyperframes`
- FFmpeg（レンダリング時）
- ブラウザエンジン（ヘッドレスレンダリング用）

## 実行条件

- OS 不問。GPU は必須ではない（CPU レンダリング）。ただし長尺・高解像度は時間がかかる。
- ディスク：リポジトリ全体で 500MB 超。npm 利用なら実装分のみ。
- 動画の素材（画像・音声）は別途用意する。

## 最短手順

```bash
# エージェントにスキルを入れ、プロジェクトを作って書き出す
npx hyperframes skills update     # リリースタグに合うコアスキルを導入
npx hyperframes init my-video
npx hyperframes preview           # ブラウザでプレビュー
npx hyperframes render            # MP4 に書き出し

# ライブラリとして使う場合
npm install hyperframes

# リポジトリのサンプルを動かす場合
git clone --depth 1 https://github.com/heygen-com/hyperframes
cd hyperframes && npm install
```

## 変更履歴

- 2026-11-03: 初回登録（star 78,130 / pushed 2026-11-03）
- 2026-11-04: スキル導入と init / preview / render の手順、無料の Studio アプリと Pro プランを追記（v0.9.13）

## 追加出典・確認範囲（2026-11-09）

HTML/CSS/GSAPを動画化するHyperFramesのreverse-any-video機能についての追加情報。

該当スキルはHyperFrames Pro専用。原チェック時のProは月25ドル・25000credits。

コードのApacheと有料Reverse機能を区別する。元映像の分解・再現は著作権や素材の利用許諾を要する。

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:04.120541+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | heygen-com/hyperframes |
| url | https://github.com/heygen-com/hyperframes |
| license | Apache-2.0 |
| language | TypeScript |
| created | 2026-03-10 |
| updated | 2026-11-09 |
| stars | 81084 |
| forks | 7486 |
| open_issues | 225 |
| commits_30d | 100 |
| commits_90d | 100 |
| commit_cadence | daily |
| size_kb | 535593 |
| archived | False |
| fetched_at | 2026-11-09T00:31:04.120541+00:00 |


- @CY160909: https://x.com/CY160909/status/2118998213474529750
- 対象資料: https://github.com/heygen-com/hyperframes
- 参照: https://github.com/heygen-com/hyperframes/blob/main/skills/reverse-any-video/SKILL.md
- 参照: https://hyperframes.studio/pricing
- 参照: https://github.com/JuneYaooo/rea-video
- 参照: https://api.github.com/repos/JuneYaooo/rea-video

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
