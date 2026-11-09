---
repo: "JuliusBrussee/caveman"
name: "Caveman"
genre: "coding-agent"
url: "https://github.com/JuliusBrussee/caveman"
author: "Julius Brussee"
license: "Apache-2.0"
stars: 118293
language: "Go"
created: "2026-04-04"
updated: "2026-11-08"
forks: 6883
open_issues: 70
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 21749
archived: false
last_release: "v4.1.0"
last_release_at: "2026-11-08"
flags: ["unverified"]
risk_notes: "効果数値（入力トークン33.2%減、54%安価、18/18正解、圧縮率など）はリポジトリ自身のベンチマークで自己申告であり、本検証では再実行していない。READMEが引用するAdobe ResearchのarXiv論文とJetBrainsのブログは原典を取得しておらず、第三者検証としては未確認。CLIのインストール・実行も未実施。APIのlicenseはApache-2.0だが、リポジトリにはLICENSE-MITも同梱されており、ファイル単位のライセンス区分は未確認。「Caveman」とロゴは商標。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2112884125120319643"]
fetched_at: "2026-11-08T15:14:30Z"
---

# Caveman — コーディングエージェントのトークンを削るskill集＋CLI

## 出来ること

- コーディングエージェントの回答を簡潔な「caveman口調」に切り替えるskill（/caveman・/ultracave・/megacave）。コード・コマンド・パス・エラー文は一字も変えず、説明の冗長さだけを削る。
- 差分から Conventional Commits 形式の短いコミットメッセージを書く /caveman-commit。型（feat/fix/refactor等）と「なぜ」を残し、git commit 自体は実行しない。
- 同じリポジトリに /caveman-review（1行1指摘のレビュー）、/caveman-compress（CLAUDE.md等の圧縮）、/caveman-stats など計28個の SKILL.md を収録。
- CLI側では、エージェントが読むログ・CSV・JSON・テスト出力の圧縮（Read less）、モデルとeffortの自動選択（Auto）、使い回すスクリプトの保存（Blocks）、Webページの圧縮取得（caveman browse）を提供。

## 目的・背景

- 「why many token when few do trick」を掲げ、エージェントの入出力トークン（＝コストと待ち時間）を減らすことを目的にする。2026年4月にジョークとして始まり、現在11.8万スター超。
- 設計方針として、ユーザーのプロンプトは書き換えない（プロンプトをcaveman化すると回答品質が落ちるという研究を根拠にしている）、コードや数値は改変しない、セキュリティ警告や不可逆操作では簡潔化を止める、とREADMEに明記。
- caveman-commit は「何をしたか」より「なぜ」を残す方針で、絵文字・AI帰属表記・冗長な説明を禁止し、破壊的変更やセキュリティ修正では必ず本文を書かせる。

## 依存関係

- skill単体（caveman-commit など）は Markdown のみで、Node.js も追加パッケージも不要。
- CLI・インストーラは Node.js 22.13+（npx）が必要。Bunでの代替も可能。
- Auto（モデル自動選択）だけは無料アカウント（caveman login）が必要。任意で自前のOpenAI等のAPIキーを追加できる。
- ライセンスはリポジトリ全体 Apache-2.0。ただし LICENSE-MIT も同梱されており、ファイル単位の区分は未確認。「Caveman」とロゴは商標。

## 実行条件

- SKILL.md 形式のskillを読めるエージェント（Claude Code、Codex、Gemini CLI、OpenCode ほか30以上）。
- caveman-commit は git リポジトリの差分を見られる状態で使う。メッセージを生成するだけで、stage・commit・amend は行わない。
- CLI機能は Mac / Linux / Windows。Node.js 22.13+。Autoを使う場合のみアカウント登録。
- CLIは既定で利用統計を送信する（プロンプト・コード・ファイルパスは含まない）。止めるには caveman telemetry off か DO_NOT_TRACK=1。

## 最短手順

- 1. Claude Code なら skill だけを入れる: `npx skills add JuliusBrussee/caveman -g`。-g はエージェントのユーザーskillディレクトリに入れる指定で、付けない場合はカレントプロジェクト側に入る。
- 2. 手動で入れる場合: このリポジトリの skills/caveman-commit/SKILL.md を `~/.claude/skills/caveman-commit/SKILL.md` に置く。frontmatter は `name: caveman-commit` と description だけなので編集不要。
- 3. Claude Code を再起動し、会話中で `/caveman-commit` を呼ぶ（Codex系は `$caveman` 記法）。変更差分を渡すと、Conventional Commits 形式のメッセージがコピペ用コードブロックで返る。適用は自分で git commit する。
- 4. CLI一式（読み込み圧縮・Auto・Blocksなど）も使うなら `npx @caveman-ai/cli@latest` を実行し、`caveman status` で何が有効か確認する。
- 5. 常用するなら Claude Code のプラグイン経由（`claude plugin marketplace add JuliusBrussee/caveman` → `claude plugin install caveman@caveman`）で対話セッションに自動適用できる。

## 変更履歴

- 2026-11-09: 初回登録
