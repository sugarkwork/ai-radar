---
repo: "morluto/rea"
name: "REA"
genre: "mcp-server"
url: "https://github.com/morluto/rea"
author: "morluto"
license: "MIT"
stars: 444457
language: "TypeScript"
created: "2026-04-14"
updated: "2026-11-09"
forks: 109755
open_issues: 1695
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 145429
archived: false
last_release: "rea-agents-6.8.0"
last_release_at: "2026-10-25"
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "GitHub API の数値と README/手順書の記述は 2026-11-09 時点で確認済み。未検証なのは (1) Ghidra/Hopper を実際に起動した動作確認、(2) README showcase の再構成数値（3,205 ケース等）で、効果は著者側の主張にとどまる。Hopper は商用（デモは制限付き）、Windows の Ghidra 対応は実験的 P0 で読み取り専用。"
source_post: "https://x.com/wquguru/status/2113181135522214168"
sources: ["https://github.com/morluto/rea", "https://api.github.com/repos/morluto/rea", "https://x.com/wquguru/status/2113181135522214168"]
type: "repo"
first_seen: "2026-11-09"
fetched_at: "2026-11-09T05:51:44Z"
---

# REA — バイナリからアプリまで、エージェント向け逆解析 MCP サーバー

## 出来ること

- ネイティブバイナリ（PE/ELF/Mach-O）、JavaScript/Electron、.NET、Android APK、Web サイト、HTTP/パケットキャプチャなどを、MCP 経由でエージェントに調査させる。結果には根拠（Evidence）と適用限界が付く。
- ネイティブ解析は既存の Ghidra・Hopper・IDA・Kuna を利用する。Ghidra アダプタは逆コンパイル、逆アセンブル、解決済み呼び出し、xref、関数ダンプなど 27 個の読み取り専用操作を公開する（Linux/macOS では関数名・コメントの編集も可能）。
- Ghidra 側は Java 拡張（ReaGhidraBridge.java）、Hopper 側は Python ブリッジ（hopper_bridge.py）として同梱され、CLI からもエージェントからも同じ操作を呼べる。
- CLI は `rea analyze-javascript-application`、`rea doctor`、`rea environment-build` など。MCP サーバーは stdio で動き、`npx rea-agents mcp` で起動する。
- 記録済みの HTTP 通信から、エージェントの学習・評価用にローカル環境（AgentEnv 形式）を生成できる。

## 目的・背景

- 元の X 投稿は「Ghidra と Hopper を Codex/Cursor に接続し、擬似コードと呼び出し連鎖をそのまま出す」と紹介している。
- 一次情報では、REA はローカルの MCP サーバー兼 CLI で、`rea setup` が Codex・Cursor・Claude Code・Gemini CLI などの設定に MCP サーバーとワークフロー指示を登録する。投稿の「接続する」はこの構成を指す。
- 2026-04 公開、MIT、TypeScript。6.8.0（2026-10-25）の時点で Ghidra 拡張・Hopper ブリッジ・多数の静的解析器・RL 環境生成まで含み、試作ではなく継続開発中の大規模実装。
- 解析はローカルで完結し、対象アプリをアップロードしない（README）。

## 依存関係

- Node.js 22.x（>=22.23.4）/ 24.x（>=24.22.1）/ 26.12.1+ と npm。Node 23・25 は非対応で、インストーラが Node を更新することはない。
- ネイティブ解析には Ghidra 12.1 以降と、そのビルドが要求する 64bit JDK（12.1 系は JDK 21+、12.2 は JDK 25+）、ホスト用ネイティブ逆コンパイラが必要（動作確認は Ghidra 12.1.4 + JDK 21）。
- Hopper は別売の商用ソフトで、無料デモはベンダー定義の制限付き。REA は既存の Hopper を再利用し、macOS 12+ か x86_64 の主要 Linux ディストリビューションでのみ自動導入を提案する。
- Linux では procps 互換の `ps` が PATH に必要（Ghidra・JADX・ファームウェア・静的 JS 解析のプロセス管理用）。
- JADX、objdump、Rizin、WABT、tshark、Apktool、adb、pwntools などは利用者が用意する。REA はこれらをインストールしない。

## 実行条件

- クライアントはローカル MCP サーバーに対応している必要がある。`rea setup` は Codex、Cursor、Claude Code、Claude Desktop、Gemini CLI、Windsurf、VS Code、GitHub Copilot CLI などを自動設定する。
- Ghidra は REA が導入しない。`GHIDRA_INSTALL_DIR` と `JAVA_HOME` を設定し、`rea doctor --json` で認識を確認してから `rea setup` する。
- Hopper は初回起動時にデモ/ライセンス選択のダイアログを同じユーザーセッションで済ませる必要がある。無人実行の前に一度起動しておく。
- Windows の Ghidra 対応は実験的（P0）で読み取り専用。IDA・Kuna・JEB はそれぞれ別途ライセンスやクライアントが必要。
- セットアップは既存のエージェント設定を書き換える（バックアップは自動作成されるが、差分は目視確認する）。

## 最短手順

- Node.js（22/24/26 系）と npm を用意する。
- `npx rea-agents setup` を実行し、使うエージェント（Codex / Cursor など）を選んで変更内容を承認する。その後エージェントを再起動する。
- ネイティブ解析を使う場合は、先に Ghidra を展開して `export GHIDRA_INSTALL_DIR=/path/to/ghidra_12.1.4_PUBLIC` と `export JAVA_HOME=/path/to/jdk-21` を設定し、`rea doctor --json` で確認する。
- エージェントに「このバイナリの関数 X の擬似コードと、その呼び出し元・参照元を根拠付きで示して」と依頼する。MCP ツール経由で Ghidra/Hopper が起動する。
- CLI だけで試すなら `npx -y rea-agents@latest analyze-javascript-application /abs/path/to/app --json`。ネイティブ解析はプロバイダ設定後に `rea` コマンドで実行する。

## 変更履歴

- 2026-11-09: 初回登録
