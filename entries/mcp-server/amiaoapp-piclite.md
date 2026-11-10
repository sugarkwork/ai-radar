---
name: "PicLite"
genre: "mcp-server"
repo: "amiaoapp/PicLite"
url: "https://github.com/amiaoapp/PicLite"
license: "GPL-3.0"
stars: 1034
forks: 66
open_issues: 0
size_kb: 17329
language: "TypeScript"
created: "2026-07-28"
updated: "2026-11-06"
archived: false
commits_30d: 70
commits_90d: 100
commit_cadence: "daily"
last_release: "v2.1.5"
flags: ["unverified"]
risk_notes: ["圧縮率・画質・処理時間、各OS向け配布バイナリと第三者MCPクライアントの実動作は未検証。プロジェクトは公式MCP SDKと実ファイルを使った試験を報告している。"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Ryrenz/status/2117830448944382018"]
fetched_at: "2026-11-10T10:43:43+00:00"
---

# PicLite — MCPで呼び出せるローカル画像・GIF圧縮ツール

## 出来ること

- 画像とGIFをローカルで一括圧縮・変換・縮小できる。MCPでは画像の寸法・バイト数・フレーム数を確認し、圧縮や透明PNGのカバー画像生成を実行できる。 [公式MCPガイド](https://raw.githubusercontent.com/amiaoapp/PicLite/main/docs/MCP.md)

## 目的・背景

- スクリーンショットなどの出力サイズを抑えるため、JPEG・WebP・PNGなどの候補を実際にエンコードして比較する。透明画像はJPEG候補から除外する。出力サイズと処理前後のプレビューは確認できるが、圧縮率や画質は独立に測定していない。 [公式README](https://raw.githubusercontent.com/amiaoapp/PicLite/main/README.md)

## 依存関係

- ソースからデスクトップ版をビルドする場合はNode.js 22.13以上、安定版Rust、対象OSのTauri 2システム依存関係が必要。READMEはGPL-3.0-or-laterと記載し、リポジトリのライセンス欄には親工程のGitHub API値を採用した。 [公式README](https://raw.githubusercontent.com/amiaoapp/PicLite/main/README.md)

## 実行条件

- Windows・macOS・Linux向けデスクトップ版がある。ブラウザ版とDocker版は訪問者のブラウザ内で画像を処理する。ローカルMCPには、stdio対応クライアントと、対象ファイルにアクセスできる実行環境が必要。ローカルstdio接続にAPIキーは不要。 [公式README](https://raw.githubusercontent.com/amiaoapp/PicLite/main/README.md) [公式MCPガイド](https://raw.githubusercontent.com/amiaoapp/PicLite/main/docs/MCP.md)

## 最短手順

- 公式リリースから対応するデスクトップ版を選ぶ。AIクライアントのstdio MCP設定で、commandにPicLite実行ファイルの絶対パス、argsに["--mcp"]を指定する。AIに対象GIFの絶対パスを渡し、piclite_compressで50%に縮小してWebPで保存し、piclite_inspectで出力がアニメーションか確認するよう依頼する。圧縮は既定で別ファイルに保存する。 [公式リリース](https://github.com/amiaoapp/PicLite/releases/tag/v2.1.5) [公式MCPガイド](https://raw.githubusercontent.com/amiaoapp/PicLite/main/docs/MCP.md)

## 変更履歴

- 2026-11-10: 初回登録
