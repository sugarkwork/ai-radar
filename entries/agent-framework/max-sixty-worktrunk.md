---
type: "repo"
name: "Worktrunk"
genre: "agent-framework"
url: "https://github.com/max-sixty/worktrunk"
author: "max-sixty (@max_sixty)"
pricing: "free"
pricing_detail: "OSS（MIT OR Apache-2.0）。ホスト版・課金なし。LLM コミット機能は手持ちのエージェント CLI の契約を使う。"
signup_required: false
repo: "max-sixty/worktrunk"
license: "MIT OR Apache-2.0"
stars: 12258
language: "Rust"
created: "2025-10-17"
updated: "2026-11-09"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/RoundtableSpace/status/2117802763262591481", "https://x.com/yozm_it/status/2118928933718823055?a=cjodEJSPnTqNRRgPDuQ&s=46", "https://x.com/yozm_it/status/2118928933718823055", "https://github.com/thedotmack/claude-mem", "https://github.com/Nutlope/hallmark", "https://github.com/anthropics/skills", "https://github.com/HKUDS/DeepTutor", "https://github.com/max-sixty/worktrunk"]
flags: ["unverified"]
risk_notes: "発見元の投稿は画面録画MCP（t.co リンク先は gmpetrov/agent-screenplay）の紹介で、worktrunk はそのツールではない。worktrunk は git worktree 管理 CLI で、投稿本文に worktrunk への言及はない。数値・機能は worktrunk 自身の API/README/公式ドキュメントで確認した。"
forks: 475
open_issues: 56
commits_30d: 100
commit_cadence: "daily"
size_kb: 63222
archived: false
fetched_at: "2026-11-09T21:33:48Z"
last_release: "v0.81.0"
last_release_at: "2026-10-20"
commits_90d: 100
license_detail: "原チェックのLICENSE/README解釈: MIT OR Apache-2.0。APIのSPDX判定とは別。利用前に現行本文を確認。"
source_post: "https://x.com/yozm_it/status/2118928933718823055"
amplifiers: []
---

# Worktrunk

## 出来ること

- git worktree をブランチ名で扱う3つの基本コマンド: `wt switch`（作成・切替。`-c` で新規ブランチ）、`wt list`（変更・ahead/behind・CI・PR・LLM要約つき一覧）、`wt merge`（squash→rebase→fast-forward→後片付けを1コマンド）、`wt remove`。
- `-x` でworktree作成と同時に任意コマンドを起動でき、並列エージェント運用の土台になる（例: `wt switch -x claude -c feature-a -- 'タスク内容'`）。`wt list` は 🤖（稼働中）/💬（入力待ち）のセッションマーカーを表示。
- エージェント統合プラグインを同梱: Claude Code / Codex / OpenCode / Pi / oh-my-pi / Gemini CLI。設定用スキル（Claude Code では `/worktrunk`）が LLM コミット・フック・パステンプレート・シェル統合の設定を補助する。
- Claude Code・OpenCode では worktree isolation のフックが `git worktree add` の代わりに `wt switch --create` / `wt remove` を通す。Claude Code 専用に `/wt-switch-create`（セッションを離れず新worktreeでタスク開始）、`/wt-diff` ペイン、statusline 出力もある。
- LLM コミットメッセージ生成: `commit.generation.command` に `claude -p` / `codex exec` / `opencode run` / `llm` / `aichat` などを指定し、差分からメッセージを作る。自前のモデルキーは持たず、既存 CLI の認証を使う。
- 周辺機能: hooks（pre-start / pre-merge / pre-commit など）、CoW によるビルドキャッシュ共有（APFS・btrfs・XFS）、`wt switch pr:123` の PR チェックアウト、worktree ごとに一意ポートを振る `hash_port`、エイリアス。

## 目的・背景

- 2025-10 公開、2026-11 時点で star 11,725。作者は Max Roos（max-sixty）。README は「並列に走らせる AI エージェントのための git worktree 管理 CLI」と自己定義している。
- 背景として README が挙げるのは、エージェントが長時間タスクを抱えると 5〜10 並列が現実になる一方、素の `git worktree add -b feat ../repo.feat && cd ../repo.feat` はブランチ名を何度も打たされ、後片付けも手作業という摩擦。worktrunk は worktree を branch と同じ手軽さにする。
- **投稿との不一致（重要）**: 発見元の X 投稿は「AI エージェントが滑らかなカーソル・ズーム・字幕つきのデモ動画（MP4）を作る無料 OSS、MCP 対応」という別ツールの紹介で、その t.co リンクは gmpetrov/agent-screenplay に解決する。worktrunk はその画面録画ツールではなく、投稿はworktrunkに触れていない。本項目はworktrunk自体の一次情報（README・公式ドキュメント・GitHub API）に基づく。
- 位置づけは「AI そのもの」ではなく、コーディングエージェントを並列で走らせるための開発環境側の道具。エージェントは `wt` をただのシェルコマンドとして呼べる。

