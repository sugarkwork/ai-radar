---
repo: "alchaincyf/huashu-design"
name: "Huashu Design"
genre: "prompt-design"
url: "https://github.com/alchaincyf/huashu-design"
stars: 29080
forks: 3134
open_issues: 0
size_kb: 231798
language: "HTML"
created: "2026-04-19"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 31
commits_90d: 41
commit_cadence: "daily"
last_release: "v3.3.0"
flags: ["unverified"]
risk_notes: ["導入・生成・書き出しは未実行。成果物の品質、制作時間、エージェントやOSごとの動作、生成物に含まれる第三者素材の権利は未検証。最新リリースの公開時刻はタイムゾーン付きで確認できなかったため省略した。"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117324109478507007"]
fetched_at: "2026-11-10T08:41:54Z"
---

# Huashu Design — AIエージェントでデザイン案を比較し、試作品を作るスキル

## 出来ること

- 自然言語の依頼から、クリック可能なアプリ原型、編集可能なスライド、アニメーション、情報図を作る。ロゴや配色、UIスクリーンショットを渡して方向性を指定できる。

## 目的・背景

- 作者はClaude Designのワークフローを分解し、端末内のエージェントで使う手順にまとめたと説明している。READMEには作者による生成例がある。

## 依存関係

- Claude Codeなどのスキル対応エージェントが必要。READMEの導入方法はnpxを使い、スキルは同梱の参照資料・素材・スクリプト・デモを参照する。

## 実行条件

- PDF出力について、中国語READMEのDeepSeek Harnessデスクトップ版の説明では、端末にインストール済みのChromeまたはEdgeを使用する。リポジトリはMITライセンス。利用するエージェントの料金は未確認。

## 最短手順

- READMEに従い `npx skills add alchaincyf/huashu-design` で導入し、スキルのフォルダーに `references/`、`assets/`、`scripts/`、`demos/` があることを確認する。
- Claude Codeなどで『4画面のクリック可能なポモドーロアプリの原型を作って。先にデザインの方向性を3案見せて』と依頼し、進める案を指定する。

## 変更履歴

- 2026-11-10: 初回登録
