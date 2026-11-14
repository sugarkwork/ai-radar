---
name: "DSH Game Studio"
genre: "coding-agent"
url: "https://github.com/ZSeven-W/dsh-game-studio"
repo: "ZSeven-W/dsh-game-studio"
stars: 546
forks: 45
open_issues: 1
size_kb: 9264
language: "TypeScript"
created: "2026-11-05"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 11
commits_90d: 11
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/Leviwoyun/status/2118714367302877635"]
fetched_at: "2026-11-13T20:10:48.071221+00:00"
---

# DSH Game Studio

## 出来ること

- DeepSeek Harnessの会話サイドバーで、2Dトップダウンまたは3Dボクセルのテンプレートを元にゲームを作成・プレビューできる。AI画像候補の生成、ヘッドレスブラウザーでのプレイテスト、変更履歴の復元、オフラインで動作する単一HTMLへの書き出しもREADMEに記載されている。出典: https://github.com/ZSeven-W/dsh-game-studio

## 目的・背景

- ゲームの説明を一文で与え、エージェントがテンプレートからキャラクター、ルール、レベル、画面を組み立てる開発フローを提供する。READMEには作者による試作例とプレイテスト結果も記載されているが、独立した効果測定とは区別する。出典: https://github.com/ZSeven-W/dsh-game-studio

## 依存関係

- DeepSeek Harness向けのプラグイン。README記載の現行プラグインリリースは0.1.0-rc.5で、DSH 0.2.1-rc.5でテスト済み。画像候補生成にはOpenAI画像APIまたはローカルCodex CLIを利用できる。プレイテストはheadless ChromeまたはEdgeを利用する。公開や一時リンクなど、追加機能にはghまたはcloudflaredが記載されている。出典: https://github.com/ZSeven-W/dsh-game-studio

## 実行条件

- DSHの会話内でエージェントにゲーム制作を依頼する。画像生成を使う場合はOpenAIまたはCodexの利用手段が必要で、READMEによれば生成前にサービス、画像数、予想費用の承認カードが表示される。プレイテストにはheadless ChromeまたはEdgeを使う。出典: https://github.com/ZSeven-W/dsh-game-studio

## 最短手順

- 会話で作りたいゲームを一文で説明し、2D collectorまたは3D voxelテンプレートから作成する。ビルド後にサイドバーでプレビューし、必要なら画像候補を生成して選択、プレイテストを実行する。完成したゲームは単一HTMLに書き出せる。出典: https://github.com/ZSeven-W/dsh-game-studio

## 変更履歴

- 2026-11-14: 初回登録
