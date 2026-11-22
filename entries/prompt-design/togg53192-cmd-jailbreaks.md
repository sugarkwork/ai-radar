---
name: "Jailbreaks"
genre: "prompt-design"
url: "https://github.com/togg53192-cmd/jailbreaks"
repo: "togg53192-cmd/jailbreaks"
license: "unknown"
stars: 18071
language: "unknown"
created: "2026-06-18"
updated: "2026-11-16"
forks: 3173
open_issues: 52
commits_30d: 90
commit_cadence: "daily"
commits_90d: 100
size_kb: 212
archived: false
flags: ["unverified"]
risk_notes: "READMEはプロンプトの挙動がモデルやバージョンに依存し、更新で効果が変わり得ると説明している。各プロンプトの有効性は独立に確認されていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/DeepTechTR/status/2122578824512606356"]
fetched_at: "2026-11-18T00:33:21.845163+00:00"
---

# Jailbreaks

## 出来ること

- READMEによると、複数モデル向けのシステムプロンプト、ペルソナ定義、ワークスペースポリシー、AGENTS.md、設定ブロック、Ollama Modelfileを収録。システムプロンプト欄や対応するクライアント/API設定に貼り付けたり、AGENTS.mdを対象ワークスペースのルートに置いたりして利用する。READMEはプロンプトの挙動がモデルやバージョンに依存すると説明している。

## 目的・背景

- READMEは、指示の優先順位、ペルソナ設定、プロンプト衝突、ポリシー上書きがモデルの挙動に与える影響を記録する研究・教育目的のコレクションと説明している。安全なモデル設計やプロンプトインジェクション耐性の研究にも役立つと作者は述べている。

## 依存関係

- READMEに明示された必須依存関係は確認できない。利用には対象クライアントやハーネスが指定形式のシステム指示・設定を受け付ける必要がある。

## 実行条件

- 各プロンプトの対象モデルと、対応するクライアント/APIまたはハーネスが必要。READMEによると、設定ファイルの配置先はクライアントやハーネスによって異なり、プロンプトの挙動はモデルの更新やバージョンに依存する。

## 最短手順

- READMEの手順では、利用するモデルに対応するファイルを選び、システムプロンプトならクライアント/APIのシステム指示欄へ貼り付ける。AGENTS.md形式ならファイル名をAGENTS.mdとして対象リポジトリまたはワークスペースのルートに配置する。Ollama Modelfileは、例として `ollama create gemma4-jb -f gemma4.md` を実行する。

## 変更履歴

- 2026-11-22: 初回登録
