---
name: "Flecha"
genre: "coding-agent"
url: "https://github.com/lucianodiisouza/flecha-browser"
repo: "lucianodiisouza/flecha-browser"
stars: 134
forks: 22
open_issues: 2
size_kb: 5400
language: "TypeScript"
created: "2026-10-22"
updated: "2026-11-11"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/AIExplorerTim/status/2118910064606233060"]
fetched_at: "2026-11-15T00:19:36.693396+00:00"
---

# Flecha

## 出来ること

- Chromiumベースのブラウザー。サイドバー、Spaces、コマンドバー、Peek、分割表示、サイト別TypeScript/CSS、DevToolsなどを備える。READMEは、Coding agents設定でローカルMCPサーバーを有効にすると、Claude CodeやCursorなどからタブ一覧、ページ内容、コンソールログの参照、スクリーンショット、クリック、入力、JavaScript実行ができると説明している。出典: https://github.com/lucianodiisouza/flecha-browser

## 目的・背景

- READMEによると、Arc風のサイドバーやSpacesなどの操作感を保ちつつ、ウェブ開発者向けの機能を加えることを目的とする。Chromium forkを採用し、ElectronではGoogleサインインがブロックされるためとしている。出典: https://github.com/lucianodiisouza/flecha-browser

## 依存関係

- ソースからビルドする場合、README記載の要件はXcodeとコマンドラインツール、PATH上のdepot_tools、対象バージョン（158）のChromiumチェックアウト、Node 22.5以降、リポジトリルートでのnpm ci。Chromium取得は別途ChromiumのmacOSビルド手順に従う。出典: https://github.com/lucianodiisouza/flecha-browser

## 実行条件

- ソースビルド要件として、macOSとApple Siliconが記載されている。Chromiumチェックアウトには100 GB以上のディスク容量と初回ビルドに数時間を要するとREADMEは案内している。ビルド時はAPFSボリュームが必要とされる。配布版についてはApple silicon向けとIntel向けのDMGが案内されている。出典: https://github.com/lucianodiisouza/flecha-browser

## 最短手順

- 配布版はGitHub Releasesから対象CPU向けDMGを取得し、開いてFlechaをApplicationsへドラッグする手順。ソースビルドでは、Chromium 158のチェックアウトと必要ツールを用意し、READMEのdev loopに従ってnpm ci、chromium/scripts/build.sh、chromium/scripts/run.shを実行する。ここではコマンドを実行していない。出典: https://github.com/lucianodiisouza/flecha-browser

## 変更履歴

- 2026-11-15: 初回登録
