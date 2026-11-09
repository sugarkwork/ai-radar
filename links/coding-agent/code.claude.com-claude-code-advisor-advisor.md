---
name: "Claude Code advisor ツール（--advisor）"
genre: "coding-agent"
url: "https://code.claude.com/docs/en/advisor"
author: "Anthropic"
pricing: "paid"
pricing_detail: "Free プランでは Claude Code 自体が使えない。Pro 月額 $20（年払い $17/月・$200 前払い）、Max $100/月、Ultra $200/月、または Anthropic API の従量課金。advisor の呼び出しは advisor モデルのトークンとして追加課金され、サブスクではプラン上限に算入される。"
signup_required: true
flags: []
risk_notes: "一次情報（code.claude.com/docs/en/advisor、HTTP 200、2026-11-09 取得）で確認できたのは advisor ツール本体：--advisor フラグ・/advisor コマンド・advisorModel 設定の実在、モデルのペアリング表、課金の扱い、実験的機能である点。発見元ポストの主張のうち、Haiku 5.5 の読み取り専用サブエージェント3種（search/grep/docs）の並列実行と「JEV」は advisor のドキュメントに記載がなく、別機能または未確認。ポストの「Opus が3つの場面だけ介入する」は docs では“傾向”とされており、呼び出しを強制・上限する設定は存在しないため CLAUDE.md の記述で保証はできない。実験的機能のため仕様・料金・提供範囲は変更されうる。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/xsmryze/status/2112887075796111618"]
fetched_at: "2026-11-09T11:33:46Z"
---

# Claude Code の advisor ツール — 本体は速いモデル、判断だけ上位モデルに相談

## 目的

- Claude Code のセッション本体を速く安いモデル（例: Sonnet）で回し、方針決定など判断が重い場面だけ上位モデル（例: Opus）に相談させるための公式機能。全ターンを上位モデルで実行するより費用を抑えつつ、計画と完了判定の質を上げることを狙う。長いリファクタリング、同じエラーが繰り返すデバッグ、完了前に第三者の確認を入れたい作業に向く。短いタスクや、毎ターン最上位モデルが必要な作業では効果が薄いと明記されている。

## 何ができるか

- 起動時に `claude --advisor opus` のようにフラグで指定すると、そのセッションだけ advisor が有効になる（保存設定 `advisorModel` は変更しない）。`--advisor` は `claude --help` には表示されない。
- セッション中は `/advisor opus` で設定、`/advisor off` で解除、引数なしの `/advisor` で現在の advisor と受け付けるエイリアスの一覧を表示できる。`/advisor` での選択はユーザー設定の `advisorModel` に保存され、セッションをまたいで残る。設定ファイルに `{"advisorModel": "opus"}` と書けば既定値にできる。
- advisor は Anthropic 側で実行されるサーバーツールで、会話全体（すべてのツール呼び出しと結果を含む）を受け取り、助言を返す。本体モデルはその助言を踏まえて作業を続ける。
- モデルはエイリアス `fable` / `opus` / `sonnet`、または `claude-opus-5-5`・`claude-haiku-5-5` のようなフルIDで指定する。advisor は本体モデルと同等以上の能力ランクでなければならない（例: 本体 Sonnet 5.5 には Fable、Opus 5 以降、Sonnet 5.5 が使える）。Haiku 4.5 は advisor を呼べるが advisor にはなれない。
- 呼び出しのタイミングはモデルが判断する。方針を固める前、同じエラーが続いたとき、完了を宣言する前に相談する傾向があるが、ルールベースではなく、呼び出し回数を強制したり上限を設けたりする設定はない。`consult the advisor before you continue` のようにプロンプトで依頼することはできる。
- 実行中は `Advising` 行が表示され、結果は Reviewed（助言あり、Ctrl+O で内容を読める）、Declined（助言を辞退）、Unavailable（呼び出し失敗とエラーコード）で示される。
- サブエージェントは設定済みの advisor を継承し、自身のモデルに対して同じペアリング検査を受ける。

## 料金

- advisor は無料の追加枠ではなく、呼ばれるたびに advisor モデルの入力・出力トークンが課金される。API 課金なら advisor モデルのレート、サブスクリプションならプランの利用上限に算入される（Fable を advisor にした場合は、Fable 利用が usage credits 対象のプランでは同じ扱い）。
- Claude Code 自体は Free プランでは提供されず、Pro（月額 $20、年払いで $17/月・$200 前払い）、Max（$100/月）、Ultra（$200/月）で利用できる。Anthropic API の従量課金でも利用可能。
- advisor 分のトークンは `/usage` のセッション合計にも加算される。ただし毎ターンではなく判断ポイントでのみ呼ばれるため、上位モデルを常時使うより安く済むことが多いと説明されている。

## 登録の要否

- Claude アカウント（Pro / Max / Ultra などのサブスクリプション）か、Anthropic API の課金アカウントが必要。未ログインでは利用できない。
- 実験的機能で、Anthropic の API 経由でのみ動作する。Amazon Bedrock、Claude Platform on AWS、Google Cloud's Agent Platform、Microsoft Foundry では利用できない。`ANTHROPIC_BASE_URL` を設定した LLM ゲートウェイ経由では、リクエストをそのまま Anthropic API へ転送できる場合に限り利用できる。
- Anthropic から取得する機能フラグで有効化されるため、`DISABLE_TELEMETRY` などフラグ取得を止める環境変数が設定されたセッションでは無効のまま。`CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` を設定するとツール自体を無効化でき、`/advisor` は使えなくなり `advisorModel` も無視される。

## 変更履歴

- 2026-11-09: 初回登録
