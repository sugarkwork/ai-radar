---
name: "Sakutto"
genre: "other"
url: "https://github.com/jammaru/sakutto"
repo: "jammaru/sakutto"
license: "MIT"
stars: 271
language: "TypeScript"
created: "2026-11-05"
updated: "2026-11-18"
forks: 30
open_issues: 15
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 12304
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2119274964054639103"]
fetched_at: "2026-11-18T15:36:35.362557+00:00"
---

# Sakutto

## 出来ること

- ページ全体、選択テキスト、PDF、YouTubeやXなどの動画字幕、入力中の文章を翻訳するChrome・Firefox拡張。既定の翻訳エンジンはPLaMo 3 Translateで、WebGPUまたはCPU上で実行するとREADMEに記載されています。

## 目的・背景

- 読む文章と書く文章を、別のツールに切り替えずに翻訳できるようにするローカル優先の拡張として紹介されています。READMEによると、ページ本文、選択範囲、用語集、翻訳は端末上に保持され、分析やクラッシュ報告はありません。

## 依存関係

- 既定エンジンはPLaMo 3 Translateで、固定バージョンのwllamaを介して動作するとREADMEにあります。ChromeではPLaMoが生成できない11の追加翻訳先に限り、Chrome内蔵翻訳を使用します。FirefoxはPLaMoのみです。

## 実行条件

- ChromeまたはFirefoxの拡張として利用します。PLaMoはWebGPUまたはCPUで実行されます。READMEではPLaMoの対応言語を53言語と説明し、Chromeではさらに11の翻訳先を内蔵翻訳で補うとしています。PLaMoの対象に「やさしい日本語」が含まれます。

対応言語: READMEはPLaMoの対応言語を53言語と記載。ChromeではPLaMoが対応しない追加11翻訳先を内蔵翻訳で補う。個別の言語一覧は確認できる資料範囲に含まれない。（出典: https://github.com/jammaru/sakutto）
日本語対応: 日本語を翻訳先に指定可能。「やさしい日本語」への変換にも対応し、これはPLaMoのみが生成するとREADMEに記載。（出典: https://github.com/jammaru/sakutto）

## 最短手順

- READMEに記載されたChromeまたはFirefox向けの拡張をインストールし、翻訳先を設定してページや選択テキストなどから翻訳します。入力欄ではAlt+T（MacではOption+T）で翻訳プレビューを表示し、もう一度押すかCtrl+Enter（Macでは⌘+Enter）で入力欄を置き換えます。

## 変更履歴

- 2026-11-23: 初回登録
