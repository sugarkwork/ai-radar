---
name: "TAP (Tree of Attacks with Pruning)"
genre: "prompt-design"
url: "https://github.com/RICommunity/TAP"
flags: ["unverified"]
risk_notes: "READMEは、制限情報を求めるgoalと応答のtarget prefixを指定して実行する例を示している。対象モデルへの利用許可やAPI利用料金はREADMEから確認できない。"
repo: "RICommunity/TAP"
stars: 253
forks: 42
open_issues: 5
size_kb: 420
language: "Python"
created: "2023-12-01"
updated: "2024-12-10"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/mingzi206/status/2118628554883883348"]
fetched_at: "2026-11-13T00:12:59.137522+00:00"
---

# TAP (Tree of Attacks with Pruning)

## 出来ること

- 攻撃側LLMがtree-of-thought reasoningで攻撃プロンプトを生成し、評価側LLMが不適切な候補を枝刈りして対象LLMの応答を評価する、ブラックボックス型の自動jailbreak手法。READMEは実験でGPT-4やGPT-4-Turboを含むモデルに対し、少数のクエリで80%超のプロンプトがjailbreakしたと報告している。これはREADME記載の作者報告であり、独立した検証結果ではない。

## 目的・背景

- READMEでは、既存の人手によるjailbreakに対して、Tree of Attacks with Pruning（TAP）でプロンプト探索を自動化し、候補の評価と枝刈りで対象LLMへのクエリ数を抑えることを目的としている。

## 依存関係

- 攻撃側・評価側・対象の3つのLLMを使用する。READMEに記載されたモデル別設定として、GPTモデルはOPENAI_API_KEY、PaLMモデルはPALM_API_KEYを設定する。ローカルのVicunaまたはLlamaを使う場合はconfig.pyにモデルパスを設定し、第三者APIを使う場合はAPIリンクを更新する。wandb loginによるwandbの設定も案内されている。

## 実行条件

- READMEの実行例ではPythonからmain_TAP.pyを起動し、攻撃モデル、対象モデル、評価モデル、goal、target string、保存先を指定する。探索のbranching-factor、width、depthも引数で変更できる。モデルへのAPIアクセスまたはローカルモデルの設定が必要。

## 最短手順

- README記載の手順に従い、使用するモデルのAPIキーを環境変数に設定するかconfig.pyでローカルモデル/APIを設定し、wandb loginを行う。その後、READMEの例では python main_TAP.py --attack-model [[ATTACKER]] --target-model [[TARGET]] --evaluator-model [[EVALUATOR]] --goal [[GOAL]] --target-str [[TARGET_STR]] --store-folder [[FOLDER]] で実行する。READMEはrestricted informationを求めるgoalの例を示している。

## 変更履歴

- 2026-11-13: 初回登録
