---
name: "Qwen3.8 Weight-Space Programming (Calmer V2)"
genre: "model-serving"
url: "https://github.com/Xananthium/Qwen3.8-Weight-Space-Programming"
repo: "Xananthium/Qwen3.8-Weight-Space-Programming"
license: "Apache-2.0"
stars: 4
language: "Python"
created: "2026-11-05"
updated: "2026-11-07"
forks: 0
open_issues: 0
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 3
size_kb: 3330
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119249805297738022"]
fetched_at: "2026-11-18T02:19:13.192429+00:00"
---

# Qwen3.8 Weight-Space Programming (Calmer V2)

## 出来ること

- Qwen3.8 27Bのモデル重みに固定の疎な補正を加えたCalmer V1/V2を紹介し、V2のモデル配布先、研究報告、実行パッケージ、フィッティングコード、マージ済みエクスポートの記録へ案内している。README記載の評価は探索的な小規模パネルで、一般的なベンチマーク結果ではない。

## 目的・背景

- 作者によると、反復的な確認を減らしつつ有用な推論を保つ目的で編集を試みた。READMEには改善例とともに、説明の誤り、未完了回答、生成の不整形、V2の追加確認が実施できなかったことも記載されている。これらは作者の報告であり、独立した実測としては扱わない。

## 依存関係

- READMEは試用に互換性のあるGGUFエンジンが必要と案内し、Python 3.12以降を公開チェックに挙げている。具体的な依存パッケージ一覧はこのREADME抜粋では確認できない。

## 実行条件

- READMEによると、V2配布物には補正重みとマージ済みGGUFがあり、起動方法はモデルカードおよびV2ランタイム資料に案内されている。表記された測定結果はpacked-baseとFP32補正を使うランタイムに関するもので、マージ済みモデルの検証は別記録とされる。

## 最短手順

- READMEからV2モデルカードとダウンロード先へ進み、対象アーティファクトごとの検証情報と起動手順を確認する。挙動や根拠を確認する場合はV2研究報告・例・レポートを参照する。

## 変更履歴

- 2026-11-23: 初回登録
