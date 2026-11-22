---
name: "Ruff"
genre: "other"
url: "https://github.com/astral-sh/ruff"
repo: "astral-sh/ruff"
license: "MIT"
stars: 51255
language: "Rust"
created: "2022-08-09"
updated: "2026-11-16"
forks: 2724
open_issues: 2300
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 238924
archived: false
flags: ["unverified"]
risk_notes: "READMEには依存関係の明示がありません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119116419153469697"]
fetched_at: "2026-11-17T00:12:23.640229+00:00"
---

# Ruff

## 出来ること

- Pythonコードのlintとフォーマットを行います。READMEでは、900以上の組み込みルール、自動修正、キャッシュ、Flake8・isort・Blackとの機能互換を説明しています。READMEは既存ツールより10〜100倍速いと主張していますが、これは独立した実測として確認した値ではありません。

## 目的・背景

- READMEでは、複数のPython品質管理ツールの機能を単一の共通インターフェースにまとめ、代替ツールより大幅に高速にすることを目指すと説明しています。

## 依存関係

- READMEには実行時依存関係の明示がありません。導入方法としてuv、pip、pipx、Homebrew、Condaなどを挙げています。

## 実行条件

- READMEではPython 3.15互換を掲げています。uvx、uv、pip、pipxなどによる導入方法と、ruff checkおよびruff formatの実行例が記載されています。

## 最短手順

- READMEの例では、uvx ruff@0.17.5 checkでカレントディレクトリをlintし、uvx ruff@0.17.5 formatでフォーマットします。

## 変更履歴

- 2026-11-22: 初回登録
