---
repo: deepseek-ai/dsh-superagent-prototype
name: dsh-superagent (prototype)
genre: agent-framework
url: https://github.com/deepseek-ai/dsh-superagent-prototype
author: DeepSeek
license: MIT
stars: 17309
language: TypeScript
created: 2026-10-31
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/Fluyeporlaweb/status/2117544561861972226
sources:
  - https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/000-philosophy.md
forks: 1874
open_issues: 0
commits_30d: 1
commits_90d: 1
commit_cadence: monthly
size_kb: 37
archived: false
fetched_at: "2026-11-04T04:47:11Z"
---

# dsh-superagent (prototype)

## 出来ること

- **1つの GitHub リポジトリ専属の能動型コーディングエージェント**。GitHub（任意で Feishu）を監視し、許可された相手から依頼が来ると「作業項目」を開き、専用のエージェントセッションと作業ディレクトリで進め、元の会話に返信する（例: プルリクエスト）。
- 人の対応が必要なものを一覧する Web パネルが付く。
- 設計思想は「人の注意をできるだけ取らず、価値をできるだけ出す」。チームの注意を食い尽くさないよう、**頼まれたとき、またはチームが書いたルールが許すときだけ動く**。発言も、人が動く必要があるとき・成果を使えるときに限る。
- [DeepSeek Harness](https://www.deepseek.com/en/harness/) 向けのバンドルとして配布される。ドキュメントは 000 哲学 / 001 ドメインモデル / 002 認可 / 003 実行 / 004 プロンプト / 005 パネル / 006 デプロイ / 007 アーキテクチャ / 008 クックブック（Source の追加）の順に読む構成。
- セットアップはエージェントと一緒に行う。`SETUP.md` を読ませると、診断（probe）→ 1問ずつ質問 → 全計画の提示 → 実行 → 検証、の順で進む。秘密情報はチャットで聞かず、本人のターミナルで実行するコマンドとして渡す。

## 目的・背景

DeepSeek のチームが日常開発から立ち上げた**研究用プロトタイプ**。リポジトリ冒頭に「公式製品ではなく参照用」「本番品質ではない」「公開にあたり改変しており、論文 *Exploring Super-agent Design: Towards a More Autonomous Agent System* の実装と同一ではない」「論文で論じた設計の一部は将来構想で本プロトタイプには未実装」と明記されている。2026-10-31 公開、11-03 時点で 1.7 万 star。

## 依存関係

- Node.js / pnpm
- git、tmux、python3
- GitHub CLI（`gh`）で認証済みのアカウント
- `dsh`（DeepSeek Harness）CLI
- 任意: Feishu 連携を使う場合のみ `lark-cli`

（要件は `SETUP.md` の probe が `node -v; pnpm -v; git --version; tmux -V; python3 --version; gh --version; dsh --version` で確認する。）

## 実行条件

- 対象は**1リポジトリ**。チームで使う場合は、どの操作を許可するかをルールとして先に書く前提。
- GitHub 側の権限（Issue/PR 作成、ブランチ push 等）と、エージェントを動かす常設環境が必要。Feishu 連携は任意。
- 研究用コードのため、バグ・実装のばらつきが残る。導入前に内容を確認し、自環境向けに調整することが README で求められている。
- 公開版は内部版・論文実装と同一ではない。

## 最短手順

```bash
git clone https://github.com/deepseek-ai/dsh-superagent-prototype
cd dsh-superagent-prototype
# コーディングエージェントに次を依頼する:
#   「Read SETUP.md in this repository and set up dsh-superagent with me.」
```

## 変更履歴

- 2026-11-04: 初回登録（公開直後のプロトタイプ）
