---
name: "Yoga"
genre: "other"
url: "https://github.com/react/yoga"
repo: "react/yoga"
license: "MIT"
stars: 18954
language: "C++"
created: "2014-04-07"
updated: "2026-11-13"
forks: 1586
open_issues: 190
commits_30d: 16
commit_cadence: "weekly"
commits_90d: 34
size_kb: 27581
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RealMarvelX/status/2119161121387020570"]
fetched_at: "2026-11-17T06:25:05.975404+00:00"
---

# Yoga

## 出来ること

- 複数言語向けバインディングを備えた、組み込み可能なflexboxレイアウトエンジン。READMEは「Yoga is an embeddable and performant flexbox layout engine with bindings for multiple languages.」と説明している。

## 目的・背景

- アプリケーションに組み込めるflexboxレイアウトエンジンとして説明されている。性能の独立検証はREADMEに記載されていない。

## 依存関係

- メイン実装はC++ 20を対象とし、ビルドロジックにCMakeを使用する。テスト生成ではyarn classicと依存関係のインストールが必要。ninjaは必須ではない。

## 実行条件

- README記載のビルド・テスト手順は `./unit_tests Debug` と `./unit_tests Release`。テスト生成にはyarn classicを用意し、`yarn install` の後、yogaディレクトリで `yarn gentest` を実行する。

## 最短手順

- READMEの案内に従い、Debugビルドのユニットテストは `./unit_tests Debug`、Releaseは `./unit_tests Release` を実行する。テスト用fixtureの生成はyarn classicを用意して `yarn install`、続けてyogaディレクトリで `yarn gentest` を実行する。

## 変更履歴

- 2026-11-22: 初回登録
