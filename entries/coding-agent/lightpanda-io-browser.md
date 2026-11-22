---
name: "Lightpanda Browser"
genre: "coding-agent"
url: "https://github.com/lightpanda-io/browser"
repo: "lightpanda-io/browser"
license: "AGPL-3.0"
stars: 42144
language: "Zig"
created: "2023-02-07"
updated: "2026-11-17"
forks: 2124
open_issues: 81
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 47378
archived: false
flags: ["unverified"]
risk_notes: "Linuxのnightlyバイナリはglibc依存で、必要なバージョンはx86_64が2.35、arm64が2.38。musl系LinuxやAndroid/Termuxでは動作せず、WindowsはWSL経由です。ベンチマークの速度・メモリー比較はREADME記載の作者側測定条件による報告です。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/bkdgiffug/status/2119125730760241560"]
fetched_at: "2026-11-17T01:16:21.359270+00:00"
---

# Lightpanda Browser

## 出来ること

- URLのHTML、Markdown、PNG、PDF、構造化データを取得できます。CDPサーバーを起動し、Puppeteerなどから接続できます。また、WebDriver BiDiにも対応するとREADMEに記載されています。ネイティブエージェントは自然言語やスラッシュコマンドでページ移動、クリック、フォーム入力、構造化データ抽出を行い、操作をPandaScriptとして保存・再実行できます。

## 目的・背景

- AIエージェントと自動化向けに、Zigで一から実装したヘッドレスブラウザーです。READMEのベンチマークは、AWS EC2 m5.largeでネットワーク越しに933ページを要求した条件として、100ページ時のピークメモリー123MB（Headless Chromeは2GB）、実行時間5秒（Headless Chromeは46秒）と報告しています。この数値はREADME内の測定報告であり、独立した実機検証ではありません。

## 依存関係

- READMEには、公式Dockerイメージの提供、Puppeteer接続例、エージェントの対応LLMプロバイダーが記載されています。バイナリを使う場合、Linux版はglibcを必要とし、x86_64では2.35、arm64では2.38が必要です。

## 実行条件

- README記載のnightlyバイナリはLinuxとmacOSのx86_64およびaarch64向けです。Linux版はglibc 2.35以上（x86_64）、2.38以上（arm64）が必要で、musl系Linuxでは実行できません。Android/Termux向けのネイティブ版はなく、WindowsではWSL内にインストールします。DockerイメージはLinux amd64とarm64向けです。

## 最短手順

- LinuxではREADME記載の例としてnightlyバイナリを取得し、実行権限を付けてバージョンを確認します（例: `curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux`、`chmod a+x ./lightpanda`、`./lightpanda version`）。URL取得は `./lightpanda fetch --obey-robots --dump html <URL>`、CDPサーバーは `./lightpanda serve --obey-robots --host 127.0.0.1 --port 9222` で起動できます。

## 変更履歴

- 2026-11-22: 初回登録
