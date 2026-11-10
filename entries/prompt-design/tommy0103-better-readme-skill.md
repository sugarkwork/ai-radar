---
repo: "tommy0103/better-readme-skill"
name: "better-readme"
genre: "prompt-design"
url: "https://github.com/tommy0103/better-readme-skill"
license: "MIT"
stars: 32
language: "未確認"
created: "2026-10-08"
updated: "2026-10-08"
forks: 1
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 2
size_kb: 13
archived: false
author: "tommy0103"
flags: ["unverified"]
risk_notes: "GitHub の language は null（コードが無く Markdown のみ）。同梱の Art of README 本文には上流のライセンス表記が無く、上流 https://github.com/noffle/art-of-readme も 404 のため再配布条件は未確認。効果（使う前と後で変わる）は作者の主張のみで、before/after 例・テスト・第三者評価はリポジトリに無い。npx skills add は npm の skills v1.7.6 とそのドキュメントで実在を確認したが、この環境では実行できず、実際のインストール成否は未確認。投稿の画像は撮影時点で star 0 の README 画面で、現在値（31）とは一致しない。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2113035110052475218"]
fetched_at: "2026-11-09T21:41:57Z"
last_release: ""
last_release_at: ""
---

# better-readme — README を「認知ファネル」で監査・書き換えするエージェントスキル

## 出来ること

- README を「認知ファネル」の順（名前 → 一行説明 → 必要なら背景 → 実行できる使い方 → インストール → API → 注意点 → コントリビュート → ライセンス）に照らして監査し、崩れている箇所を名指しする。
- 監査で挙げる失敗パターンは6つ。メンテナ向け内容の混入、ファネルの崩壊（冒頭50行に内部詳細）、同じ事実の重複、単一ツール前提のままの記述、リンク切れやバージョンずれ、リポジトリ内の API ドキュメントへの未リンク。
- 書き換えは「削除より移動」。メンテナ向け手順は CONTRIBUTING か docs/ へ移してポインタを残し、事実は1箇所に集約し、持ち越す主張はすべてコードで再検証する。
- 編集前の事前チェックを要求する。git status（未コミットの変更を踏まない）、origin/main との差分、README の文言を固定しているテストや CI の検出、パッケージ用 README やサイト側の複製といった派生ドキュメントの有無。
- テストが文言を固定している場合は、見出し文字列やファイル一覧ではなく要件（順序、リンクの存在）を検証する形に作り替え、変更したアサーションの根拠を書く。黙ってテストを弱めることは禁じている。
- 翻訳は直訳ではなく意訳。対象言語の技術文書のリズムで書き、英語のまま定着した語（provider、agent、session など）は残し、見出し構造を原文と揃え、言語版同士を上部で相互リンクする。
- 納品前に、相対リンクと画像の解決、README を読むテストの実行、初見者としての読み直しを行う。バッジや star chart などの装飾は、消す前に作者へ確認する。

## 目的・背景

- 元ネタは noffle（Kira Oakley）の文章「Art of README」。認知ファネル（広い情報から狭い情報へ並べる）と、読者に早く降りてもらうことを良しとする考え方を、エージェントが実行できる手順に落としたもの。
- 中心にあるのは「売り込まない」という原則。同梱原文の該当箇所は「your job, when you're doing it with optimal altruism in mind, isn't to "sell" people on your work. It's to let them evaluate what your creation does as objectively as possible」。SKILL.md も「The job is not to sell; it is to let each reader evaluate fit as fast as possible, including bailing out early.」と要約している。
- SKILL.md は原文を README に転載させず「Do not reproduce it in the READMEs you write — apply it.」と指示し、参照用に references/art-of-readme.md（原文の逐語コピー、18,257バイト、404行）を同梱している。
- 上流 https://github.com/noffle/art-of-readme は現在 404。作者は「上流リンクが切れたので同梱した」と説明しており、こちらでも 404 を確認した。現在の noffle アカウントは 2021年作成・公開リポジトリ0件で、原作者のアカウントではない。
- 投稿の主張のうち「the art of readme の原則ベース」「npx skills add の1行」は実体と一致する。「使う前と後でかなり変わる」は作者の感想で、リポジトリに before/after の実例は無い。
- 作者は tommy0103（Yuu）。2026-10-08 公開の個人リポジトリで、コミットは初回投入と MIT ライセンス追加の2件のみ。

## 依存関係

- 配布は npm パッケージ skills（v1.7.6、MIT、リポジトリは vercel-labs/skills）。npx 経由で CLI（bin/cli.mjs）が動き、skills add owner/repo の GitHub shorthand を受け付ける。
- CLI はリポジトリ内の skills/<name>/SKILL.md を検出して導入する。このリポジトリは skills/better-readme/SKILL.md という、その discovery 規則に合う構成になっている。
- 導入先は既定でカレントプロジェクトの <agent>/skills/（Claude Code なら .claude/skills/）、-g を付けると ~/.claude/skills/ などユーザー全体。実体は .agents/skills/ に置かれ、各エージェントのディレクトリへリンクされる。
- スキル本体は Markdown 2ファイルのみ。サーバー、API キー、追加ランタイムは不要で、README を読み書きできるエージェント側の能力だけを使う。
- 対象プロジェクトで git が使えることが前提。事前チェックで git status と origin/main との差分を取るため。

## 実行条件

- ライセンスは MIT（Copyright (c) 2026 tommy0103 and contributors）。
- 同梱の Art of README 本文には上流のライセンス表記が無く、上流ページも 404 のため、その再配布条件は未確認。スキル本体の MIT とは別扱いと考えた方がよい。
- 発動条件は SKILL.md の description。README のレビュー・改善・書き換え・翻訳を頼んだとき、または README が良いか聞いたとき。
- 書き込みを伴う（README の置換、docs への移動、テストの書き換え）。作業ツリーが汚れている場合は新しい worktree で作業するよう SKILL.md が指示しており、そのまま実行すると未コミットの変更を壊しうる。
- star 31 / fork 1 / open issue 0、最終 push は 2026-10-08。コミットは公開当日の2件のみで直近30日は0件、公開後のメンテナンスは無い。
- 効果測定、before/after の実例、テスト、issue での利用報告はリポジトリに無い（未確認）。効果は手順の具体性から判断するしかない。

## 最短手順

- 対象プロジェクトのルートで `npx skills add tommy0103/better-readme-skill` を実行する。
- 導入先のエージェントを選ぶ。プロジェクト単位なら既定のまま、全プロジェクトで使うなら `-g` を付ける。
- まず監査だけ頼む。例: Audit my README.
- 書き換えるなら「Rewrite this README in funnel order and move the maintainer docs out.」、翻訳なら「Add an idiomatic Chinese version of this README.」のように依頼する。
- 差分を確認する。移動された節、落とされた記述、変更されたテストの根拠が説明されているかを見てからコミットする。

## 変更履歴

- 2026-11-09: 初回登録
