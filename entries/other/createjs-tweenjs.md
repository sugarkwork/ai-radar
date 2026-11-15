---
name: "TweenJS"
genre: "other"
url: "https://github.com/CreateJS/TweenJS"
repo: "CreateJS/TweenJS"
stars: 3553
forks: 936
open_issues: 12
size_kb: 25241
language: "JavaScript"
created: "2011-03-19"
updated: "2023-12-18"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Feljoy_ix/status/2121787138455040333"]
fetched_at: "2026-11-15T03:18:46.721176+00:00"
---

# TweenJS

## 出来ること

- JavaScriptオブジェクトの数値プロパティとCSSスタイルプロパティを補間する。Tweenを連結して値の変更、待機、コールバックなどを構成できる。Timelineは複数のTweenを同期し、グループとして操作する。Easeはイージング関数を提供する。出典: https://github.com/CreateJS/TweenJS

## 目的・背景

- EaselJSとの連携を意図して開発されたが、EaselJSに依存せず利用できる。TickerとEventは既定で同じクラスを使用する。出典: https://github.com/CreateJS/TweenJS

## 依存関係

- READMEではEaselJSへの依存はないと説明されている。TickerとEventは既定で使用するが、追加の依存関係についてはREADMEに記載がない。出典: https://github.com/CreateJS/TweenJS

## 実行条件

- JavaScriptで利用するライブラリ。Tweenの設定で、時間の代わりにtickを使うことや、CSSプロパティのマッピングなどを指定できる。具体的なランタイム要件はREADMEに記載がない。出典: https://github.com/CreateJS/TweenJS

## 最短手順

- READMEの例では `createjs.Tween.get(myTarget).to({x:300},400).set({label:"hello!"}).wait(500).to({alpha:0,visible:false},1000).call(onComplete)` の形でTweenを作成する。これはREADME掲載の使用例であり、独立した実機検証ではない。出典: https://github.com/CreateJS/TweenJS

## 変更履歴

- 2026-11-15: 初回登録
