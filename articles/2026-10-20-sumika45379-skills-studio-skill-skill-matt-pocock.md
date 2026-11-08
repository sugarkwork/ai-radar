---
name: "「長くなる一方のSkill」を「短く効くSkill」にする、Matt Pocock式の作り方"
genre: "article"
url: "https://x.com/i/article/2109147034867658752"
author: "@sumika45379 (Skills Studio)"
source_post: "https://x.com/sumika45379/status/2112569775713120636"
published: "2026-10-20"
type: "article"
first_seen: "2026-10-20"
added: "2026-11-08"
sources: ["https://github.com/mattpocock/skills", "https://www.youtube.com/watch?v=QsU0f-547rQ", "https://code.claude.com/docs/en/skills", "https://x.com/sumika45379/status/2112569775713120636"]
flags: ["unverified"]
risk_notes: "2026-10-10時点「スター28万超」という記事の数字は当時の値を再現できず、2026-11-08実測は318,171（記事の数字は古いスナップショットで、現在は上回る）。種動画の内容は説明欄のチャプター（5段）と公開日まで確認、本編の逐語と図版は未確認。動画側の「22 million+ people use them」は一次確認なし（記事はこの種のインストール数を載せていない）。効果（送り返しの減少）の第三者計測は記事にも当方にも見つからない。記事は本文中2箇所でLINE友だち追加による「Skill10選」配布へ誘導する販促導線を含む。"
fetched_at: "2026-11-08T13:26:55Z"
---

# 「長くなる一方のSkill」を「短く効くSkill」にする、Matt Pocock式の作り方

## テーマ

- Claude Code / Agent Skills の SKILL.md を「短く効かせる」ための実践記事。Matt Pocock が公開している skills リポジトリ（MIT、2026-11-08 実測 stars 318,171）の実物を教材に、何をSkillにするか → どう短く書くか → どう呼ばせるか → どう削るか、の順で組み立てている。
- 記事は本人（Matt Pocock）の公開文書で確認できる部分と、Austin Marchese の解説動画（2026-09-29 公開）に基づく紹介者の要約を、明示的に分けて書く。日本語の実践記事としては珍しいほど切り分けが丁寧で、その切り分け自体を検証できる。

## 著者の主張

- Skillが効かないときに注意書きを足すのは逆効果。足りないのは文の量ではなく「何をSkillにして何を消すか」の選び方だ、というのが記事の中心。
- Skillにするのは「AIによく頼む作業」ではなく「何度も直させている作業」。直しの回数で選び、範囲は仕事全体ではなく直した一点・工程単位まで狭くする。
- 書くときは、AIが学習済みで持っている確立した言葉（leading word）を先に探す。造語は定義のトークンを自分で払うことになる。
- 自分で打って呼ぶSkillは `disable-model-invocation: true` で自動呼び出しを切り、説明文も常時コンテキストから外す。代わりに「いつ使うか」は人が覚える（"The human is the index."）。
- 効果は数値化せず、1週間使って「結果を送り返した回数」が減ったかで判断する。そのうえで no-op（言われなくてもやる指示）の文を1文ずつ消し、挙動が変わらなければ文ごと削る。禁止形ではなく肯定形で書く。

## 裏取り・注意点

