---
name: "Blackbird"
genre: "other"
url: "https://github.com/antoniaci/blackbird"
repo: "antoniaci/blackbird"
license: "unknown"
stars: 10154
language: "Python"
created: "2022-05-06"
updated: "2026-11-03"
forks: 1472
open_issues: 16
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 8
size_kb: 14580
archived: false
flags: ["unverified"]
risk_notes: "README記載の「低い誤検出率」やAIによるプロファイリングの有効性は独立検証されていない。ライセンスはAPI上unknown。README内のclone先は別リポジトリ p1ngul1n0/blackbird を指しており、対象リポジトリでの実行・依存関係は確認できない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118713263290741015"]
fetched_at: "2026-11-13T20:09:13.755613+00:00"
---

# Blackbird

## 出来ること

- READMEによると、ユーザー名またはメールアドレスを600以上のプラットフォームで検索し、結果をPDF/CSVに出力するCLI。任意のAI機能は見つかったサイト名を分析してユーザーの行動・技術プロフィールを返すと説明されている。READMEはAIへ送信するのはサイト名のみと主張している。

## 目的・背景

- READMEは、WhatsMyNameとの連携により逆ユーザー名検索を行い、検索結果の分析を支援するOSINTツールと説明している。

## 依存関係

- READMEはPythonのrequirements.txtを使う手順を示し、WhatsMyNameとの統合を記載している。対象リポジトリの依存内容はREADMEから確認できない。

## 実行条件

- READMEの手順はPython環境とpipによる依存インストールを前提とする。AI機能の利用にはAPIキー設定が必要と記載されている。第三者のLinux向けOTinstallerを使う選択肢も記載されている。利用時はREADMEの許可なく使用しない旨の注意に従うこと。

## 最短手順

- README記載の手順は、リポジトリをcloneし、requirements.txtをインストールした後、`python blackbird.py --username johndoe` または `python blackbird.py --email johndoe@example.com` を実行するもの。AI利用はAPIキーを設定し、`python blackbird.py --username johndoe --ai` を実行する。clone例は別リポジトリ p1ngul1n0/blackbird を指定しているため、対象リポジトリでそのまま適用できるかは未確認。

## 変更履歴

- 2026-11-14: 初回登録
