---
name: "Voxarium"
genre: "tts-audio"
url: "https://github.com/AhmadMansy/voxarium"
repo: "AhmadMansy/voxarium"
license: "AGPL-3.0"
stars: 7
language: "TypeScript"
created: "2026-10-29"
updated: "2026-11-08"
forks: 0
open_issues: 9
commits_30d: 40
commit_cadence: "daily"
commits_90d: 40
size_kb: 17353
archived: false
flags: ["unverified"]
risk_notes: "LinuxとmacOSはCIで未検証。PythonモデルはWindowsでもKokoro、Supertonic、Piper以外がエンドツーエンド未検証とREADMEに記載。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/dextune/status/2121037326759473319"]
fetched_at: "2026-11-13T11:10:54.873037+00:00"
---

# Voxarium

## 出来ること

- Windows、Linux、macOS向けのローカルTTSスタジオ。スクリプトから音声を生成し、音声の選択・調整、最大50行のバッチ処理、WAV/MP3出力ができる。ローカルAPI、MCPサーバー、CLIも提供するとREADMEに記載。

## 目的・背景

- 作者は、音声生成、音声ファイル、履歴、書き出しをローカルに保ち、モデルの初回ダウンロード後はオフラインで使えるアプリとして説明している。

## 依存関係

- ソースからビルドする場合はNode.js 22以上が必要。小型モデルはアプリ内のWebAssemblyまたはWebGPUで動作し、その他のモデルはローカルPythonサイドカーを使うとREADMEに記載。

## 実行条件

- README記載の要件はWindows 10/11 x64、Linux x64、またはmacOS。GPUは任意。LinuxとmacOSはビルドされるがCIでは未検証。PythonモデルはWindowsでKokoro、Supertonic、Piperがエンドツーエンドで確認済みで、ほかの12モデルはレシピがあるものの未確認。

## 最短手順

- READMEはGitHub ReleasesからOS別インストーラーを取得し、SHA256SUMS.txtと照合する手順を案内している。初回起動時にモデルを選び、必要なモデルファイルをダウンロードする。ソースビルドにはNode.js 22以上が必要。

## 変更履歴

- 2026-11-13: 初回登録
