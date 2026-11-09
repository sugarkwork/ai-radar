---
type: "repo"
repo: "cursor/plugins"
name: "pstack（Lauren Tan / poteto）"
genre: "coding-agent"
url: "https://github.com/cursor/plugins"
author: "Lauren Tan (@poteto)"
license: "MIT"
stars: 15813
language: "TypeScript"
created: "2026-01-23"
updated: "2026-11-07"
forks: 1653
open_issues: 641
commits_30d: 69
commits_90d: 99
commit_cadence: "daily"
size_kb: 6148
archived: false
last_release: ""
last_release_at: ""
added: "2026-11-09"
fetched_at: "2026-11-09T10:35:00Z"
flags: ["unverified"]
risk_notes: "【投稿の主張と実体】投稿は『SpaceXAI の Lauren Tan が /loop と /goal を使って80以上の GrokBot エージェントを動かし、85%のエンジニアが10以上を並列運用、Chief of Staff agent が全体を管理』と引用するが、この引用は一次情報で確認できなかった。添付動画（実測 55分47秒 / 1920x1078 / 30fps）を取得し7点のフレームを確認したところ、話者カードは『Lauren Tan / Software engineer | SpaceXAI』で本人の講演だが、内容は trust ladder・検証スキル・pstack・社内フレームワーク Dune の説明で、確認した範囲に『80+ agents』『/loop』『/goal』『Chief of Staff』『85%』は出てこない。同一講演の公開版（@poteto 本人投稿、38:02、『how i shipped 2,500 PRs last month』）の書き起こしにも該当発言はなく、『80%』は別の再アップロードの書き起こしでは『仕事の8割は1ディレクトリに閉じる』という局所性の文脈で出ており、エージェント数の主張とは無関係。同じ講演を再アップロードしたYouTubeチャンネル複数が『20+』『15+』『80+ agents』『85%』『1%』と互いに矛盾する煽り文を説明欄に付けており、投稿の引用はこの種の二次的な煽り文と一致する。よって引用は出典不明（本人発言として未確認）。/loop と /goal は Cursor Agent（および Grok Build）のスラッシュコマンドで、Grok Bot のコマンドではない（pstack README も『cursor's /loop command』と明記）。『85%のエンジニアが10+』は一次情報なし。Lauren Tan の所属自体は本物で、元 Meta（React Compiler）→ Cursor → SpaceXAI の Grok Bot 担当（動画の話者カード、GitHub、本人投稿で一致）。【指標の注意】pstack は cursor/plugins モノレポ内のサブディレクトリで単独リポジトリは存在しない。stars/forks/open_issues は親リポジトリ全体の値（15,813 / 1,653 / 641）。size_kb は pstack 配下の blob 合計 6,295,660 bytes の KB 換算（6,148KB）で、親リポジトリ全体は 18,538KB。commits は path=pstack で絞った実測（30日69、90日99）。親リポジトリ直下にライセンスはないが pstack/LICENSE は MIT。投稿の引用元X記事2件（2091522676426694656 等）は非ログインでログイン画面へリダイレクトされ本文を読めないことを実際に確認しており、内容は推測していない。"
sources: ["https://github.com/cursor/plugins/tree/main/pstack", "https://github.com/cursor/plugins/blob/main/pstack/README.md", "https://github.com/cursor/plugins/blob/main/pstack/plugin.json", "https://github.com/cursor/plugins/blob/main/pstack/LICENSE", "https://github.com/cursor/plugins/blob/main/pstack/docs/guide/01-setup.md", "https://github.com/cursor/plugins/pull/73", "https://x.com/poteto/status/2102050467505430555", "https://ai.engineer/speakers/lauren-tan", "https://cursor.com/docs/agent/overview", "https://x.com/xsmryze/status/2109764661356671245"]
source_post: "https://x.com/xsmryze/status/2109764661356671245"
first_seen: "2026-10-12"
---

# pstack — 検証を先に置く、コーディングエージェント向けの実務スキル一式（/poteto-mode）

## 出来ること

