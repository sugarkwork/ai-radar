---
name: "OpenViking"
genre: "rag"
url: "https://github.com/volcengine/OpenViking"
repo: "volcengine/OpenViking"
license: "AGPL-3.0"
stars: 42312
language: "Python"
created: "2026-01-05"
updated: "2026-11-16"
forks: 3502
open_issues: 1463
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 431730
archived: false
flags: ["unverified"]
risk_notes: "README記載のLoCoMo・tau2-benchの評価値は作者による報告で、独立実測ではない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/ruyi3699/status/2119092260176584874"]
fetched_at: "2026-11-16T21:10:24.388506+00:00"
---

# OpenViking

## 出来ること

- 知識・メモリ・スキルをviking://仮想ファイルシステム上にまとめ、ls、tree、read、write、grepで閲覧・編集できる。ディレクトリ単位の検索、L0要約・L1概要を確認してから詳細（L2）を読む方法、セッションの保存とメモリ抽出を提供するとREADMEに記載されている。READMEはLoCoMoとtau2-benchの評価結果も報告しているが、作者による報告であり独立検証ではない。

## 目的・背景

- エージェントのメモリを不透明なテキスト・埋め込みの集合として扱わず、保存内容を閲覧・編集できるコンテキストデータベースとして管理することを目的とする。

## 依存関係

- READMEの記載範囲では、モデルプロバイダー、埋め込みモデル、VLMが必要。個別のパッケージ依存関係はここで確認できた資料には記載がない。

## 実行条件

- 独自サーバーをデプロイする場合、READMEはuv、Python 3.10以上、および埋め込みモデルとVLMを備えたモデルプロバイダーを必要条件としている。ブラウザーで試せるStudioも案内されている。

## 最短手順

- README記載の最短導入方針は、まずOpenVikingサーバーを用意し、既存サーバーがあればエージェント連携へ進むこと。独自デプロイにはuv、Python 3.10以上、埋め込みモデルとVLMを備えたモデルプロバイダーが必要。README本文が途中で切れているため、以降の具体的な導入コマンドは確認できていない。

## 変更履歴

- 2026-11-22: 初回登録
