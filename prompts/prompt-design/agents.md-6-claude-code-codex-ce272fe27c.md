---
type: "prompt"
name: "AGENTS.md 6節テンプレート（Claude Code / Codex 共用）"
genre: "prompt-design"
url: "https://x.com/sumika45379/status/2112521726399836208"
author: "@simplifyinAI（Simplifying AI）/ 画像投稿 @sumika45379"
source_post: "https://x.com/sumika45379/status/2112521726399836208"
sources: ["https://x.com/simplifyinAI/status/2105863469585313910", "https://code.claude.com/docs/en/memory", "https://developers.openai.com/codex/guides/agents-md", "https://x.com/sumika45379/status/2112521726399836208"]
first_seen: "2026-10-20"
added: "2026-11-08"
target: "Claude Code / OpenAI Codex（AGENTS.md を読むコーディングエージェント）"
transcribed_from: "image"
prompt_sha1: "ce272fe27cd46407141bd7481707265df3d7a2c6"
flags: ["unverified"]
risk_notes: "配布元の同定が部分的。@simplifyinAI が 2026-10-02 に同内容の AGENTS.md テンプレートを投稿していることは確認したが、その投稿の添付画像そのものは取得できておらず、本画像との同一性は未確認。本画像は VS Code のスクリーンショットで、ワークスペース名 token-demo、ステータスバー landon-art であり、オリジナルの作者・リポジトリは特定できていない。同じ33行は @Voxyz_ai 名義の文字起こし（copybook、2026-09-30）にも一致し、初出は不明。ライセンス表記なし。Claude Code 側の AGENTS.md 対応は v2.1.277 以降に限られ、CLAUDE.md があると既定では読まれない点は利用前に確認が必要。"
fetched_at: "2026-11-08T13:20:17Z"
---

# AGENTS.md 6節テンプレート（Claude Code / Codex 共用）

## 目的

- Claude Code と Codex の両方が読む AGENTS.md に、計画・最小変更・分担・バグ・確認・記録の6節を短い箇条書きで固定した雛形。1行ごとにエージェントの行動を変えることを狙い、長い説明ではなく実行可能な指示だけを並べる。

## 前提

- - AGENTS.md はリポジトリ直下（または作業ディレクトリ）に置く Markdown。Codex は作業前にネイティブで読む。Claude Code は v2.1.277 以降で、作業ディレクトリ以上に `CLAUDE.md` / `.claude/CLAUDE.md` / `CLAUDE.local.md` が無い場合にだけ `AGENTS.md` を読む。
- 特定の言語・フレームワーク・コマンドに依存しない。`PLAN.md` という名前の計画ファイルと、末尾 `Lessons` 節への追記を前提にしている。
- 画像からの文字起こし（`transcribed_from: image`）。改変・要約・翻訳はしていない。空行は画像どおり。

## プロンプト本文

```
# AGENTS.md

Shared by Codex and Claude Code. Every line here should change what you do.

## 1. Plan before you touch code
- Long task: first tell me in 2-3 sentences what you think I'm after
- Start only after I say yes
- Write the steps to `PLAN.md`, each with how you'll prove it works
- Two failed tries on one step: stop, note what failed, re-plan
- Pausing mid-task: leave `PLAN.md` so a new session can pick it up

## 2. Smallest change that works
- Stay inside this task. Don't break anything that already works
- Tradeoff? Weigh UX (users), DX (the next dev) and AX (the next agent)
- No new dependencies, renames or refactors nobody asked for
- Back up before deleting or overwriting anything

## 3. Split work across subagents
- Explorer reads, worker edits, reviewer only reports and never edits
- Each gets one job, a done condition and a 5-line report
- Parallel is fine. Two agents on the same file is not
- Check the key claim in a report before you build on it

## 4. Own the bug
- Reproduce it with my steps first. Can't reproduce it? Tell me what you need
- Fix the cause, then run the same steps again
- Never silence an error to make it go away

## 5. Verify before you say done
- Run the tests and read the output yourself
- UI: open it and try to break it: empty input, double submit, refresh
- Didn't run a check? Say so. An unrun check is not a pass
- Report in 2-3 lines: what you picked, what you gave up, and why

## 6. Write down every correction
- When I correct you, add a line under Lessons: "When X, do Y"
- Same mistake twice: the lesson is unclear. Rewrite it
- Ask me before changing anything above Lessons

## Lessons
<!-- Newest on top. Delete what no longer applies. -->
```

## 使い方

- 1. リポジトリ直下に `AGENTS.md` として保存する。
2. Claude Code 側に `CLAUDE.md` がある場合は、`CLAUDE.md` に `@AGENTS.md` の1行を足すか、Project instructions 設定を `claude-md-and-agents-md` にして両方読ませる（既定は `claude-md-or-agents-md` で、CLAUDE.md があると AGENTS.md は読まれない）。
3. Codex はそのまま読む。階層ごとに指示を変えたいときは各ディレクトリに `AGENTS.md` を置く（root から cwd まで連結、`AGENTS.override.md` が優先）。
4. 6節のうち案件に合わない行は削る。`PLAN.md` は既存の計画ファイル名に置き換える。
5. `Lessons` は運用しながら育つ想定。訂正のたびに「When X, do Y」の1行を上に足す。

## 注意点

- - **Claude Code の既定は「CLAUDE.md があれば AGENTS.md を読まない」。** 公式ドキュメントの表でも、AGENTS.md と CLAUDE.md が併存する場合は「Your CLAUDE.md files only」と明記されている。`CLAUDE.local.md` でも同じ判定になるため、個人メモを置くと AGENTS.md が読まれなくなる。
- **バージョン条件がある。** AGENTS.md の直接読み込みは v2.1.277 以降。それ以前の Claude Code では読まれないので、`@AGENTS.md` の import で回避する。
- **強制力はない。** Claude Code のドキュメントは CLAUDE.md を「コンテキストであり、強制される設定ではない」と説明しており、確実に止めたい操作は PreToolUse フックで縛る必要がある。AGENTS.md も同じ性質で、6節は行動を促す指示であって保証ではない。
- **数値の根拠は示されていない。** 「2-3 sentences」「5-line report」「Two failed tries」は経験則で、出典・実測はない。
- **字体の出所が不明。** 画像は VS Code のスクリーンショットで、ワークスペースは `token-demo`、ステータスバーは `landon-art`。配布元のリポジトリではなく、オリジナルの作者は特定できていない。同じ33行は @Voxyz_ai 名義の文字起こしにも一致する。
- **ライセンス表記なし。** X 投稿の文面であり、再利用・再配布の条件は明示されていない。
- 本項目は指示文の記録であり、内容の有効性を実測したものではない。

## 変更履歴

- 2026-11-08: 初回登録
