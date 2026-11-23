---
name: "Douyin Downloader"
genre: "other"
url: "https://github.com/jiji262/douyin-downloader"
repo: "jiji262/douyin-downloader"
license: "MIT"
stars: 12648
language: "Python"
created: "2023-05-25"
updated: "2026-11-21"
forks: 1936
open_issues: 40
commits_30d: 19
commit_cadence: "weekly"
commits_90d: 52
size_kb: 7274
archived: false
flags: ["unverified"]
risk_notes: "キーワード検索とプロフィール情報取得はサインインが必要。READMEによると、CLIで動画・写真などをダウンロードする機能はDouyinのリクエスト検証により制限され、プロフィール投稿のブラウザ経由も成功保証はない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/bkdgiffug/status/2119425203671310514"]
fetched_at: "2026-11-22T04:59:57.125105+00:00"
---

# Douyin Downloader

## 出来ること

- AIエージェント向けCLIとskillにより、Douyinのホットボード、リンク判定、ライブ録画、ローカル音声文字起こし、環境確認を利用できる。キーワード検索とプロフィール情報の取得はサインインが必要。従来型CLIは一括処理、日付範囲、再試行、履歴管理に対応する。READMEは、動画・写真等のCLIダウンロードが現在のリクエスト検証に阻まれていると説明している。

## 目的・背景

- Claude Code、CodexなどのエージェントからDouyin関連の情報取得や処理を呼び出せるようにするプロジェクト。agentコマンドは安定したエラーコードを含むJSON行を出力し、同梱skillが呼び出し方を案内する。

## 依存関係

- AIエージェントモードのloginにはPlaywrightとChromium、transcribeにはWhisperが必要。従来型CLIのREADME手順ではPython 3.10以上、requirements.txt、Playwright、Chromiumを導入する。ライブ録画はFFmpegを使うとREADMEに記載されている。

## 実行条件

- README記載の従来型CLIはWindows、macOS、Linux上のPython 3.10以上で利用する。agentモードはサインイン情報を ~/.douyin-dl に保存し、DOUYIN_DL_HOMEで保存先を変更できる。DOUYIN_PROXYでプロキシを指定できる。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- agentモードは `uv tool install douyin-dl-cli` または `pipx install douyin-dl-cli` でCLIを導入し、`douyin-dl agent doctor` を実行する。skillを導入した後、エージェントから利用する。従来型CLIはリポジトリをcloneし、READMEの手順で依存関係を導入、config.example.ymlをconfig.ymlにコピーして設定・ログインし、`python run.py -c config.yml` を実行する。

## 変更履歴

- 2026-11-23: 初回登録
