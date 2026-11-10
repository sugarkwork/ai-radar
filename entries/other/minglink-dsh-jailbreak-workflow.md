---
repo: Minglink/dsh-jailbreak-workflow
name: DSH 破甲ワークフロー（dsh-jailbreak-workflow）
genre: other
url: https://github.com/Minglink/dsh-jailbreak-workflow
license: 未確認（API は NOASSERTION、標準ライセンスファイル無し）
language: TypeScript
created: 2026-11-01
updated: "2026-11-05"
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/NFT_Chen/status/2117486881399284175
flags: [prompt-injection]
risk_notes: "モデルの拒否応答を回避する『破甲（jailbreak）』プロンプトを自動生成するためのワークフロー。各サービスの利用規約違反になり得る。記録のみで、実行・生成した内容の利用はしない。"
stars: 816
forks: 284
open_issues: 4
commits_30d: 18
commits_90d: 18
commit_cadence: "weekly"
size_kb: 40252
archived: false
fetched_at: "2026-11-09T21:41:12Z"
last_release: ""
last_release_at: ""
---

# DSH 破甲ワークフロー（dsh-jailbreak-workflow）

## 出来ること

- DeepSeek Harness（DSH）上で動く**ワークフロープラグイン**。画布でフローを設計し、計画プロンプトにコンパイルしてモデル自身に実行させる（分岐・ループ・並列に対応）。
- 同梱の「破甲制作」パイプラインは15ステップ。200以上の探針で対象モデルの拒否パターンを分類し、拒否されにくい言い回しを生成、API で検証する、という流れを自動化する。
- 生成物は複数のテンプレート（いわゆる破甲詞）として出力される。

## 目的・背景

2026-11-01 作成。モデルの安全機構（拒否応答）を回避するプロンプトの作成を、職人芸ではなく再現可能なパイプラインにすることを狙ったもの。中国語圏の AI コミュニティで拡散し、★309。投稿では「DSH の破甲核兵器」として紹介されている。

## 依存関係

- DeepSeek Harness（DSH）本体と、そのワークフロープラグイン機構
- Node.js / TypeScript（プラグイン実行）
- 検証ステップで対象モデルの API キー

## 実行条件

- DSH が動作する環境。
- API 検証を行う場合、対象プロバイダのアカウントと課金。
- **利用条件の確認が前提**。多くのモデルプロバイダは安全機構の回避を規約で禁止している。生成物の配布・商用利用は特に注意。

## 最短手順

```text
（記録のみ。導入手順はリポジトリの README を参照）
```

## 変更履歴

- 2026-11-04: 初回登録（★309 / pushed 2026-11-03 / TypeScript / ライセンス表記なし）。`prompt-injection` フラグ付きで記録のみ
