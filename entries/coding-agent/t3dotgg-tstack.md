---
repo: "t3dotgg/tstack"
name: "tstack"
genre: "coding-agent"
url: "https://github.com/t3dotgg/tstack"
stars: 3411
forks: 258
open_issues: 15
size_kb: 25
language: "Python"
created: "2026-10-24"
updated: "2026-10-28"
archived: false
license: "MIT"
commits_30d: 5
commits_90d: 5
commit_cadence: "weekly"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "各スキルの実行結果、Claude CodeとCodex間の挙動差、レビュー品質や作業時間への効果は未検証。GitHubの公開Releases一覧には掲載なし。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2117504564941508613"]
fetched_at: "2026-11-10T09:17:55+00:00"
---

# tstack — Claude CodeとCodex向けのPR作業スキル集

## 出来ること

- PRの説明作成、CIやレビュー指摘への対応、複数モデルによるレビューなどの手順を、用途別のスキルとしてエージェントから呼び出せる。READMEに記載された機能で、実行結果は未検証。 [README](https://raw.githubusercontent.com/t3dotgg/tstack/main/README.md)

## 目的・背景

- 作者が日常的に使う手順を、他の利用者が編集して使える形で公開したもの。モデル構成などの個人設定はCLAUDE.mdやAGENTS.mdに分ける構成を案内している。 [README](https://raw.githubusercontent.com/t3dotgg/tstack/main/README.md)

## 依存関係

- READMEは認証済みのGitHub CLIを要件に挙げている。babysit-prの待機スクリプトにはPython 3、councilとsol-loopには別プロバイダーのモデルを呼べる実行環境が必要。一部のスキルは別のスキルを呼び出す。 [README](https://raw.githubusercontent.com/t3dotgg/tstack/main/README.md)

## 実行条件

- Claude CodeまたはCodexで使う。一部はT3 Codeの機能が利用できる場合にそれを使い、利用できない場合はホスト側の標準ツールに切り替わるとREADMEに記載されている。配布ライセンスはMIT。 [README](https://raw.githubusercontent.com/t3dotgg/tstack/main/README.md)

## 最短手順

- リポジトリのskillsディレクトリから、使うスキルと依存スキルをClaude Codeなら ~/.claude/skills/、Codexなら ~/.codex/skills/ に配置する。 [README](https://raw.githubusercontent.com/t3dotgg/tstack/main/README.md)
- 対象リポジトリを開いたエージェントの会話で、READMEの呼び出し語を入力する。PR作成を依頼する場合は `file a PR` で `file-pr` を呼び出す。 [README](https://raw.githubusercontent.com/t3dotgg/tstack/main/README.md)

## 変更履歴

- 2026-11-10: 初回登録
