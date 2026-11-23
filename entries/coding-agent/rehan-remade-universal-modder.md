---
name: "universal-modder"
genre: "coding-agent"
url: "https://github.com/rehan-remade/universal-modder"
repo: "rehan-remade/universal-modder"
license: "MIT"
stars: 9830
language: "Python"
created: "2026-09-30"
updated: "2026-11-22"
forks: 1109
open_issues: 25
commits_30d: 91
commit_cadence: "daily"
commits_90d: 100
size_kb: 41839
archived: false
flags: ["unverified"]
risk_notes: "falによるアセット生成にはAPIキーが必要で、SprixenとVoidlessは別料金のサービスとして記載されています。ゲーム上での検証などの効果はREADMEの説明に基づき、独立実測ではありません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119407086572364163"]
fetched_at: "2026-11-22T04:21:34.828119+00:00"
---

# universal-modder

## 出来ること

- READMEでは、AIコーディングエージェントがPCゲームのエンジンや改造経路を調べ、コードを読み、改造を作成し、ゲーム内で検証するためのスキル、ツール、共有知識ベースを提供すると説明しています。アセット生成にはfal連携のほか、ローカルComfyUIや別サービスの利用方法も記載されています。

## 目的・背景

- ゲームごとの改造・解析・検証の記録を知識ベースに蓄積し、後続のエージェントが既存の手順や注意点を参照できるようにする構成です。READMEによると、ノートには動作したバージョン、採用した経路、検証内容、問題と対処を記録します。

## 依存関係

- README記載の基本要件はGit、Python 3.10以降、ffmpegで、uvを推奨しています。3Dからスプライトをレンダリングする場合はBlenderが必要です。falのアセット機能にはfal APIキーが必要で、SprixenとVoidlessの機能にはそれぞれ別のAPIキーが必要です。

## 実行条件

- Claude Code、Codex、Gemini CLI、VS Code/Copilot、Cursor、OpenCodeなどの導入手順が記載されています。WindowsゲームはネイティブまたはWSLから操作するとREADMEにあります。fal連携を使わない場合のComfyUI利用方法も案内されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEのCodex向け手順は `codex plugin marketplace add rehan-remade/universal-modder` の後に `codex plugin add universal-modder@universal-modder` を実行します。クローンを使う場合はリポジトリ内でエージェントを起動し、必要に応じて `um` CLIを導入します。

## 変更履歴

- 2026-11-23: 初回登録
