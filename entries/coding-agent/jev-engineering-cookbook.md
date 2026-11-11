---
name: "Jev Cookbook"
genre: "coding-agent"
url: "https://github.com/Jev-Engineering/cookbook"
repo: "Jev-Engineering/cookbook"
license: "MIT"
stars: 30
language: "Jupyter Notebook"
created: "2026-10-06"
updated: "2026-11-10"
forks: 5
open_issues: 129
commits_30d: 73
commit_cadence: "daily"
commits_90d: 100
size_kb: 38359
archived: false
flags: ["unverified"]
risk_notes: "The README does not identify the license or provide the runtime requirements of each recipe. Box requires the Jev 1.14 preview and experimental images header. Quality, latency, and cost are not established by synthetic runs; live-result claims require held-out recorded inference with model version, date, and sample count."
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2120147118237114757"]
fetched_at: "2026-11-11T06:11:22.093945+00:00"
---

# Jev Cookbook

## 出来ること

- Jev の System One に状態と型付き質問を渡し、Choice（選択）、Noul（命題判定）、Score（ルーブリック評価）、Box（画像内の対象位置）などの構造化回答を得るノートブック教材。README では50/100レシピが公開済みと説明されています。

## 目的・背景

- 個別の限定的な判断を組み合わせる方法を学ぶためのカリキュラムです。README の説明では、Jev が意味判断を行い、算術・検索・ポリシー・権限・実行は Python が担います。

## 依存関係

- README のクイックスタートは Python 3.10 以降、git、`pip install -e ".[dev]"` を記載しています。API キーなしでオフライン実行でき、ライブの Jev 呼び出しは任意で自身のキーを使います。Box は Jev 1.14 preview と experimental images header が必要です。

## 実行条件

- 基本的な Python 知識が前提です。README によると、教材データはレシピ用の準備済みテキストまたは JSON fixture で、アクションはシミュレーションされます。オフラインでは fixture を再生し、ライブ呼び出しは明示的に有効化します。

## 最短手順

- README の手順は、リポジトリを clone し、`cookbook` ディレクトリで仮想環境を作成・有効化し、`pip install -e ".[dev]"` を実行してから、`python tools/execute_notebook.py recipes/_template` でテンプレートをオフライン実行します。

## 変更履歴

- 2026-11-11: 初回登録