- grill-me の実物を確認。GitHub API で取得した `skills/productivity/grill-me/SKILL.md` は7行で、frontmatter は name / description / `disable-model-invocation: true`、本文は `Call the Skill tool with "grilling".` の1行。記事のコードブロックと完全に一致する。
- 本体の `grilling`（30行）は disable-model-invocation を持たず、README は「The reusable interview primitive behind `grill-me`」と説明する。入口だけを user-invoked にするという記事の理解は正しい。39個の SKILL.md のうち27個が `disable-model-invocation: true` を設定している。
- `disable-model-invocation: true` の挙動は Claude Code 公式ドキュメントの表と一致する。公式は「Set to `true` to prevent Claude from automatically loading this skill」とし、表では「Claude can invoke: Not on its own」「When loaded into context: Description not in context, full skill loads when invoked」。記事の「説明文も普段の文脈に入らず、呼んだときに初めて全体が読み込まれる」は正確。
- スター数だけは記事の数字を再現できない。記事は「2026年10月10日時点で28万超」とするが、当時の値を後から測る手段がなく、2026-11-08 の GitHub API 実測は 318,171（fork 26,629、MIT、作成 2026-02-03、最終push 2026-11-05）。記事の数字は古いスナップショットで、現在はそれを上回る。
- 記事が「本人の文書」として引く文言は原文で確認できた。README 冒頭 "My agent skills that I use every day to do real engineering - not vibe coding."、writing-for-agents/SKILL.md の "a made-up word recruits no priors: you pay in definition tokens what a pretrained word gives free; reach for an existing word first."、同 "The human is the index."、SKILL-MECHANICS.md の "Pick model-invocation only when the agent must reach the skill on its own, or another skill must. If it only ever fires by hand, make it user-invoked and pay no context load."。no-op を1文ずつ消す話と「象」の比喩も同 SKILL.md にある。
- 一方 "A skill is a correction you got tired of making." はリポジトリ全体（SKILL.md 39本を含む）を検索しても見つからない。記事自身が「紹介者の要約で本人の文書には無い」と明記しており、この区別は正確。「send it back」テストも紹介者の命名で、動画のチャプター名 "Step 4: Iterate With the Send It Back Test" と一致する。
- 種動画は実在する。Austin Marchese「Matt Pocock's EXACT System To 10x Your Claude Skills」、2026-09-29 公開（15分27秒）。説明欄のチャプターが5段（Notice What You Keep Sending Back / Use Leading Words / Make Skills Smaller and Harder to Use / Send It Back Test / Cut the No-Ops）で、記事の「5つの段」と対応する。ただし本編の逐語は未確認（自動字幕のみ）で、記事の代弁が動画のどの発言に対応するかまでは追えていない。
- 「2026年3〜4月に不具合報告が2件、どちらも閉じられている」も GitHub Issues で確認。#31935「disable-model-invocation: true does not suppress skill descriptions from context」（2026-03-07 起票、03-11 close）が「説明文が文脈から外れない」、#32817「Skill tool blocks user-requested invocation when disable-model-invocation is set」（2026-03-10 起票、03-14 close）が「人からも呼べなくなる」に対応する。
- 紹介元の体験談も実在。Ryo Nakae の Zenn 記事（2026-04-09 公開）は「18回に渡って徹底的に質問されました」「`/grill-me` を使い始めてからはプランモードを使わなくなりました」と書いている。記事の引用は正確だが、2026年4月時点の旧版での記録で、現在の grill-me とは中身が異なる可能性がある（記事もそう注記している）。
- 動画は「22 million+ people use them」とインストール数を主張するが、一次情報では確認できない。記事がこの種の数字を載せず「本人や公式の資料で確かめられなかった」と書いているのは、こちらの確認結果と整合する。
- 効果（Skillを短くする・自動呼び出しを切ることで送り返しが減るか）の第三者計測は、記事にも当方の調査にも見つからない。ここは著者の設計思想と紹介者の運用案の範囲として読む必要がある。
- 記事は本文中2箇所で LINE 友だち追加から「Matt PocockのSkill10選」を受け取る導線（リード獲得）に誘導し、末尾も同導線と自アカウントの宣伝で終わる。技術内容は一次資料と一致するが、販促部分と本文は分けて読む。図版は未確認（本文の主張はテキストと一次資料で裏取り済みのため、推測では補っていない）。

## 出典

- 記事: https://x.com/i/article/2109147034867658752 （公開 2026-10-20、著者 @sumika45379 / Skills Studio）
- 元投稿: https://x.com/sumika45379/status/2112569775713120636
- mattpocock/skills（README・ライセンス・stars）: https://github.com/mattpocock/skills
- grill-me の SKILL.md: https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md
- grilling の SKILL.md: https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md
- writing-for-agents の SKILL.md: https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md
- writing-for-agents の SKILL-MECHANICS.md: https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md
- Claude Code 公式ドキュメント（Skills / Control who invokes a skill）: https://code.claude.com/docs/en/skills
- 種動画: Austin Marchese「Matt Pocock's EXACT System To 10x Your Claude Skills」（2026-09-29）: https://www.youtube.com/watch?v=QsU0f-547rQ
- 体験談: Ryo Nakae「grill-me スキルがめちゃ良いので布教したい」（2026-04-09）: https://zenn.dev/ryonakae/articles/8783c6b3ead2cb
- 不具合報告: https://github.com/anthropics/claude-code/issues/31935 ・ https://github.com/anthropics/claude-code/issues/32817

## 変更履歴

- 2026-11-08: 初回登録
