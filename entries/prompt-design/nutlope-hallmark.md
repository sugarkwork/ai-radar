---
type: "repo"
name: "Hallmark（AIっぽさを名指しで潰すデザインスキル）"
genre: "prompt-design"
url: "https://github.com/Nutlope/hallmark"
repo: "Nutlope/hallmark"
license: "MIT"
stars: 51710
language: "CSS"
created: "2026-04-27"
updated: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/opensourcelab9/status/2118601779063701949", "https://x.com/yozm_it/status/2118928933718823055?a=cjodEJSPnTqNRRgPDuQ&s=46", "https://x.com/yozm_it/status/2118928933718823055", "https://github.com/thedotmack/claude-mem", "https://github.com/Nutlope/hallmark", "https://github.com/anthropics/skills", "https://github.com/HKUDS/DeepTutor", "https://github.com/max-sixty/worktrunk"]
flags: ["unverified"]
risk_notes: "リリースもタグも無い（`/releases` と `/tags` が空、バージョンは SKILL.md と package.json の 2.0.0 表記のみ）。更新は活発だが 30日85コミットの大半が数十件のコミュニティPRを同一分にまとめてマージしたもので、内容はテーマ検証・sloplint・capture のバグ修正が中心（docs/スクリプトのみで実行バイナリは無い）。未解決が issue 25・PR 15。リポジトリは 228MB（site/ と docs/screenshots/ の画像が主因）で、インストールされるスキル本体は 7.1MB。ブラウザ検査（`--render`）は puppeteer-core + Chrome が要り、無い場合は『render tier not run』と出して静的検査だけに落ちる（実測）。同期間の★増分『+7,600』は投稿の主張で、stargazers API が 4万件超のページを返さない（page 400 で 404）ため検証できない。★は API 値 49,068 を採る（投稿の『4.8万』とほぼ一致、やや過小）。同梱の写真755枚は Wikimedia Commons の CC0/PD/CC BY/CC BY-SA で、CC BY 系は著作者・ライセンス・元ページの表示が条件。スキルはエージェントのフル権限で走る（skills.sh の警告）ので、導入前に SKILL.md と scripts/ を読むべき。画像生成ステップだけは TOGETHER_API_KEY（FLUX.1.1-pro、有料）を使う。eval/README が『claude -p ではスキルは自動発火しない』と明記しており、名前で呼ぶ運用が前提。"
forks: 2750
open_issues: 52
commits_30d: 85
commit_cadence: "daily"
size_kb: 233716
archived: false
fetched_at: "2026-11-09T21:41:54Z"
last_release: ""
last_release_at: ""
commits_90d: 100
author: "Nutlope"
source_post: "https://x.com/yozm_it/status/2118928933718823055"
amplifiers: []
---

# Hallmark — 「AIが作ったと分かるUI」を名指しで潰すデザインスキル。8画面幅の実ブラウザ検査と別AIレビューを強制する（Claude Code / Codex / Cursor / OpenCode）

## 出来ること