- `/poteto-mode` に作業内容を渡すと、23のプレイブック（investigation、bug fix、perf、hillclimb、refactoring、feature、prototype、visual parity、eval、babysit、shipping、autonomous run、orchestrate、autopilot-full/stack、session pickup、multi-phase plan など）から1つ選び、手順を todo リストに複写して他のスキルを必要な順に呼ぶ。
- 検証スキルを生成する。`/create-verification-skill` はアプリを実際に操作して合否を出す project-local スキルと feature map を作り、`/create-formal-verification-skill` は並行性・リトライ・状態機械・パーサ向けに TLA+ などで1つの性質を検証するスキルを作る。
- 複数エージェントの並列実行を前提にしたスキルがある。`/swarm`（別スライスをN並列→1レポート）、`/arena`（同じ課題をN案→良い部分を採用）、`/interrogate`（別モデルに差分を壊しにいかせる）、`/orchestrate`、`/autopilot-full`。
- コードを書く前の理解と設計に寄ったスキル群: `/how`、`/why`、`/teach`、`/recall`、`/architect`、`/blast-radius`、`/tdd`、`/benchmark-checklist`、`/no-comments`、`/unslop`、`/technical-writing`。
- 自分の進め方をスキル化する `/automate-me`、繰り返す指摘を履歴から分類して lint/型/CI に落とす `/correct`、長いタスクの判断履歴を残す `/show-me-your-work`。
- Grok Bot を webhook で起こす UI を作る `/make-bot-ui` も同梱（Tailscale 前提の sender-key 受け渡しを含む）。

## 目的・背景

- 作者 Lauren Tan（@poteto）は元 Netflix、Meta の React Compiler コアチームを経て Cursor（現 SpaceXAI）で Grok Bot を担当。大量のエージェントを並列で走らせると『質の低いPRが増える』という問題に対し、スループットではなく検証可能性を先に投資する立場を取る。
- README の主張は『速く行きたいなら先に深く行け』『行数を最大化しない、むしろ少なく高品質に書く』。コードベース・静的解析・lint/CI・rules・skills の順に、エージェントの間違いを『起きにくくする』方向へ積み上げる。
- 講演では同じ考えを trust ladder（1体→1〜5体→5〜10体→10〜20体→数百→数千）として説明し、信頼できる検証手段がないまま台数を増やすと regression と低品質PRが増えると警告している。
- 本エントリの pstack は cursor/plugins モノレポ内のサブディレクトリ（path=pstack）で、単独リポジトリは存在しない。stars/forks/open_issues は親リポジトリ cursor/plugins 全体の値。

## 依存関係

- Cursor: チャットで `/add-plugin pstack`。
- Claude Code: `/plugin marketplace add cursor/plugins` → `/plugin install pstack@cursor-plugins`。コマンドは `pstack:` 接頭辞になり、`/poteto-mode` は `/pstack:poteto-mode`。
- モデルへのアクセスが必須。既定はコード委譲が Grok、判断・文章が Opus 5.5 で、`/setup-pstack` が役割ごとのモデルを `~/.cursor/rules/pstack-models.mdc`（Claude Code は `~/.claude/rules/pstack-models.md`）に書き出す。
- Cursor 専用機能（Bugbot、automations、`/loop`、`/goal`）に依存する手順は Claude Code では注記付きでスキップされる。
- TLA+ モデルを同梱するため、形式検証スキルを使う場合は TLA+ ツールチェーン（TLC）を別途用意する。mjs スクリプトと harness 生成には Node.js を使う。

## 実行条件

- エージェントのチャット内で動く。常駐プロセスやサーバは不要で、SKILL.md と同梱スクリプトをエージェントが読む。
- subagent とレビューパネルを多用するためトークン消費が大きい。公式ガイドは reasoning budget を下げる、役割を `auto`/`inherit-parent` にする、パネルを短くする、`/poteto-mode` を本当に厳密さが要る作業に限定する、という節約法を示す。
- `/poteto-mode` を全ターン保持したい場合は `/` メニューから Option+Enter（Mac）/ Alt+Enter（Windows）で Custom Mode にする。通常の Enter は1メッセージ限り。
- 検証スキルは対象アプリの起動方法（dev サーバ、CLI、Chrome DevTools など）に依存するため、プロジェクトごとに1度作る必要がある。

## 最短手順

- 1. Cursor で `/add-plugin pstack` を実行（Claude Code は marketplace 経由で install）。
- 2. `/setup-pstack` を実行し、reasoning budget と役割ごとのモデルを選ぶ。
- 3. 新しいチャットで `/poteto-mode` を選び、成果物と合格条件を自分の言葉で書く（例: `/poteto-mode add a --json flag. text output stays byte-identical. verify both.`）。
- 4. 提示された todo リストの手順と、証拠（テスト、trace、スクリーンショット）を確認する。
- 5. 検証スキルが無いプロジェクトなら、setup 時の提案を受けて `/create-verification-skill` で1つ作る。

## 変更履歴

- 2026-11-09: 初回登録
