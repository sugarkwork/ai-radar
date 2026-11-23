---
name: "PKHeX"
genre: "other"
url: "https://github.com/kwsch/PKHeX"
repo: "kwsch/PKHeX"
license: "unknown"
stars: 5284
language: "C#"
created: "2014-06-28"
updated: "2026-11-16"
forks: 980
open_issues: 8
commits_30d: 26
commit_cadence: "daily"
commits_90d: 72
size_kb: 136711
archived: false
flags: ["unverified"]
risk_notes: "READMEは、暗号化されていないセーブデータを入力として想定すると説明している。実際の対応範囲はゲーム世代やファイル形式に依存する。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119361788617650385"]
fetched_at: "2026-11-19T18:09:53.623961+00:00"
---

# PKHeX

## 出来ること

- ポケモン本編シリーズのセーブエディター。READMEによると、セーブデータや個体ファイル、ふしぎなおくりものファイルなどを扱い、表示したデータを編集して保存できる。世代間転送時の形式変換、Pokémon ShowdownのセットやQRコードのインポート／エクスポートにも対応する。

## 目的・背景

- セーブデータやポケモン関連データの閲覧・編集、共有や世代間転送を行うためのツール。READMEは、他のプレイヤーに知らせずに大幅に改造したポケモンを対戦や交換に使わないよう注意している。

## 依存関係

- READMEで明記されている同梱コード・素材の出典は、QRコード生成コードのQRCoderと、色違いスプライト集のpokesprite。

## 実行条件

- Windows Formsアプリケーション。READMEによると、ビルドには.NET 10とC# 14対応コンパイラが必要。コンソール固有の鍵で暗号化されていないセーブデータを想定し、コンソールとの入出力にはCheckpointなどのセーブデータ管理ツールを使うよう案内している。

対応言語: READMEにはインターフェース翻訳をリソース／外部テキストファイルでサポート可能とあるが、対応するUI言語の一覧は示されていない。（出典: https://github.com/kwsch/PKHeX）
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの案内に従い、対象ゲームからセーブデータを保存データ管理ツールで取り出し、PKHeXで開いてデータを編集・保存する。コンソールへ戻す場合も保存データ管理ツールを使う。ビルドする場合は.NET 10とC# 14対応コンパイラを用意し、DebugまたはRelease構成を選ぶ。

## 変更履歴

- 2026-11-23: 初回登録
