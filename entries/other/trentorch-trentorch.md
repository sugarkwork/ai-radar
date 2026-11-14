---
name: "TrenTorch"
genre: "other"
url: "https://github.com/TrenTorch/TrenTorch"
repo: "TrenTorch/TrenTorch"
license: "unknown"
stars: 842
language: "Python"
created: "2026-08-21"
updated: "2026-11-14"
forks: 88
open_issues: 19
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 226035
archived: false
flags: ["unverified"]
risk_notes: "READMEではPolyForm Noncommercial 1.0.0と記載されています。商用利用の可否やその他の利用条件はライセンス本文を確認してください。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118873065706934431"]
fetched_at: "2026-11-14T17:05:32.238723+00:00"
---

# TrenTorch

## 出来ること

- NumPyを基礎に機械学習フレームワークの仕組みを学ぶCLIカリキュラムと、ブラウザーで取り組めるコーディング問題を提供します。READMEにはWeb版の問題数を1,647、CLI版を20モジュールと記載。問題には課題文、理論、スターターファイル、テスト、参照解答が含まれます。

## 目的・背景

- 作者は、既存の機械学習フレームワークを使うだけでなく、その仕組みを理解するために一から構築する教材を作ったと説明しています。CLIカリキュラムはTinyTorch（Harvard CS249r）の実装を独自の形式で再構築・拡張したものとREADMEに記載されています。

## 依存関係

- CLIの導入手順はPython仮想環境、requirements.txt、編集可能インストールを使います。Webアプリのローカル実行手順はNode.jsのnpmを使い、ローカルでサインインを利用する場合はSupabaseプロジェクトのキーが必要とREADMEに記載されています。個別の依存パッケージやバージョンはREADME抜粋から確認できません。

## 実行条件

- READMEはPython 3.10以降を掲示しています。Web版はブラウザー内のPyodideでPythonを実行し、利用開始時はGitHub、Google、またはメールでのサインインが必要と説明しています。CLIはターミナルで実行します。

## 最短手順

- CLI: `git clone https://github.com/TrenTorch/TrenTorch.git`、`cd TrenTorch/TrenTorch_CLI`、Python仮想環境を作成・有効化し、`pip install -r requirements.txt`、`pip install -e .`、`tren setup`、`tren module start 01` の順に実行します。Windows PowerShell向け手順もREADMEにあります。Web版はREADME記載のtrentorch.comを開いてサインインします。

## 変更履歴

- 2026-11-14: 初回登録
