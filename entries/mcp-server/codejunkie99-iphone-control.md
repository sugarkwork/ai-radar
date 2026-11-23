---
name: "iPhone Control"
genre: "mcp-server"
url: "https://github.com/codejunkie99/iphone-control"
repo: "codejunkie99/iphone-control"
license: "Apache-2.0"
stars: 10
language: "Python"
created: "2026-11-08"
updated: "2026-11-08"
forks: 2
open_issues: 0
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 1
size_kb: 55
archived: false
flags: ["unverified"]
risk_notes: "READMEはmacOS 27上の実機での操作例とSIMULATEDバックエンドによる49テストを報告している。通常の承認付きモードでは、ミラーリング画面がどのiPhoneを表示しているか特定する文書化済みインターフェースがないため操作がブロックされる。--unattendedではデバイス識別を所有者の申告に委ねる。実機での独立検証は未実施。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Av1dlive/status/2119377712272027975"]
fetched_at: "2026-11-19T21:09:52.260848+00:00"
---

# iPhone Control

## 出来ること

- Claude Code・Codex向けMCPサーバーとGrok Bot向けCLIを通じて、Mac上のiPhone Mirroringに表示されたiPhoneを操作する。接続・端末・セッション状態や機能の確認、スクリーンショット取得とOCR、タップ、文字入力、キー入力、スクロール、最大20ステップのバッチ操作を提供する。READMEによれば入力先はiPhone Mirroringウィンドウに限られ、シェル実行や一般的なデスクトップ自動化の機能はない。

## 目的・背景

- エージェントから所有者自身のiPhoneを操作するためのプロトタイプ。READMEは、通常モードではセッションと各操作をメニューバーから所有者が承認し、「Stop now」で即時停止できると説明している。

## 依存関係

- macOS上のApple iPhone Mirroringを利用する。macOSバックエンドは画面取得・操作・OCRにPyObjCを使用する。Claude Code/CodexではMCPサーバー、Grok BotではCLIを利用する。

## 実行条件

- セットアップ手順はリポジトリのdocs/SETUP.mdを参照。README記載の実機試行環境はmacOS 27と物理iPhone。通常の承認付きモードでは、ミラーリングウィンドウに表示中のiPhoneを特定できないため操作がブロックされる。--unattendedは端末の識別を所有者の申告に依存させる。

対応言語: 操作で入力できるのは任意の文字列だが、READMEは対応する自然言語の範囲を明示していない。OCRの対応言語も不明。（出典: https://github.com/codejunkie99/iphone-control）
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの案内に従いdocs/SETUP.mdを読み、利用するクライアントに合わせてMCPサーバーまたはCLIを設定する。CLIはiphonectl statusで状態を確認し、iphonectl observeで画面を取得する。操作のコマンド例・設定詳細はREADMEが案内するdocs/SETUP.mdとexamples/を参照。

## 変更履歴

- 2026-11-23: 初回登録
