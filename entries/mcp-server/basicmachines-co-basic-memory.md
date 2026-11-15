---
name: "Basic Memory"
genre: "mcp-server"
url: "https://github.com/basicmachines-co/basic-memory"
repo: "basicmachines-co/basic-memory"
license: "AGPL-3.0"
stars: 4583
language: "Python"
created: "2024-12-02"
updated: "2026-11-15"
forks: 360
open_issues: 55
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 60537
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/stewy0x/status/2121929768996110590"]
fetched_at: "2026-11-15T14:19:09.788975+00:00"
---

# Basic Memory

## 出来ること

- READMEでは、知識をMarkdownファイルとして保存し、AIと人間が同じファイルを読み書きできると説明されています。観察記録とwikilinksによる知識グラフ、意味検索、任意のcross-encoder reranking、MCP経由のAIクライアント連携を提供します。

## 目的・背景

- AIクライアントやIDEをまたいで知識を保持し、以前の作業や記録を参照できるようにするツールです。READMEはローカル保存を基本とし、必要に応じてクラウド同期も選べると説明しています。

## 依存関係

- ローカル導入にはPythonを`uv`経由で利用します。READMEによると、Basic Memory 0.23はFastMCP 4のプレリリースに依存し、uvで導入する際に`--prerelease=allow`が必要です。

## 実行条件

- README記載のローカル導入条件はPython環境とuvです。クラウド利用は別経路で、READMEには月額料金と7日間の無料トライアルが記載されています。

## 最短手順

- ローカル導入はREADME記載のコマンドを使用します: `uv tool install basic-memory --prerelease=allow`。Postgresで意味ベクトルをMilvusに保存する場合は、README記載の任意extra `uv tool install "basic-memory[milvus]" --prerelease=allow` を使います。

## 変更履歴

- 2026-11-15: 初回登録