- AI生成UIの『それっぽさ』を名指しで禁止する。Floor は16条で無効化不可：紫→青グラデ、`transition: all`、ローマン見出し中のイタリック1語、eyebrow（見出し上の小ラベル）、字間を開けた大文字ラベル、絵文字アイコン、カード内カード、`100vw`、捏造したメトリクス/ testimonial / ロゴウォール など
- 50のテーマ（素材）からプロンプトに合う3つを配る `theme.mjs deal`、ページの骨格を仕事から決める `draw`。テーマは各8KB以下の1ファイル＋完成画で、レイアウトは指示しない（同じテーマでも2回振れば別ページになる）
- `sloplint.mjs <file|dir> --render` が実ブラウザで 320 / 375 / 414 / 768 / 1024 / 1280 / 1440 / 1920 の8幅を検査する（コントラスト、横スクロール、ヒーローが1280×800に収まるか、行折れ、画像欠け）。puppeteer-core が無ければ静的検査のみに落ちる
- `--before` でリンク・フォーム・ハンドラ・見出しを記録し、`--kept` で1つでも消えていたらリデザインを失敗させる（既存ページの改装で中身を落とさないため）
- 語彙は3つ：`/hallmark <prompt>`（新規）、`/hallmark redesign <path>`（内容と配線を保ったまま作り直す）、`/hallmark audit <path>`（報告のみ）。『custom』と言えばテーマを捨ててプロンプトだけから設計する
- ヒーローだけを先に作り、残りを作る前に冷たい目でレビューさせる（`review-hero.md` / `review-finish.md` の別コンテキスト・レビュアー）。最後に `sloplint --render` が通るまで直す
- 755枚の写真ライブラリを主題で引く（Wikimedia Commons、CC0/PD/CC BY/CC BY-SA、使った写真は著作者・ライセンス・元ページをページ上に明記）
- 出力は自己完結の HTML + CSS。CSS の1行目に「採った決定」をスタンプとして書き、`.hallmark/preflight.json` に事前調査をキャッシュする
- 実測（このスキルを入れて手元で実行）：`font-family:Inter` 直書き・紫→青グラデ・`transition:all`・`100vw`・`<h1>` 内の `<em>` を並べただけのページで **11 FAIL / 1 WARN** を返し、各項目に `:行` と修正案が付いた

## 目的・背景

- Together AI の Hassan El Mghari（Nutlope）による、Claude Code / Codex CLI / Cursor / OpenCode 向けの Agent Skill。『AIが作ったと分かるUI』の特徴を抽象論ではなく個別のゲート番号で列挙し、出力を機械的に検査するのが売り
- 設計は「床（Floor）は絶対、Reflex は理由を書けば上書き可、Finish は助言」の3層。Floor はモデルが訓練で落ちる既定（eyebrow、紫グラデ、絵文字アイコン、`transition: all` 等）を名指しで塞ぐ
- 発見元の投稿は『★4.8万・今週+7,600・MIT』と主張。API 実測は ★49,068 / fork 2,600 / 作成 2026-04-27 / 最終 push 2026-11-05 で、★はほぼ一致（API値を採用）。週次増分は stargazers API の取得上限で確認できない
- リポジトリには評価ハーネス `eval/` が同梱されている：Tier A は実 `claude -p "/hallmark <brief>"` を回して stamp の有無・参照ファイルの読み順・コストを解析、Tier B はスキルをシステムプロンプトに固めた素のAPI比較。8本の brief に『捏造メトリクスを誘う』『写真主導』などを用意し、sloplint のスコアと視覚ジャッジ（`judge.py`）で採点する
- eval/README は『`claude -p` ではスキルは自動発火しないので名前で呼ぶ。これは適合性テストであって自動発火テストではない』と明記している（＝実運用でも `/hallmark` と書くのが確実）
- 既存デザインには勝手に触らない思想で、`redesign` / `audit` は名前を出した時だけ動く。README の Inspired by には Impeccable、anthropics の frontend-design、Open Design、taste-skill など同系統のスキルが並ぶ

## 依存関係

- Node 18 以上（検証環境は v26.12.1）。スキル本体は Markdown（SKILL.md 18KB＋references 配下24ファイル＋テーマ50）＋ `scripts/*.mjs`
- 導入は `npx skills`（npm の `skills` パッケージ＝vercel-labs/skills 1.7.6、実測で導入成功）。代替として Claude Code の plugin marketplace、または clone して `node skills/hallmark/scripts/install.mjs`
- ブラウザ検査のみ `npm i -g puppeteer-core` ＋ Chrome（`HALLMARK_PUPPETEER` / `CHROME_PATH` でパス指定可）。無い場合は静的検査だけが走る
- 写真は同梱せず、`scripts/photos.json`（452KB）に Wikimedia Commons の URL・著作者・ライセンスを持つ。画像生成を使う場合だけ `TOGETHER_API_KEY`（Together の FLUX.1.1-pro、有料・任意）
- フォントはテーマが指定する Google Fonts 等を前提にするため、オフラインや閉域では表示が代替フォントになる
- 外部 MCP は必須ではない（Inspo MCP があればシグナルとして読む、という任意連携）

