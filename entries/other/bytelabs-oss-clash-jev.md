---
repo: "bytelabs-oss/clash-jev"
name: "clash-jev"
genre: "other"
url: "https://github.com/bytelabs-oss/clash-jev"
stars: 37
forks: 11
open_issues: 2
size_kb: 5806
language: "Python"
created: "2026-09-21"
updated: "2026-10-14"
archived: false
license: "MIT"
commits_30d: 2
commits_90d: 6
commit_cadence: "monthly"
last_release: ""
last_release_at: ""
flags: ["unverified"]
pricing_detail: "READMEの著者は約20試合で1試合あたり150〜200件のJevリクエストと約0.004米ドルの費用を報告。現行のAPI料金は未確認。"
risk_notes: "約135msはREADMEが示すJevの単一応答の目安。全体遅延、勝率、端末ごとの認識精度、現行API料金は未検証。READMEは自動プレイがSupercellの利用規約に反すると明記している。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:32:31+00:00"
---

# clash-jev — Androidのゲーム画面を構造化し、Jevで手を選ぶ実装例

## 出来ること

- ADBで取得したH.264映像から手札、エリクサー、タワーなどを読み取り、既定で毎秒JSONのゲーム状態を組み立てる。Jevが戦略、カード、配置マスを順に選び、実行可能性を検査してからタップする。
- 判断時の入力、選択肢ごとの確率、遅延を動画と同期して記録する。READMEの約135msは単一応答の著者報告で、カードを出す判断には直列で3リクエストかかる。

## 目的・背景

- 画面認識と行動選択を分けた意思決定の実験。プレイ方策の学習や強化学習は使わず、画面内の兵種を識別する小型ネットワークは著者が手作業でラベル付けした画像で学習している。APIリクエスト失敗時にはベースライン方策が代替し、ログで区別する。

## 依存関係

- macOSまたはLinux、Python 3.12以上、ADB、OpenCV。実機の画面取得にはUSBデバッグを有効にしたAndroid端末とClash Royaleが必要。Jevを呼ぶ場合はTypeSafe APIキーとネット接続が必要。

## 実行条件

- コードはMIT。READMEはゲームのカードやアートの権利がSupercellにあり、自動プレイが同社の利用規約に反すると記載している。GitHubのReleases一覧には公開リリースが表示されていなかった。

## 最短手順

- READMEのSetupに沿って仮想環境を作り、パッケージをインストールする。AIエージェントから画面認識を呼ぶには、用意した保存フレームを `clash-jev snap --image frame.png` に渡す。このCLIは読み取った状態と有効な手を出力し、Jevにはリクエストを送らない。
- モデルの判断も確認する場合は、READMEの環境設定に沿ってTypeSafe APIキーを設定し、同じ保存フレームを `clash-jev play --image frame.png` に渡す。READMEによれば保存フレームから一度だけ意思決定する。今回の精査は資料確認のみ。

## 変更履歴

- 2026-11-11: 初回登録
