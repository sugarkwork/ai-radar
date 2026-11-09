---
name: "【公式】Claude Codeの「直しました」で終わらせない。画面の確認まで任せるSkillの作り方"
genre: "article"
url: "https://x.com/i/article/2109537400099930112"
published: "2026-10-23"
author: "sumika45379 / Skills Studio"
flags: ["unverified"]
risk_notes: "記事ページは非ログインだと x.com のログイン画面へリダイレクトされ（HTTP 200）、本文は封筒JSONの articleText に依拠。published は発見元ポストの日時（2026-10-23）で、記事ページ上の公開日は未確認。動画の字幕が取得できず、動画内の具体発言（3つの確認例、CLS 実演）は直接確認していない。v2.1.286 の自動実行は公式ドキュメントで確認済みだが、著者自身は /verify を実行しておらず、記事もその旨を明記している。末尾に LINE 友だち追加でプロンプト集を配る導線がある。"
type: "article"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2113776948740796721"]
fetched_at: "2026-11-09T08:32:37Z"
---

# 【公式】Claude Codeの「直しました」で終わらせない。画面の確認まで任せるSkillの作り方

## テーマ

- Claude Code に画面を直させたあとの「本当に意図どおりか」の確認を、人が毎回目視するのではなく Skill に書き出して Claude 自身に回させる方法の解説。
- Anthropic 公式YouTube「Building verification loops in Claude Code」（2026-09-25 公開、約3分）と公式ドキュメント code.claude.com/docs/en/skills を典拠に、同梱 /verify の初回記録 → Skill への追記 → Chrome DevTools MCP で CLS を測る、という流れを組み立てている。
- 対象は Claude Code を使う開発者。テストや型チェックは通るが画面の崩れやレイアウトシフトを毎回手で確認している、という場面を想定している。

## 著者の主張

- テストや型チェックが全部通っても変更が意図どおりだとは証明できず、最後の確認は今も人の役割。確認の手順と「何が合格か」を書き残せば、Claude が自分で確かめ、スクショと数値を証拠に返す。
- 同梱の /verify は時間とトークンを使うため Claude からは自動で呼ばれない。最初は自分で /verify と打つ。初回にうまくいった手順が .claude/skills/verify/SKILL.md に記録され、リポジトリ直下では同梱版を置き換え、以後は Claude が必要に応じて自分から使えるようになる（書き換えは手順が誤っていたときだけ）。DB など特殊な起動が要る場合は /run-skill-generator で起動レシピを先に記録する。
- 記録された Skill は完成品ではなく出発点で、次の3つを追記する。(1) いつ動かすか（例: 見た目を変えたとき）(2) 失敗したらどうするか（例: 原因を直して再確認）(3) 何が合格の証拠か（例: 指定幅のスクショと決めた数値）。
- 数値で測れる例として、Google の Chrome DevTools MCP（claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest）の性能トレースでレイアウトシフトを CLS として測り、「CLS が 0.1 以下なら合格」と書けば Claude が数字で合否を判断できる、と主張。
- 公式ドキュメントによれば v2.1.286 以降、verify という名前の Skill があるとコミット直前に実行するよう Claude へ指示が入る（/verify が記録した Skill は対象、同梱の /verify は対象外、docs のみ・tests のみの変更は除外）。Qiita の追試では verify で 3/3、verify2 で 0/3 だったとして、名前そのものが合図だと述べる。
- 実演では「いいね」ボタン追加の依頼に対し、Claude が開発サーバー起動→ページ操作→スクショ→性能トレースでずれを検出→修正して再確認、まで誰も指示せずに完結したと紹介。

## 裏取り・注意点

