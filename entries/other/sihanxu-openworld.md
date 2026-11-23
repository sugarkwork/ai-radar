---
name: "OpenWorld RPG"
genre: "other"
url: "https://github.com/SihanXU/openworld"
repo: "SihanXU/openworld"
license: "unknown"
stars: 131
language: "TypeScript"
created: "2026-09-30"
updated: "2026-11-19"
forks: 13
open_issues: 6
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 690176
archived: false
flags: ["unverified"]
risk_notes: "READMEにライセンスの説明はあるものの、取得済みの情報ではライセンスを確認できない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119391988822753287"]
fetched_at: "2026-11-20T00:13:40.445816+00:00"
---

# OpenWorld RPG

## 出来ること

- ブラウザーで遊べるピクセルアートのオープンワールドRPG。千以上のマップ、クエスト、戦闘、クラフト、農業、建築などを備えるとREADMEに記載。TypeScript製の決定論的なエンジンと、ブラウザーまたはデスクトップで使えるエディターも含む。AIルールサービスは任意で、既存ルールのない行動に対するルール案をサンドボックスで検証してから適用する設計。NPCワークショップではアイテムやエリアの案を作成し、確認後にセーブデータへ読み込める。

## 目的・背景

- READMEでは、OpenWorldを研究論文「Large Symbolic World」（準備中）の研究プラットフォームと説明している。ゲーム内の世界はデータとして記述されたルールに従い、モデルなしでもプレイできる。

## 依存関係

- 開発・起動要件はNode.js 24とnpm。言語モデルは任意。ローカルでNPC作成機能を使う場合は、READMEにDEEPSEEK_API_KEYの設定とClaude CodeのPATH設定が記載されている。

## 実行条件

- READMEの手順は、npm install、npm run gen:world、npm run dev。npm run devでモデルバックエンドを選択し、ゲームはローカルの開発サーバーで起動する。AIサービスなしで遊ぶ場合はnpm run dev:clientを使える。

対応言語: ゲーム内の対応言語として英語と中国語をREADMEが挙げている。（出典: https://github.com/SihanXU/openworld）
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- リポジトリを取得し、Node.js 24とnpmを用意して、npm install、npm run gen:world、npm run devを順に実行する。AIバックエンドを使う場合は、READMEのAI setupに従ってバックエンドと設定値を選ぶ。

## 変更履歴

- 2026-11-23: 初回登録
