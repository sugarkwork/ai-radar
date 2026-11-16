---
name: "YARA"
genre: "other"
url: "https://github.com/VirusTotal/yara"
repo: "VirusTotal/yara"
license: "BSD-3-Clause"
stars: 10043
language: "C"
created: "2012-12-06"
updated: "2026-10-27"
forks: 1605
open_issues: 170
commits_30d: 16
commit_cadence: "weekly"
commits_90d: 29
size_kb: 24478
archived: false
flags: ["unverified"]
risk_notes: "プロジェクトはメンテナンスモードです。READMEに記載された具体的なサポート期間や今後の更新方針は確認できません。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/RoundtableSpace/status/2119071100307169630"]
fetched_at: "2026-11-16T17:11:37.542909+00:00"
---

# YARA

## 出来ること

- テキストまたはバイナリのパターンと真偽式を組み合わせたルールを作成し、ファイルを識別・分類できます。ワイルドカード、大文字小文字を区別しない文字列、正規表現、特殊演算子などを利用できます。出典: https://github.com/VirusTotal/yara

## 目的・背景

- マルウェア研究者によるマルウェアサンプルの識別・分類を主な目的とします。READMEでは「or whatever you want to describe」とも説明されています。出典: https://github.com/VirusTotal/yara

## 依存関係

- READMEは依存関係を列挙していません。Pythonから使う方法として yara-python 拡張に言及しています。

## 実行条件

- Windows、Linux、Mac OS Xで動作し、コマンドラインまたは yara-python 拡張を使ったPythonスクリプトから利用できます。出典: https://github.com/VirusTotal/yara

## 最短手順

- ルールに文字列パターンと、それらを評価する condition の真偽式を記述します。READMEの例では、3つの文字列パターンのいずれかを含むファイルを silent_banker として報告するルールが示されています。出典: https://github.com/VirusTotal/yara

## 変更履歴

- 2026-11-16: 初回登録
