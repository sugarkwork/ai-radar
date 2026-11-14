---
name: "Casting-Workflow"
genre: "prompt-design"
url: "https://github.com/dama-cyber/Casting-Workflow"
repo: "dama-cyber/Casting-Workflow"
license: "unknown"
stars: 710
language: "Python"
created: "2026-06-23"
updated: "2026-08-07"
forks: 136
open_issues: 1
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 710
archived: false
flags: ["unverified"]
risk_notes: "内容の独創性や朱雀検出への効果はREADME内の作者の説明であり、独立検証は確認できません。READMEはMITと記載していますが、測定データ上のライセンス情報はunknownです。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/superfang119/status/2118760449340760396"]
fetched_at: "2026-11-14T02:10:46.086273+00:00"
---

# Casting-Workflow

## 出来ること

- 小説テキストを分類別の語料として読み込み、複数作品から人物・情節・句式・高頻度語の指紋を抽出して統合し、LLMに渡す創作コンテキストまたは段階別のプロンプトを生成します。README記載の12段階には、着想、人設、大綱、開篇、本文、続写・拡写などがあります。後処理スクリプトと品質監査ツールも含みます。

## 目的・背景

- 小説の創作工程を、語料の準備、指紋の蒸留、LLMでの生成、後処理、監査に分けて支援することを目的としています。READMEは指紋の交差処理によりタイプの共通要素を残すと説明しています。独創性や検出回避の効果は作者の説明で、独立検証は示されていません。

## 依存関係

- READMEによると、外部依存はjiebaのみで、それ以外は標準ライブラリです。requirements.txtの具体的な内容はこの資料では確認できません。

## 実行条件

- Python環境と入力となる分類別の小説 .txt ファイルが必要です。各分類で5篇以上を推奨し、不足時は利用可能な健全ファイルを使用するとREADMEにあります。初回のfusion/clean実行時には分詞モデルを読み込みます。

## 最短手順

- 1. requirements.txtを使って依存関係をインストールします。2. 分類に対応するcorpus配下のフォルダに小説 .txt を置きます。3. `python run_pipeline.py --category 05_古代言情` を実行し、`output/fusion_context.txt`を生成します。4. 生成コンテキストをLLMに渡して物語を作成します。READMEは、段階別利用には`--stage`、前段階の出力の引き継ぎには`--previous-output`を案内しています。

## 変更履歴

- 2026-11-14: 初回登録
