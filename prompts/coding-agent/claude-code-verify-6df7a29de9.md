---
name: "Claude Code コミット前検証スキル verify（テスト→差分レビュー→差し戻し）"
genre: "coding-agent"
url: "https://x.com/sumika45379/status/2112744441161322975"
prompt_sha1: "6df7a29de964f422a7a057e37a2f1dd7b8facf6c"
target: "Claude Code v2.1.286 以降（.claude/skills/verify/SKILL.md に置くプロジェクトスキル）"
transcribed_from: "image"
flags: ["unverified"]
risk_notes: "同梱の /verify とコミット前実行の仕様は code.claude.com の公式ドキュメントで確認できた。一方、Voxyz_ai が配布する SKILL.md の実ファイル（GitHub / gist）は発見できず、画像は SKILL.md 本文そのものではなく手順を図解したインフォグラフィック。そのため frontmatter や実行コマンドの具体、原文の正確な文言は未確認（unverified）。「OpenAI のレビュー基準」は OpenAI の公式文書ではなく、レビュー観点の通称とみられる。スキルはモデルへの指示であり、実行を強制するものではない。"
type: "prompt"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/sumika45379/status/2112744441161322975", "https://pbs.twimg.com/media/HVH535vbsAAOk7r.png"]
fetched_at: "2026-11-08T14:31:55Z"
---

# Claude Code コミット前検証スキル verify（テスト→差分レビュー→差し戻し）

## 目的

- コミットの直前に、その変更が「意図しない挙動変化」や「データに消える恐れのある変更」を含んでいないかを Claude 自身に確認させ、危険ならコミットさせずに修正へ戻すためのプロジェクトスキル。テストが通ることと、その差分が妥当であることを別々に確かめる点が要点。

## 前提

- Claude Code v2.1.286 以降。スキルは `.claude/skills/verify/SKILL.md`（プロジェクトスキル）に置く。
- セッション開始時点でそのスキルが存在している必要がある。あとから作っても、そのセッションのコミット前実行は有効にならない。
- Claude がスキルを呼べる設定であること。`disable-model-invocation: true` にするとコミット前実行の指示自体が降りない。`includeGitInstructions` を切っている場合も同様に対象外。
- 同梱の `/verify` は別物で、こちらは「アプリをビルドして起動し、実際の挙動を確認する」スキル。コミット前に自動で走るのはプロジェクト側に置いた verify スキルだけで、同梱版・プラグイン・claude.ai 由来のスキルは対象外。
- テスト・型チェック・リントのコマンドがプロジェクトに用意されていること（無いものは実行されない）。

## プロンプト本文

```
VERIFY BEFORE EVERY COMMIT · CLAUDE CODE · OPENAI REVIEW STANDARD

Claude finishes a change and wants to commit
     |
     +--> docs or tests only: skipped
     |
     v
+-------------------------------------------------------------+
| verify   .claude/skills/verify/SKILL.md                     |
|                                                             |
| 1  run the checks you have: tests, types, lint              |
|    one fails -> stop and say where                          |
|                                                             |
| 2  review the diff with OpenAI's review standard            |
|    one-line summary first                                   |
|    behavior changes · data loss · missing edge tests        |
|    each finding: input -> expected vs actual                |
+-------------------------------------------------------------+
     |
     +-----------------+-----------------+
                       |                 |
        unwanted behavior change    only other findings
         or possible data loss
                       |                 |
                       v                 v
                   no commit          list them
              fix, back to step 1     then commit

One skill file in your repo. Claude runs it before each commit it makes.

```

## 使い方

- `mkdir -p .claude/skills/verify` して SKILL.md を作り、`name: verify` と `description`（いつ使うか）の frontmatter を付けたうえで、画像の内容をそのまま本文に置く。
- 手順1の「チェック」はプロジェクトの実コマンド（例: `npm test`、`tsc --noEmit`、`eslint .`）に置き換える。複数あるなら全部列挙する。
- 古い版を使っているなら先に `claude update` で v2.1.286 以降にする。
- 作成後は新しいセッションを開始してから作業させる。既存セッションには反映されない。
- リポジトリ直下に置いた場合、同梱の `/verify` はこのファイルに置き換わる（Claude が起動レシピを記録した場合と同じ扱い）。手で `claude` を起動して `/verify` を打つと、この手順が走る。
- 止める基準（挙動変化・データ消失）をチームの言葉で具体化しておくと、レビュー観点がぶれにくい。

## 注意点

- 画像は SKILL.md の原文ファイルではなく、3段の手順を図解したインフォグラフィック。frontmatter・対象コマンド・例外規定は含まれていないので、そのままコピーしても動くスキルにはならない。
- Voxyz_ai の配布物（GitHub リポジトリや gist）は確認できなかった。画像が唯一の一次情報で、著者の原文の正確な文言は未確認。
- 「OpenAI のレビュー基準」は OpenAI の公式仕様として公開されている文書ではなく、レビュー観点（挙動変化・データ消失・端のケースのテスト不足）の通称とみられる。
- スキルはモデルへの指示であって強制機構ではない。確実に止めたいなら PreToolUse フックで `permissionDecision: deny` を返すなど、決定論的に動く仕組みを併用する。
- 「文書やテストだけの変更は対象外」という除外は公式仕様側の条件で、スキル単体の記述ではない。テストを書き換えて通す抜け道がある点は運用でカバーする。

## 変更履歴

- 2026-11-09: 初回登録
