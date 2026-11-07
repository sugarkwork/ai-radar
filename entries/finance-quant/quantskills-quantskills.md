---
repo: "quantskills/quantskills"
name: "QuantSkills"
genre: finance-quant
url: "https://github.com/quantskills/quantskills"
license: "unknown"
stars: 2538
language: "JavaScript"
created: "2026-06-25"
updated: 2026-11-04
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 229
open_issues: 1
commits_30d: 61
commits_90d: 100
commit_cadence: daily
size_kb: 68094
archived: false
fetched_at: "2026-11-04T22:53:49Z"
---

# QuantSkills

## 出来ること

- AI エージェント向けの定量リサーチ用スキル／エージェントのコミュニティ目録。スナップショット時点で **218アセット / 10カテゴリ**。
- カテゴリは、01 データ接口（7）、02 因子研究（44）、03 市場・銘柄分析（45）、04 リスク監視（22）、05 バックテストと執行（26）、06 研究再現（30）、07 検証・品質（13）、08 ニュース検索（10）、09 定量エージェント（15）、10 基盤・テンプレート（6）。
- 各アセットは「主段階・入力・出力・接口状態」のメタデータ付きで一覧化され、`data-ingestion → feature-engineering → … → execution` のワークフローマップに沿って組み合わせられる。
- 参加用に `skill-template` / `agent-template` / `registry` の3リポジトリが用意され、データ・仮定・パラメータ・制約・リスク境界を書いて提出するルールになっている。
- GitHub Pages のインタラクティブ目録と本体サイト（quantskills.ai）がある。

## 目的・背景

定量の知見を「記述でき、再現でき、議論できる」形にすることを掲げる。PandaAI 発のコミュニティプロジェクトだが、PandaAI の公式認定でも投資助言でもないと明記されている。目録は公開メタデータの定期スナップショットで、品質・収益・本番可用性の保証はしない。

## 依存関係

- 目録自体はブラウズするだけなら依存なし。個々の Skill / Agent はそれぞれのリポジトリの手順に従う。

## 実行条件

- **免責の扱い**: README が「品質の裏付け・収益の約束・本番利用の保証ではない」と明言している。個別アセットのデータソースとリスク境界は自分で確認する必要がある。
- リポジトリにライセンスファイルがなく、GitHub API 上もライセンス未設定。個別アセットはそれぞれ別ライセンス。
- A株・中国市場向けのアセットが中心で、日本株・米株向けは 03 カテゴリの一部に限られる。

## 最短手順

```text
https://github.com/orgs/quantskills/repositories  から目的のアセットを選ぶ
https://quantskills.github.io/quantskills/        で分類ごとに眺める
```

## 変更履歴

- 2026-11-03: 初回登録（star 2,521 / pushed 2026-11-03 / ライセンス未設定）
