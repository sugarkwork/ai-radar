---
repo: "remotion-dev/skills"
name: "Remotion Agent Skills"
genre: "video-gen"
url: "https://github.com/remotion-dev/skills"
license: "unknown"
stars: 6707
language: "TypeScript"
created: "2026-01-19"
updated: "2026-11-09"
forks: 728
open_issues: 23
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 34
size_kb: 634
archived: false
author: "remotion-dev"
flags: []
risk_notes: "リポジトリにLICENSEファイルが無く、GitHub APIのlicenseもnull（raw.githubusercontent.com/.../LICENSE は404）。コードの再配布条件は不明で、Remotion本体の「Remotion License」（企業規模により有償）がスキル利用に及ぶかはREADMEに記載が無い。効果（生成品質・速度の向上）を測った第三者検証も存在しない。Skillはエージェントへの指示文であり、出力の正しさは利用側のモデルとRemotionのバージョンに依存する。"
last_release: ""
last_release_at: ""
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-09T21:46:22Z"
---

# Remotion Agent Skills — AIエージェントにReact動画制作の作法を教える公式スキル集

## 出来ること

- Remotion公式が配布する13個のAgent Skill（/remotion-best-practices, /remotion-create, /remotion-markup, /remotion-studio, /remotion-render, /remotion-maps, /remotion-captions, /remotion-saas, /remotion-interactivity, /remotion-docs, /remotion-license, /remotion-upgrade, /remotion-multimedia）をエージェントに読み込ませられる。
- /remotion-markup でタイトルカード・アニメーション・レイアウト・タイポグラフィ・音声・フォント・タイミングの実装作法を、/remotion-captions で字幕、/remotion-maps でMapbox/MapLibre/CesiumJSを使った地図アニメーションを扱える。
- /remotion-create でプロジェクトやコンポジションの雛形を生成し、/remotion-studio でプレビュー、/remotion-render で動画または静止画へレンダリングする流れをエージェントに実行させられる。
- /remotion-docs でRemotionドキュメントを検索しMarkdownとして取得、/remotion-upgrade でRemotion本体・関連パッケージ・導入済みスキルの更新ができる。
- /remotion-saas でRemotionを組み込んだプロダクトのアーキテクチャ指針、/remotion-interactivity でStudio上で編集可能なコードにする方法を参照できる。

## 目的・背景

- Remotion（Reactで動画を記述するフレームワーク）の公式組織 remotion-dev が、agentskills.io のAgent Skills形式で「Remotionプロジェクトで作業する際のベストプラクティス」を配布するリポジトリ。
- コーディングエージェントがRemotionのAPIや流儀を誤って使う問題に対し、モデル側の学習に頼らず公式の指示書を渡すことで対処する狙い。READMEは packages/skills/scripts/sync-readme.ts により自動生成され、スキル定義と一覧が同期される運用。
- 新規Remotionプロジェクト作成時（bun create video）にもスキル追加を提案する導線が用意されている。

## 依存関係

- 導入ツール: Node.js（npx skills add）またはGitHub CLI（gh skill install）。
- 利用先: Remotionプロジェクト（TypeScript/React）。
- /remotion-multimedia はブラウザ向けメディア処理ライブラリ Mediabunny を前提とする。
- /remotion-maps は Mapbox・MapLibre・MapTiler・GeoJSON・CesiumJS を、/remotion-render はRemotionのレンダリング系パッケージを前提とする。
- リポジトリにLICENSEファイルは無く（GitHub APIのlicenseはnull）、再配布条件は未記載。

## 実行条件

- Claude Code / Codex / Kimi Code / Cursor など、Agent Skillsを読み込めるエージェント環境であること。
- スキルはテキストの指示書であり、単体で動画を生成するサーバーではない。プレビューとレンダリングにはNode.js上のRemotion実行環境が必要。
- レンダリングやStudioの利用はRemotion本体のライセンス条件に従う（企業規模により有償）。スキル側に軽減・代替の記載は無い。
- 効果（品質・速度の向上）を測った第三者検証は公開されていないため、導入効果は利用側で評価する必要がある。

## 最短手順

- 1. ターミナルで npx skills add remotion-dev/skills を実行する（README記載の一次手順）。
- 2. GitHub CLI派は gh skill install remotion-dev/skills でも導入できる。
- 3. 新規プロジェクトなら bun create video を実行し、プロジェクト作成時にスキル追加の選択肢を承諾する。
- 4. エージェントに /remotion-best-practices を読ませる（どのスキルを使うか不明な場合はこれ1つで全体を包含）。
- 5. 目的別に /remotion-create（雛形生成）、/remotion-markup（実装作法）、/remotion-render（書き出し）などをプロンプトで呼ぶ。例: /remotion-markup Create an animated title card using Inter.
- 6. 最新APIを確認したいときは /remotion-docs に質問する（例: /remotion-docs How to set up Remotion Lambda?）。

## 変更履歴

- 2026-11-07: 初回登録
