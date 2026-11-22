---
name: "terminal-browser"
genre: "other"
url: "https://github.com/zenbu-labs/terminal-browser"
repo: "zenbu-labs/terminal-browser"
stars: 4690
forks: 243
open_issues: 128
size_kb: 23683
language: "TypeScript"
created: "2026-07-06"
updated: "2026-11-16"
archived: false
license: "MIT"
commits_30d: 96
commits_90d: 100
commit_cadence: "daily"
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/awe0_io/status/2119114978372551110"]
fetched_at: "2026-11-16T23:15:32.470248+00:00"
---

# terminal-browser

## 出来ること

- ターミナル内でブラウザーを起動し、URLを開く、分割ペインで表示する、SSH経由でリモート側のネットワークへ接続する、既存のTUIに埋め込むといった使い方ができます。CLIから開いているブラウザーを操作する機能もあります。出典: https://github.com/zenbu-labs/terminal-browser/blob/main/README.md

## 目的・背景

- kitty graphics protocolに対応するターミナルで、Chromiumが生成した画素を表示し、画面の変更領域を小さなパッチとして送る仕組みを説明しています。作者の説明によると、描画はElectronのoffscreen rendering APIを使い、端末入力をChromiumへ合成イベントとして送ります。出典: https://github.com/zenbu-labs/terminal-browser/blob/main/README.md

## 依存関係

- READMEでは、Chromiumの描画にElectronのoffscreen rendering APIを使用し、外側のUIにRustベースのグラフィックスエンジンとReactのカスタムレンダラーを使用すると説明しています。pixelライブラリは、この描画基盤を使ったターミナル向けグラフィカルアプリケーションの作成に利用できます。出典: https://github.com/zenbu-labs/terminal-browser/blob/main/README.md

## 実行条件

- README記載の導入方法はmacOS・Linux向けのcurlインストーラーまたはHomebrewです。WindowsではWSLが必要で、対応ターミナルは限られると記載されています。画素表示にはkitty graphics protocolをサポートするターミナルが必要です。出典: https://github.com/zenbu-labs/terminal-browser/blob/main/README.md

## 最短手順

- macOS・Linuxでは `brew install terminal-browser`、またはREADME記載のcurlインストーラーを使い、`terminal-browser` で起動します。URLを指定して開く場合は `terminal-browser open <url>`。READMEは導入・実行方法を示すもので、ここでは実行確認していません。出典: https://github.com/zenbu-labs/terminal-browser/blob/main/README.md

## 変更履歴

- 2026-11-22: 初回登録
