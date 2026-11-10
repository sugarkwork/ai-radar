---
type: "repo"
name: "Graphicle（コードグラフと記憶を1つのMCPサーバでエージェントに渡すRust製ツール）"
genre: "mcp-server"
url: "https://github.com/Graphicle-AI/graphicle"
repo: "Graphicle-AI/graphicle"
license: "Apache-2.0"
stars: 543
language: "Rust"
created: "2026-10-14"
updated: "2026-11-09"
added: "2026-11-06"
first_seen: "2026-11-05"
sources: ["https://x.com/Ryrenz/status/2118146955763130525", "https://www.karlex.ai/graphicle"]
flags: []
risk_notes: "速度・メモリ・記憶精度の数値はすべてベンダーの自己計測（docs/benchmarks.md に手法と条件が書かれている）。速度比較の相手 Graphify 0.9.100 は、更新差分が無いケースでは Graphicle より速かったと README 自身が5件の反例を挙げている。コードグラフのエンジンは Graphify の Rust 移植で、Graphify Labs とは無関係と明記されている。インストールは Homebrew か `curl -fsSL .../install.sh | sh` 形式なので中身を確認してから実行したい。`graphicle setup` は AGENTS.md の書き換えと Git フック（post-commit / post-merge / post-checkout）の設置を行うが、変更前にバックアップを取り `graphicle disconnect` で戻せる。既定で1日1回の新バージョン確認リクエストだけは自動送信される（GRAPHICLE_NO_UPDATE_NOTIFIER=1 で停止）。Windows は x86-64 のプレビュー版で未コード署名。投稿が挙げる SWE-bench Verified の『上位5ファイルで75/100命中、BM25は61』は README の記載と一致するが独立検証はしていない。"
forks: 41
open_issues: 0
commits_30d: 100
commit_cadence: "daily"
size_kb: 32410
archived: false
fetched_at: "2026-11-09T21:38:55Z"
last_release: "v0.1.14"
last_release_at: "2026-11-09"
commits_90d: 100
---

# Graphicle — リポジトリのコードグラフとプロジェクト記憶を、1つのMCPサーバから引用付きでエージェントに渡す

## 出来ること

- リポジトリを**コードグラフ**に変換し、あわせてドキュメント・設計判断・過去のエージェントセッションを**記憶**として保持する。エージェントはその両方から、ファイル名と行番号付きの抜粋だけを受け取る
- MCPサーバとして動く：`graphicle setup` が Claude Code / Codex / Cursor / VS Code / Claude Desktop を見つけて、それぞれにコードグラフ・recall・memory を出すMCPサーバを登録する。Claude Code には5つのツールを渡す
- ターミナルから直接問い合わせる：`graphicle ask "where is tax added to prices?"` → 4抜粋・606/3000トークン、のように**指定したトークン予算内**で根拠を返す。モデルを設定しなければ抜粋だけを返し、`graphicle config set model anthropic|openai|ollama` で文章の回答も付く
- 影響範囲の確認：`graphicle graph affected "retry()"` で、あるシンボルを変えると何が壊れうるかを出す
- `graphicle open` でグラフ・出典・記憶をブラウザで閲覧。`graphicle doctor` で動作確認、`graphicle disconnect` で setup が触ったファイルを全て元に戻す
- セッション記録：Claude Code と Codex のセッションを捕捉し、Git フック（post-commit / post-merge / post-checkout）でコードグラフを追従させる
- **ハッカソン由来の追加機能**：Meta Model API のキーがあると `graphicle see`（computer use でブラウザ上のバグを再現）、`graphicle pixel`（モデルが指した箇所を描いているコードを特定）、`graphicle fix`（修正してテストを回し、失敗した行を次のラウンドに読ませる）が使える
- チーム向けに共有サーバとしても動かせる（`docs/team.md`）。データは SQLite 1ファイル

## 目的・背景

- 大規模リポジトリでコーディングエージェントが最初にやるのは grep で、無関係なファイルを開いてコンテキストを埋めたまま本命に辿り着かない。Graphicle は「コードの地図」を先に作って渡すことでそこを短絡させる
- 作者の計測では、Kubernetes v1.37.1 の初回コードグラフ構築が 1分14秒（比較対象 Graphify 0.9.100 は29分18秒）、コミット後の更新中央値が prometheus で 4.9秒（同 32.1秒）。13リポジトリ39測定のうち34で Graphicle が速く、残り5は「変更が無い更新」で Graphify が先に打ち切るケース
- 記憶の評価は LoCoMo-10 で 87.7（Hindsight 0.10.2 が 87.3、Mem0 OSS 2.2.1 が 81.9）。会話1件あたりの取り込みモデル呼び出しは約12回で、Hindsight の約160回・Mem0 の約332回より大幅に少ない
- 提供は KarLex AI（Meta の Global AI Developer Hackathon で原型が作られた）。コードグラフ部分は Graphify の Rust 移植で、その旨がクレジットされている

## 依存関係

- 単体のRustバイナリ。Python・Docker・DBサーバは不要。データは SQLite 1ファイル
- インストール：Homebrew（`brew install graphicle-ai/tap/graphicle`）、またはリリースの install.sh、各種アーカイブ
- 必須なのは OS だけ。**APIキーもアカウントも不要**（テレメトリ無し、既定の外部通信は新バージョン確認のみ）
- 文章回答や `see` / `fix` を使う場合だけ、Anthropic / OpenAI / Ollama、または Meta Model API のキーが要る

## 実行条件

- 対応：macOS / Linux / Windows（x86-64 プレビュー、未コード署名）
- `graphicle setup` は**リポジトリのファイルを書き換える**：AGENTS.md に2行追記（Claude Code のみの環境では追記しない）、Git フック3種の設置、各エージェントの設定変更。変更したファイルは一覧表示され、事前にバックアップが取られる
- 速度の優位は「初回構築」と「差分更新」で大きく、「変更が無いときの更新」では差が付かない（README 自身が認めている）
- トークン削減は**主張していない**（grep と同等だった、と明記）。売りは精度と出典の追跡可能性
- 記憶の数値は開発セット・単一のオープンモデル（Qwen3.8-27B）を読み手兼判定者にした比較で、本番ワークロードでの再現は別途必要

## 最短手順

```bash
# 1) インストール
brew install graphicle-ai/tap/graphicle
# Homebrew が無い場合（中身を確認してから実行する）
#   curl -fsSL https://github.com/graphicle-ai/graphicle/releases/latest/download/install.sh | sh

# 2) リポジトリで初期化（索引構築 + コードグラフ + エージェント接続 + Gitフック）
cd your-repo
graphicle setup            # 変更内容を確認しながら進める
graphicle setup --yes      # 確認を省く場合

# 3) 動作確認と問い合わせ
graphicle doctor
graphicle ask "how are failed requests retried?"
graphicle graph affected "retry()"
graphicle open             # グラフ・出典・記憶をブラウザで見る

# 4) 文章回答を付けたい場合
graphicle config set model anthropic     # または openai / ollama

# 5) 全部元に戻す
graphicle disconnect
```

## 変更履歴

- 2026-11-06: 初回登録
