---
repo: "valuecodes/jev-on-air"
name: "JevOnAir"
genre: "finance-quant"
url: "https://github.com/valuecodes/jev-on-air"
stars: 0
forks: 0
open_issues: 3
size_kb: 999
language: "TypeScript"
created: "2026-09-26"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 11
commits_90d: 47
commit_cadence: "weekly"
last_release: "v0.1.0"
flags: ["unverified"]
risk_notes: "公開READMEとリリース記述を確認した。CLIの動作、収益性、判断精度、配信から模擬約定までの遅延、外部サービスの現行料金と利用条件は未検証。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115461838607659474"]
fetched_at: "2026-11-10T12:19:45Z"
---

# JevOnAir — 配信の文字起こしと市場データを使うペーパートレードCLI

## 出来ること

- YouTube配信を文字起こしし、Alpacaから取得した価格データと合わせてJevに渡す。著者のREADMEによれば、判断と模擬約定は標準出力とJSONL台帳に記録される。
- CLIは録画の再生と過去イベントのバックテストにも対応する。

## 目的・背景

- 発言と価格の推移を入力にしたAIの判断を、模擬ポートフォリオで追跡する研究用ツール。処理の構成と操作手順を文書で確認した。

## 依存関係

- Node.js 26、pnpm 12、uv、ffmpeg。文字起こしにはyt-dlpとfaster-whisper、市場データにはAlpaca、判断にはTypeSafe AIのJevを使う。

## 実行条件

- uvとffmpegをPATHに置き、AlpacaとTypeSafe AIのAPIキーを設定する。READMEによればAlpacaはペーパートレード口座のキーを利用できる。リポジトリのライセンスはMIT。

## 最短手順

- リポジトリ直下で `pnpm install` を実行し、`.env.example` を `.env` にコピーしてREADME指定のAPIキーを設定する。
- 端末ツールを使えるAIエージェントから `pnpm cli jev <YouTube配信URL> --language=en --json` を呼び出す。模擬取引のイベントは標準出力のJSONLで読み取れる。

## 変更履歴

- 2026-11-10: 初回登録
