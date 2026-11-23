---
name: "video-spec-builder"
genre: "prompt-design"
url: "https://github.com/feicaiclub/video-spec-builder"
repo: "feicaiclub/video-spec-builder"
license: "MIT"
stars: 1078
language: "JavaScript"
created: "2026-05-16"
updated: "2026-05-18"
forks: 128
open_issues: 2
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 247
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/bkdgiffug/status/2119361788496298116"]
fetched_at: "2026-11-19T18:09:09.846317+00:00"
---

# video-spec-builder

## 出来ること

- 動画の目的、対象、長さ、伝えたいこと、素材、スタイルなどを対話で整理し、各ショットの映像内容・見せ方・秒数・次のショットへのつなぎ方を記した video-spec.md を作成します。既存の video-spec.md の一部を変更する場合も、変更の意図や他のショットへの影響を確認して仕様を更新します。

## 目的・背景

- READMEでは、動画制作で難しいのはレンダリングより、頭の中の曖昧なアイデアを実際に撮影・制作できる内容へ具体化することだと説明しています。このスキルは、曖昧な表現の具体化や、抜けている構成要素の検討、素材のショット単位への分割と順序付けを支援すると作者が述べています。

## 依存関係

- README記載のワークフローでは、仕様作成に video-spec-builder、動画レンダリングに HyperFrames を使います。両方を skills CLI で導入する手順が示されています。

## 実行条件

- README記載では Node.js 18 以降が必要です。Codex、Claude Code、Cursor などで使う方法が説明されています。動画仕様作成とレンダリングの具体的な機能は、利用するスキルやレンダラーの内容に依存します。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの手順は、`npx skills add heygen-com/hyperframes` と `npx skills add feicaiclub/video-spec-builder` を実行して導入し、CodexまたはClaude Codeで「I want to make a 3-minute product demo, posting it on YouTube」のように依頼するものです。対話後に video-spec.md が作成されたら、`/hyperframes` に渡してレンダリングします。

## 変更履歴

- 2026-11-23: 初回登録
