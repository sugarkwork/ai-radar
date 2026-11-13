---
name: "Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)"
genre: "eval"
url: "https://github.com/patrickrchao/JailbreakingLLMs"
flags: ["malicious", "unverified"]
risk_notes: "READMEは、攻撃者LLMが対象LLMへ反復問い合わせして安全ガードレールを回避するプロンプトを生成すると説明し、例としてコンピューターへの侵入方法を要求する目標を掲載しています。安全性評価の研究用途として登録しますが、悪用可能な内容です。 APIキーとWandBアカウントが必要です。READMEに記載されたモデル選択肢や実行手順が現在も利用可能かは確認していません。"
repo: "patrickrchao/JailbreakingLLMs"
stars: 817
forks: 128
open_issues: 13
size_kb: 41
language: "Python"
created: "2023-10-13"
updated: "2025-07-02"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/mingzi206/status/2118628554883883348"]
fetched_at: "2026-11-13T00:12:43.073340+00:00"
---

# Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)

## 出来ること

- PAIR（Prompt Automatic Iterative Refinement）で、攻撃者LLMが対象LLMへのブラックボックス問い合わせを反復し、候補の脱獄プロンプトを生成・改良します。READMEは、GPT-3.5/4、Vicuna、GeminiPro-2などでの実験結果として、少ない問い合わせ回数での成功や転移性を報告しています。これはREADMEにある作者の報告で、独立した実測ではありません。

## 目的・背景

- LLMの安全ガードレールに対する敵対的な脱獄の脆弱性を特定し、将来の悪用防止に役立てる研究です。READMEは、実験にAdvBenchの有害行動50件のカスタムサブセットを使ったと説明しています。

## 依存関係

- READMEによると、実行環境のセットアップにDockerfileが用意されています。利用するモデルに応じたOPENAI_API_KEY、ANTHROPIC_API_KEY、GOOGLE_API_KEYが必要で、実験ログの記録には事前のWandBログインが必要です。VicunaまたはLlamaをローカル実行する場合はconfig.pyにモデルのパスを設定します。

## 実行条件

- READMEに示された攻撃・対象モデルの選択肢はvicuna、llama-2、gpt-3.5-turbo、gpt-4、claude-instant-1、claude-2、gemini-proです。判定モデルはgpt-3.5-turbo、gpt-4、no-judgeです。no-judgeは判定を省略し、常に10点中1点を出力すると説明されています。標準設定はn-streams 5、n-iterations 5です。

## 最短手順

- READMEの手順は、必要なAPIキーを環境変数に設定し、WandBへログインしたうえで、`python3 main.py --attack-model [ATTACK MODEL] --target-model [TARGET MODEL] --judge-model [JUDGE MODEL] --goal [GOAL STRING] --target-str [TARGET STRING]`を実行することです。全引数の説明はmain.pyを参照するよう記載されています。

## 変更履歴

- 2026-11-13: 初回登録
