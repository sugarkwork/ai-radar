---
name: "losslesscut-mcp"
genre: "mcp-server"
url: "https://github.com/bariswha/losslesscut-mcp"
repo: "bariswha/losslesscut-mcp"
stars: 4
forks: 0
open_issues: 0
size_kb: 443
language: "JavaScript"
created: "2026-11-11"
updated: "2026-11-12"
archived: false
license: "MIT"
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/doodi_dev/status/2121789030299754718"]
fetched_at: "2026-11-15T08:13:40.533104+00:00"
---

# losslesscut-mcp

## 出来ること

- READMEによると、FFmpegを使って動画のメディア情報、フレーム、シーン変化、無音区間、黒画面、音量、キーフレームを解析します。また、LosslessCutのローカルHTTP APIを介してファイルを開き、セグメントを設定・選択し、選択したセグメントを書き出せます。作者はLosslessCut 3.70.2での実行例を掲載しています。

## 目的・背景

- ClaudeなどのAIアシスタントから動画を解析し、LosslessCutを操作してカット作業を行うためのMCPサーバーです。READMEは、カット処理をLosslessCutとFFmpegが再エンコードなしで行うと説明しています。

## 依存関係

- README記載の要件は、LosslessCut 3.70以降、Node.js 20以降、stdioサーバーに対応したMCPクライアントです。解析ツールにはFFmpegとFFprobeがPATH上に必要です。

## 実行条件

- LosslessCutを`--http-api`付きで起動し、既定では`127.0.0.1:8080`で待ち受けさせます。HTTP APIは既定で無効です。READMEは、APIに認証がなく、起動中は同じコンピューター上のプログラムから制御できるため、使用中のみ有効にするよう記載しています。

## 最短手順

- READMEのClaude Code向け手順は、LosslessCutを`--http-api`付きで起動し、`claude mcp add losslesscut -- npx -y github:bariswha/losslesscut-mcp`でMCPサーバーを追加する方法です。その後、アシスタントに動画の絶対パスを指定して解析やカットを依頼します。

## 変更履歴

- 2026-11-15: 初回登録