## 依存関係

- Git 2.43 以上（公式 FAQ が明記）。
- シェル統合: `wt config shell install` を実行すると bash/zsh/fish に組み込まれ、worktree への移動が `cd` なしで効く。
- 導入経路: Homebrew（macOS/Linux）、`cargo install worktrunk`、winget（Windows では `git-wt` 名で入る）、pacman、conda-forge / Pixi。
- Cargo 経由のビルドは bash 構文ハイライト用に C99 コンパイラが必要（公式 FAQ）。
- LLM コミット機能を使う場合のみ外部 CLI が必要: claude / codex / opencode / llm / aichat。Codex 経路は JSON 解析に `jq` も要る。
- エージェント連携は各エージェント側のプラグイン機構に依存（Claude Code は plugin marketplace、Gemini CLI は extensions）。

## 実行条件

- macOS / Linux / Windows。Windows は `wt` が Windows Terminal のコマンドと衝突するため `git-wt` で入り、フックは Git Bash 前提（Git for Windows 必須）。
- 対象リポジトリのルート（または配下）で実行する。worktree のパスは `worktree-path` テンプレート設定で決まる。
- プラグイン導入はエージェントの設定領域を書き換える: Claude Code は `claude plugin marketplace add max-sixty/worktrunk`、OpenCode は `~/.config/opencode/plugins/worktrunk.ts`、Pi は `~/.pi/agent/extensions/`、oh-my-pi は `~/.omp/agent/hooks/pre/`。
- プロジェクト由来の hook / alias は初回実行時に承認を求め、結果は approvals.toml に保存される（自分で定義した user hook は承認不要）。
- `wt merge` / `wt remove` はブランチ削除や worktree 削除を伴う。未コミット変更がある worktree の削除は失敗する仕様なので、force 前提の運用はしない。

## 最短手順

- 1. インストール（Git 2.43+ が必要）: `brew install worktrunk && wt config shell install`（macOS/Linux）。Cargo なら `cargo install worktrunk && wt config shell install`。
- 2. 使っているエージェントにスキルとフックを入れる: Claude Code は `wt config plugins claude install`、Codex は `wt config plugins codex install`、OpenCode は `wt config plugins opencode install`、Gemini CLI は `gemini extensions install https://github.com/max-sixty/worktrunk`。
- 3. AI への依頼文の例: 「worktrunk で feature-auth の worktree を作って、その中で Claude に『ログイン画面を実装して』と渡して」。エージェントは `wt switch -x claude -c feature-auth -- 'ログイン画面を実装して'` を実行する（Claude Code ならプラグインの `/wt-switch-create` スキルでも同じことができる）。
- 4. 進捗確認はエージェントに「`wt list` で全worktreeの状態を見せて」と頼む。CI・差分・PR・🤖/💬 マーカーが1画面で出る。
- 5. 仕上げは「`wt merge main` で統合して、終わったworktreeを `wt remove` で片付けて」。LLM コミットを有効にしていれば squash メッセージも自動生成される。
- CLI を直接叩く場合の最小形: `wt switch --create feature-auth` → 作業 → `wt list` → `wt merge main` → `wt remove`。
- シェル統合を入れていない環境では `cd` が効かないため、`wt switch` の後に表示されるパスへ自分で移動するか、先に `wt config shell install` を済ませる。

## 変更履歴

- 2026-11-06: 初回登録

## 追加出典・確認範囲（2026-11-09）

複数の開発作業をgit worktreeで管理するWorktrunkの再紹介。

ローカルGitとエージェントCLI契約が前提。LLMコミット機能はモデルを内蔵するものではない。

週間ランキングの集計方法は未確認。今回の出典を既存の別ツールの紹介投稿と区別して追加する。

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:55.516488+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | max-sixty/worktrunk |
| url | https://github.com/max-sixty/worktrunk |
| license | NOASSERTION |
| language | Rust |
| created | 2025-10-17 |
| updated | 2026-11-08 |
| stars | 12119 |
| forks | 468 |
| open_issues | 53 |
| commits_30d | 100 |
| commits_90d | 100 |
| commit_cadence | daily |
| size_kb | 62934 |
| archived | False |
| fetched_at | 2026-11-09T00:30:55.516488+00:00 |
| license_detail | 原チェックのLICENSE/README解釈: MIT OR Apache-2.0。APIのSPDX判定とは別。利用前に現行本文を確認。 |


- @yozm_it: https://x.com/yozm_it/status/2118928933718823055
- 対象資料: https://github.com/max-sixty/worktrunk
- 参照: https://github.com/thedotmack/claude-mem
- 参照: https://github.com/Nutlope/hallmark
- 参照: https://github.com/anthropics/skills
- 参照: https://github.com/HKUDS/DeepTutor

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
