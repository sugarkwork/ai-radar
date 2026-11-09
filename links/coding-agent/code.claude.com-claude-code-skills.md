---
name: "Claude Code Skills 機能"
genre: "coding-agent"
url: "https://code.claude.com/docs/en/skills"
author: "Anthropic"
pricing: "paid"
pricing_detail: "Claude Code は Free プラン非対応（料金ページの比較表で Claude Code: Free=No）。Pro 月額 $20（年払い $17/月・$200 前払い）、Max $100/月、Ultra $200/月、Team スタンダード $25/席/月（年払い $20）、Team プレミアム $125/席/月（年払い $100）、Enterprise $20/席/月（年払い・20席以上）＋従量、または Anthropic API のトークン従量課金。スキル機能自体の追加料金はない。"
signup_required: true
flags: ["unverified"]
risk_notes: "投稿の主要な主張は一次情報で確認できた：`.claude/skills/<skill-name>/SKILL.md` と `~/.claude/skills/<skill-name>/SKILL.md` の配置、description が常時コンテキストに載り本文は起動時に読み込まれる点、`allowed-tools`／`context: fork`／`paths` の実在、description+when_to_use の 1,536 文字上限、SKILL.md を 500 行未満に保つ指示、scripts 配下が「executed, not loaded」である点。一方で次の差がある。(1) 「Anthropic just shared one of the best tricks」とあるが新公開の裏技ではなく以前から文書化された標準機能（ページ最終更新 2026-11-04）。(2) `allowed-tools` の許可はそのスキルを起動したターン限りで、次のメッセージを送ると失効する。(3) スクリプトのファイル自体は読まれないが、インライン shell 展開の実行結果はスキル本文に注入されコンテキストに入るため、コンテキスト消費がゼロになるわけではない。(4) `context: fork` は会話履歴を引き継がないが、CLAUDE.md はエージェントの起動コンテキストとして読み込まれる（Explore／Plan エージェントは除く）。(5) 投稿が繰り返す「JEV」「JEV engineering」「routes micro-forks in milliseconds」は一次情報に記載がなく、スキル機能とは無関係の宣伝とみられる（未確認）。(6) 添付は動画1本のみで静止画はなく、動画フレームの書き起こしは行っていない。上記の各主張は動画ではなく一次情報の本文と突き合わせて個別に判定した。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/xsmryze/status/2113669627209208129"]
fetched_at: "2026-11-09T12:09:39Z"
---

# Claude Code のスキル — SKILL.md に手順を畳み、必要になったときだけ読み込ませる

## 目的

- 同じ手順・チェックリスト・多段の作業指示を毎回チャットに貼り付ける代わりに、`SKILL.md` 1ファイル（＋任意の補助ファイル）として再利用可能な形で置いておくための Claude Code の公式機構。CLAUDE.md が「事実」向けなのに対しスキルは「手順」向けで、本文は使うときだけ読み込まれるため、長い参照資料を常時コンテキストに載せずに済む。

## 何ができるか

- スキルの実体は `SKILL.md` 1ファイル。置き場所は `.claude/skills/<skill-name>/SKILL.md`（プロジェクト単位。コミットすればそのリポジトリで作業する全員が使える）、`~/.claude/skills/<skill-name>/SKILL.md`（自分の全プロジェクト）、`<plugin>/skills/<skill-name>/SKILL.md`（プラグイン）、`--add-dir` で追加したディレクトリ、claude.ai アカウント同期など。ディレクトリ名（または frontmatter の `name`）が `/skill-name` コマンドになる。
- 既定ではスキルの `description`（＋`when_to_use`）だけが一覧としてコンテキストに載り、本文はリクエストが説明に一致したとき、または `/skill-name` で明示起動したときに読み込まれる。一覧は description と when_to_use の合計 1,536 文字で切り詰められるので、用途を先頭に書く。
- frontmatter で挙動を制御できる：`allowed-tools` はそのターンに限りツールを許可（次のメッセージで失効）、`context: fork` は会話履歴を引き継がないサブエージェントとして実行（結果は既定でバックグラウンド到着、`background: false` で待つ）、`paths` は glob に一致するファイルを扱うときだけ自動起動、`disable-model-invocation`／`user-invocable` で起動主体を制限、`model`／`effort` でモデルと推論量を上書き。
- 補助ファイルを同梱できる。`reference.md` や `examples.md` は必要時に読み込まれ、`scripts/` 配下は「executed, not loaded」＝スクリプトは実行されるが本文としては読み込まれない。`${CLAUDE_SKILL_DIR}` を bash 注入や `allowed-tools` のパスに使うと、同梱スクリプトを権限プロンプトなしで実行できる。SKILL.md は 500 行未満に保ち、詳細は別ファイルへ移すことが推奨されている。
- 引数（`$ARGUMENTS` / `$ARGUMENTS[N]` / `$N`）、インラインの shell コマンド展開による動的コンテキスト注入、`/write-tests /fix-issue 123` のような複数スキルの同時指定、skill-creator による eval（description の当たり外れ調整、版の A/B 比較）も用意されている。
- AI から使う形：Claude Code の CLI／IDE／デスクトップ／Web セッション内で、モデルが description を見て自動起動するか、ユーザーが `/skill-name` で起動する。Agent SDK や `claude -p` からも同じスキルを読み込ませられる（非対話では先頭の1つだけ読み込む）。MCP サーバーではない。

## 料金

- スキル機能自体に追加料金はなく、Claude Code の利用料に含まれる。ただし Claude Code は Free プランでは提供されない（料金ページの比較表で Claude Code: Free=No）。Pro 月額 $20（年払い $17/月・$200 前払い）、Max $100/月、Ultra $200/月、Team スタンダード $25/席/月（年払い $20）、Team プレミアム $125/席/月（年払い $100）、Enterprise $20/席/月（年払い・20席以上）＋従量、または Anthropic API のトークン従量課金が必要。
- スキル本文は一度読み込まれると以降のターンもコンテキストに残り続けるため、行数が継続的なトークンコストになる。スクリプトの出力もコンテキストに入るので、出力を短く要約するほど安く済む。

## 登録の要否

- ページの閲覧に登録は不要。利用には Claude アカウントでのサインインと、Claude Code が使えるプラン（Pro 以上）または API 課金アカウントが必要。
- プロジェクトの `.claude/skills/` にコミットしたスキルは、そのリポジトリで作業する他の利用者にも読み込まれる。組織配布は managed settings のディレクトリ、個人用は `~/.claude/skills/`、配布物としてまとめるならプラグインの `skills/` を使う。

## 変更履歴

- 2026-11-09: 初回登録
