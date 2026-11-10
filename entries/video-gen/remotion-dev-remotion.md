---
repo: "remotion-dev/remotion"
name: "Remotion"
genre: "video-gen"
url: "https://github.com/remotion-dev/remotion"
license: "unknown"
stars: 72099
forks: 6003
open_issues: 206
size_kb: 4491236
language: "TypeScript"
created: "2020-06-23"
updated: "2026-11-10"
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v4.0.542"
flags: ["unverified"]
risk_notes: "ローカルでのレンダリング、出力品質、制作時間・費用の削減効果、発見投稿にある特定モデルでの再現性は未検証。最新リリースのタグは確認済みだが、タイムゾーン付きの公開日時は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117231247433118169"]
fetched_at: "2026-11-10T08:25:35Z"
---

# Remotion — Reactで動画を作り、コーディングエージェントで編集する

## 出来ること

- Reactで動画の構成やアニメーションを記述し、Remotion Studioでプレビューして動画を書き出せる。

## 目的・背景

- 映像をコードとして管理し、再利用できるモーション素材や動画テンプレートを作るためのフレームワーク。Agent Skillsを利用すると、コーディングエージェントに動画の実装や修正を依頼できる。

## 依存関係

- 動画の記述にはReactを使う。公式のエージェント向け手順にはNode.js、npm、対応するコーディングエージェントが必要。

## 実行条件

- 公式の導入ガイドではNode.js 16以上またはBun 1.0.3以上。macOSは15以上で、Linuxではglibcの要件と追加パッケージがある。
- 公式料金表では個人と3人以下の企業は規約に従って無償で商用利用できる。無償条件を満たさない場合はCompany Licenseが必要で、エージェントの利用料は別途かかる場合がある。

## 最短手順

- Node.js環境で `npx create-video --yes --blank my-video` を実行し、`my-video` に移動する。
- `npx remotion skills add` でAgent Skillsを追加し、`npm run dev` でStudioを起動する。
- 別のターミナルで同じプロジェクトをClaude Codeなどのコーディングエージェントで開き、たとえば『商品名と特徴を順に表示する短い紹介動画を作って』と依頼する。Studioで確認し、必要に応じて修正して書き出す。

## 変更履歴

- 2026-11-10: 初回登録
