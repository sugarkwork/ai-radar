---
repo: storytold/craft-anything
name: Craft Anything
genre: coding-agent
url: https://github.com/storytold/craft-anything
license: Apache-2.0
stars: 17885
language: Rust
created: 2026-10-31
updated: 2026-11-06
added: 2026-11-03
sources:
  - https://x.com/rammcodes/status/2117515072893284799
forks: 3282
open_issues: 207
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 10525
archived: false
fetched_at: "2026-11-06T22:52:41Z"
last_release: v0.5.0
last_release_at: 2026-11-06
---

# Craft Anything

## 出来ること

- 対象（Web サイト、デスクトップアプリ、スマホアプリ、ゲーム、ファイル）を**実測ツールで調査**し、何でどう作られているかを証拠付きで返す。各回答に信頼度・網羅率・限界が付く。
- 調査結果をもとに、手元のコーディングエージェントに**新しいプロジェクトを実装させる**。実装後は元と見比べて差分を指摘し、修正ラウンドを回す（`--rounds`）。
- 調査ツールはすべて CLI サブコマンドかつ MCP ツールとして公開される。アプリを開かずにエージェントから丸ごと実行できる。
- プロジェクト管理: `Documents/Craft Anything` 配下に1プロジェクト1フォルダ。`craft.json`（要求・対象・状態・履歴）、`capture/`（取得物）などを保持し、`--continue-in` / `--existing edit` で継続編集できる。
- ネイティブアプリ。macOS / Windows / Linux / FreeBSD と Web（WebAssembly、ブラウザ内で動作）に対応。
- **承認をプロジェクト単位で決める**（v0.5.0）: ビルダーの承認をアクションの種類ごとにどう扱うかをプロジェクトごとに選べる。プロンプト欄の下のメニューか `/approvals` から設定する。
- **OpenCode 実行**: ネイティブの OpenCode 実行にも Craft Anything のツールが渡り、ツール呼び出しが画面に出る。

## 目的・背景

storytold による「clean-room」実装支援ツール。100% Rust、Apache-2.0（README のバッジは MIT OR Apache-2.0 表記）。2026-10-31 作成で公開直後、pushed 2026-11-03。README 自身が **early alpha** と明記している。背景として、既存ソフトの見た目・挙動を「調べて自分の版を作る」作業を、対象の複製ではなく調査＋再実装として回す枠組みになっている。

## 依存関係

- Rust **1.97 以上**（依存 crate の要求。`rustup update`）。
- Debian / Ubuntu でデスクトップアプリをビルドする場合は追加パッケージ: `libxkbcommon-dev libwayland-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libgtk-3-dev`。
- **ビルドにはサインイン済みのコーディングエージェントが必須**。第一対応は Claude Code で、利用者の `claude` をそのまま実行する（アカウント情報はツール側で扱わない）。**GitHub Copilot** はインストール済みの Copilot CLI を ACP 経由で使える（別途 `copilot login` でサインイン）。Codex アダプタは存在するが実インストールでの検証は未実施。ACP 対応の他エージェント（Gemini CLI / Qwen Code / opencode / goose / Hermes / Maki）はバックエンド単位で切替可能だが、実際に動かして確認済みなのは Maki のみ。
- 質問・分析用のモデルとして Anthropic / OpenAI / OpenRouter / ローカルの OpenAI 互換サーバーを Settings → AI で設定できる。

## 実行条件

- OS: macOS / Windows / Linux / FreeBSD / Web。デスクトップ版は GTK 系依存のため Linux では上記パッケージが必要。
- 事前に `craft-anything-cli doctor` でインストール・コーディングエージェント・エンジンの状態を確認できる。
- ステータスは early alpha。README は「重要な作業に使う前に既知の制約を確認するように」としている。
- 「clean room」は提供する機能と拒否する操作に関するルールで、OS レベルのサンドボックスではない。PC を隔離するものではなく、エージェントは利用者と同じ権限で動く。どの操作を拒否できるかはエージェントごとに異なる。
- ビルド時に依存パッケージの導入コマンドが実行され、そのインストールスクリプトも動く。未知のコマンド種別は確認を挟むが、「常に許可」を選ぶと以後は無確認で走る。
- 対象ソフトの利用規約・著作権の扱いは README に規定がない（未確認）。調査対象の再実装が許される範囲は各自で判断する必要がある。

## 最短手順

```bash
git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything                    # デスクトップアプリ
cargo install --path apps/craft-anything-cli             # CLI を入れる場合
craft-anything-cli doctor                                # 環境チェック
craft-anything-cli rebuild https://example.com "Recreate this website"
craft-anything-cli mcp                                   # MCP クライアントにツールを提供
```

## 変更履歴

- 2026-11-03: 初回登録（star 6,863 / pushed 2026-11-03 / early alpha）
- 2026-11-04: Copilot CLI対応、clean roomがOSサンドボックスでない点を追記（078cf0c）
- 2026-11-06: プロジェクト単位の承認設定と `/approvals`、ネイティブ OpenCode へのツール供給を追記（v0.5.0 / 3122cd1）
