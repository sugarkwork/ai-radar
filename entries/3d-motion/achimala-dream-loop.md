---
repo: "achimala/dream-loop"
name: "dream-loop"
genre: "3d-motion"
url: "https://github.com/achimala/dream-loop"
stars: 1914
forks: 193
open_issues: 4
size_kb: 6768
language: "JavaScript"
created: "2026-09-07"
updated: "2026-09-09"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 5
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: ["最新リリースは取得がタイムアウトしたため未確認。", "作者のREADMEではCodex上のGPT-6 Astraのみでテスト済み。Claude Opus 5.5での動作、比較ベンチマーク、デモの画質・FPS、実行費用は未検証。"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117231247433118169"]
fetched_at: "2026-11-10T08:25:19+00:00"
---

# dream-loop：目標画像を基準に3Dシーンの実装を反復するエージェントスキル

## 出来ること

- ゲームやアプリの目標スクリーンショットを生成し、実装のキャプチャとの差をAIが指摘する。エージェントはその指摘をもとに実装を修正する。

## 目的・背景

- 目標画像を共有し、構図・照明・材質・細部の差を修正項目に落とし込む。Pro手順には評価配点と、改善が停滞した場合の停止条件がある。
- 作者はREADMEでThree.jsの作例を公開している。評価点は手順内で判定役が付けるもので、独立した性能測定値ではない。

## 依存関係

- エージェントには画像生成へのアクセスと画像入力が必要。READMEではサブエージェントの利用を強く推奨し、Pro手順では判定役にサブエージェントを使う。
- 独自の3Dモデリングを行う場合はBlenderを用意する。READMEはBlender MCPまたはスクリプトインターフェースを推奨している。

## 実行条件

- 実装を動かして現状のスクリーンショットを取得できる環境を用意する。READMEの動作確認例はCodex上のGPT-6 Astra。
- リポジトリのライセンスはMIT。外部の画像生成APIを使う場合の料金と利用条件は提供元に依存する。

## 最短手順

- README記載の `npx skills add achimala/dream-loop` でスキルを導入する。
- 導入先のエージェントに `dream loopを使って、ブラウザで動く等角投影の3Dシーンを作って` と依頼する。目標画像があれば添付し、実行時間を制限したい場合は依頼に上限を含める。

## 変更履歴

- 2026-11-10: 初回登録
