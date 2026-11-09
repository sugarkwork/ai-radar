---
name: "Jev Skill Typeahead"
genre: "coding-agent"
url: "https://www.aitmpl.com/component/mods/productivity/jev-skill-typeahead"
pricing: "free"
pricing_detail: "Mod 本体は MIT ライセンスの davila7/claude-code-templates に含まれ、npx で取得できてアカウント登録は不要（aitmpl.com に料金ページはなく /pricing は 404）。ただし Jev による確率判定を有効にする場合は TypeSafe API キー（または Vercel AI Gateway のキー）が必要で、その外部サービスの料金は別。キー未設定でもキーワード一致モードで動作する。"
signup_required: false
author: "davila7 (claude-code-templates) / 判定モデル Jev は TypeSafe"
flags: ["unverified"]
risk_notes: "投稿の「確率つきで出る」は半分正確。停止後に出る『Jev decided』行の % はバックエンド(Jev)が返す probability だが、入力中に即時表示される % は名前・説明と下書きの語の重なり（IDF 重み付き被覆率。policy.ts では 100*raw/total/1.6 を丸めた値）であって確率ではない。builtin プロバイダでは確率が返らず「—」表示になる。予測精度の実測値・ベンチマークは README になく、効果は著者の主張のみ。README 自身が「ライブのタイピング経路はエンジンの型を読んで確認しただけで、セッションに打ち込んでは検証していない」と明記している。Jev キーを設定すると下書き本文と全候補の名前・説明が停止ごとに外部(api.typesafe.ai 等)へ送信されるため、機密プロンプトでは keywords か builtin を選ぶ必要がある。Claude Code 2.1.287 以降が必須。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2113246504584663509"]
fetched_at: "2026-11-08T18:34:40Z"
---

# Jev Skill Typeahead — Claude Code の入力中に「次に使うスキル」を先読み表示する Mod

## 目的

- Claude Code でプロンプトを書いている最中に、その依頼で Claude が呼びそうなスキルとサブエージェントをプロンプト欄の上のバンドに先回り表示する。
- どのスキルが使われるか分からないまま送信してしまう状態を減らし、送信前に候補と確度を確認できるようにする。

## 何ができるか

- 入力のたびに下書きを読み、スキル名・説明とのキーワード一致（IDF 重み付き）で候補をランキング。打鍵中の語は前方一致で当て、コードブロックと URL は照合から除外。散文は内容語 2 語または 24 文字以上で表示が始まる。
- 600ms 入力が止まると Jev（TypeSafe の System One 判定モデル）へ 1 リクエスト送り、候補ごとの probability と 3 つのゲート質問（システムに作用するか／専門家が手順に従う作業か／散文だけで足りるか）から「実際に呼ばれる」1 件を ▶ でマーク。条件はゲート平均 0.3 以上かつ probability 0.35 以上。
- バンド表示は「82% anthropic-skills:pptx will be called」のように候補名・%・メーターを並べ、対象スキル数とサブエージェント数をヘッダに出す。`/jev-skill-typeahead` で最大 8 候補の詳細ペイン（スコア、説明全文、一致した語）を開ける。
- マークされた候補は送信時に `<skill_relevance>` ノートとしてモデルへ渡され、Skill ツール／Agent ツールでの利用を促す（attach、デフォルト有効）。判定後に本文を編集した場合や判定前に送信した場合は付かない。
- プロバイダは auto（既定。TypeSafe キー→Gateway キー→キーワードのみの順）／typesafe／gateway／builtin（Claude Code 内蔵の小型モデルを `$.model.classify` で使用）／keywords（判定しない）から選べる。キーなしの auto はネットワーク通信を一切しない。
- 設定はユーザー設定の `pluginConfigs["jev-skill-typeahead@skills-dir"].options` に置く: provider、language（en/es、ラベルのみ）、maxRows（既定 4、1〜8）、pauseMs（600、最小 150）、minWords（2）、includeSubagents（true）、timeoutMs（4000、最小 500）、attach、neverSuggested（カンマ区切り名）、logDecisions、gateThreshold、confidenceThreshold、typesafeApiKey／gatewayApiKey。
- 導入は Claude Code 2.1.287 以降のプロジェクトで `npx claude-code-templates@latest --mod productivity/jev-skill-typeahead` の後に `claude` を起動。初回セッションに `[jev-skill-typeahead] ready: …` の行が出る。導入後は `claude plugin validate productivity/jev-skill-typeahead` でフックイベントと `$` 呼び出しを確認できる。
- スラッシュコマンドは候補に出さない設計（`/`・`!`・`#` で始まる下書きは行を出さない）。キーワード一致の段階はローカル計算のみで、外部送信は Jev 判定時だけ。

## 料金

- Mod 本体は無料。MIT ライセンスの davila7/claude-code-templates に同梱され、npx で取得できる（アカウント登録は不要）。
- aitmpl.com に料金ページは存在せず（https://www.aitmpl.com/pricing は 404）、課金導線は確認できない。
- Jev の確率判定を使う場合のみ TypeSafe API キー（または Vercel AI Gateway のキー）が必要で、その外部サービスの費用は別途。キーなしでも keywords モード／builtin モードで動作する。

## 登録の要否

- 登録不要。GitHub アカウントも aitmpl.com のアカウントも作らずに npx で導入できる。
- TypeSafe／Vercel AI Gateway の API キーは任意。確率判定を有効にしたい場合だけ用意する。

## 変更履歴

- 2026-11-09: 初回登録