## 実行条件

- MIT。無料・アカウント不要。ただし写真の CC BY / CC BY-SA 分はページ上での出典表示が条件
- インストールはスキル定義をコピーするだけで、常駐プロセスもAPIキーも要らない（`~/.claude/skills/hallmark` / `~/.agents/skills/hallmark` に 7.1MB）
- エージェントのフル権限で動く（skills.sh も『Review skills before use』と警告）。`scripts/` は Node でファイルを書き、`capture.mjs` は指定URL/ローカル dev server をブラウザで開くので、対象プロジェクトの範囲を意識する
- 自動発火は環境依存（eval/README は `claude -p` で発火しないと明記）。確実にするなら `/hallmark <prompt>`、Codex なら `$hallmark <prompt>`、あるいは『use hallmark to build ...』と名指しする
- 既存ページへの適用は明示した時だけ。何も言わずに既存UIをいじる使い方は想定されていない
- リリース・タグが無いのでバージョン固定は commit SHA で行う（現在の SKILL.md は 2.0.0）
- 検証時点の未解決は issue 25 件・PR 15 件。30日で85コミットと活発だが、テーマやゲートの番号は今後も動きうる

## 最短手順

```bash
# 1) スキルを入れる（-g で全プロジェクト、外せばカレントのみ。Node 18+）
npx skills add nutlope/hallmark -g
#    1つのハーネスだけに入れる場合
npx skills add nutlope/hallmark -g --agent claude-code   # codex / cursor / opencode / github-copilot

# 2)（任意）実ブラウザ検査を有効にする
npm i -g puppeteer-core      # Chrome 本体も必要

# 3) エージェントで呼ぶ（Claude Code なら /hallmark、Codex なら $hallmark）
/hallmark 請求書のリコンサイルSaaSのLP。B2Bの経理担当、14日トライアル
/hallmark redesign ./src/app     # 既存を内容ごと作り直す
/hallmark audit ./index.html     # 報告だけ

# 4) 手元で lint するだけなら（スキル同梱のスクリプトを直接）
node ~/.claude/skills/hallmark/scripts/sloplint.mjs ./index.html --render

# 5) Claude Code のプラグインとして入れる場合
#    /plugin marketplace add nutlope/hallmark
#    /plugin install hallmark@hallmark   → /hallmark:hallmark
```


## 変更履歴

- 2026-11-06: 初回登録

## 追加出典・確認範囲（2026-11-09）

AIらしい定型デザインを避けるHallmarkスキルの再紹介。

Claude等のエージェントと、選択機能に応じたChrome/ブラウザ検査環境に依存。

ランキングは投稿者の集計で、今回あらためて効果・ブラウザ検査を追試したわけではない。

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:53.895013+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | Nutlope/hallmark |
| url | https://github.com/Nutlope/hallmark |
| license | MIT |
| language | CSS |
| created | 2026-04-27 |
| updated | 2026-11-05 |
| stars | 50958 |
| forks | 2707 |
| open_issues | 49 |
| commits_30d | 85 |
| commits_90d | 100 |
| commit_cadence | daily |
| size_kb | 233716 |
| archived | False |
| fetched_at | 2026-11-09T00:30:53.895013+00:00 |


- @yozm_it: https://x.com/yozm_it/status/2118928933718823055
- 対象資料: https://github.com/Nutlope/hallmark
- 参照: https://github.com/thedotmack/claude-mem
- 参照: https://github.com/anthropics/skills
- 参照: https://github.com/HKUDS/DeepTutor
- 参照: https://github.com/max-sixty/worktrunk

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
