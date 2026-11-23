---
name: "Obsidian Web Clipper"
genre: "other"
url: "https://github.com/obsidianmd/obsidian-clipper"
repo: "obsidianmd/obsidian-clipper"
license: "MIT"
stars: 5620
language: "TypeScript"
created: "2024-08-29"
updated: "2026-11-20"
forks: 795
open_issues: 277
commits_30d: 25
commit_cadence: "daily"
commits_90d: 36
size_kb: 9672
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/rosemoni18/status/2119211334797840872"]
fetched_at: "2026-11-20T03:08:34.694138+00:00"
---

# Obsidian Web Clipper

## 出来ること

- ブラウザーでWebページをハイライトして取り込み、保存した内容をMarkdownファイルとしてオフラインで読めるようにします。テンプレート、変数、フィルターの機能については公式ドキュメントを参照できます。

## 目的・背景

- Web上の情報を、長期保存やオフライン閲覧に向くMarkdownファイルとして手元に残すためのブラウザー拡張機能です。

## 依存関係

- READMEでは、ブラウザー互換性にwebextension-polyfill、コンテンツ抽出とMarkdown変換にdefuddle、HTMLサニタイズにDOMPurifyなどを使用すると説明しています。

## 実行条件

- READMEに記載された配布先はChromium系ブラウザー、Firefox（Firefox Mobileを含む）、Safari（macOS、iOS、iPadOS）、Microsoft Edgeです。ローカルビルドにはnpmを使い、iOS SimulatorでのテストにはmacOSとXcodeが必要です。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の公式ブラウザー配布先から拡張機能をインストールします。開発用にローカル導入する場合は、`npm run build`を実行し、Chromiumでは`chrome://extensions`のDeveloper modeから`dist`を読み込み、Firefoxでは`about:debugging#/runtime/this-firefox`から`dist_firefox/manifest.json`を一時アドオンとして読み込みます。

## 変更履歴

- 2026-11-23: 初回登録
