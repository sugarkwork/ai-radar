---
repo: "karpathy/nn-zero-to-hero"
name: "Neural Networks: Zero to Hero"
genre: "other"
url: "https://github.com/karpathy/nn-zero-to-hero"
stars: 25433
forks: 3697
open_issues: 54
size_kb: 50
language: "Jupyter Notebook"
created: "2022-09-08"
updated: "2024-08-18"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日は未確認。ノートブックは実行しておらず、依存ライブラリの対応バージョン、必要な計算資源、学習成果は独立検証していない。外部サービスの利用条件や料金は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115051970251628961"]
fetched_at: "2026-11-10T11:50:44+00:00"
---

# Neural Networks: Zero to Hero — 誤差逆伝播からGPTまでの実装講座

## 出来ること

- microgradで誤差逆伝播を追い、makemoreで文字単位のbigramモデルと多層パーセプトロンを実装する。後続の講義はGPTとBPEトークナイザーを扱う。GPT回の補助資料は動画説明欄からたどる。

## 目的・背景

- 講義でコードを書きながらニューラルネットワークを組み立てる教材。手計算で逆伝播を追う演習を通じ、計算グラフ上で勾配がどう伝わるかを学ぶ構成。

## 依存関係

- 教材はJupyterノートブック形式。makemore回ではPyTorchのテンソルを扱う。リポジトリのライセンスはMIT。

## 実行条件

- 初回講義はPythonの基礎と高校レベルの微分の知識を前提とする。一部の演習にはGoogle Colabへのリンクがある。

## 最短手順

- READMEのLecture 1から講義動画とlectures/microgradのノートブックを開き、講義に沿って勾配計算を追う。次にLecture 2のmakemoreノートブックで文字単位のbigramモデルに進む。

## 変更履歴

- 2026-11-10: 初回登録