- 確認できた: 公式ドキュメント（2026-11-09 取得、HTTP 200）に「Run your checks before each commit」節があり、セッション開始時に verify（または simplify）名の Skill があると、docs/tests のみの変更を除いてコミット直前に実行する指示が入る／v2.1.286 以降が条件、と明記されている。記録先 .claude/skills/verify/SKILL.md、同梱版の置き換え、誤ったときだけ編集、/run-skill-generator、同梱 /verify が手動呼び出しのみ、も記事の記述と一致。
- 確認できた: Qiita（suwa_nobu、2026-10-01）の実測は verify 3/3・verify2 0/3・2.1.285 で 0/3・docs のみと tests のみは 0/3 で、記事の引用（3/3、verify2 は 0）と一致。ただし同記事は「公式ドキュメントにはまだ記載がない」時点の計測で、現在のドキュメントには記載がある。
- 確認できた: web.dev は CLS 0.1 以下を good の目安（75パーセンタイルで評価）と明記。Chrome DevTools MCP は ChromeDevTools/chrome-devtools-mcp として実在し（2026-11-09 時点 55,001 stars）、performance_start_trace が LCP/INP/CLS を返す。公式YouTube は Claude チャンネルで、タイトル・公開日 2026-09-25・長さ188秒・概要欄の公式ドキュメント該当節へのリンクを確認。
- 未確認: 記事ページは非ログインだとログイン画面へリダイレクトされ（HTTP 200）、本文は封筒JSONの articleText を使用。公開日は発見元ポストの 2026-10-23 で代用しており、記事ページ上の日付は未確認。
- 未確認: 動画の字幕取得に失敗（timedtext が空応答）したため、動画内の3つの確認例（Web/バックエンド/モバイル）、CLS を測る実演、話者の発言そのものは直接確認していない。概要欄の章立て（Hand off your manual checks / Codify your checks / The verification loop）とは整合する。
- 注意: v2.1.286 の自動実行には条件がある——セッション開始時に Skill が存在すること、Claude が呼べること（disable-model-invocation: true だと対象外）、includeGitInstructions が無効化されていないこと。記事は simplify 名やこれらの条件に触れていない。
- 注意: 記事のインストール行 `claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest` は配布元 README の記載と一致しない（README は Claude Code 向けにプラグイン経由の手順を案内。npx パッケージ名 chrome-devtools-mcp@latest 自体は一致）。README は性能ツールが trace URL を CrUX API に送る場合があることも明記している。
- 注意: 著者自身が「こちらで /verify は回しておらず、動画で生成された Skill の中身も未確認」と明記している。記事は公式資料の解説であり、実測記事ではない。
- 注意: 記事末尾は LINE 友だち追加でプロンプト集（確認表を作るプロンプト、SKILL.md 見本、試し方）を配る導線。配布物の中身と品質は未検証。
- 注意: 封筒の media 画像（pbs.twimg.com/media/HWWvkhaa4AAPVqD.jpg）は stageshow を紹介する別投稿の画像で、本記事の図ではない（vision で確認）。記事内の図は「最初は自分で /verify」と起動→実行→確認の3段階を示すもので、内容は記事本文と整合。

## 出典

- 記事: https://x.com/i/article/2109537400099930112 （発見元ポスト: https://x.com/sumika45379/status/2113776948740796721、2026-10-23）
- Claude Code 公式ドキュメント「Extend Claude with skills」（#run-your-checks-before-each-commit を含む）: https://code.claude.com/docs/en/skills
- Claude 公式YouTube「Building verification loops in Claude Code」（2026-09-25）: https://www.youtube.com/watch?v=mQZB0l-rhxE
- Chrome DevTools MCP: https://github.com/ChromeDevTools/chrome-devtools-mcp （ツール一覧: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md）
- web.dev「Cumulative Layout Shift (CLS)」: https://web.dev/articles/cls
- Qiita「スキルの名前を verify にするだけで、Claude Code はコミット前にそれを実行する」（suwa_nobu、2026-10-01）: https://qiita.com/suwa_nobu/items/cc0fb4a9e10100991bba

## 変更履歴

- 2026-11-09: 初回登録
