---
name: "PaperOrchestra"
genre: "agent-framework"
url: "https://github.com/google-research/paper-orchestra"
repo: "google-research/paper-orchestra"
license: "Apache-2.0"
stars: 2982
language: "Python"
created: "2026-05-01"
updated: "2026-11-15"
forks: 413
open_issues: 37
commits_30d: 6
commit_cadence: "weekly"
commits_90d: 6
size_kb: 2059
archived: false
flags: ["unverified"]
risk_notes: "データセットはこのリポジトリに含まれず、READMEでは別途公開予定とされています。利用するモデルに応じたAPIキー等が必要ですが、利用料金や生成物の品質はREADMEから確認できません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2122627051517833466"]
fetched_at: "2026-11-18T00:40:18.126480+00:00"
---

# PaperOrchestra

## 出来ること

- READMEによると、Outline、Literature Review、Section Writing、Content Refinement、Plottingの各エージェントを連携させ、文献の検索・統合、原稿の執筆・推敲、プロットや概念図の生成を行います。対象会議のテンプレートに沿ったLaTeX原稿を生成すると説明されています。生成品質は独立に確認していません。

## 目的・背景

- アイデアや実験ログなどのプレライティング資料から、研究論文の原稿作成までを支援することを目的とするマルチエージェントフレームワークです。

## 依存関係

- READMEはPython 3.11のConda環境とrequirements.txtからの依存関係インストールを案内しています。Semantic Scholar、OpenAI、Vertex AIまたはGeminiのAPI設定例があり、使用するモデルに応じたキーやプロジェクト設定が必要です。

## 実行条件

- 入力資料のディレクトリとLaTeXテンプレートのディレクトリを指定してCLIを実行します。出力先は指定可能で、plottingは既定で無効です。データセットはリポジトリに含まれておらず、READMEでは別途公開予定とされています。

## 最短手順

- README記載の手順は、Python 3.11のConda環境を作成・有効化し、`pip install -r requirements.txt`を実行して、必要に応じてモデル用API設定を`.env`に記入することです。その後、`paper_writing_cli.py`に`--raw_materials_dir`、`--latex_template_dir`、`--output_dir`を指定して実行します。READMEには`./paper_writing_cli.sh`を使う方法もあります。

## 変更履歴

- 2026-11-22: 初回登録
